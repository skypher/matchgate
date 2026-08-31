#!/usr/bin/env python3
"""Check exact identities, then replay floating-point acceptance rows."""

from __future__ import annotations

import argparse
from collections import deque
import csv
from fractions import Fraction
from itertools import combinations
import math
import os
from pathlib import Path
import subprocess
import sys


CHECKED_FIELDS = (
    "rho",
    "expectation",
    "normalized",
    "limit_constant",
    "observed_sqrt_correction",
)


Subset = tuple[int, ...]


def subset_distance(left: Subset, right: Subset) -> int:
    return sum(abs(a - b) for a, b in zip(left, right, strict=True))


def cumulative_area(left: Subset, right: Subset, population_size: int) -> int:
    return sum(
        abs(
            sum(value <= level for value in left)
            - sum(value <= level for value in right)
        )
        for level in range(1, population_size)
    )


def token_neighbors(subset: Subset, population_size: int) -> list[Subset]:
    occupied = set(subset)
    neighbors: list[Subset] = []
    for value in subset:
        for moved in (value - 1, value + 1):
            if 1 <= moved <= population_size and moved not in occupied:
                neighbors.append(tuple(sorted(occupied - {value} | {moved})))
    return neighbors


def exact_pairwise_mean(population_size: int, subset_size: int) -> Fraction:
    vertices = list(combinations(range(1, population_size + 1), subset_size))
    distance_sum = 0
    for source in vertices:
        graph_distances = {source: 0}
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for neighbor in token_neighbors(current, population_size):
                if neighbor not in graph_distances:
                    graph_distances[neighbor] = graph_distances[current] + 1
                    queue.append(neighbor)
        if len(graph_distances) != len(vertices):
            raise ValueError(
                f"token graph N={population_size} k={subset_size} is disconnected"
            )
        for target in vertices:
            coordinate_distance = subset_distance(source, target)
            transport_area = cumulative_area(source, target, population_size)
            if graph_distances[target] != coordinate_distance:
                raise ValueError(
                    "configuration metric mismatch: "
                    f"N={population_size} k={subset_size} "
                    f"source={source} target={target} "
                    f"graph={graph_distances[target]} coordinate={coordinate_distance}"
                )
            if transport_area != coordinate_distance:
                raise ValueError(
                    "transport identity mismatch: "
                    f"N={population_size} k={subset_size} "
                    f"source={source} target={target} "
                    f"area={transport_area} coordinate={coordinate_distance}"
                )
            distance_sum += coordinate_distance
    return Fraction(distance_sum, len(vertices) ** 2)


def exact_hypergeometric_mean(population_size: int, subset_size: int) -> Fraction:
    denominator = math.comb(population_size, subset_size)
    total = Fraction(0)
    for marked_size in range(1, population_size):
        lo = max(0, subset_size - population_size + marked_size)
        hi = min(subset_size, marked_size)
        weights = {
            value: math.comb(marked_size, value)
            * math.comb(population_size - marked_size, subset_size - value)
            for value in range(lo, hi + 1)
        }
        if sum(weights.values()) != denominator:
            raise ValueError(
                f"hypergeometric normalization mismatch at "
                f"N={population_size} k={subset_size} r={marked_size}"
            )
        numerator = sum(
            abs(left - right) * left_weight * right_weight
            for left, left_weight in weights.items()
            for right, right_weight in weights.items()
        )
        total += Fraction(numerator, denominator**2)
    return total


def exact_walk_bridge_area(half_length: int) -> Fraction:
    total_area = 0
    for up_steps_tuple in combinations(range(2 * half_length), half_length):
        up_steps = set(up_steps_tuple)
        height = 0
        for step in range(2 * half_length):
            height += 1 if step in up_steps else -1
            if step < 2 * half_length - 1:
                total_area += abs(height)
    return Fraction(total_area, math.comb(2 * half_length, half_length))


def bridge_area_formula(half_length: int) -> Fraction:
    return Fraction(
        half_length * 4**half_length,
        2 * math.comb(2 * half_length, half_length),
    )


def central_mean_formula(site_count: int) -> Fraction:
    mixture = sum(
        (
            Fraction(math.comb(site_count, m) ** 2, 1)
            * Fraction(
                m * 4**m,
                (2 * m + 1) * math.comb(2 * m, m),
            )
        )
        for m in range(1, site_count + 1)
    )
    return Fraction(
        2 * site_count + 1,
        2 * math.comb(2 * site_count, site_count),
    ) * mixture


