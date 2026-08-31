# Hard-target roadmap

The four fixed buckets below measure final-facing theorem closure.  They do not
credit outlines, interfaces, or manuscript polish.

| Weight | Final-facing obligation | Acceptance check | Status |
|---:|---|---|---|
| 15% | Matchgate metric and transport identity | Exact graph distance is identified with the cumulative-count area | Closed in Proposition 2.1 and Lemma 2.2 of `paper/main.tex` |
| 45% | Central Brownian-area theorem | Distributional limit and expectation constant follow with uniform integrability | Closed in Theorem 4.1; the moment bounds and Brownian-area normalization pass the end-to-end check |
| 20% | Fixed density and fluctuations | General \(\rho\) constants and the variance asymptotic are proved | Closed in Theorem 4.1 and Proposition 3.2 |
| 20% | Matchgate/complexity integration | Conjecture 14 and the Haar graph asymptotic are proved; the Krylov implication is proved separately by the graph/Krylov filtration comparison for an explicitly specified Hamiltonian, Liouvillian, time, and Lanczos basis; reproducible checks agree | Closed in Corollary 4.2, Lemma 5.1, Corollaries 5.2 and 5.3, Proposition 6.2, Theorem 6.4, `SOURCES.md`, and `results/exact_mean.tsv` |

Overall hard-target meter: **100% theorem-slot closure** (15% + 45% + 20% +
20%). Acceptance basis: the current two-pass build from 2026-08-31 exits
successfully, and its final pass and `build/main.log` contain no LaTeX warnings
or unresolved references. `make check-exact-mean` passes the exact rational
metric, transport, hypergeometric, bridge-area, and central-mean checks and all
14 recorded floating-point rows; the two independent finite-sum evaluations
agree on the central cases, and the ρ=1/2, 1/4, and 1/10 rows approach their
stated constants. The novelty-search boundary, including the token-graph and
one-dimensional Wasserstein literature, is the qualified statement in
`SOURCES.md`.
