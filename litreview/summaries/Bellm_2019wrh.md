# Spacetime colour reconnection in Herwig 7
- **ID / links:** Bellm:2019wrh · INSPIRE 1755108 · arXiv 1909.08850 · DOI 10.1140/epjc/s10052-019-7533-6
- **Authors / collab, year, journal:** J. Bellm, C. B. Duncan, S. Gieseke, M. Myska, A. Siódmok, 2019, Eur. Phys. J. C (DOI above) (CoEPP-MN-19-04, MCNET-19-21, KA-TP-08-2019, HERWIG-2019-01, LU-TP 19-41). Read from arXiv v3 (3 Dec 2019).
- **Type:** MC/model (with tune and comparison to LHC 7 TeV minimum-bias data)
- **Relevance:** 2 · RQs: 1, 2, 3
- **Full text source:** arxiv

## Takeaways
- This is the first Herwig 7 CR model to use spacetime information. MPI scattering centres get transverse positions, sampled from the eikonal overlap (Bessel/K_3 profile, Eqs. 6–7). Final-shower partons are smeared around their MPI centre by a lifetime τ_0 = ħm/ν² (Eqs. 12–14). This lab-frame decay distance ∝ E/ν² is equivalent to the standard formation time E/k⊥² (App. A, Eq. 21).
- Baryonic CR (Gieseke:2017clv) is kept, but the cluster mass measure is replaced by a boost-invariant (along z) distance R_ij² = Δr_ij²/d_0² + Δy_ij² (Eq. 15). A reconnection is accepted if it reduces ΣR (mesonic Eq. 16, baryonic Eq. 17), with flat probabilities p_M,reco and p_B,reco = w_b.
- Tune "H7 + STCR" (Tab. 1, p. 11): ν² = 4.5 GeV², d_0 = 0.15 fm, w_b = 0.98, together with retuned MPI parameters (σ_tot = 96.0 mb, R_Diff = 0.2, p⊥^min = 3.0 GeV, μ²_hard = 1.5 GeV²; μ²_soft = 0.254 GeV² determined, not tuned). Two variations: (ν² = 2.1 GeV², d_0 = 0.55 fm) and (3.3 GeV², 0.05 fm) (Fig. 8, p. 9).
- **Data comparison** (LHC 7 TeV MB/UE): "reasonable agreement" for η and p⊥ spectra (Fig. 9). There are problems in the N_ch distribution: the central tune overshoots at high N_ch, and Variation 1 (larger d_0, hence more CR) does better (Fig. 10, p. 11). In the ATLAS UE the turn-on is slightly too low for p⊥^lead < 2.5 GeV, and Σp⊥ is ~10% too large above 2.5 GeV (Fig. 12, p. 11). The proton yield is "fairly poorly described" (Fig. 11, p. 11).
- The stated motivation is causality of CR and later extension to larger systems (heavy ions, p. 1, 12). The paper is a pp proof of concept only.

## Setup
- **Generator:** Herwig 7 angular-ordered shower, cluster hadronisation, eikonal MPI with hard and soft scatters (Eqs. 1–3).
- **MPI coordinates (Sec. 3.1):**
  - b is sampled from the joint Poissonian P_h,k(b) for h hard and k soft scatters (Eq. 2, Fig. 1).
  - Centres are sampled from the integrand of the overlap convolution (Eq. 7), with separate μ² for hard and soft scatters.
  - Beam remnants sit at (±b/2, 0) (Fig. 2, p. 5).
  - A black-disc profile is shown for comparison only (Fig. 2 right).
- **Shower spacetime (Sec. 3.2):**
  - A virtuality-dependent lifetime (Eq. 8) with a minimum width Γ = ν²/M is used only for diagnostics.
  - Distances travelled in the last shower step reach the fm scale and dominate the total. For MB and DY with ν² ≤ 2 GeV², ~90% of the distance comes from the last step (Figs. 3–5, pp. 5–8).
  - The distances depend strongly on ν² (Fig. 3).
  - Higgs behaves differently because of the Higgs decay lifetime (p. 6).
