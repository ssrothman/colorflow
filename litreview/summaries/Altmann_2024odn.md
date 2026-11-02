# String Junctions Revisited
- **ID / links:** Altmann:2024odn · INSPIRE 2778945 · arXiv 2404.12040 (v3, 29 Jun 2024) · DOI 10.1007/JHEP07(2024)238
- **Authors / collab, year, journal:** J. Altmann, P. Skands (Oxford / Monash), 2024, JHEP 07 (2024) 238
- **Type:** MC/model
- **Relevance:** 2 · RQs: 1, 2, 3, 4
- **Full text source:** arxiv

Page numbers below are the printed ones (PDF page − 1).

## Takeaways
- Revises the fragmentation of **string junctions** formed by the Pythia QCD-based CR model (Christiansen–Skands 2015). The CR algorithm itself is unchanged except for a new mass-aware string-length (λ) measure, default from Pythia 8.311 (Eqs. 2.4, 2.7). The main change is a new, non-iterative junction-rest-frame (JRF) determination. The old one failed for about 10% of LHC minimum-bias events (pp. 12, 24). The new one also covers soft legs: oscillating massless endpoints, and a massive slow endpoint that captures the junction, the "**pearl on a string**" (§3.2, §4).
- Junction baryons are a large share of baryons in the CR-with-junctions model at 7 TeV: up to about 50% of all baryons (peaking near p⊥ ≈ 3 GeV; the text says "light-flavour") and up to about 75% of heavy-flavour baryons (highest at low p⊥) (Fig. 13, p. 29). The low-p⊥ junction-baryon mechanism is the model's explanation of the LHC Λc⁺/D⁰ rise and of the dilution of the Λb asymmetry (pp. 11–12).
- Against data, CR + junctions (old or new) describes CMS Λ/K⁰_S, ALICE Λc⁺/D⁰ and the LHCb Λb asymmetry. It **overpredicts LHCb Λb⁰/B⁰ by about a factor 2** at low p⊥, and it **underpredicts Ξ/Λ and Ξc ratios** strongly (Figs. 21–23, pp. 39–41). The authors conclude that junctions/CR alone cannot produce strangeness enhancement, and that b vs c baryon production is an open problem.
- RQ4 proposals (pp. 43–44, Fig. 24):
  - Measure Λb/Λc, B⁰/D⁰ and Ξb ratios, and global event properties of events with low-p⊥ heavy hadrons.
  - Use **baryon–antibaryon correlations** to tell junction baryons (weakly correlated) from diquark string breaks (strong) and popcorn (milder).
  - Look again at **e⁺e⁻ → WW** for junction–antijunction CR topologies: an enhancement of back-to-back baryon–antibaryon pairs, not modelled in the LEP-era CR models.
  - Compare triplet and octet string fragmentation: gluon-jet tips, LEP "hairpin" configurations, diffractive LHC events.

## Setup
- **Generator and tunes.** Pythia 8.310 ("old" junction model) vs 8.311 ("new"). Both use the QCD-CR "CR Mode 2" parameters (Christiansen–Skands 2015), with Monash 2013 (no junctions) as the baseline. Full parameter table in Tab. 1 (p. 46): CR mode 1, m0 = 0.3, junctionCorrection j₀ = 1.20, timeDilationMode 2 (par 0.18), aLund 0.36, bLund 0.56, probQQtoQ 0.078, remnantMode 1, saturation 5, lambdaForm 0, pNormJunction 2 GeV.
- **Retuning.** Only two changes relative to CR Mode 2 (pp. 37–38):
  - MPI pT0Ref goes from 2.15 to 2.25 GeV, to restore dN_ch/dη (Fig. 19).
  - StringFlav:probQQ1toQQ0join goes from {0.0275 ×4} to the Pythia defaults {0.5, 0.7, 0.9, 1.0}. This raises spin-1 junction-diquark (spin-3/2 baryon) production, motivated by the ALICE Σc/D⁰ and Λc(←Σc)/Λc data (Fig. 20). No full retune.
