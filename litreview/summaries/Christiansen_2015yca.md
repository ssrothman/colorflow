# Colour Reconnection at Future e⁺e⁻ Colliders
- **ID / links:** Christiansen:2015yca · INSPIRE 1380468 · arXiv 1506.09085 · DOI 10.1140/epjc/s10052-015-3674-4
- **Authors / collab, year, journal:** J. R. Christiansen, T. Sjöstrand (Lund), 2015, Eur. Phys. J. C (per DOI; volume/page not printed on the arXiv version). LU TP 15-25 / MCnet-15-15
- **Type:** phenomenology (MC/model comparison)
- **Relevance:** 3 · RQs: 2, 3, 4
- **Full text source:** arxiv

## Takeaways
- Re-tests LEP2 W⁺W⁻ → 4q colour reconnection (CR) with the newer LHC-era Pythia 8 models: gluon-move (GM-I move only, GM-II flip only, GM-III both) and the SU(3)-colour-rule "QCD-based" CS model with junctions, alongside re-implemented SK-I/SK-II/SK-II′ (pp. 2–4).
- CR-induced W-mass shifts at 170 GeV are model-dependent in **sign** as well as size: SK-I about +10 to +18 MeV, SK-II about −13 to −18 MeV, GM-I about −27 to −41 MeV, GM-II about +31 to +49 MeV, GM-III and CS within ±7 MeV. The move and flip steps of GM cancel almost exactly in GM-III, and the authors call this accidental (Tab. 1, p. 6; text p. 5).
- The shifts grow at 240 GeV (GM-II about +370 to +400 MeV, GM-III about +100 MeV, SK-I about +90 MeV). CS shows almost no effect at any energy (Tab. 2, p. 6; text p. 5). The authors argue for repeating the m_W(4q) − m_W(2qℓν) comparison at a future collider as a CR constraint.
- Against the preliminary LEP particle-flow ratio r = 0.969 ± 0.011 ± 0.009 ± 0.006, only GM-I (r > 1) is excluded at > 3σ (3.9σ). No-CR is at 2.0σ, and the other models are at 0.6–2.1σ (Tab. 3, Tab. 4, p. 8; text p. 7).
- New RQ4 tests: (i) the hadronic/semileptonic multiplicity ratio, which is exactly 2 without CR and 1.93–1.97 with CR models at 170 GeV (p. 7). (ii) In H → W⁺W⁻ → 4q, CR distorts the Higgs-parity angles (θ₁, θ₂, Φ) about as much as a 2–5% CP-odd admixture (Fig. 3, p. 9; Fig. 4, p. 10; conclusions p. 10).

## Setup
- MC study with Pythia 8 (p. 3). CR is applied after the parton shower and before hadronisation. The default MPI-based Pythia CR model is not usable in e⁺e⁻ and is not studied (p. 3).
- Models (pp. 3–4):
  - **SK-I and SK-II.** Space-time string-overlap models (Type I / Type II superconductor analogy). SK-I has a strength parameter, and the best LEP fit had about 50% of events reconnected (p. 3). In the primed variants, a reconnection is accepted only if it reduces λ.
  - **GM.** Minimises λ = Σ ln(1 + m_ij²/m₀²) (Eq. 1) by gluon moves and string flips, with no colour algebra and no space-time (Fig. 1). Parameters are tuned to LHC minimum bias.
  - **CS.** SU(3) colour rules plus a causality requirement, and junction formation. "CS max" ignores the colour rules.
  - Colour ropes are explicitly not considered (p. 4).
- **W mass (Sect. 3).** e⁺e⁻ → W⁺W⁻ → 4q at 170 GeV (also 240 and 350 GeV), 10⁶ events per model. Exactly 4 Durham jets with k⊥ cut 8 GeV, E_jet > 20 GeV, separation > 0.5 rad. Four jet-pairing methods: MC truth; minimise |m̄_W − 80|; minimise the sum of both |m_W − 80|; maximise opening angles. Breit–Wigner broadening is removed by subtracting the produced W mass (pp. 4–5).
- **Particle flow (Sect. 4).** Mimics L3 at 183 GeV: Durham y_cut = 0.005, inter-jet angle requirements, rescaled angle φ_r (Fig. 2). R_N is the ratio of intra-W (A+C) to inter-W (B+D) particle flow in a φ_r window (Eq. 2), and r = R_N^CR / R_N^noCR.
- **Higgs CP (Sect. 5).** μ⁺μ⁻ → H⁰ → W⁺W⁻ → 4q, used as a technical trick to isolate the decay. 10⁸ events per model and per parity fraction. CP-odd admixture is parametrised by the fraction f (Eqs. 3–4). Durham k⊥ 8 GeV, E_jet > 10 GeV, pairing by min |M_W − 80| (pp. 8–9).

