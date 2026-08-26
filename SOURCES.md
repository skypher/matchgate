# Source audit

Checked on 2026-08-25 against the linked primary sources.

## Matchgate commutator graph

Maxwell West, Neil Dowling, Angus Southwell, Martin Sevior, Muhammad Usman,
Kavan Modi, and Thomas Quella, “A graph-theoretic approach to chaos and
complexity in quantum systems,” SciPost Physics Core 8, 081 (2025),
[doi:10.21468/SciPostPhysCore.8.4.081](https://doi.org/10.21468/SciPostPhysCore.8.4.081)
([publisher PDF](https://www.scipost.org/SciPostPhysCore.8.4.081/pdf)).

- Section IV, Eqs. (50)–(51): vertices of Cκ are ordered κ-subsets of [2n],
  and graph edges change the coordinate ℓ¹ distance by one.
- Appendix C, Eq. (C2): the shortest-path distance is exactly
  ∑ᵢ|sᵢ−tᵢ|.
- Appendix C, Theorem 13 and Eq. (C9): A(κ,n) is the uniform pairwise mean of
  that distance.
- Appendix C, Conjecture 14: A(n,n)=ω(n) and A(n,n)=o(n²).
- Proposition 7 and Eq. (38): Haar-averaged graph complexity from a fixed
  Pauli vertex equals its mean distance to the component.
- Lemma 9 and its Appendix A proof, Eqs. (A78)–(A86): for a specified
  time-independent Hamiltonian H, its Liouvillian, and the Krylov basis
  generated from the initial Pauli string, graph complexity at time t is
  bounded above by that H-dependent Krylov complexity.

The transition from Eq. (A81) to Eq. (A82) in the cited proof is not used in
the manuscript: coefficient products in that display need not be nonnegative.
Corollary 5.2 instead gives a self-contained proof from the nested inclusions
between the Lanczos filtration and the graph-distance filtration.  The cited
lemma records the originating statement, while the projection argument in the
manuscript supplies the inequality used here.

These are two distinct statements. A Haar-distributed endpoint U†PU does not
by itself specify H or a Krylov basis. The manuscript therefore uses Eq. (38)
only for the Haar graph-complexity average and states Lemma 9 separately as a
pointwise Hamiltonian-dependent implication.

The recent paper formulates Conjecture 14; its Section II.A attributes the
introduction of commutator graphs to an earlier paper by Díaz et al.

## Token graphs of paths

Sofía Ibarra and Luis Manuel Rivera, “The automorphism groups of some token
graphs,” Proyecciones Journal of Mathematics 42 (2023), 1627–1651,
[doi:10.22199/issn.0717-6279-5954](https://doi.org/10.22199/issn.0717-6279-5954)
([publisher PDF](https://www.scielo.cl/pdf/proy/v42n6/0716-0917-proy-42-06-1627.pdf)).

- Section 1 defines the k-token graph Fₖ(Γ): vertices are k-subsets of V(Γ),
  and an edge moves one token along one edge of Γ to an unoccupied vertex.
- Lemma 5.2 gives, for ordered vertices u={u₁<⋯<uₖ} and v={v₁<⋯<vₖ} of
  Fₖ(Pₙ), the distance d(u,v)=∑ᵢ|vᵢ−uᵢ|.

Thus the matchgate component is an already studied graph family. The new use
in the manuscript is the matchgate identification and the asymptotic analysis
of its uniform pairwise distance, not the token-graph name or metric formula.

## Finite-population invariance principle

Bengt Rosén, “Limit theorems for sampling from finite populations,” Arkiv för
Matematik 5 (1965), 383–424,
[doi:10.1007/BF02591138](https://doi.org/10.1007/BF02591138).

- Page 384: a random permutation is uniform sampling without replacement.
- Page 398: W(σ²,T) is the tied-down Wiener process; at T=1 its covariance is
  σ²(min(s,t)−st), so W(1,1) is the standard Brownian bridge.
- Page 406, Remark 1 to Theorem 12.1: Noether’s condition is
  maxᵢ|aᵢ−μ|/(∑ᵢ(aᵢ−μ)²)¹ᐟ²→0.
- Theorem 13.1, pages 407–410: under Noether’s condition the linearly
  interpolated, standardized partial-sum process converges weakly in C[0,1]
  to W(1,1) when the full population is sampled.
- Theorem 3.1, page 386: convex functions of a sum sampled without
  replacement are bounded by the corresponding with-replacement expectation;
  this supplies the moment-generating-function bounds used for both the
  counting-process difference and M.

For a population of κₙ ones and 2n−κₙ zeros with κₙ/(2n)→ρ∈(0,1), Noether’s
condition is at most [2nρₙ(1−ρₙ)]⁻¹ᐟ²→0, so the cited functional theorem
applies exactly to the counting process used in the manuscript.

## Brownian and Bernoulli bridge areas

Svante Janson, “Brownian excursion area, Wright’s constants in graph
enumeration, and other Brownian areas,” Probability Surveys 4 (2007), 80–145,
[doi:10.1214/07-PS104](https://doi.org/10.1214/07-PS104).

- Section 20 defines the absolute Brownian-bridge area with the same standard
  bridge normalization used in the manuscript.
- Equation (135) and Table 2 on page 107 give its moments; in particular E𝒜=√(2π)/8 and
  E𝒜²=7/60.

Uwe Schwerdtfeger, “Linear functional equations with a catalytic variable and
area limit laws for lattice paths and polygons,” European Journal of
Combinatorics 36 (2014), 608–640,
[doi:10.1016/j.ejc.2013.10.004](https://doi.org/10.1016/j.ejc.2013.10.004).

- Section 14.2 derives absolute-area moments for Bernoulli walks and proves
  joint moment convergence with the endpoint after the m³ᐟ² and m¹ᐟ²
  rescalings.
- This is prior literature for the discrete bridge-area mechanism. The
  manuscript therefore attributes that mechanism and locates its distinct
  contribution in the matchgate finite-population application, fixed-density
  factor, exact central formula, and finite-size correction.

## One-dimensional Wasserstein and empirical-process context

Marco De Angelis and Ander Gray, “Why the 1-Wasserstein distance is the area
between the two marginal CDFs,” arXiv:2111.03570 (2021),
[doi:10.48550/arXiv.2111.03570](https://doi.org/10.48550/arXiv.2111.03570).

- The paper states and explains the one-dimensional identity equating W₁ with
  the area between cumulative distribution functions. Lemma 2.2 of the
  manuscript is its equal-weight lattice specialization.

Eustasio del Barrio, Evarist Giné, and Carlos Matrán, “Central limit theorems
for the Wasserstein distance between the empirical and the true
distributions,” Annals of Probability 27 (1999), 1009–1071,
[doi:10.1214/aop/1022677394](https://doi.org/10.1214/aop/1022677394).

- This is prior literature for Brownian-bridge limits and moment convergence
  of one-dimensional L¹ empirical-process/Wasserstein functionals.
- Its model is an i.i.d. empirical sample against the underlying distribution.
  The present manuscript instead compares two fixed-cardinality samples drawn
  without replacement from a growing finite population at nonzero sampling
  density; Rosén's finite-population bridge theorem supplies the different
  covariance factor.

## Novelty-search boundary

On 2026-08-25, searches covered the exact title and DOI of West et al.;
“Conjecture 14” with “matchgate”; “Brownian bridge” with “matchgate commutator
graph”; “A(n,n)” with “matchgate graph distance”; k-token graphs and symmetric
powers of paths combined with average distance or Wiener index; and empirical
Wasserstein/Brownian-bridge limits with sampling without replacement. These
searches located the prior metric and transport frameworks recorded above but
no separate resolution of the specific matchgate Conjecture 14. This records
the scope of the search rather than a guarantee of priority. The distinct
claims made in the manuscript are the matchgate application, its explicit
positive-density finite-population limit and variance, and the exact central
formula with its first finite-size correction.
