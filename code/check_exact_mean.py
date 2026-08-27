#!/usr/bin/env python3
"""Replay the exact-mean acceptance table with explicit numerical tolerances."""

from __future__ import annotations

import argparse
import csv
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
