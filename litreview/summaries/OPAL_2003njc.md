# Tests of models of color reconnection and a search for glueballs using gluon jets with a rapidity gap
- **ID / links:** OPAL:2003njc · INSPIRE 620566 · arXiv hep-ex/0306021 · DOI 10.1140/epjc/s2004-01809-2
- **Authors / collab, year, journal:** OPAL Collaboration (G. Abbiendi et al.), 2004, Eur. Phys. J. C 35 (2004) 293 (CERN-EP-2003-031)
- **Type:** experimental
- **Relevance:** 3 · RQs: 1a, 1b, 2, 3, 4
- **Full text source:** arxiv

Page anchors are the preprint's printed page numbers (printed p. N = PDF page N+1). All 43 PDF pages were read; the author list was skipped.

## Takeaways
- This is the LEP1 single-system (Z → qq̄g) colour-reconnection (CR) test. It is the "Z → 3-jet" result that the LEP-wide WW CR combination cites for ruling out ARIADNE-1 and Rathsman's GAL-type model (see ALEPH_2013dgf). Gluon jets are anti-tagged with b vertices (12 611 jets, ⟨E⟩ ≈ 22 GeV, purity 95 %). OPAL then selects the ~5 % that have a rapidity gap (655 jets, purity 86 %) and studies the "leading part" beyond the gap (pp. 16, 19, 39).
- The signature is clean. CR models produce an isolated, colour-singlet gluonic string beyond the gap (Fig. 1b). Its charge is zero and it has an even number of charged particles. The models therefore predict large **spikes at n_ch^leading = 2, 4 (6)** and an excess at **Q_leading = 0** (Figs. 10, 13, 14; pp. 22, 27). The data show no spikes.
- **Rathsman-CR (Pythia 5.7, R₀ = 0.1) and Ariadne-CR (Lönnblad, PARA(26) = 9) are "strongly disfavored"** with standard parameters (p. 22). Fitting the suppression parameter to the Q_leading = 0 bin gives:
  - R₀ = 0.0085 ± 0.0075 (stat) ± 0.0087 (syst), consistent with 0 (p. 28);
  - PARA(26) = 96 (central), 41 at +1σ, against the default 9, which is effectively the large-N_C, no-CR limit (p. 34).
- A retune of the shower cutoffs can also make the models fit the gap data, but only with unphysical values: Q₀ ≈ 3.2–5.5 GeV (Rathsman, normally 1–2 GeV) or p_T,min ≈ 1.5–4.7 GeV (Ariadne-CR, normally 0.6–0.7 GeV). These retunes wreck the inclusive Z event shapes: total χ² rises from 243.5 to 327–1118 for Rathsman and from 32.4 to 133–3019 for Ariadne-CR (Tab. 3; pp. 31, 34; normal ranges quoted on pp. 33, 36). The authors conclude that CR as implemented in these two models is disfavoured (p. 39).
- **Herwig-CR (cluster CR, probability 1/9): no definite conclusion.** At hadron level it also predicts even-n spikes (Fig. 14a), but detector resolution washes them out (Fig. 11). The data are "better described" by Herwig without CR (p. 40).
- The glueball search finds no significant signal (Sect. 8): there are only ~2σ excesses in M_leading at 1.0–2.5 GeV and in M^{+−+−} at 2.5–3.0 GeV (pp. 36–37).

## Setup
- **Data and selection.** OPAL, e⁺e⁻ → Z, 1993–95 (within 3 GeV of the peak), ~2.72 M hadronic events, of which 2.407 M pass track/thrust cuts (pp. 5–6).
  - Particles are tracks (pion mass) plus EM clusters after track-cluster matching (pp. 5–6).
  - Jets: Durham, forced to exactly 3 jets, energies computed from the angles (p. 11).
  - Gluon jet = anti-tagged jet. The two quark jets need secondary vertices with L/σ_L > 2 (highest-energy jet) or > 5 (lower-energy jets) (p. 16).
  - Hardness scale κ_jet = E_jet sin(θ_min/2) (Eq. 1). Cuts: κ_jet ≥ 7 GeV, E_jet < 35 GeV, ≥ 2 particles. This gives 12 611 jets with ⟨E⟩ = 21.7 GeV (RMS 6.6 GeV) and Jetset purity 94.6 ± 0.1 % (p. 16; Fig. 6). Ariadne-CR gives a purity of only ~72 % (footnote 5).
