# Source audit

Checked through 2026-09-01 against the linked primary sources.

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

Lemma 5.1 of the manuscript independently derives the matchgate specialization
of Proposition 7 from adjacent Majorana exchanges, Haar invariance, and
Parseval's identity; the citation records the originating general statement.

The transition from Eq. (A81) to Eq. (A82) in the cited proof is not used in
the manuscript: coefficient products in that display need not be nonnegative.
Corollary 5.3 instead gives a self-contained proof from the nested inclusions
between the Lanczos filtration and the graph-distance filtration.  The cited
lemma records the originating statement, while the projection argument in the
manuscript supplies the inequality used here.

These are two distinct statements. A Haar-distributed endpoint U†PU does not
by itself specify H or a Krylov basis. The manuscript therefore uses Eq. (38)
only for the Haar graph-complexity average and states Lemma 9 separately as a
pointwise Hamiltonian-dependent implication.

The recent paper formulates Conjecture 14; its Section II.A attributes the
introduction of commutator graphs to an earlier paper by Díaz et al.

N. L. Diaz, Diego García-Martín, Sujay Kazi, Martin Larocca, and M. Cerezo,
“Showcasing a Barren Plateau Theory Beyond the Dynamical Lie Algebra,”
arXiv:2310.11505 (2023),
[doi:10.48550/arXiv.2310.11505](https://doi.org/10.48550/arXiv.2310.11505).

- West et al., Section II.A, identifies this paper as the source that
  introduced the commutator graph for free-fermionic trainability.

## Rectangular minuscule lattices and the prior distance theorem

Colin Defant, Valentin Féray, Philippe Nadeau, and Nathan Williams, “Wiener
Indices of Minuscule Lattices,” Electronic Journal of Combinatorics 31(1),
P1.41 (2024),
[doi:10.37236/12002](https://doi.org/10.37236/12002)
([publisher PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i1p41/pdf/)).

- Section 1.3 defines \(P_{m,k}=J([m]\times[k])\), whose elements are lattice
  paths with \(m\) up-steps and \(k\) down-steps. Its Hasse graph is isomorphic
  to the token graph \(F_m(P_{m+k})\): an adjacent up/down swap adds or removes
  one cell of the order ideal.
- Their Eq. (2) is \(d(p,q)=\frac12\sum_i|p_i-q_i|\). For the membership path
  of a subset \(S\), \(p_i=2C_S(i)-i\), so this distance is exactly
  \(\sum_i|C_S(i)-C_T(i)|=D_{N,k}(S,T)\).
- Corollary 3 gives the ordered-pair Wiener index
  \[
  d(P_{m,k})=\frac{mk}{4m+4k+2}
  \binom{2m+2k+2}{2k+1}.
  \]
  Dividing by \(\binom{m+k}{k}^2\) gives the exact uniform pairwise mean used
  in the manuscript. In matchgate notation this is
  \[
  \mathbb E D_{N,k}=\frac{k(N-k)}{4N+2}
  \frac{\binom{2N+2}{2k+1}}{\binom Nk^2}.
  \]
- Proposition 5 proves convergence in distribution and in moments for the
  distance in an \((\alpha n)\times n\) rectangle:
  \[
  n^{-3/2}D_{\alpha,n}\Rightarrow
  \sqrt{2\alpha(1+\alpha)}\int_0^1|B(t)|\,dt.
  \]
  With \(\alpha=\rho/(1-\rho)\), take the second rectangle dimension to be
  \(N-k\).  Since \((N-k)/n\to2(1-\rho)\), conversion to the manuscript's
  \(n^{-3/2}\) normalization multiplies the limiting coefficient by
  \([2(1-\rho)]^{3/2}\), giving \(4\sqrt{\rho(1-\rho)}\). Moment convergence
  also supplies the mean and variance constants for fixed-aspect rectangles.
  At \(\alpha=1\), it gives the central law and Conjecture 14 after applying
  West et al.'s matchgate-component identification.

This 2024 result predates the matchgate conjecture and is the direct prior
mathematical theorem. The manuscript's distinct roles are to make the
matchgate/minuscule-lattice implication explicit, give an independent
finite-population proof for arbitrary density sequences, derive the stated
matchgate complexity consequences, and supply the projection proof of the
graph--Krylov inequality.

## Token graphs of paths

Ruy Fabila-Monroy, David Flores-Peñaloza, Clemens Huemer, Ferran Hurtado,
Jorge Urrutia, and David R. Wood, “Token graphs,” Graphs and Combinatorics 28
(2012), 365–380,
[doi:10.1007/s00373-011-1055-9](https://doi.org/10.1007/s00373-011-1055-9).

- This paper introduces the k-token graph Fₖ(G): its vertices are the
  k-subsets of V(G), and adjacency moves one token along an edge of G to an
  unoccupied vertex.

Koenraad M. R. Audenaert, Chris Godsil, Gordon Royle, and Terry Rudolph,
“Symmetric squares of graphs,” Journal of Combinatorial Theory, Series B 97
(2007), 74–90,
[doi:10.1016/j.jctb.2006.04.002](https://doi.org/10.1016/j.jctb.2006.04.002).

- This paper treats the equivalent symmetric-power graph construction and its
  quantum-mechanical interpretation.

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

Wassily Hoeffding, “Probability inequalities for sums of bounded random
variables,” Journal of the American Statistical Association 58 (1963), 13–30,
[doi:10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).

- Theorem 4 compares convex functions of sums sampled without replacement to
  their with-replacement counterparts. The manuscript uses this result for
  moment-generating-function bounds, with Rosén's Theorem 3.1 supplying the
  same formulation.

Bengt Rosén, “Limit theorems for sampling from finite populations,” Arkiv för
Matematik 5 (1965), 383–424,
[doi:10.1007/BF02591138](https://doi.org/10.1007/BF02591138).

- Page 384: a random permutation is uniform sampling without replacement.
- Page 398: W(σ²,T) is the tied-down Wiener process; at T=1 its covariance is
  σ²(min(s,t)−st), so W(1,1) is the standard Brownian bridge.
- Page 406, Remark 1 to Theorem 12.1: Noether’s condition is
  maxᵢ|aᵢ−μ|/(∑ᵢ(aᵢ−μ)²)¹ᐟ²→0.
- Theorem 13.1, pages 408–411: under Noether’s condition the linearly
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

- Section 12.2 derives absolute-area moments for Bernoulli walks and proves
  joint moment convergence with the endpoint after the m³ᐟ² and m¹ᐟ²
  rescalings.
- This is prior literature for the discrete bridge-area mechanism. The
  manuscript therefore attributes that mechanism and locates its distinct
  contribution in the explicit matchgate/minuscule-lattice application, the
  independent finite-population proof for arbitrary density sequences, and
  the graph- and Krylov-complexity consequences.

## Operator Krylov complexity

Daniel E. Parker, Xiangyu Cao, Alexander Avdoshkin, Thomas Scaffidi, and Ehud
Altman, “A universal operator growth hypothesis,” Physical Review X 9 (2019),
041017,
[doi:10.1103/PhysRevX.9.041017](https://doi.org/10.1103/PhysRevX.9.041017).

- Section III, Eqs. (3)–(8), gives the infinite-temperature
  Hilbert–Schmidt operator space, Liouvillian, Lanczos recursion, and Krylov
  amplitudes. Section V.A, Eq. (26), defines the Krylov position expectation.
  The manuscript uses the same ∑ⱼ j|dⱼ(t)|² convention and proves its matchgate
  graph comparison directly.

## One-dimensional Wasserstein and empirical-process context

S. S. Vallender, “Calculation of the Wasserstein Distance Between Probability
Distributions on the Line,” Theory of Probability and Its Applications 18
(1974), 784–786,
[doi:10.1137/1118101](https://doi.org/10.1137/1118101).

- This is the classical source for the one-dimensional Wasserstein formula.
  The manuscript uses its equal-mass lattice specialization and also gives a
  self-contained proof in Lemma 2.2.

S. S. Vallender, “Addendum: Calculation of the Wasserstein Distance Between
Probability Distributions on the Line,” Theory of Probability and Its
Applications 26 (1982), 435,
[doi:10.1137/1126051](https://doi.org/10.1137/1126051).

- The addendum corrects Remark 1 and formula (3) of the original note. It does
  not change the one-dimensional CDF-area identity used in the manuscript.

Marco De Angelis and Ander Gray, “Why the 1-Wasserstein distance is the area
between the two marginal CDFs,” arXiv:2111.03570 (2021),
[doi:10.48550/arXiv.2111.03570](https://doi.org/10.48550/arXiv.2111.03570).

- The paper states and explains the one-dimensional identity equating W₁ with
  the area between cumulative distribution functions. Lemma 2.2 of the
  manuscript is its equal-weight lattice specialization.

Rebecca Bourn and Jeb F. Willenbring, “Expected Value of the One-Dimensional
Earth Mover’s Distance,” Algebraic Statistics 11 (2020), 53–78,
[doi:10.2140/astat.2020.11.53](https://doi.org/10.2140/astat.2020.11.53).

- This paper first studies one-dimensional earth mover distance for uniform
  weak compositions of a fixed integer and then passes to a uniform
  probability-simplex law.
- A stars-and-bars word is simultaneously a weak composition of `k` into
  `N-k+1` parts and a `k`-subset of `[N]`. Under this bijection the cumulative
  histogram discrepancy is exactly the subset distance `D_{N,k}` by the
  discrete transport identity. Thus the discrete sampling laws are the same
  after the parameter change, not different laws.

Rebecca Bourn and William Q. Erickson, “Palindromicity of the Numerator of a
Statistical Generating Function,” Discrete Mathematics 348 (2025), 114336,
[doi:10.1016/j.disc.2024.114336](https://doi.org/10.1016/j.disc.2024.114336)
([arXiv version](https://arxiv.org/pdf/2307.02652)).

- Section 3 interprets the discrete earth mover distance through symmetric
  differences of Young diagrams.
- Theorem 4.3 uses the Type A minuscule-lattice Wiener formula of Defant et al.
  to give
  \[
  \mathbb E\operatorname{EMD}
  =\frac{s(b-1)}{4s+4b-2}
   \frac{\binom{2s+2b}{2s+1}}{\binom{s+b-1}{s}^2}
  \]
  for uniform weak compositions of `s` into `b` parts. Setting `s=k` and
  `b=N-k+1` gives exactly
  \[
  \mathbb E D_{N,k}
  =\frac{k(N-k)}{4N+2}
   \frac{\binom{2N+2}{2k+1}}{\binom Nk^2}.
  \]
- The manuscript therefore does not claim the discrete EMD closed form or the
  Young-diagram symmetric-difference viewpoint as new. Its Proposition 6.3 is
  a different conditional identity: it conditions on `M=|S\setminus T|` and
  factors the expectation into a simple-walk bridge area and exchangeable
  active-site gaps.

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
- The article has a correction in Annals of Probability 31 (2003), 1142–1143,
  [Project Euclid: aop/1048516548](https://projecteuclid.org/journals/annals-of-probability/volume-31/issue-2/Correction--Central-limit-theorems-for-the-Wasserstein-distance-between/aop/1048516548.pdf).
  The correction concerns Proposition 6.4 and later heavy-tail results; those
  statements are not used in the manuscript. The Project Euclid identifier is
  not a registered DOI.

## Stirling remainder

*NIST Digital Library of Mathematical Functions*, Release 1.2.7 of
2026-06-15, [Section 5.11](https://dlmf.nist.gov/5.11).

- Equation (5.11.1) gives the logarithmic Stirling series. Section 5.11(ii)
  states that for positive real arguments its remainder has the sign of and is
  bounded in magnitude by the first neglected term. Applied to
  log(m!)=log m+log Γ(m), this supplies the O(m⁻⁵) remainder used for the
  finite-size expansion.

## Novelty-search boundary

The initial 2026-08-25 search used matchgate and token-graph terminology and
missed the rectangular-minuscule-lattice formulation.  A referee audit on
2026-08-31 added searches for rectangular minuscule lattices, Hasse-diagram
Wiener indices, lattice-path distance, and expected one-dimensional earth
mover distance.  Those searches located Defant et al., whose Corollary 3 and
Proposition 5 are the direct prior exact-mean and Brownian-bridge results for
the same graphs.  A further audit on 2026-09-01 located Bourn and Erickson,
whose Theorem 4.3 records the same closed mean in discrete EMD notation and
whose Section 3 supplies the prior Young-diagram symmetric-difference
interpretation.

Accordingly, the manuscript does not claim priority for the fixed-aspect-ratio
Brownian-bridge law, its moment limits, the closed pairwise mean, or the
central correction obtained from that closed form.  Its distinct claims are
the explicit matchgate/minuscule-lattice identification and resulting
application to Conjecture 14; an independent finite-population proof valid for
every density sequence; the Haar matchgate specialization; the projection
proof of the graph--Krylov comparison; and the central conditional-on-
`|S\setminus T|` bridge-and-gap identity as a distinct exact formula.  This
records the scope of the search rather than a guarantee that no other
overlapping work exists.
