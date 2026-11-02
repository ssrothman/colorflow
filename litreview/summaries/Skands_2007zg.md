# Non-perturbative QCD Effects and the Top Mass at the Tevatron
- **ID / links:** Skands:2007zg · INSPIRE 745970 · arXiv hep-ph/0703081 · DOI 10.1140/epjc/s10052-007-0352-1
- **Authors / collab, year, journal:** P. Skands (Fermilab), D. Wicke (Wuppertal), 2007, Eur. Phys. J. C (per DOI; volume/page not printed on arXiv v2). FERMILAB-PUB-06-340-T
- **Type:** phenomenology (MC/model)
- **Relevance:** 3 · RQs: 1, 2, 3
- **Full text source:** arxiv

## Takeaways
- Introduces the Pythia 6.4 "colour annealing" CR toy models (types 0/1/2, the basis of the Perugia-era CR). Each string piece survives with probability (1 − ξ_R)^{n_int}, where n_int is the number of MPI (Eq. 1). Reconnected dipoles are re-strung by an annealing minimisation of the string-length measure Λ = Π m_i²/M₀² (Eq. 2).
- The physical motivation (RQ1) is the Tevatron minimum-bias ⟨p⊥⟩(N_ch). Uncorrelated strings would give ⟨p⊥⟩ roughly independent of N_ch, and only models with strong colour correlations, explicit CR or the ad hoc correlations of Tune A/DW, describe the rise. The NOCR model fails (Fig. 1, p. 3–4).
- In a generator-level toy semileptonic tt̄ top-mass analysis, the tunes differ by about ±1.1 GeV (fitted) and ±1.5 GeV (after JES rescaling with m_W) in calibration offset (p. 5, Fig. 3).
- The authors split this into about ±1 GeV perturbative, mainly old virtuality-ordered vs new p⊥-ordered shower, and about ±0.5 GeV "non-perturbative" spread within a shower class, which includes CR (p. 6, abstract). This was an early, influential estimate of the CR / non-perturbative top-mass systematic.

## Setup
- Tevatron Run II, pp̄ at √s = 1960 GeV, Pythia 6.408 (p. 3).
- **CR model (p. 2).** Dipoles not surviving Eq. 1 are collected and re-connected by an annealing algorithm minimising Λ (Eq. 2; the actual measure uses four-products of dipole-endpoint momenta).
  - Three variants: Type 0, where colour collapse is driven by free triplets and gg loops are naturally suppressed; Type 1, where gg loops are suppressed by brute force; Type 2, where they are not suppressed.
  - The top and W (cτ ~ 0.1 fm) decay products fully participate in CR.
- **Tunes (Tab. I).**
  - Old UE model: A, DW, A_PT (A with the new p⊥-ordered FSR), A_CR (A with the old UE and Type 0 annealing, ξ_R = 0.25).
  - New interleaved UE: S0 (Type 0, ξ_R = 0.2), S1 (Type 1, 0.35), S2 (Type 2, 0.15), NOCR (ξ_R = 0, reference only).
  - FSR Λ_QCD for the new shower comes from a fit to ALEPH event shapes.
  - Fig. 3 additionally includes Rick Field's tune "BW".
- **Constraints.** No direct data comparison: the new tunes are constrained by matching Tune A's P(N_ch) and ⟨p⊥⟩(N_ch) in min-bias (p. 3), since "Tune A" describes CDF data.
- **Toy m_top (Sect. III.B, p. 5).** Generator level; lepton and neutrino from MC truth.
  - Jets: cone ΔR = 0.5, p_T > 15 GeV, exactly 4 jets, unique ΔR parton matching (25–27% of semileptonic events pass).
  - m_top from the three hadronic-top jets, Gaussian fit within ±15 GeV iterated to be symmetric (m_top^fit).
  - JES factor s_JES = 80.4 GeV / m_W(jj) gives m_top^scaled.
  - Generated m_top from 165 to 185 GeV in 1 GeV steps. Calibration slopes are consistent with 1 at the 2% level (Fig. 2). Offsets are evaluated at m_top^gen = 175 GeV with statistical precision about 0.1 GeV.

## Results
- **Min-bias tuning (Fig. 1).** All tunes give similar P(N_ch).
  - For ⟨p⊥⟩(N_ch), all models with colour correlations roughly agree. NOCR shows the "close-to-constant behaviour of uncorrelated string decays" (p. 4).
  - Approximate reading of Fig. 1 (bottom): NOCR rises only from about 0.4 to about 0.45 GeV between N_ch ≈ 40 and 140, while the other tunes reach about 0.55–0.62 GeV at N_ch ≈ 140.
  - The LEP-like non-perturbative fragmentation ⟨p⊥⟩_NP is about 0.36 GeV (p. 3).