- **Model (Sec. 3.3):** only final partons get coordinates, transverse plane only (no z, t). Each is shifted from its MPI centre by an exponentially distributed decay time with mean τ'_0 = ħE/ν² (Eqs. 9, 10, 14). q q̄ from the non-perturbative gluon splitting share the same position; octet clusters are forbidden (p. 7).
- **CR (Sec. 4):**
  - Plain spacetime CR (Eq. 16) is presented. A similar model was studied in a 2010 diploma thesis (Röhr [45]).
  - The tuned model is baryonic spacetime CR. Partner search uses the existing rapidity-axis projection of Gieseke:2017clv. Diquarks are formed from the pair closest in R (Eq. 15), with averaged positions and rapidities. The baryonic condition is Eq. 17.
- **Other MPI changes (Sec. 5):** improved kinematics, a diffraction ratio R_Diff, a new cross-section treatment, and a changed MB dummy process and partner finding. Details are deferred to [46] = arXiv:1911.13149.
- **Tuning:** Autotunes + Rivet + Professor against ALICE, ATLAS and CMS data [53–57]. σ_tot is constrained against Donnachie–Landshoff (DLMode1/2) (Fig. 8 left, p. 9). The strangeness-production probability is kept from [14]; there is no full retune of hadronisation (p. 11).

## Results
- **χ² landscape:**
  - (R_Diff, σ_tot) minimum near σ_tot ≈ 96–100 mb, R_Diff ≈ 0.18–0.2 (Fig. 8 left, p. 12).
  - (μ²_hard, p⊥^min) minimum near p⊥^min ≈ 3 GeV², μ²_hard ≈ 1.5 GeV² (Fig. 8 middle). This is read from the plot; Tab. 1 quotes p⊥^min = 3.0 GeV, while the axis is labelled GeV².
  - (ν², d_0) valley at d_0 ≈ 0.1–0.2 fm, broad in ν² ≈ 3–6 GeV² (Fig. 8 right).
- **Tuned values (Tab. 1, p. 11):**
  - ν² = 4.5 GeV², "rather large" relative to the shower Q² cutoff.
  - d_0 = 0.15 fm: the transverse length scale of CR.
  - w_b = 0.98: "seems to be very large", but candidate triplets are already strongly preselected (p. 11).
- **η and p⊥ spectra** in five N_ch / p⊥^track slices at 7 TeV (ATLAS [55]): good agreement. Variations mainly shift the normalisation of the N_ch ≥ 20 slice (Fig. 9, p. 12).
- **N_ch distributions:**
  - For N_ch ≥ 2 and N_ch ≥ 20 with p⊥ > 100 MeV, MC/data is ~1 up to N_ch ~ 100 and then rises above data. The ratio panels reach ~1.3–1.5 at the highest N_ch (Fig. 10, p. 13; read off the plot).
  - For p⊥ > 500 MeV the tune overshoots at high N_ch, by ~1.2–1.4 in the ratio panel (read off the plot).
  - Variation 1 (more CR) is closer to data at high N_ch (p. 11).
- **Insensitive observables:** the rapidity-gap cross-section (ATLAS [59]) and π/K/p yields (ALICE [53]) barely change under the spacetime variations (Fig. 11, p. 13). Protons are poorly described (p. 11). The authors say small gaps are driven by MPI and are "relatively invariant to CR", while large gaps come from diffraction.
- **ATLAS UE [56]** (Fig. 12, p. 14):
  - The turn-on is slightly too low below p⊥^lead = 2.5 GeV.
  - Σp⊥ is about 10% too large above 2.5 GeV, also in the Δφ dependence.
  - The authors attribute this to the absence of azimuthal correlations between MPI scatters in Herwig, where CR is the only correlating mechanism (p. 11).