## Results
- **Mass shifts at 170 GeV (Tab. 1, p. 6).** ⟨δm̄_W⟩ in MeV, for pairing methods 1/2/3/4; statistical uncertainty 4 MeV.

  | Model | Method 1 | Method 2 | Method 3 | Method 4 |
  |---|---|---|---|---|
  | SK-I | +18 | +13 | +14 | +10 |
  | SK-II | −14 | −13 | −18 | −18 |
  | SK-II′ | −6 | −7 | −9 | −9 |
  | GM-I | −41 | −28 | −37 | −27 |
  | GM-II | +49 | +34 | +40 | +31 |
  | GM-III | +2 | −1 | −5 | −3 |
  | CS | +7 | +3 | +6 | +3 |
  | CS max | +136 | +73 | +131 | −131 |

  SK-I and SK-II differ slightly from the original SK paper because the shower is now p⊥-ordered (p. 5). The authors say the CS max case "is already excluded at hadron colliders" (p. 5). Our observation, not remarked on in the paper: the CS max entries are exactly the negatives of the no-CR ⟨Δm̄_W⟩ column (−136, −73, −131, +131), including the sign flip for method 4, which looks suspicious (possible table artefact); treat the CS max row with caution.
- **Mechanism of the GM shifts (p. 5).** The move step attaches a large-angle gluon from W₁ to W₂, which raises m(W₂) less than it lowers m(W₁), so ⟨m_W⟩ decreases. The flip step creates strings between the Ws, which produces particles outside the W "cones" and raises m_W.
- **Energy dependence (Tab. 2, p. 6).** Statistical uncertainty 5 MeV; ranges are over pairing methods 1–3.

  | Model | 240 GeV (MeV) | 350 GeV (MeV) |
  |---|---|---|
  | SK-I | +87 to +95 | +70 to +72 |
  | SK-II | +26 to +30 | +18 |
  | SK-II′ | +24 to +26 | +15 to +16 |
  | GM-I | −68 to −74 | −50 |
  | GM-II | +369 to +402 | +369 |
  | GM-III | +93 to +105 | +60 |
  | CS | +8 to +10 | +3 to +4 |

  Shifts rise from threshold to intermediate energy and then fall. Two competing effects explain this: a single reconnection has a larger effect at higher energy, but two strings are less likely to overlap (p. 5).
- **Particle flow, LEP data (pp. 5–6).** The preliminary LEP combination [29] gives r = 0.969 ± 0.011(stat) ± 0.009(syst.corr) ± 0.006(syst.uncorr), 2.2σ from no-CR (text, p. 6). Our check: adding the three errors in quadrature gives (1 − 0.969)/0.0154 = 2.0σ, matching the no-CR entry of Tab. 4; the paper does not explain the 2.2σ (possibly a different error treatment in the preliminary combination [29]). The later combination [11] disfavours no-CR at 2.8σ when combined with the mass-shift results, but publishes no separate r.
- **Particle flow, model predictions (Tab. 3, p. 8).** At 183 GeV in the 0.2–0.8 window, R_N^noCR = 1.1482 and the statistical uncertainty on r is about 0.0025.

  | Model | r (0.2–0.8) |
  |---|---|
  | SK-I | 0.9802 |
  | SK-II | 0.9916 |
  | SK-II′ | 0.9931 |
  | GM-I | 1.0293 |
  | GM-II | 0.9440 |
  | GM-III | 0.9918 |
  | CS | 0.9910 |
  | SK-I max | 0.9360 |
  | CS max | 0.9781 |

  Narrower windows give larger deviations from 1, for example GM-II 0.9181 and SK-I max 0.9068 in the 0.4–0.6 window (Tab. 3). GM-I is the only model with r > 1, because its gluon moves lower the radiation in regions B and D (p. 7).
- **Comparison with data, deviations n_σ (Tab. 4, p. 8).**

  | Model | n_σ |
  |---|---|
  | no CR | 2.0 |
  | SK-I | 0.7 |
  | SK-II | 1.5 |
  | SK-II′ | 1.6 |
  | GM-I | 3.9 |
  | GM-II | 1.6 |
  | GM-III | 1.5 |
  | CS | 1.4 |
  | SK-I max | 2.1 |
  | CS max | 0.6 |

  The authors: GM-I is the only model excluded at 3σ, and SK-I with default strength agrees well (p. 7).
- **Energy dependence of r (Tab. 5, p. 8).** Uses an alternative pairing similar to mass method 3, 0.2–0.8 window, statistical uncertainty about 0.0015.

  | Model | 183 GeV | 240 GeV | 350 GeV |
  |---|---|---|---|
  | R_N^noCR | 1.9003 | 1.1764 | 1.4459 |
  | SK-I | 0.9900 | 0.9820 | 0.9829 |
  | GM-II | 1.0247 | 1.0130 | 1.0022 |
  | GM-III | 0.9768 | 0.9362 | 0.9228 |
  | CS | 0.9902 | 0.9993 | 1.0028 |
  | SK-I max | 0.9667 | 0.9030 | 0.8502 |

  The extreme models deviate more at higher energy, the moderate models show no clear trend, and CS shows no sensitivity (p. 7).
