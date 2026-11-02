# Colour Reconnection from Soft Gluon Evolution
- **ID / links:** Gieseke:2018gff · INSPIRE 1689160 · arXiv 1808.06770 · DOI 10.1007/JHEP11(2018)149
- **Authors / collab, year, journal:** S. Gieseke, P. Kirchgaeßer, S. Plätzer, A. Siódmok, 2018, JHEP 11 (2018) 149 (KA-TP-23-2018, MCnet-18-22, HERWIG-2018-02). Read from arXiv v1 (21 Aug 2018).
- **Type:** theory / MC/model (toy studies; no data comparison)
- **Relevance:** 3 · RQs: 1, 2
- **Full text source:** arxiv

Page numbers below are the printed page numbers (PDF page = printed + 1).

## Takeaways
- Gives a perturbative basis for CR. The cluster colour state |τ⟩ is evolved with the one-loop soft anomalous dimension: a matrix exponential of T_i·T_j (α_s/2π)(½ln²(M_ij²/μ²) − iπ ln(M_ij²/μ²)) (Eq. 4.2). The probability of reconnecting to another colour flow |σ⟩ is |⟨σ|U|τ⟩|² / Σ_ρ|⟨ρ|U|τ⟩|² (Eqs. 4.3–4.4). The colour-flow basis is non-orthogonal (⟨ij|ij⟩ = N², ⟨ij|ji⟩ = N; p. 8).
- The ansatz on its own prefers colour flows with lower cluster masses and smaller rapidity separation between the q and q̄ of a cluster (Figs. 2, 4, 5, pp. 10–12). No mass-ordering veto is imposed (p. 11). The authors call this "strong support for geometric models considered earlier" (abstract); p. 20 says it "confirms earlier work on geometrically inspired reconnection models [15]", i.e. the baryonic/geometric CR of Gieseke:2017clv. The old Herwig plain CR is contrasted with these (p. 19).
- In the solvable two-cluster case, p_rec = 1/10 at minimal mixing (U_21 = 0) and 9/10 at maximal mixing (U_11 = 0) (Eq. 5.6, p. 8). These are not strict bounds: per-event p_rec spans ≈0 to ≈0.85 at √s = 3000 GeV (Fig. 11, p. 16). As a function of M_i/M_f (sum of initial over alternative cluster masses), p_rec rises smoothly from ≈0.1 to a plateau of ≈0.9 (√s = 3000 GeV) or ≈0.8 (√s = 10 GeV) (Fig. 15, p. 20). The old Herwig plain CR instead uses a step function with a flat tuned probability (p. 19).
- In 4- and 5-cluster systems the most common outcome is a single transposition, i.e. a reconnection within one pair of clusters (Fig. 13, p. 18). The authors read this as evidence that small subsystems evolve independently. They argue CR is therefore "not simply a 1/N suppressed effect" (p. 18).
- Baryonic reconnections come out naturally (Eqs. 4.5–4.10). The mean probability is ~2–12% and rises with the number of clusters (Fig. 6, p. 12). It is strongly enhanced when the three quarks (and three antiquarks) are close in ΔR (Fig. 8, p. 14). The reverse process ("unbaryonization") is also computed (Fig. 9, p. 15). It is absent from existing baryonic-CR models (p. 21).

## Setup
- **Framework:** amplitude-level soft-gluon evolution in the colour-flow basis (Eqs. 3.1–3.2). The infrared renormalisation operator Z gives the evolution equation (3.4). The one-loop soft anomalous dimension Γ = Σ(−T_i·T_j)Γ_cusp ln(−s_ij/μ²) + Σγ_i, with Γ_cusp = α_s/4π (Eq. 3.6). The evolution operator U (Eq. 3.8) is applied only to massless final-state partons, with non-cusp γ_i neglected. Each dipole has its own upper scale M_ij².
- **Ansatz (Sec. 4):** the shower is taken to have resummed the logs of Q²/M_ij² down to M_ij² ~ 2p_i·p_j ~ Q_0². CR is then evolution from M_ij² = 2p_i·p_j down to μ² below the cluster masses (Eq. 4.2). The free parameters are μ and α_s. The authors used α_s = 0.118 and say it should also be tunable (p. 17).
- **Baryons:** a baryon/antibaryon pair is an antisymmetrised colour structure |B_ijk⟩ with normalisation N_B² = 4/3 (Eqs. 4.5–4.6), giving the amplitude in Eq. 4.7 and the generalised probabilities in Eqs. 4.9–4.10. The unbaryonizing amplitude is Eq. 4.11.
- **Two-cluster sandbox (Sec. 5):** U = e^Ω is a closed-form 2×2 matrix (Eqs. 5.2, 5.4). The Coulomb (iπ) term is dropped in this section, since numerically it is negligible for massless clusters (p. 8).
- **Numerics (Sec. 6):** systems of 2–5 clusters. Kinematics come from RAMBO (flat phase space) or from a Jadach/UA5-type cylindrical phase-space generator. The initial colour connections are either the generators' own or random (p. 11). The Sec. 6.1–6.2 mass axes extend to ≈3000 GeV, consistent with √s = 3000 GeV [unverified: √s not stated explicitly for Secs. 6.1–6.2]. Some use √s = 10 GeV for a more realistic cluster mass spectrum (p. 15). μ = 1 or 0.01 GeV.
- No full event generator and no data. This is explicitly a "theoretical consideration to constrain the structure of an improved colour reconnection model" (p. 18).