- **Calibration offsets (Fig. 3).**
  - Uncorrected fits lie below the input ("somewhat lower", mainly due to out-of-cone corrections, p. 5); ≈ 8.5–10.5 GeV below (read off Fig. 3).
  - After JES rescaling, the offsets are a few GeV above the input, an over-correction (p. 5; read off the figure: about +1 to +4 GeV).
  - Spread between models: about ±1.1 GeV (m_top^fit) and about ±1.5 GeV (m_top^scaled). Varying the fit range and function changes these by ≤ 20% (pp. 5–6).
- **Decomposition (p. 6).** The largest difference is between the virtuality-ordered (green) and p⊥-ordered (blue) shower classes, which the authors see as perturbative and "should already be present" in the Pythia–Herwig systematic. Within each class, the differences are about ±0.5 GeV. The authors attribute these to non-perturbative origin, while noting that this lumps CR together with IR regularisation, beam remnants, etc.
- **Conclusions (pp. 6–7).**
  - CR in hadron collisions is both experimentally and theoretically motivated.
  - Non-perturbative uncertainties, CR among them, are likely relevant for sub-GeV m_top.
  - The authors suggest constraining with Drell–Yan and dijet UE data at Q ~ m_top, and say jet universality between LEP and hadron colliders "should probably not be treated as inviolate".

## Assessment
- This is the origin of the "colour annealing" CR used in Perugia tunes and of the widely quoted ~0.5 GeV non-perturbative m_top uncertainty. The estimate is however a **generator-level toy**, with no detector simulation, truth-matched jets and a single simple estimator. The ±0.5 GeV is a within-class *spread* of tunes that differ in UE, beam-remnant and IR parameters too (Tab. I), not an isolated CR on/off effect.
- The tunes are constrained only against Tune A, not against data directly (p. 3), and only via two min-bias distributions. ξ_R is therefore not sharply determined.
- The (1 − ξ_R)^{n_int} scaling is explicitly a rough ansatz (p. 2). It makes e⁺e⁻ CR probability equal to ξ_R, but no LEP constraint is applied, on the grounds that jet universality may be violated (p. 2).
- Fig. 3 points are read only approximately. Exact per-tune offsets are not tabulated, so only the authors' ±1.1 / ±1.5 / ±0.5 GeV statements should be quoted.
- Comparison with later Pythia 8 work (Argyropoulos:2014zoa, see that summary): default CR shifts the reconstructed m_top by −0.4 GeV, and tuned CR-model variations around default give up to +200/−800 MeV (its p. 15 text; maximal-strength shifts are in its Tab. 1) — the same order as the ±0.5 GeV non-perturbative spread found here. The two numbers are defined differently (tune spread here vs CR-model/strength variations there), so this is our comparison, not a like-for-like one.

## Leads
- Sandhoff & Skands, Les Houches 2005, hep-ph/0602198 (FERMILAB-CONF-05-518-T); Sandhoff diploma thesis WU D 05-08: precursor work to this study.
- Sjöstrand & Skands, JHEP 0403 (2004) 053, hep-ph/0402078, and EPJC 39 (2005) 129, hep-ph/0408302: the new interleaved MPI/UE model and beam-remnant colour treatment underlying the S-tunes.
- Gustafson, Pettersson, Zerwas, PLB 209 (1988) 90: the first CR study in WW (perturbative, large effects).
- Rathsman, "Generalized Area Law", PLB 452 (1999) 364, hep-ph/9812423: a string-reinteraction model minimising a similar measure.
- Edin, Ingelman, Rathsman, PLB 366 (1996) 371, hep-ph/9508386, and Buchmüller & Hebecker, PLB 355 (1995) 573, hep-ph/9504374: soft colour interactions and rapidity gaps.
- Enberg, Ingelman, Timneanu, PRD 64 (2001) 114015, hep-ph/0106246: soft colour interactions and gaps at the Tevatron.
- Edin, Ingelman, Rathsman, PRD 56 (1997) 7317, hep-ph/9705311: CR in quarkonium production.
- Webber, J. Phys. G 24 (1998) 287, hep-ph/9708463: cluster-based CR model.
- Gustafson & Häkkinen, ZPC 64 (1994) 659; Lönnblad, ZPC 70 (1996) 107; Friberg, Gustafson, Häkkinen, NPB 490 (1997) 289, hep-ph/9604347: dipole-based CR models.
- OPAL, PLB 453 (1999) 153, hep-ex/9901019; OPAL, hep-ex/0508062; ALEPH, EPJC 48 (2006) 685, hep-ex/0604042; DELPHI, PLB 643 (2006) 147, hep-ex/0610031: LEP2 CR searches.
- Khoze & Sjöstrand, PLB 328 (1994) 466, hep-ph/9403394: CR in tt̄ in e⁺e⁻.
- R. Field, hep-ph/0510198: Tune A/DW UE tunes with implicit colour correlations.
- Forward: Skands Perugia tunes (arXiv:1005.3457; not cited here, our addition) and later m_top CR studies citing this.