- **Rapidity-gap definition.** Rapidities are taken relative to the jet axis.
  - "y_min sample": the smallest particle rapidity is y_min ≥ 1.4 (496 jets).
  - "Δy_max sample": for jets with y_min < 1.4, the largest gap between adjacent particles is Δy_max ≥ 1.3 (159 jets).
  - Total: 655 jets, purity 85.7 ± 1.0 % (pp. 17–19; Figs. 7–9).
  - The cuts were chosen where δ = (CR − noCR)/noCR becomes significant (Eq. 2; Figs. 8b, 9b).
  - Herwig-CR shows no excess in Δy_max (Fig. 9b), so it is tested with the y_min sample only (p. 19).
  - Leading part = all particles beyond the gap. Distributions are normalised to all 12 611 gluon jets, so they are sensitive to the gap rate (p. 19).
- **Observables.** n_ch^leading and Q_leading (charge sum, as suggested by Minkowski–Ochs [9]). Both are shown at detector level (Figs. 10–12) and at hadron level (Figs. 13–14).
  - Unfolding: an unfolding matrix plus bin-by-bin factors from Herwig, with corrections of ~40 % (pp. 26–27).
  - Systematics (pp. 9, 27): correction model (Jetset, Ariadne, Herwig-CR), tracks only, |cos θ| < 0.70, p_T > 0.15 GeV, and L/σ_L > 3 for quark tagging (1002 jets, purity 76 %).
- **Models.**
  - No-CR: Jetset 7.4, Herwig 6.2 and Ariadne 4.11, OPAL-tuned (Tabs. 1–2).
  - CR: Ariadne-CR (Lönnblad, an extension of Gustafson–Häkkinen; the three MSTA(35) variants coincide in Z decays, footnote 3); Herwig-CR (Corcella et al., PRECO = 1/9); and Rathsman-CR (Pythia 5.7, R₀ = 0.1, OPAL Jetset tune) (pp. 6–8).
  - Ariadne-CR and Herwig-CR were retuned slightly to give the right ⟨n_ch⟩: PARJ(42) 0.63 → 0.55; CLMAX 3.35 → 3.75 and RMASS(13) 0.75 → 0.793 (p. 8). The Pythia built-in Sjöstrand–Khoze CR was not used because it does not apply to Z decays (p. 8).
- **Inclusive Z cross-check.** S, A, −ln y₃₄ and y_T are corrected to hadron level. χ² values use total errors without correlations and are meant as relative measures within one model family only (pp. 9–11; Tab. 3).

## Results
- **The CR models are invisible in inclusive Z data** (Tab. 3, χ² over 81 bins):

| Model | χ² | ⟨n_ch⟩ |
|---|---|---|
| Ariadne | 36.9 | 21.06 |
| Ariadne-CR | 32.4 | 21.09 |
| Jetset | 200.7 | 21.09 |
| Rathsman-CR | 243.5 | 20.80 |
| Herwig | 127.9 | 21.14 |
| Herwig-CR | 151.6 | 21.06 |

  - The LEP average is ⟨n_ch⟩ = 21.15 ± 0.29 (p. 11).
  - The ~20 % χ² increases for Herwig-CR and Rathsman-CR come mainly from y_T (p. 11).
- **Gap rates.** δ_ymin rises above y_min ≈ 1.4. For Rathsman-CR/Jetset it reaches ~+3 at y_min ≈ 2.5, i.e. about 4× the no-CR rate; Ariadne-CR is smaller and Herwig-CR smaller still (≈ read from Fig. 8b). Rathsman-CR and Ariadne-CR show a clear excess above Δy_max ≈ 1.3, while Herwig-CR shows none (Fig. 9b).
- **Detector level, standard selection** (Fig. 10; p. 22):
  - Rathsman-CR and Ariadne-CR predict ~2× the data at n_ch^leading = 2 and ~1.5× at n = 4 (≈ read from Fig. 10). The data show no spiking.
  - Jetset describes the data except at n = 1, 2, 4, where the data are > 1σ higher. Ariadne is worse.
  - Q_leading = 0: Jetset and Ariadne are ~20 % below the data, and the CR models are far above (Fig. 12a; p. 22). Herwig (no CR) describes Q_leading well.
  - The authors therefore do not read the Jetset/Ariadne deficits as evidence for CR (p. 24).
