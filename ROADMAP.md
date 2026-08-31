# Hard-target roadmap

The four fixed buckets below measure final-facing theorem closure.  They do not
credit outlines, interfaces, or manuscript polish.

| Weight | Final-facing obligation | Acceptance check | Status |
|---:|---|---|---|
| 15% | Matchgate metric and transport identity | Exact graph distance is identified with the cumulative-count area | Closed in Proposition 2.1 and Lemma 2.2 of `paper/main.tex` |
| 45% | Central Brownian-area theorem | Distributional limit and expectation constant follow with uniform integrability | Closed in Theorem 4.1; the moment bounds and Brownian-area normalization pass the end-to-end check |
| 20% | Fixed density and fluctuations | General \(\rho\) constants and the variance asymptotic are proved | Closed in Theorem 4.1 and Proposition 3.2 |
| 20% | Matchgate/complexity integration | The prior rectangular-minuscule-lattice theorem is explicitly connected to Conjecture 14; the independent Haar graph asymptotic and the Krylov implication are proved for an explicitly specified Hamiltonian, Liouvillian, time, and Lanczos basis; reproducible checks agree | Closed in Proposition 2.1, Corollary 4.2, Lemma 5.1, Corollaries 5.2 and 5.3, Propositions 6.1, 6.3, and 6.5, Theorem 6.4, `SOURCES.md`, and `results/exact_mean.tsv` |

Overall hard-target meter: **100% theorem-slot closure** (15% + 45% + 20% +
20%). Acceptance basis: the current two-pass build from 2026-08-31 exits
successfully, and its final pass and `build/main.log` contain no LaTeX warnings
or unresolved references. `make check-exact-mean` passes the exact rational
metric, transport, hypergeometric, published closed-form, bridge-area, and
central-mean checks and all 14 recorded floating-point rows; the two
independent finite-sum evaluations agree on the central cases, and the ρ=1/2,
1/4, and 1/10 rows approach their stated constants. The source audit in
`SOURCES.md` records the direct prior rectangular-minuscule-lattice theorem
and bounds the manuscript's novelty claims accordingly.