- **λ-measure.** The dipole measure becomes λ = Σ max[ln((E_i+|p|)/(m_i+m0)), 0] in the pair rest frame (Eq. 2.4); the old form is Eq. 2.3. The junction legs use the same form with j₀(m_i+m0) in the denominator, evaluated in the JRF (Eq. 2.7). The new measure goes to 0 as |p| → 0, so heavy-quark masses no longer inflate string lengths (p. 6). The old form is kept via ColourReconnection:lambdaForm.
- **Junction fragmentation (standard).** Boost to the JRF. Build fictitious mirror legs. Fragment the two softest legs (now chosen by lowest |p|, previously by lowest energy) inward. Form a junction diquark, which as of 8.311 must have positive mass (Eq. 2.8). Fragment the last leg as a dipole; the breaks adjacent to the junction form the "junction baryon" (Fig. 5, pp. 9–11).
- **Junction motion theory.**
  - Mercedes frame (120° opening angles): Eqs. 3.1–3.5. It always exists for massless partons, but may not exist for massive ones (pp. 13–14).
  - Soft massless leg: it oscillates through the junction, and each oscillation shrinks by a factor 1/3 (Fig. 6, p. 15).
  - Pearl on a string: the case where, in the massive parton's rest frame, the other two legs open by more than 120°. The equation of motion is dp/dx = −2κ (Eqs. 3.6–3.7, App. B), so x_max = p₀/2κ. It is approximated by dx/dt = v₀ exp(−1.75 t/m) for κ ~ 1 GeV/fm (Eq. 3.8; Fig. 7 compares this with the numerical solution for u/d, c and b).
  - Optional "gluon-pearl" approximation: a light pearl is replaced by a massless gluon kink (Fig. 8, pp. 18–20).
  - Gluon kinks passing through the junction: theory only, not implemented (§3.3, Figs. 9–11).
- **New JRF algorithm.** The algorithm steps through a time-ordered sequence of three-parton frames (Mercedes or pearl). Each frame lasts for p_small, the smallest of |p_g|/2 and 2|p_q| (p. 25, Fig. 12). The frames are combined in an exponentially time-weighted average with scale p′_norm, derived from pNormJunction = 2 GeV, and stepping stops at p_max = 5 p_norm (Eqs. 4.1–4.2, p. 28). Fail-safes cover massive gluons and collinear partons (§4.2).
- **Tests.**
  - A toy three-parton system: two 50 GeV massless legs back to back plus one d (0.33 GeV) or b (4.8 GeV) quark along x, in the Ariadne frame. Diquark string breaks and popcorn are switched off (Fig. 14, p. 30).
  - pp NSD at 7 TeV and inelastic at 13 TeV, compared with Rivet analyses: CMS dN/dη, ⟨p⊥⟩(N_ch), Λ/K⁰_S, Ξ/Λ; ALICE Σc/D⁰, Λc/D⁰, Ξc ratios; LHCb Λb⁰/B⁰ and Λb asymmetry (Figs. 18–23). Lifetime cut τ_max = 10 mm/c.

## Results
- **λ-measure change.** It leaves junction-baryon fractions essentially unchanged (Fig. 13; old and new curves overlap within the MC statistics shown).
  - All baryons: the junction fraction is about 0.34 in the lowest p⊥ bin, peaks at about 0.5 near p⊥ ≈ 3 GeV, and falls to about 0.35–0.38 at 10 GeV.
  - Heavy-flavour baryons: the fraction falls from about 0.75 to about 0.6.
  - Both fractions are flat in |y|, at about 0.42 (all) and 0.70 (heavy) (Fig. 13; my reading of the plot).
- **Toy pearl tests.** Here old and new should coincide only above Ariadne-frame quark velocities of 0.98 (light d) and 0.64 (b) for p_norm = 2 GeV (p. 31).
  - The new average JRF lowers the multiplicity and ⟨p⊥⟩ of hadrons from the two hard legs by a few per cent for the d pearl (new/old about 0.95–0.99) and by ≲ 1.5% for the b pearl (Fig. 15).
  - The junction baryon is *harder* in the new model for b (⟨p⊥⟩ new/old up to about 1.1 at v ≈ 0.5; Fig. 16). The authors' explanation: the old model put too much p⊥ into the leg hadrons and compensated with a softer junction diquark (p. 33).
  - For light pearls, the old model gives junction baryons moving *opposite* to the junction (⟨v_x⟩ < 0, down to about −0.08) and negative junction-diquark masses (about −0.8 GeV). The new model fixes both (Fig. 17, p. 34).
  - Fragmentation errors of the "stuck in joining" type drop by about a factor 15 in dijet events at LHC energies (footnote 3, p. 35).
- **Gluon-pearl approximation.**
  - In the toy it raises ⟨p⊥⟩ and n_had relative to the standard new treatment, with a discontinuity at v = 1/2 (Figs. 15–16).
  - In 7 TeV pp it is used for only about 0.01% of junction baryons, with no visible effect on Λ/K⁰_S or Ξ/Λ (Fig. 18, p. 36). It is therefore off in the data comparisons.