def run_exact_identity_checks() -> None:
    central_means: dict[int, Fraction] = {}
    for population_size in range(2, 9):
        for subset_size in range(1, population_size):
            pairwise_mean = exact_pairwise_mean(population_size, subset_size)
            hypergeometric_mean = exact_hypergeometric_mean(
                population_size, subset_size
            )
            if pairwise_mean != hypergeometric_mean:
                raise ValueError(
                    "exact hypergeometric mean mismatch: "
                    f"N={population_size} k={subset_size} "
                    f"pairwise={pairwise_mean} hypergeometric={hypergeometric_mean}"
                )
            if population_size % 2 == 0 and subset_size == population_size // 2:
                central_means[population_size // 2] = pairwise_mean
        print(
            f"exact metric/transport/hypergeometric N={population_size}/8 pass",
            flush=True,
        )

    for half_length in range(1, 7):
        enumerated = exact_walk_bridge_area(half_length)
        formula = bridge_area_formula(half_length)
        if enumerated != formula:
            raise ValueError(
                "walk-bridge area mismatch: "
                f"m={half_length} enumerated={enumerated} formula={formula}"
            )
    print("exact walk-bridge areas m=1..6 pass", flush=True)

    for site_count in range(1, 6):
        pairwise_mean = central_means.get(site_count)
        if pairwise_mean is None:
            pairwise_mean = exact_pairwise_mean(2 * site_count, site_count)
        formula = central_mean_formula(site_count)
        if pairwise_mean != formula:
            raise ValueError(
                "central exact mean mismatch: "
                f"n={site_count} pairwise={pairwise_mean} formula={formula}"
            )
    print("exact central means n=1..5 pass", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    if not rows:
        raise ValueError(f"no acceptance rows found in {path}")
    required = {"n", "k", *CHECKED_FIELDS, "mixture_difference"}
    missing = required.difference(rows[0])
    if missing:
        raise ValueError(f"missing result columns: {sorted(missing)}")
    return rows


def parse_result_lines(output: str) -> dict[tuple[int, int], dict[str, str]]:
    parsed: dict[tuple[int, int], dict[str, str]] = {}
    for line in output.splitlines():
        if not line.startswith("result "):
            continue
        fields = dict(
            token.split("=", 1) for token in line.split()[1:] if "=" in token
        )
        key = (int(fields["n"]), int(fields["k"]))
        parsed[key] = fields
    return parsed


def run_density(
    executable: Path, density: str, rows: list[dict[str, str]]
) -> dict[tuple[int, int], dict[str, str]]:
    command = [
        str(executable),
        "--rho",
        density,
        *(row["n"] for row in rows),
    ]
    environment = os.environ.copy()
    environment["OMP_NUM_THREADS"] = os.environ.get(
        "MATCHGATE_CHECK_THREADS", "8"
    )
    print(
        f"density={density} cases={len(rows)} "
        f"threads={environment['OMP_NUM_THREADS']}",
        flush=True,
    )
    completed = subprocess.run(
        command,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=environment,
    )
    if completed.returncode != 0:
        print(completed.stdout, end="", flush=True)
        raise RuntimeError(
            f"{executable} exited with status {completed.returncode}"
        )
    parsed = parse_result_lines(completed.stdout)
    if len(parsed) != len(rows):
        print(completed.stdout, end="", flush=True)
        raise RuntimeError(
            f"expected {len(rows)} result lines for density {density}, "
            f"found {len(parsed)}"
        )
    return parsed


def numerically_equal(field: str, actual: float, expected: float) -> bool:
    if math.isnan(expected):
        return math.isnan(actual)
    if math.isnan(actual):
        return False
    if field == "mixture_difference":
        return math.isclose(actual, expected, rel_tol=0.0, abs_tol=5e-10)
    return math.isclose(actual, expected, rel_tol=5e-13, abs_tol=5e-12)


def check_row(
    expected: dict[str, str], actual: dict[str, str]
) -> list[str]:
    failures: list[str] = []
    expected_n = int(expected["n"])
    expected_k = int(expected["k"])
    if int(actual["n"]) != expected_n or int(actual["k"]) != expected_k:
        failures.append(
            f"identity: got n={actual['n']} k={actual['k']}, "
            f"expected n={expected_n} k={expected_k}"
        )

    for field in CHECKED_FIELDS:
        actual_value = float(actual[field])
        expected_value = float(expected[field])
        if not numerically_equal(field, actual_value, expected_value):
            failures.append(
                f"{field}: got {actual_value:.17g}, "
                f"expected {expected_value:.17g}"
            )

    expected_mixture = expected["mixture_difference"]
    actual_mixture = float(actual["mixture_difference"])
    if expected_mixture == "less_than_1e-13":
        if math.isnan(actual_mixture) or abs(actual_mixture) >= 1e-13:
            failures.append(
                "mixture_difference: "
                f"got {actual_mixture:.17g}, expected absolute value < 1e-13"
            )
    else:
        expected_value = float(expected_mixture)
        if not numerically_equal(
            "mixture_difference", actual_mixture, expected_value
        ):
            failures.append(
                f"mixture_difference: got {actual_mixture:.17g}, "
                f"expected {expected_value:.17g}"
            )
    return failures


def main() -> int:
    arguments = parse_args()
    run_exact_identity_checks()
    rows = read_rows(arguments.results)

    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["rho"], []).append(row)

    actual_rows: dict[tuple[int, int], dict[str, str]] = {}
    for density, density_rows in grouped.items():
        actual_rows.update(
            run_density(arguments.executable, density, density_rows)
        )

    all_failures: list[str] = []
    for index, expected in enumerate(rows, start=1):
        key = (int(expected["n"]), int(expected["k"]))
        actual = actual_rows.get(key)
        if actual is None:
            all_failures.append(f"n={key[0]} k={key[1]}: missing result")
            continue
        failures = check_row(expected, actual)
        if failures:
            all_failures.extend(
                f"n={key[0]} k={key[1]}: {failure}"
                for failure in failures
            )
        else:
            print(
                f"row {index}/{len(rows)} n={key[0]} k={key[1]} pass",
                flush=True,
            )

    if all_failures:
        print("acceptance check failed:", flush=True)
        for failure in all_failures:
            print(f"  {failure}", flush=True)
        return 1

    print(f"all {len(rows)} acceptance rows pass", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
