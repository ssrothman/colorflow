# Measurements of observables sensitive to colour reconnection in tt̄ events with the ATLAS detector at √s = 13 TeV
- **ID / links:** ATLAS:2022ctr · INSPIRE 2152933 · arXiv 2209.07874 · DOI 10.1140/epjc/s10052-023-11479-x · HEPData 10.17182/hepdata.135459.v1 · Rivet ATLAS_2022_I2152933
- **Authors / collab, year, journal:** ATLAS Collaboration (CERN-EP-2022-167), 2023, Eur. Phys. J. C 83 (2023) 518
- **Type:** experimental
- **Relevance:** 3 · RQs: 2, 3 (also context for the CR uncertainty on m_top)
- **Full text source:** arxiv (v2, 31 Aug 2023; anchors are the printed page numbers. Physics content pp. 1–50, references pp. 51–57, author list from p. 58 on, not read)

## Takeaways
- First dedicated CR-sensitive measurement in tt̄ (p. 4). In dileptonic eμ + 2 b-tags (+ ≤1 extra jet) events, it measures charged-particle multiplicity n_ch, Σ_{n_ch} p_T, and Σp_T in bins of n_ch. Only charged particles **outside** jets (ΔR > 0.4) and away from the leptons count (p. 12, Tab. 1). These are unfolded to particle level. HEPData record 10.17182/hepdata.135459.v1 with Rivet analysis ATLAS_2022_I2152933 (from hepdata.net, not stated in the paper).
- **Switching CR off is disfavoured** in both PYTHIA 8 (R_rec = 0: "not compatible", p. 36; "excluded", p. 42) and HERWIG 7.2 ("do not describe data well", with partial compensation by the UE modelling, p. 39) (Figs. 12, 13). SHERPA 2.2.10, which has no CR model, disagrees: χ² = 77/7 (n_ch) and 211/10 (Σp_T) (Tab. 6). Note that in Tab. 6 PYTHIA CR1 has a worse n_ch χ² (98/7), and A14 has worse global (434 vs 263) and 2D (224 vs 124) χ² than SHERPA. Maximal CR strength in PYTHIA CR0 (R_rec = 10) is still compatible with the data (p. 36).
- **No model describes everything.** Best overall is POWHEG+HERWIG 7.0.4 (χ² 39/7, 16/10, 2D 29/8). Among the PYTHIA 8 models, the gluon-move model CR2 is worst for Σp_T (179/10). The HERWIG statistical CR model is best for n_ch overall (23/7); among the HERWIG 7.2 CR variants, the baryonic CR model is best for Σp_T (20/10; HERWIG 7.0.4 is lower overall at 16/10) (Tab. 6, p. 34; p. 39).
- The observables are as sensitive to MPI/UE parameters as to CR: the data prefer a lower p_T0^ref than A14's 2.09 GeV (Fig. 12, p. 36). The authors' conclusion is that CR and MPI parameters must be tuned simultaneously (p. 42).
- The top-specific CR models (TCR1–5, Argyropoulos–Sjöstrand) barely change these observables. Only TCR1 (forced random) and TCR3 (forced farthest) differ visibly between s = 0.1 and s = 1.0, mainly in the 2D distribution (Fig. 14, p. 39; p. 42). A plausible reason (reviewer's interpretation, not stated in the paper) is that jets, and thus most of the top decay products, are excluded from the measurement.

## Setup
- **Data and selection.** LHC Run 2, 13 TeV, 139 fb⁻¹ (2015–2018), with ⟨μ⟩ rising from 13 to 36 (p. 8).
  - Exactly one e and one μ with opposite charge, p_T > 25 (27) GeV, |η| < 2.5; m_ℓℓ > 15 GeV.
  - 2 or 3 anti-kT R = 0.4 jets with p_T > 25 GeV, |η| < 2.5, of which exactly 2 are b-tagged (DL1r, 70% WP); n_trk,out ≤ 100 (pp. 11–12).
  - 195 507 data events vs 199 000 ± 11 000 expected; tt̄ purity ≈ 96%; single top 3.2% (Tab. 2, p. 15).
- **Observables (particle level).** Charged particles with p_T > 500 MeV, |η| < 2.5, τ > 30 ps, excluding those within ΔR < 0.4 of a jet or ΔR < 0.01 of the leptons (pp. 11–12).
  - n_ch binning: [0,10,…,60,80,100].
  - Σp_T binning: 10 GeV bins up to 100 GeV, then overflow.
  - 2D binning as in Tab. 1 (p. 13).
- **Detector-level treatment.**
  - Pile-up and secondary tracks are subtracted stochastically using MC templates (Eqs. 1–2, p. 17). The scale factors come from z0 and d0/σ fits: c_PU = 0.91–1.36 (Tab. 3) and c_sec = 2.34 ± 0.02 (p. 18).
  - A tracking-efficiency correction is then applied (Eq. 3, p. 19), followed by iterative Bayesian unfolding (3 iterations) with a POWHEG+PYTHIA 8 response (p. 21).
- **Nominal MC.** POWHEG-BOX v2 hvq + PYTHIA 8.230 with the A14 tune (CR0, MPI-based CR), h_damp = 1.5 m_top (p. 9).
- **Alternative models compared (Sec. 2, Sec. 9):**
  - PYTHIA 8 CR0/CR1/CR2 with dedicated tunes from ATL-PHYS-PUB-2017-008. CR1 is the QCD-based model with junctions; CR2 is gluon-move (p. 5).
  - PYTHIA 8 variations: noCR (R_rec = 0); maxCR (R_rec = 10, default 1.71); p_T0^ref = 2.0 / 2.2 (default 2.09); A14 Var1 up/down (p. 36).
  - PYTHIA 8 top-specific TCR1–TCR5 at strength s = 0.1 and 1.0 (p. 6). The base tune used for these samples is not stated.
  - POWHEG+HERWIG 7.0.4 (H7-UE-MMHT), 7.1.3 (H7.1-Default) and 7.2.1 (H7.2-Default, with the improved MPI model), all with plain CR (p. 6).
  - HERWIG 7.2 statistical CR, baryonic CR and noCR (pp. 6–7, 39).
  - SHERPA 2.2.10, which has no CR (p. 4).
- **Comparison method.** χ² uses the full covariance matrix: stat, experimental systematics, signal and background modelling, plus "theory" uncertainties (ME/PS scales and h_damp) (p. 33). For normalized distributions one bin is dropped, so NDF = N_b − 1.

## Results
- **Fiducial cross-section.** σ_tt̄^fid = 4.94 +0.43/−0.41 (syst) ± 0.03 (stat) ± 0.08 (lumi) pb (p. 33).
- **Precision.** 2–10% in central bins and up to ≈50% in outer bins (p. 42).
  - In the tails, the dominant uncertainties are PS/hadronisation (H7 vs PYTHIA) and the CR-model envelope (CR0–CR2) (p. 28; Fig. 7, p. 29).
  - In the lowest n_ch / Σp_T bin, pile-up subtraction dominates (≈15–22%, read off Fig. 8, p. 30).
  - Track and jet systematics dominate the experimental part (Fig. 5).
- **Sensitivity to radiation.** h_damp = 3 m_top changes the edge bins by up to ≈15%, but the bulk only by a few %. ISR and FSR variations are smaller and of opposite sign (Fig. 9, p. 31). The authors conclude that the observables are only weakly sensitive to extra radiation, so differences between generators are mainly due to CR/UE modelling (p. 31).
- **χ² for the nominal normalized distributions (Tab. 6, p. 34).** NDF = 7 / 10 / 17 / 8 for n_ch / Σp_T / Global / Σp_T in bins of n_ch.

  | Set-up | n_ch | Σp_T | Global | 2D |
  |---|---|---|---|---|
  | POWHEG+PYTHIA 8.230 (A14) | 62 | 106 | 434 | 224 |
  | CR0 (dedicated tune) | 55 | 113 | 629 | 129 |
  | CR1 | 98 | 60 | 581 | 158 |
  | CR2 | 58 | 179 | 402 | 238 |
  | POWHEG+HERWIG 7.0.4 | 39 | 16 | 145 | 29 |
  | POWHEG+HERWIG 7.1.3 | 53 | 42 | 188 | 41 |
  | POWHEG+HERWIG 7.2.1 | 78 | 25 | 313 | 87 |
  | HERWIG Baryonic CR | 75 | 20 | 241 | 29 |
  | HERWIG Stat CR | 23 | 40 | 121 | 39 |
  | SHERPA 2.2.10 | 77 | 211 | 263 | 124 |

  The authors' reading (pp. 34–36):
  - n_ch is described about equally well by PYTHIA 8 and HERWIG 7. HERWIG is much better for Σp_T and for the 2D distribution.
  - Successive HERWIG versions get worse for n_ch and stay similar for Σp_T.
  - SHERPA disagrees, "illustrating the importance" of CR. SHERPA predicts too few particles and too soft a Σp_T spectrum (p. 42). In Fig. 10a its pred./data ratio is ≈1.5–1.9 in the lowest n_ch bins (read from the figure).
  - CR0 with the dedicated tune beats A14 on n_ch and 2D, but its global χ² is larger.
  - CR1 is best for Σp_T and worst for n_ch among the PYTHIA CR models.
  - None of the PYTHIA CR models or A14 describes the low-Σp_T region. In the first Σp_T bin, pred./data ≈ 1.5–1.8 (Fig. 11b, read from the figure).
- **χ² for the other PYTHIA variations is not tabulated** (noCR, maxCR, p_T0^ref, Var1, TCR). Only figures and qualitative statements are given:
  - noCR is "not compatible" with the data. In Fig. 12a it overshoots high n_ch, with pred./data ≈ 1.7 in the 60–80 bin, and the 2D distribution is strongly distorted (Fig. 12c).
  - maxCR is still compatible.
  - Integrated Σp_T is insensitive to the CR strength, but Σp_T within n_ch slices is sensitive to it.
  - There is "clear sensitivity" to p_T0^ref, with a preference for a value below the A14 one (p. 36).
- **HERWIG 7.2 noCR.** It does not describe the data, but the UE modelling partly compensates. Statistical CR is best for n_ch and baryonic CR is best for Σp_T. The authors state that even without retuning both agree better than plain CR; per Tab. 6 this holds for global and 2D χ², but Stat CR is worse than plain CR (H7.2.1) for Σp_T (40 vs 25/10). HERWIG's Σp_T agreement is better than that of any other generator (p. 39, Fig. 13).
- **TCR models (Fig. 14, p. 39).** All TCR samples, including s = 0.1, deviate visibly from the data in the 2D distribution. For example, pred./data is ≈0.5–0.75 in the high-Σp_T bins of n_ch ∈ [20,40) and up to ≈1.5–1.8 in the low-Σp_T bins of n_ch ∈ [40,60) and [60,80) (read from Fig. 14c). The paper attributes the s-dependence only to TCR1 and TCR3, and gives no χ².
- **Alternative χ² treatments (App. C, Tabs. 7–8, pp. 43–50).**
  - With the "Total" covariance (no extra theory uncertainties), χ² generally rises, often sharply (a few values barely change, e.g. Stat CR n_ch 23 → 23, HERWIG 7.0.4 Σp_T 16 → 17). Examples: PYTHIA 8.230 Σp_T 293/10; SHERPA n_ch 459/7.
  - "De-correlate modelling" puts modelling uncertainties on the diagonal only, and χ² falls drastically. Examples: PYTHIA 8.230 24/7 (n_ch) and 18/10 (Σp_T); CR0 8/7; HERWIG 7.0.4 2/10 (Σp_T); Stat CR 7/7 (n_ch); SHERPA still 148/7 and 155/10 (Tab. 7).
  - The authors conclude that the large χ² values in the "Total" scenario come from the bin-to-bin correlations of the modelling uncertainties (p. 49). Rankings stay similar: HERWIG 7.0.4 is best overall and SHERPA worst (p. 49), though in the de-correlated 2D χ² PYTHIA 8.230 (155) is slightly worse than SHERPA (137) (Tab. 7).
  - Tab. 8 (absolute cross-sections, NDF 8/11/19/9) shows the same pattern; e.g. nominal SHERPA 144/8 (n_ch), 275/11 (Σp_T); HERWIG 7.0.4 22/11 (Σp_T).
- **Authors' outlook.** The CR-model variations can be used to build a CR uncertainty (for m_top, quoted as up to 400 MeV in Ref. [13], p. 4). The results are input for simultaneous CR + MPI tuning (p. 42).

## Assessment
- **The χ² values do not give usable p-values.** Most models have χ²/NDF ≫ 1 with the nominal covariance; even the best per-observable values are 1.6–3.6 per NDF (HERWIG 7.0.4 Σp_T 16/10, Stat CR n_ch 23/7, 2D 29/8). The values swing by up to an order of magnitude depending on how the modelling-uncertainty correlations are treated (Tabs. 6–7). The two observables are also strongly correlated: the global χ² is usually far above the sum of the n_ch and Σp_T χ² values (exception: SHERPA, 263 vs 77 + 211). The **relative ranking** is the more robust content, but only partly: HERWIG (esp. 7.0.4) is best in all scenarios; SHERPA (no CR) is clearly worst in the "Total" scenario, but in nominal Tab. 6 it is not uniformly below PYTHIA (its global and 2D χ² beat A14, and CR1 is worse for n_ch). The authors call CR2 the worst PYTHIA CR model (p. 42; true for Σp_T and 2D, while CR0 has the largest global χ² and CR1 the largest n_ch χ²). noCR is disfavoured in both generators (explicitly "excluded" only for PYTHIA, p. 42).
- **"noCR excluded" is shown only visually** (Figs. 12–13), without a χ². The statement that maxCR is "still compatible" is likewise qualitative.
- **The paper cannot separate CR from MPI/UE.** CR is degenerate with the MPI cutoff p_T0^ref and with the UE tune. The SHERPA result (no CR, yet *fewer* particles than data) shows that the MPI/UE set-up can outweigh the expected CR effect. "SHERPA fails because it lacks CR" is therefore the authors' interpretation, not something the measurement isolates. The same caveat applies to HERWIG noCR, where the UE "compensates" (p. 39).
- **The measurement mostly probes the UE region.** Excluding particles within jets removes most of the region where CR involving the top decay products would act. It therefore tests MPI-level CR in a tt̄ environment, not top-decay CR as such. This explains the weak sensitivity to TCR models. The tt̄-specific reconnection relevant for m_top (e.g. b-jet / W-jet reconnection) remains largely unconstrained.
- **The TCR comparison is hard to interpret.** The base tune for the TCR samples is not stated, and even s = 0.1 deviates strongly in the 2D bins. The discrepancy may come from the base set-up rather than from TCR itself. This cannot be resolved from the paper.
- **Unfolding prior.** Unfolding uses a PYTHIA 8 (CR0/A14) response. Stress tests show closure within ≈5% (p. 22). Some residual prior dependence is possible in the tails, where the uncertainties are ≈50%.
- **Use in the review.** It is a key LHC tt̄ counterpart to the LEP W⁺W⁻ CR results and to the CMS tt̄ UE / CR-tune studies (CMS 1807.02810, 2205.02905). It is in HEPData with a Rivet analysis, so it is usable for tuning. It does not produce a quantitative CR-uncertainty prescription for m_top itself.

## Leads
- Argyropoulos & Sjöstrand, "Effects of color reconnection on tt̄ final states at the LHC", JHEP 11 (2014) 043, arXiv:1407.6653: defines the TCR1–5 top-specific models tested here.
- ATLAS, ATL-PHYS-PUB-2017-008, "A study of different colour reconnection settings for Pythia8 generator using underlying event observables" (CDS 2262253): source of the CR0/CR1/CR2 tunes and of the CR envelope used in ATLAS m_top.
- CMS, "CMS PYTHIA 8 colour reconnection tunes based on underlying-event data", arXiv:2205.02905 (EPJC 83 (2023) 587): CMS counterpart CR tunes (CP5-CR1/CR2) and their m_top impact.
- CMS, "Study of the underlying event in top quark pair production in pp collisions at 13 TeV", EPJC 79 (2019) 123, arXiv:1807.02810: earlier tt̄ UE measurement, also sensitive to CR.
- Christiansen & Skands, "String formation beyond leading colour", JHEP 08 (2015) 003, arXiv:1505.01681: the QCD-based CR (CR1) model.
- Gieseke, Röhr & Siódmok, "Colour reconnections in Herwig++", EPJC 72 (2012) 2225, arXiv:1206.0041: the plain and statistical CR models in Herwig.
- Gieseke, Kirchgaesser & Plätzer, "Baryon production from cluster hadronisation", EPJC 78 (2018) 99, arXiv:1710.10906: the baryonic CR model, best for Σp_T here.
- Bellm, Duncan, Gieseke, Myska & Siódmok, "Spacetime colour reconnection in Herwig 7", EPJC 79 (2019) 1003, arXiv:1909.08850: newer Herwig CR, cited as a review of CR effects.
- Bellm, Gieseke & Kirchgaesser, "Improving the description of multiple interactions in Herwig", EPJC 80 (2020) 469, arXiv:1911.13149: the H7.2 MPI changes that affect these observables.
- Ortiz Velasquez et al., "Color reconnection and flowlike patterns in pp collisions", PRL 111 (2013) 042001, arXiv:1303.6326: CR as the origin of flow-like ⟨p_T⟩(n_ch) (RQ1, small-system collectivity).
- Sjöstrand, "Colour reconnection and its effects on precise measurements at the LHC", arXiv:1310.8073: CR overview, including m_top.
- Reichelt, Richardson & Siódmok, "Improving the simulation of quark and gluon jets with Herwig 7", EPJC 77 (2017) 876, arXiv:1708.01491: cited for the Herwig CR rule forbidding colour-singlet reconnection after non-perturbative g→qq̄ splitting.
- CMS, all-jets m_top + combination, EPJC 79 (2019) 313, arXiv:1812.10534: source of the "CR uncertainty up to 400 MeV" figure.
- ATLAS, UE in Z events at 13 TeV, EPJC 79 (2019) 666, arXiv:1905.09752: complementary UE/CR-sensitive measurement in a colour-singlet process.
- Follow-up (not cited; forward-citation search suggested): later tunes and m_top CR-uncertainty studies using the Rivet analysis ATLAS_2022_I2152933.
