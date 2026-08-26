# Project goal

Prove the unconditional asymptotic theorem for average pairwise distance in
matchgate commutator-graph components and translate it to graph and Krylov
complexity.  The central component theorem must resolve Conjecture 14 of West
et al., *A graph-theoretic approach to chaos and complexity in quantum
systems* (arXiv:2502.16404).

For independent uniform \(\kappa_n\)-subsets
\(S=(s_1<\cdots<s_{\kappa_n})\) and
\(T=(t_1<\cdots<t_{\kappa_n})\) of \([2n]\), set
\[
D_n(S,T)=\sum_{i=1}^{\kappa_n}|s_i-t_i|.
\]
The main paper theorem is, whenever \(\kappa_n/(2n)\to\rho\in(0,1)\),
\[
\frac{D_n}{n^{3/2}}
 \Rightarrow 4\sqrt{\rho(1-\rho)}\int_0^1|B(t)|\,dt,
\qquad
\mathbb E D_n\sim
\frac{\sqrt{2\pi}}2\sqrt{\rho(1-\rho)}\,n^{3/2}.
\]
In particular, for the central component \(\kappa_n=n\),
\[
\frac{D_n}{n^{3/2}}\Rightarrow2\int_0^1|B(t)|\,dt,
\qquad
\mathbb E D_n\sim\frac{\sqrt{2\pi}}4n^{3/2}.
\]

## Priority order

1. Exact matchgate metric and discrete transport identity.
2. Brownian-bridge area limit with a justified expectation passage.
3. Fixed-density theorem and a variance or concentration estimate.
4. Exact translation to graph complexity and the cited Krylov bound.
5. Reproducible exact/numerical checks and finite-size analysis.
6. Novelty audit and final paper integration.

The default deliverable is a paper proof.  Do not work on Lean unless the user
explicitly requests it.