- **Multiplicity ratio (p. 7).** N_ch(4q) / (N_ch(qqℓν) − 1), with ℓ = e, μ, equals 2 without CR. At 170 GeV the authors find 1.96 (GM-I), 1.97 (GM-II), 1.93 (GM-III; here the move and flip effects add coherently) and 1.97 (CS), with "similar results" for SK. They call it more sensitive than the four-jet angular measurement for CS. No uncertainties are quoted.
- **Higgs parity (Fig. 3).** All three angles show visible deviations at the percent level for f = ±0.05 and for the CR models. For θ₁ and θ₂, CR and CP-oddness shift the distributions in the same direction; for Φ they shift them in opposite directions, so a simultaneous fit could separate the two effects (p. 9). The interference sign is unimportant: the f = +0.05 and f = −0.05 curves almost coincide.
- **Higgs parity (Fig. 4, p. 10).** χ²/NDF relative to a CP-even, no-CR Higgs, for the θ₁ angle (the caption calls it φ₁). Values ≈ (read off Fig. 4; line identities from the legend colours/dash styles in the PDF vector graphics): no-CR with f = 0.01/0.02/0.03/0.04/0.05 ≈ 0.8/1.2/3.1/8.9/20; horizontal lines GM-II (blue dashed) ≈ 13.5, GM-I (red dashed) ≈ 3.7, SK-I ≈ 2.1, SK-II ≈ 1.9, GM-III ≈ 1.6, SK-II′ and CS ≈ 1.05. The crossover, where CP-oddness matches the CR effect, is at f ≈ 2–5%, "with the higher values for somewhat more extreme CR models" (p. 9). The authors say that limits below 2% should be reachable if CR is modelled carefully.
- **Outlook (p. 10).** At the tt̄ threshold, three colour singlets (W, W, bb̄) increase the possibilities for CR. Only early studies exist [33], and dedicated work is needed.

## Assessment
- Useful as the bridge between LHC-tuned CR models (GM, CS) and LEP2 W⁺W⁻ constraints. The key qualitative lesson is that **the sign of δm_W is model-dependent**: SK-I vs SK-II, and GM-I vs GM-II. A single "CR on/off" systematic is therefore not conservative.
- The comparison with LEP data uses only the *preliminary* r from hep-ex/0612034 [29], because the final LEP combination (Phys. Rept. 532) does not publish r. The authors themselves note that the experiment-level results are detector-level, so the comparison uses only the ratio to no-CR. These are approximate tests, not a refit.
- Minor internal tension. The text says maximal SK-I "gives too large shifts and so can be excluded" (p. 7), yet Tab. 4 lists it at 2.1σ, comparable to no-CR at 2.0σ. "Excluded" there seems to be meant loosely.
- r for GM-II is 0.9440 with the L3-like pairing (Tab. 3) but 1.0247 at the same √s with the alternative pairing (Tab. 5). The observable is strongly analysis-dependent, so Tab. 5 should not be compared directly with LEP data. The baseline R_N^noCR also differs (1.1482 vs 1.9003).
- The multiplicity-ratio and Higgs-CP numbers have no quoted uncertainties or detector effects. The Higgs study uses μ⁺μ⁻ → H as a technical device, and only the θ₁ χ² is shown. Treat the 2–5% crossover as an order-of-magnitude indication.
- Rope or string-overlap effects (Bierlich et al.) are explicitly excluded, so this is not a complete map of models.

## Leads
- Christiansen & Skands, "String formation beyond leading colour", arXiv:1505.01681 (journal ref not given in this paper): defines the CS (QCD-based CR) model used here.
- Argyropoulos & Sjöstrand, JHEP 1411 (2014) 043, arXiv:1407.6653: GM models and CR in tt̄ (already summarised as Argyropoulos_2014zoa).
- LEP EW WG, "Electroweak measurements in e⁺e⁻ collisions at W-pair energies", Phys. Rept. 532 (2013) 119, arXiv:1302.3415: final LEP CR combination (2.8σ against no-CR).
- LEP EW WG, preliminary combination, arXiv:hep-ex/0612034: the source of r = 0.969 used here.
- OPAL, EPJC 45 (2006) 291, hep-ex/0508062; DELPHI, EPJC 51 (2007) 249, arXiv:0704.0597; ALEPH m_W, EPJC 47 (2006) 309, hep-ex/0605011; DELPHI m_W, EPJC 55 (2008) 1, arXiv:0803.2534: LEP2 CR measurements and the m_W(4q) vs m_W(2qℓν) CR constraints.
- Khoze & Sjöstrand, "Color correlations and multiplicities in top events", PLB 328 (1994) 466, hep-ph/9403394: CR at the tt̄ threshold in e⁺e⁻.
- Skjold & Osland, PLB 311 (1993) 261, hep-ph/9303294, and NPB 453 (1995) 3, hep-ph/9502283: angular correlations for Higgs CP in H → VV. Context for the RQ4 Higgs test.
- Bierlich, Gustafson, Lönnblad, Tarasov, JHEP 1503 (2015) 148, arXiv:1412.6259: overlapping strings / ropes, the alternative mechanism not studied here.
- Forward: papers citing this one for FCC-ee / CEPC CR studies (e.g. W mass at 240 GeV, tt̄ threshold).