- **Herwig-CR** (y_min sample): there is a systematic excess over Herwig at n = 2–5 (Fig. 11) and an excess at Q_leading = 0, 1 (Fig. 12b). The overall description is "reasonable", and Herwig without CR is best (pp. 22, 24).
- **Hadron level** (Fig. 13): the same pattern, and Rathsman-CR also spikes at n = 6. For Herwig-CR, the hadron-level spikes at n = 2, 4, 6 (Fig. 14a) suggest that the isolated gluonic system is a general CR feature (pp. 27–28).
- **Stability checks.** With softer gluon jets (4 < κ_jet < 7 GeV, κ_jet < 4 GeV) or energy-ordered gluon tagging (94 000 jets, ⟨E⟩ = 12.9 GeV, purity 81 %; 6604 gap jets, purity 56 %), the predicted spikes, especially at n = 4, are much less prominent. The data conclusions are unchanged (pp. 24, 26). The sensitivity therefore needs hard, acollinear gluons.
- **Parameter scans.** The quantity scanned is ΔQ = MC − data in the hadron-level Q_leading = 0 bin (Figs. 15, 16; band = ±1σ total).
  - **Rathsman-CR** (Fig. 15; pp. 28–33):
    - ΔQ → 0 needs Λ_QCD ≈ 1.3 GeV or Q₀ ≳ 4 GeV. Varying a or σ_q cannot do it.
    - Retuned to (Q₀, b) = (5.5 GeV, 0.27 GeV⁻²): ΔQ = 6.7 × 10⁻⁷, but χ²_Z = 1117.7 against 243.5 standard (Tab. 3). The 1σ/2σ-compatible tunes (3.7, 0.35) and (3.2, 0.38) give χ² = 435.1 and 327.2 (p. 31).
    - The Λ_QCD route gives at best ΔQ = 0.012 with χ² = 2.1 × 10⁴. The combined Λ_QCD + Q₀ route gives ΔQ = 0.004 with χ² = 1606 (p. 33).
  - **Ariadne-CR** (Fig. 16; pp. 33–36):
    - Retuned to p_T,min = 4.7 GeV, b = 0.17 GeV⁻²: χ²_Z = 3019.3 against 32.4 standard. The 1σ/2σ tunes (2.0 GeV, 0.35) and (1.5 GeV, 0.42) give 333.1 and 132.6.
    - Λ_QCD is limited by Λ < p_T,min. The best Λ_QCD + p_T,min solution gives ΔQ = 0.0041 with χ² = 2095.
- **Glueball search** (detector level, compared with no-CR models; pp. 36–38; Fig. 18):
  - M_leading for the Q_leading = 0 jets (250 jets): the three bins at 1.0–2.5 GeV give χ² = 11.5 (Jetset), 7.3 (Herwig) and 6.0 (Ariadne), described as about 2σ.
  - M^{+−+−}: the largest excess is at 2.5–3.0 GeV, ~2σ above Ariadne.
  - M^{+−} and the cos θ* of opposite-charge pairs are well described. The Herwig spike at 0.77 GeV in M^{+−} comes from a too-narrow ρ.
  - Conclusion: no evidence for glueball-like or scalar objects.

## Assessment
- **Strength of the exclusion.** No formal CL is given for the main statement. The most quantitative handle is the R₀ fit. From the quoted errors, R₀ = 0.1 lies ~8σ from the fitted 0.0085 ± 0.0115 (our estimate, adding stat and syst in quadrature and assuming Gaussian errors).
  - The retune argument is qualitative because the inclusive χ² values ignore correlations (p. 10). Still, the χ² increases are by factors of 1.3–90 within the same model family, and the required cutoffs are far outside normal ranges.
  - The exclusion is robust for the *specific* 1990s implementations. It does not show that "soft colour rearrangement in e⁺e⁻ is absent".
