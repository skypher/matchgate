# Hard-target roadmap

The four fixed buckets below measure final-facing theorem closure.  They do not
credit outlines, interfaces, or manuscript polish.

| Weight | Final-facing obligation | Acceptance check | Status |
|---:|---|---|---|
| 15% | Matchgate metric and transport identity | Exact graph distance is identified with the cumulative-count area | Closed in Proposition 2.1 and Lemma 2.2 of `paper/main.tex` |
| 45% | Central Brownian-area theorem | Distributional limit and expectation constant follow with uniform integrability | Closed in Theorem 4.1; the moment bounds and Brownian-area normalization pass the end-to-end check |
| 20% | Fixed density and fluctuations | General \(\rho\) constants and the variance asymptotic are proved | Closed in Theorem 4.1 and Proposition 3.2 |
| 20% | Matchgate/complexity integration | Conjecture 14 and the Haar graph asymptotic are proved; the Krylov implication is stated separately for a specified Hamiltonian, Liouvillian, time, and Lanczos basis; reproducible checks agree | Closed in Corollaries 4.2, 5.1, and 5.2, Proposition 6.2, Theorem 6.4, `SOURCES.md`, and `results/exact_mean.tsv` |

Overall hard-target meter: **100% theorem-slot closure** (15% + 45% + 20% +
20%). Acceptance basis: the current two-pass build from 2026-08-26 exits
successfully, and its final pass and `build/main.log` contain no LaTeX warnings
or unresolved references; all 45 labels and all 73 reference/citation uses
resolve; the two independent finite-sum evaluations agree on the recorded
central cases; and fresh replays at ρ=1/2, 1/4, and 1/10 approach their stated
constants. The novelty-search boundary, including the token-graph and
one-dimensional Wasserstein literature, is the qualified statement in
`SOURCES.md`.
