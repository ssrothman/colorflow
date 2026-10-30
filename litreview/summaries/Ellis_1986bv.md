# Soft Radiation in Parton-Parton Scattering
- **ID / links:** Ellis:1986bv · INSPIRE 233672 · arXiv — · DOI 10.1016/0550-3213(87)90456-1 (erratum: Nucl. Phys. B294 (1987) 1180, DOI 10.1016/0550-3213(87)90629-8)
- **Authors / collab, year, journal:** R.K. Ellis, G. Marchesini, B.R. Webber, 1987, Nucl. Phys. B286 (1987) 643–656
- **Type:** theory
- **Relevance:** 3 · RQs: 1b, 1d, 2 (indirectly 4)
- **Full text source:** zotero

## Takeaways
- Explicit soft-gluon (eikonal) decomposition (priority "first" [unverified]) of all 2→3 parton processes in hadron–hadron scattering into colour-flow "antennae" [ij], including interference between incoming (spacelike) and outgoing (timelike) partons (Eqs. 8, 11–17).
- After azimuthal averaging, each antenna [ij] splits into two angular-ordered cones (Eqs. 18–20). Around every hard parton i there is a cone bounded by the nearest *other hard parton* (θ_i < θ_ij), inside which emission is plain bremsstrahlung 2C_i g²/(k²ζ_i) × H (Eqs. 5, 22). Beyond it, at leading N, emission continues into larger cones bounded by *colour-connected* partners (p. 650, Eq. 34).
- At leading order in N_c, colour-unconnected pairs contribute no antenna. Example: in qq̄→γ*g there is no (12) term, so no leading-N radiation fills the region between the two incoming beams (Eq. 21, p. 650; Fig. 1, p. 651). Unconnected regions get only O(1/N²) terms, which have no collinear singularities.
- Where the hard process has several leading-N colour flows (identical quarks Eq. 25, qq̄→gg Eq. 28; gg→gg Eq. 30 is written as a sum over pairings with H₁^(d) weights rather than explicitly as flows), the cone contributions carry kinematics-dependent weights, which the paper states are positive at least at leading N (Eq. 34) and checks explicitly for Eqs. 26, 31–33. This gives the initial-condition prescription (HERWIG use is later work, not in this paper; ref. [5] is "work in progress"): choose the colour flow / cone for each leg with these probabilities, then run independent angular-ordered showers (backward for initial state, forward for final state) (Eq. 34, p. 655).
- No observable or data comparison. The paper implies depleted soft radiation between partons that are not colour-connected (it calls process (E) "most closely analogous to e⁺e⁻→qq̄g", p. 650; the "string/drag effect" framing is the summariser's). Reviewer context, not in the paper: this underlies later Tevatron colour-coherence tests in multijet and W+jet events.

## Setup
- Processes: all 2→3 QCD processes at O(g⁶), (A) qq'→qq'g, (B) qq→qqg, (C) qq̄→ggg, (D) gg→ggg; the others follow by crossing. Also radiative Drell–Yan (E) qq̄→γ*gg (Eqs. 6–7). Exact matrix elements are taken from Berends et al., Kunszt–Pietarinen, Gottschalk–Sivers and Ellis–Gonsalves (ref. [12,14], p. 646).
- Method: take the soft limit k→0 of the exact |M|², written as Σ_ij [ij] A_ij with eikonal factor [ij] = g² p_i·p_j/(p_i·k k·p_j) (Eqs. 3–4). Rewrite it with ζ_i = 1−cos θ_i (Eq. 18) and average over the azimuth about each parton, which turns [ij] into (ij)+(ji) with step functions Θ(ζ_ij−ζ_i) (Eqs. 19–20). Then classify the angular regions around parton 1 (Tab. 2).
- Approximations: soft (eikonal) limit, azimuthal averaging, SU(N) colour with leading-N (large-N_c) truncation. Terms of relative order 1/N² (sometimes 1/N) are dropped outside the collinear cones (pp. 650–654). No hadronization, no numerics.

## Results
- **General structure:** for each of the four hard partons there is a cone θ_i < θ_ij (j = nearest other hard parton) in which radiation is exactly Σ|M^(H)|² → (2g²C_i/k²)(1/(1−cos θ_i)) Σ|M^(h)|², with C_i = C_F (quark) or C_A (gluon). Only these four contributions are collinear-singular (Eq. 5, p. 645).
- **Process (A) qq'→qq'g** (Eq. 8): soft limit = H^(a) × {2C_F([14]+[23]) + (1/N)[12;34]}. [12;34] = 2[12]+2[34]−[13]−[14]−[23]−[24] has no collinear singularities (Eq. 9). The colour flow is unique (t-channel, Fig. 2), and the antennae connect incoming 1 to outgoing 4 and incoming 2 to outgoing 3. In angular-ordered form (Eqs. 23–24) each cone is bounded by the colour-connected parton, up to O(N⁻²) corrections (p. 651).
- **Process (B) identical quarks** (Eqs. 11–12): the soft limit is not a single H × eikonal sum. Two leading-N flows exist: t-channel (Fig. 2) with weight H^(a)(s,t,u) − H₁^(b)/N, and u-channel (Fig. 3) with weight H^(a)(s,u,t) − H₁^(b)(s,u,t)/N (Eq. 25). For quark 1 with θ₁₃<θ₁₄ (Tab. 2):
  - region 1 (θ₁ < all θ_1j): plain bremsstrahlung (Eq. 22);
  - region 2 (θ₁₃<θ₁<θ₁₂,θ₁₄): a leading-N contribution W₁^(B)(2) = g²/(Nk²ζ₁){N²H^(a)(s,t,u) − 2NH₁^(b)(s,u,t) + H^(a)(s,u,t)}, positive-definite for all N (Eq. 26);
  - region 3: 2g²C_F H^(a)(s,t,u)/(k²ζ₁);
  - regions 4, 5: zero at leading N, after dropping terms of relative order N⁻¹ (Eq. 27, p. 653). Region 6 is kinematically excluded (Tab. 2, p. 653; footnote on p. 652).
- **Process (C) qq̄→gg(+g)** (Eqs. 13, 28): two leading-N flows (Fig. 4a,b). Outside the primary cone, the H₁^(c), H₂^(c) terms cancel the flow in which parton 1 is not connected to the relevant direction. For quark 1 in regions 2, 3: W₁^(C)(2,3) = (2g⁶C_F/k²ζ₁)(N/2)t²(1/tu − 2/s²). This has no t-channel pole, which reflects the cancellation of flow 4a (Eq. 29, p. 654). W₁^(C)(4,5)=0 at leading N.
- **Process (D) gg→ggg** (Eqs. 14–15, 30): a symmetric (2/3)C_A Σ over all pairs plus C_A H₁^(d) terms for the three pairings, with H₁^(d)(s,t,u)+H₁^(d)(t,s,u)+H₁^(d)(u,t,s)=0. Outside-cone radiation from gluon 1 is given explicitly for region 2 (Eq. 31) and regions 3, 4 (Eqs. 32–33). The authors state all of these are positive and so can be used as probabilities.
- **Radiative Drell–Yan (E)** (Eqs. 16–17, 21): W^(E) = {2C_F[(14)+(24)] + C_A[(41)+(42)] + (1/N)[(14)−(12)+(24)−(21)]} H. Interpretation: radiation from the incoming q is confined to θ₁<θ₁₄ and from q̄ to θ₂<θ₂₄. The outgoing gluon radiates half into the cone bounded by each incoming parton. The correction of relative order N⁻² lives in θ₁₄<θ₁<θ₁₂ and θ₂₄<θ₂<θ₂₁ and has no collinear singularity. There is no (12)/(21) term at leading N because q and q̄ are not colour-connected (p. 650; Fig. 1, p. 651).
- **General formula and MC prescription:** W_i^(H) = (2C_i g²/k²ζ_i) Σ_{j: θ_i<θ_ij} A_ij^(h). The authors claim it is positive at least at leading N and so defines probabilities for the first emission into cones (Eq. 34). They propose:
  1. choose the hard 2→2 process from PDFs and cross sections;
  2. choose a cone for each external line with these probabilities;
  3. evolve each line independently by angular ordering (backward for incoming, forward for outgoing).
  They claim this "should incorporate correctly all leading infrared logarithms" at large N. Replacing the soft singularity with the full Altarelli–Parisi function adds the leading collinear logs (p. 655).
- **Erratum** (NPB294 (1987) 1180): Table 1 entry H₁^(c)(s,t,u) should read (1/4)g⁴N(t²+u²)[(1−2/N²)/(tu) − 2/s²]. The printed version had C_F and (1−1/N²).

## Assessment
- This is the theoretical foundation of colour-coherent initial conditions for hadron-collider parton showers (the HERWIG approach). It is the direct prerequisite for interpreting Tevatron/LHC colour-coherence measurements, e.g. the η/φ distribution of a soft third jet around the second jet, and soft-radiation patterns in W+jet. It is not itself an RQ4 proposal: no hadron-level observable, no numbers, no figures beyond colour-flow diagrams.
- The key physics claim is that soft radiation follows colour-connected dipoles that cross the initial/final boundary. For distinguishable quarks the flow is unique (t-channel), so radiation should be enhanced between beam 1 and jet 4 and depleted between the two beams. This is a clean qualitative prediction that experiments can test.
- Limitations:
  - Leading-N_c only. Outside the collinear cones, 1/N and 1/N² interference terms are dropped. For (B) and (D) the separation into flows is partly a matter of choice. Positivity is asserted for leading N (and for Eq. 26 at all N), not proven in general.
  - The azimuthal averaging discards the azimuthal anisotropy that actually produces the "drag" effect within cones. That anisotropy is exactly what observables like jet pull or third-jet azimuthal distributions probe. So the angular-ordered MC reproduces the coherence pattern only on average, and the full antenna [ij] (Eq. 18) contains more information than the shower keeps. This bears on later comparisons of angular-ordered vs dipole showers in coherence tests.
  - Only one soft gluon (2→3). Multiple soft emission and non-global effects are assumed to follow from independent angular-ordered evolution. The paper does not address subleading-colour (Coulomb/Glauber) phases, which later work (factorisation breaking, super-leading logs) showed to matter for initial-final interference.
- Superseded or extended in practice by Marchesini & Webber's general hard-process HERWIG paper (1988) and later by dipole/antenna showers (Ariadne, Pythia 8 interleaved, Vincia). The erratum only affects H₁^(c), not the conceptual results.

## Leads
- G. Marchesini, B.R. Webber, Nucl. Phys. B238 (1984) 1, coherent timelike shower MC (ref. [7]). The base algorithm this paper extends to hadron collisions.
- S. Catani, M. Ciafaloni, G. Marchesini, Nucl. Phys. B264 (1986) 588, angular ordering for spacelike (initial-state) radiation (ref. [6]). The prerequisite for the initial-state cones.
- Ya.I. Azimov, Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, Phys. Lett. B165 (1985) 147 (ref. [13]), the perturbative string/drag effect from eikonal antenna patterns, i.e. the e⁺e⁻ counterpart of this paper.
- A. Bassetto, M. Ciafaloni, G. Marchesini, Phys. Rep. 100 (1983) 201 (ref. [1]), review of jet structure and coherence/angular ordering.
- A.H. Mueller, Phys. Lett. B104 (1981) 161, and B.I. Ermolaev, V.S. Fadin, JETP Lett. 33 (1981) 285 (refs. [2,4]), the original soft-gluon coherence / angular-ordering papers.
- T. Sjöstrand, Phys. Lett. B157 (1985) 321 (ref. [11]), backward evolution for initial-state showers.
- B.R. Webber, Ann. Rev. Nucl. Part. Sci. 36 (1986) 253 (ref. [9]), review of MC with coherence and cluster hadronization.
- Not cited in the paper, a natural follow-up: G. Marchesini, B.R. Webber, Nucl. Phys. B310 (1988) 461, "Monte Carlo simulation of general hard processes with coherent QCD radiation", the HERWIG implementation of this prescription. Also the Tevatron colour-coherence measurements (CDF 1994, D0 1997) that test it.

## Verification
Checked 2026-10-30 by an independent reader: 46 claims checked, 7 corrected, 1 unverifiable.
- Takeaway 2: the plain-bremsstrahlung cone (Eq. 5) is bounded by the nearest *other hard parton*, not the nearest colour-connected one; colour-connected partners bound the larger leading-N cones.
- Takeaway 4: softened. The paper asserts positivity only "at least to leading order in N" (Eq. 34), checked explicitly for Eqs. 26, 31–33. Eq. 30 is not written as explicit colour flows. HERWIG use is later work (ref. [5] is "work in progress").
- Takeaway 5: the "string/drag effect" analogy and Tevatron follow-up are marked as reviewer context, not the paper's claims.
- Fig. 1 is on p. 651 (the text discussing it is on p. 650). Region 6 is excluded in Tab. 2 (p. 653), with the footnote on p. 652. Eq. 27 drops terms of relative order N⁻¹.
- Process (E): the N⁻² term also covers θ₂₄<θ₂<θ₂₁.
- Typo: Kunszt (not Kunzst).
- Unverifiable: whether this is the "first" such decomposition.