- **What is actually constrained** is *intra-system* CR in a single colour singlet (Z → qq̄g), via isolated gluon loops (Gustafson–Häkkinen / Rathsman GAL / Lönnblad dipole swapping). Inter-W CR in LEP2 WW is a different process.
  - The LEP combination nonetheless uses this result to discard ARIADNE-1/GAL as WW CR models (ALEPH_2013dgf, pp. 66–67). That transfer is reasonable because the same reconnection rule acts in both, but it is an extrapolation.
- **Tension with HERA and Tevatron.** Rathsman's model with R₀ = 0.1 was found to describe rapidity-gap measurements in ep and pp̄ collisions (p. 8, citing Enberg–Ingelman–Timneanu [30]; Rathsman_1998tp). These Z data want R₀ ≈ 0. So a single "universal" soft-colour-interaction strength does not hold across e⁺e⁻ and hadron-initiated processes, or the e⁺e⁻ implementation differs. This bears directly on RQ1/RQ2: gap formation at HERA/Tevatron may need a mechanism, such as the hadron remnant, that is absent in e⁺e⁻.
- **Caveats.**
  - The no-CR baselines also miss the gap data: Jetset and Ariadne are ~20 % low at Q_leading = 0 (Fig. 12a). The data lie *between* the no-CR and CR predictions, and the authors admit that a small amount of CR is allowed (pp. 22–24). The unfolding uses Herwig, and the purity estimate is model-dependent (72 % in Ariadne-CR).
  - The parameter scans are one-at-a-time, apart from the two-parameter iterations described.
- **Relevance to modern MC.** PYTHIA 8 (QCD-based CR with junctions, gluon-move), Herwig 7 (plain/statistical/baryonic CR) and ropes all produce colour-singlet gluon systems at some rate. This observable (n_ch^leading even-n spikes, Q_leading = 0 in gap gluon jets) is a sharp, underused e⁺e⁻ test of any CR model that acts in a single system. It has RQ4 value for an FCC-ee/Z-pole re-analysis. We did not check whether a HEPData record or Rivet analysis exists, and that should be checked.
- **Gluon "ladder/octet" picture.** The glueball motivation (octet field, Fig. 17) is speculative. The null result constrains only resonance production at the ~2σ level with 250–655 jets.

## Leads
- OPAL, Eur. Phys. J. C11 (1999) 217 [11]: the earlier OPAL gluon-jet rapidity analysis that already tested Ariadne-CR. It is the precursor result.
- P. Minkowski & W. Ochs, Phys. Lett. B485 (2000) 139 [9]: proposes the gap-gluon-jet glueball and charge test. It is an RQ4 proposal.
- J. Rathsman, Phys. Lett. B452 (1999) 364 [27]: the GAL/Rathsman CR model tested here (already summarised as Rathsman_1998tp; check that the IDs match).
- L. Lönnblad, Z. Phys. C70 (1996) 107 [25] and G. Gustafson & J. Häkkinen, Z. Phys. C64 (1994) 659 [28]: the Ariadne-CR model and its origin (Lonnblad_1995yk and Gustafson_1994cd are already summarised).
- G. Corcella et al., JHEP 0101 (2001) 010 [18]: HERWIG 6 with the cluster CR model, PRECO = 1/9.
- SLD, Phys. Rev. Lett. 76 (1996) 4886 [10]: rapidity gaps in inclusive and 2-/3-jet Z events, an earlier e⁺e⁻ gap test.
- R. Enberg, G. Ingelman & N. Timneanu, J. Phys. G26 (2000) 712; Phys. Rev. D64 (2001) 114015 [30]: SCI/GAL descriptions of HERA and Tevatron gaps, the counterpart to the tension noted above.
- C. Peterson & T.F. Walsh, Phys. Lett. B91 (1980) 455 [40]: colour-octet fields and glueball production in gluon jets.
- V.A. Khoze & T. Sjöstrand, Z. Phys. C62 (1994) 281 and Phys. Rev. Lett. 72 (1994) 28 [29]: SK CR, which was not applicable to Z decays here.
- Forward: papers citing this one for modern CR tests in e⁺e⁻ (e.g. Christiansen–Skands-type QCD-based CR, Herwig 7 CR). A `citing 620566` run is worthwhile.