- **Global pp observables.** dN_ch/dη and ⟨p⊥⟩(N_ch) (CMS 7 TeV) are equally well described by Monash, old and new, within about 10% (Fig. 19).
- **Σc.** With the CR Mode 2 spin-1 suppression, Σc/D⁰ and Λc(←Σc)/Λc are overpredicted. Theory/data for the dashed curves is ≈ 1.3–2 (several points off the ratio-panel scale; ≈ read off Fig. 20 main panels). With the default probQQ1toQQ0join, both junction models are near the data. Monash is at about 0.15 on the right panel, versus data of about 0.3–0.4 (Fig. 20).
- **Λ/K⁰_S (CMS 7 TeV).**
  - Old and new junction models agree with each other and with the data at the peak, p⊥ ≈ 2–3 GeV. Monash is about 30–35% low there (theory/data about 0.65–0.7; Fig. 21 top left).
  - Above about 5 GeV all models overpredict. The authors attribute this to diquark string breaks, because Monash shows it too (p. 39).
  - As a function of |y|: data about 0.54, both CR models about 0.53, Monash about 0.37 (Fig. 21 top right). The text calls default Pythia low by over 20% (p. 11).
- **Ξ/Λ.** All models underpredict. The junction models are lower (theory/data about 0.7–0.8 vs |y|) than Monash (about 0.8–0.9) (Fig. 21 bottom). The authors read this as needing strangeness enhancement beyond junctions (p. 40).
- **Λc⁺/D⁰ (ALICE 13 TeV, |y| < 0.5).** Data about 0.5 at low p⊥. Both junction models reproduce the trend, with theory/data ≈ 0.7–1.0 (Fig. 22 ratio panel). Monash is about 0.05–0.1 (Fig. 22 top left). The new model is "largely unchanged, … slightly higher relative enhancement at very low p⊥" (p. 41).
- **Λb⁰/B⁰ (LHCb 13 TeV, 2 < y < 4.5).** Data about 0.45 at low p⊥. The old model reaches about 1.2 and the new about 1.05 in the lowest bin. The text says "overpredicted by a factor of two in both" (p. 41). Monash is at about 0.1. The data show similar p⊥ shapes for Λc/D⁰ and Λb/B⁰, starting at about 0.5, which neither model reproduces (Fig. 22 top right, p. 41).
- **Λb asymmetry (LHCb 7 TeV, 2.15 < y < 4.10, 2 < p⊥ < 27 GeV).** Monash predicts about 12% at low p⊥ and 7–12% across y. Data and both junction models are at about 0–4%. The authors say the junction models slightly over-dilute the asymmetry, "consistent with" the Λb/B⁰ excess (Fig. 22 bottom, p. 41).
- **Ξc⁰/D⁰, Ξc⁺/D⁰, Ξc⁰/Λc⁺, Ξc/Σc (ALICE, |y| < 0.5).** All models are far below the data. For example, Ξc⁰/D⁰ data is about 0.35 at low p⊥ against models at about 0.05 (theory/data about 0.2–0.4; Fig. 23). This holds whichever junction treatment is used (p. 41). The Fig. 23 caption says 7 TeV, but the cited ALICE data [37] are at 13 TeV (inconsistency in the paper).

## Assessment
- This is mainly a technical consistency and robustness upgrade of the hadronization (junction fragmentation) step behind the Pythia QCD-CR model. It does not test CR as such. The physics conclusions about CR come from data comparisons where old and new are almost identical. The junction mechanism, with its default j₀ = 1.2 and the CR Mode 2 tune, is what drives the baryon enhancement.
- **Strongest constraint for our synthesis: Λb⁰/B⁰.** The QCD-CR + junction picture, which "explains" Λc/D⁰, overshoots Λb⁰/B⁰ by about 2×. This is a quantitative tension in the junction-CR explanation of heavy-baryon enhancement, and it bears on RQ1 (origin of baryon enhancement: CR junctions vs other mechanisms) and RQ3. The authors cannot say whether Λb is too high or B⁰ too low (p. 41).
- The Ξ and Ξc failures point to a separate strangeness mechanism (e.g. ropes). This supports the view that CR-junctions and ropes/strangeness enhancement are complementary rather than competing explanations of small-system effects. That is the authors' reading, without a combined fit.
- **Caveats.**
  - There is no retune. probQQ1toQQ0join was changed by eye from Σc data, and the authors call it "preliminary" (p. 38).
  - The "old" curves differ from published QCD-CR curves because of this parameter (p. 41).
  - The pearl motion uses a fitted exponential (Eq. 3.8), with an unspecified κ uncertainty.
  - Gluon kinks propagating through the junction are not implemented.
  - All comparisons are by eye with MC-stat ratio panels. No χ² is given.