- **Outlook (p. 12):** restrict reconnection to MPI subsystems close in spacetime (Blok et al. [60]); use the soft-gluon-evolution CR of Gieseke:2018gff [18] in a spacetime neighbourhood; study Bose–Einstein correlations versus hadron position (Bialas & Zalewski [61]).

## Assessment
- **What is spacetime here:** the coordinates are a phenomenological smearing, not a dynamical evolution. Only transverse positions are used (no time ordering), so the causality motivation is not implemented. "Causally disconnected" reconnection is only suppressed through the Δr/d_0 term.
- **Tuned scales:** d_0 = 0.15 fm is smaller than the proton radius and the MPI-centre spread (~0.5–1 fm; Fig. 2), and ν² is large. The tuned model therefore weights transverse separation strongly. The χ² surface in d_0 is well defined while ν² is weakly constrained (Fig. 8 right).
- **Weak constraint on the spacetime parameters:** the data used (MB/UE at 7 TeV, identified-hadron yields, gaps) are largely insensitive to the new parameters (Fig. 11), and the N_ch tail remains problematic (Fig. 10). There is no direct test of CR (e.g. ⟨p⊥⟩(N_ch), baryon/meson ratios vs multiplicity, flow-like correlations), nor any comparison with plain mass-based CR or with the default Herwig 7 tune on the same plots. So the paper does not show the spacetime measure is *better* than momentum-space CR, only that it can be tuned to comparable agreement [our reading; no default-tune curves are shown].
- **w_b ≈ 1:** baryonic reconnection is accepted almost always once the geometric preselection passes. Baryon-rate control therefore sits in the preselection, not in w_b.
- **Context:** this is a precursor for heavy-ion and small-system CR in Herwig, relevant to RQ1 (CR versus flow/ropes in dense systems). It complements Pythia's spacetime framework (Ferreres-Solé & Sjöstrand 2018) and Bierlich et al. rope/shoving work.

## Leads
- Bellm, Gieseke, Kirchgaeßer, arXiv:1911.13149 (ref. [46]): the MPI/diffraction model modifications used here; needed to separate MPI from CR effects. Not in DB.
- Gieseke, Kirchgaeßer, Plätzer, EPJC 78 (2018) 99, arXiv:1710.10906: the baryonic CR this builds on. (Gieseke:2017clv, queued.)
- Ferreres-Solé & Sjöstrand, EPJC 78 (2018) 983, arXiv:1808.04619: Lund spacetime hadronization, the Pythia counterpart. Not in DB.
- Bierlich & Rasmussen, arXiv:1907.12871 (ref. [28]): dipole evolution in spacetime in γ*A, relevant to CR/collectivity in larger systems. Not in DB.
- Bierlich, Gustafson, Lönnblad, Tarasov, JHEP 03 (2015) 148, arXiv:1412.6259, and Bierlich, Gustafson, Lönnblad, arXiv:1612.05132 (refs. [23, 24]): ropes and collective hadronization with spacetime. (1412.6259 = Bierlich:2014xba, queued; 1612.05132 not in DB.)
- Blok, Jäkel, Strikman, Wiedemann, JHEP 12 (2017) 074, arXiv:1708.08241: MPI spatial correlations, proposed for restricting CR to nearby subsystems. (Blok:2017pui, queued.)
- Duncan & Kirchgaeßer, EPJC 79 (2019) 61, arXiv:1811.10336: strangeness production in cluster hadronisation, relevant to the strangeness-enhancement versus CR question. Not in DB.
- Bialas & Zalewski, PLB 727 (2013) 182, arXiv:1309.6169: Bose–Einstein correlations and hadron emission positions, a spacetime-sensitive observable for CR. Low priority.
- Röhr, "Colour Charge Effects in Hadronization", Diplomarbeit KIT 2010 (ref. [45]): earliest spacetime-like CR in Herwig; thesis, likely hard to obtain. Low priority.