## Results
- **Mesonic CR:**
  - RAMBO: the cluster mass spectrum shifts to lower values after evolution (Fig. 2 left, p. 10).
  - UA5 with its own (already local) colour connections: the evolution can instead produce some heavier clusters (Fig. 2 right).
  - UA5 with random initial connections: masses drop strongly (Fig. 4, p. 11). The ΔY of reconnected q q̄ pairs moves from a broad distribution peaking near ΔY ≈ 10 to one peaked at small ΔY (Fig. 5b, p. 12). The effect is smaller for RAMBO (Fig. 5a).
- **Two-cluster analytics:**
  - p_rec = |U_11 + N U_21|² / (|N U_11 + U_21|² + |U_11 + N U_21|²) (Eq. 5.6).
  - Minimal mixing, p_rec = 1/10, occurs when U_21 = 0 ⇔ ln²M_12² + ln²M_34² = ln²M_13² + ln²M_24² (Eq. 5.7). Maximal mixing, p_rec = 9/10, occurs when U_11 = 0 (pp. 8–9). p_rec itself can be lower (it vanishes for U_11 = −N U_21, from Eq. 5.6; cf. the peak at 0 in Fig. 11).
  - In a frame where p_1 and p_4 are back to back, mixing is minimal when p_T2 ~ p_T3 and ΔY ~ 0 (Eq. 5.8, p. 9), so reconnection is more likely at large ΔY.
- **Baryonic CR:**
  - The average probability is 2–12% depending on the phase-space generator, and grows from 3 to 5 clusters (Fig. 6, p. 12).
  - For UA5 kinematics with the original connections, the baryonic probability is higher than with random ones. The authors explain that mesonic CR is suppressed there (p. 13).
  - The distribution of baryonic probabilities peaks at 0, with a tail up to ~0.7 (Fig. 7, RAMBO, p. 13).
  - For 3 clusters, the median baryonic probability falls from ≈0.55 at (⟨ΔR_B⟩+⟨ΔR_B̄⟩)/2 ≈ 0.7 to ≈0 above ≈2 (Fig. 8, p. 14). The authors note that baryon and antibaryon clusters can still overlap, since their mutual distance is not used (p. 14).
- **Unbaryonization:** the median probability rises from ≈0.15–0.19 for compact baryonic clusters to ≈0.3–0.4 for spread-out ones (Fig. 9, p. 15). Outliers at large values are attributed to low statistics.
- **Parameters:**
  - Smaller μ gives stronger CR (μ = 0.01 vs 1 GeV, 4 clusters at √s = 10 GeV). It shifts cluster masses down and pushes the colour-length drop Δ_if = 1 − λ_final/λ_initial (λ = ΣM_i², Eqs. 6.3–6.4) toward positive values. Δ_if peaks at 0 but has a negative tail, since mass-increasing flows are not vetoed (Fig. 10, p. 16).
  - At √s = 3000 GeV the 2-cluster p_rec spans 0–1. At √s = 10 GeV with μ = 1 GeV it is narrowly distributed around 0.1. Lowering μ to 0.01 GeV recovers the broad distribution (Fig. 11, p. 16).
  - The authors claim an energy-independent prescription exists because Γ depends only on M_ij/μ (p. 17). Cluster mass distributions scaled by √s look similar at 10 and 3000 GeV (Fig. 12, p. 17).
- **Robustness checks:**
  - Replacing ln(M²/μ²) → ln(M²/μ² + 1) changes nothing (p. 17).
  - Light constituent masses (0.3 GeV) have only small effects (pp. 17–18). b-quark masses are expected to matter but were not studied (p. 18).
  - Switching off the Coulomb term has no effect for high-mass systems and "some effects" for small-mass systems (p. 18). The size is not quantified.