- **RQ4 value.** The proposed tests (Λb/Λc, B⁰/D⁰, baryon–antibaryon correlation strength as a discriminator of junction vs diquark-break vs popcorn baryons, and junction–antijunction baryons in e⁺e⁻ → WW) are concrete. However, no quantitative predictions are given for them, and Fig. 24 is a schematic only.

## Leads
- Sjöstrand & Skands, "Baryon number violation and string topologies", NPB 659 (2003) 243 [hep-ph/0212264]: the original junction fragmentation and JRF algorithm that this paper replaces.
- Bierlich, Gustafson, Lönnblad, Shah, "The dynamic hadronization of charm quarks in heavy-ion collisions", arXiv:2309.12452: rapidity-based λ for heavy quarks, the alternative to Eq. 2.4. Charm hadronization in dense string environments (ropes/CR).
- LHCb, "Enhanced production of Λb⁰ baryons in high-multiplicity pp collisions at 13 TeV", PRL 132 (2024) 081901 [2310.12278]: the Λb/B⁰ data that the CR-junction model overpredicts by 2×. Multiplicity dependence is key for RQ1/3.
- LHCb, "Observation of a Λb⁰–Λ̄b⁰ production asymmetry in pp at 7 and 8 TeV", JHEP 10 (2021) 060 [2107.09593]: a direct observable sensitive to junction CR (beam-remnant vs junction Λb).
- ALICE, "Prompt D⁰, Λc⁺, Σc⁰,⁺⁺(2455) production in pp at 13 TeV", PRL 128 (2022) 012001 [2106.08278]: Λc/D⁰ and Σc data used to tune the junction diquark spin.
- ALICE, Ξc⁰ and Ξc⁺ cross sections at 13 TeV, arXiv:2105.05187: Ξc data that no CR/junction model describes.
- ALICE, "Exploring the non-universality of charm hadronisation through … Λc⁺ in jets", arXiv:2301.13798: a jet-level test of charm-baryon production mechanisms (CR vs coalescence).
- ALICE, "Flavor dependence of the baryon-to-meson ratio in pp at 13 TeV", PRD 108 (2023) 112003 [2308.04873], and "Charm production and fragmentation fractions at midrapidity in pp at 13 TeV", JHEP 12 (2023) 086 [2308.04877]: the breakdown of jet universality in heavy flavour.
- ALICE, "Enhanced production of multi-strange hadrons in high-multiplicity pp", Nature Phys. 13 (2017) 535 [1606.07424]: strangeness enhancement that, per this paper, junctions alone cannot explain (if not already in the DB).
- Bierlich, "Rope hadronization and strange particle production", EPJ Web Conf. 171 (2018) 14003 [1710.04464], and "Hadronisation models and colour reconnection", PoS DIS2016 051 [1606.09456]: the rope alternative/complement.
- Hunt-Smith & Skands, "String fragmentation with a time-dependent tension", EPJC 80 (2020) 1073 [2005.06219]: string-environment dependence. Cited for e⁺e⁻ multiplicity-dependent observables as RQ4 targets.
- Fischer & Sjöstrand, "Thermodynamical string fragmentation", JHEP 01 (2017) 140 [1610.09818]: an alternative string-breaking model with close-packing.
- Bellm, Duncan, Gieseke, Myska, Siódmok, "Spacetime colour reconnection in Herwig 7", EPJC 79 (2019) 1003 [1909.08850]: a Herwig CR model with baryonic clusters, for comparison with junctions.
- OPAL, "Tests of models of color reconnection and a search for glueballs using gluon jets with a rapidity gap", EPJC 35 (2004) 293 [hep-ex/0306021], and Siebel, Moriond 2005 [hep-ex/0505080]: gluon-jet / octet-string tests that the authors suggest revisiting.
- Eden & Gustafson, "Baryon production in the string fragmentation picture", Z. Phys. C 75 (1997) 41 [hep-ph/9606454], and Andersson, Gustafson, Sjöstrand, Phys. Scripta 32 (1985) 574: popcorn baryon production. Baryon–antibaryon correlations as a discriminator (RQ4).
- Rathsman, "A generalized area law for hadronic string re-interactions", PLB 452 (1999) 364 [hep-ph/9812423], and Sandhoff & Skands, "Colour annealing" (Les Houches 2005, FERMILAB-CONF-05-518-T): early pp CR toy models.
- Follow-up search: papers citing this one on junction-antijunction / baryon correlations in e⁺e⁻ → WW, and later Altmann–Skands work on b vs c CR and strangeness at junctions (the authors announce both, pp. 40–44).
