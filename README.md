# Brownian-bridge scaling of distances in matchgate commutator graphs

This repository develops a paper proof of the Brownian-bridge area law for
average distances in matchgate commutator-graph components and its consequence
for graph complexity averaged over both the initial vertex and a Haar matchgate
unitary.  The main source is [`paper/main.tex`](paper/main.tex).  Exact
finite-size expectation checks are implemented in
[`code/exact_mean.cpp`](code/exact_mean.cpp).

For κₙ/(2n)→ρ∈(0,1), the manuscript gives the distributional limit, the mean
constant, and
Var(D₂ₙ,κₙ)∼ρ(1−ρ)(28/15−π/2)n³. It also gives the exact central mean and
its first n¹ᐟ² correction. The Haar-averaged graph-complexity consequence is
stated separately from the Hamiltonian-dependent pointwise inequality between
graph and Krylov complexity.

Build the manuscript with pdfLaTeX:

```sh
make paper
```

Build and run the exact expectation checker with:

```sh
make exact-mean
./build/exact_mean 100 200 400 800
```

Run exact rational small-case checks and replay every recorded floating-point
acceptance row with tolerance checks using Python 3:

```sh
make check-exact-mean
```

The archived manuscript revision is tagged
[`paper-2026-08-31`](https://github.com/skypher/matchgate/tree/paper-2026-08-31).

The recorded table was generated with GCC 13.3.0 using C++20 and OpenMP. The
program evaluates exact finite-sum identities with `long double`, `lgammal`,
and normalized exponential weights; its decimal outputs are floating-point
approximations rather than certified intervals.

Each command-line argument is the number of matchgate sites \(n\); the checker
uses the central component \(\kappa=n\) unless `--rho` is supplied.

For the central component, the program evaluates the mean in two independent
ways: the cumulative hypergeometric formula and the symmetric-difference
bridge formula.  It also reports the observed coefficient of the \(\sqrt n\)
correction, whose theorem value is \(-5\sqrt{2\pi}/64\).

Recorded acceptance outputs are in [`results/exact_mean.tsv`](results/exact_mean.tsv),
and the source-level citation audit is in [`SOURCES.md`](SOURCES.md).