- **Subsystems:** for 4 clusters the transposition counts are roughly 11/15/7/1 for 0/1/2/3 transpositions. For 5 clusters they are roughly 4/9/8/3/0.3 for 0/1/2/3/4 (Fig. 13, p. 18; read off the bar chart, arbitrary normalisation).
- **Proposed model inputs (p. 19–20):**
  - use the analytic two-cluster p_rec(M_i/M_f) in place of a flat probability;
  - use three-cluster detachment for a dynamic baryonic-CR probability, possibly via a 1/N expansion [Plätzer 2014];
  - include unbaryonization.
  - The predictive parameters are α_s and μ (and possibly N) (p. 20).

## Assessment
- **What it shows:** this is a feasibility and motivation study. All results are toy cluster ensembles with hand-chosen kinematics (RAMBO, UA5). No events from a parton shower are used and there is no comparison to data. The claimed "support" for geometric CR models is qualitative: both prefer lower masses and smaller ΔY.
- **Physical status of the ansatz:** it is not derived. Two choices are imposed:
  - Γ is extrapolated below the shower cutoff (μ ≪ Q_0, even μ = 0.01 GeV), where perturbation theory does not apply.
  - The initial scale is set per dipole to the cluster mass M_ij² = 2p_i·p_j (Eq. 4.2).
  The "probability" in Eq. 4.4 is a normalised overlap in a non-orthogonal basis, not a cross-section ratio. α_s and μ are in practice tuning parameters, so this is better called a perturbatively inspired model than a perturbative prediction.
- **The 1/10 and 9/10 values** come from the N = 3 two-cluster algebra (Eq. 5.6 with ⟨ij|ji⟩ = N): 1/(N²+1) and N²/(N²+1) at minimal and maximal mixing. The median p_rec in Fig. 15 saturates at ≈0.9 for favourable mass ratios and sits at ≈0.1 for M_i ≤ M_f (p. 19). So favourable configurations never reconnect with certainty, and typical unfavourable ones keep a ~10% chance, although individual events can have p_rec ≈ 0 (Fig. 11). This is a distinctive prediction compared with mass-veto models.
- **"Not simply 1/N suppressed" (p. 18):** the claim rests on the distribution of transposition counts in toy RAMBO events at √s = 3000 GeV, not on an explicit 1/N expansion. We take it as suggestive.
- **Relation to other approaches:** in spirit this links CR to beyond-leading-colour soft evolution (Plätzer; Martinez et al. CVolver). Christiansen–Skands (1505.01681) uses SU(3) multiplet algebra to similar effect in the string picture. The Coulomb/Glauber phase is kept in the formalism but found numerically minor here (p. 17–18).
- **Implementation:** the full model was announced as "ongoing work" (p. 2). Bellm:2019wrh (p. 12 there) cites this paper [18] as a possible future direction in a spacetime neighbourhood, so it was apparently not yet in Herwig by late 2019 [unverified for later releases].

## Leads
- Plätzer, "Summing Large-N Towers in Colour Flow Evolution", EPJC 74 (2014) 2907, arXiv:1312.2448: provides the colour reconnectors and 1/N expansion behind U. (In DB: Platzer:2013fha, queued.)
- Martínez, De Angelis, Forshaw, Plätzer, Seymour, "Soft gluon evolution and non-global logarithms", arXiv:1802.08531 (journal ref not given in the paper): amplitude-level full-colour evolution, cited as the BLC shower route (p. 2, 21). Not in DB.
- Gieseke, Kirchgaeßer, Plätzer, "Baryon production from cluster hadronisation", EPJC 78 (2018) 99, arXiv:1710.10906: the baryonic CR model this paper aims to improve. (Gieseke:2017clv, queued.)
- Ferreres-Solé & Sjöstrand, "The space-time structure of hadronization in the Lund model", EPJC 78 (2018) 983, arXiv:1808.04619: spacetime hadronization, cited as promising for CR (p. 3). Not in DB.
- Reichelt, Richardson, Siódmok, "Improving the simulation of quark and gluon jets with Herwig 7", EPJC 77 (2017) 876, arXiv:1708.01491: CR effects on jets; cited among CR/UE refs. Not in DB.
- Lönnblad, "Reconnecting coloured dipoles", Z. Phys. C 70 (1996) 107: early dipole CR model. (Lonnblad:1995yk, already read.)
