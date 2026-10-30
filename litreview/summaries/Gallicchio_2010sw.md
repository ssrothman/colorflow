# Seeing in Color: Jet Superstructure
- **ID / links:** Gallicchio:2010sw · INSPIRE 844004 · arXiv 1001.5027 · DOI 10.1103/PhysRevLett.105.022001
- **Authors / collab, year, journal:** J. Gallicchio, M. D. Schwartz, 2010, Phys. Rev. Lett. 105 (2010) 022001
- **Type:** phenomenology
- **Relevance:** 3 · RQs: 1b, 1d, 2, 4
- **Full text source:** arxiv

## Takeaways
- Introduces **jet pull** t⃗ = Σ_{i∈jet} (p_T^i |r_i| / p_T^jet) r⃗_i, with r⃗_i = (Δy_i, Δφ_i) measured from the jet axis (Eq. 1). This is the founding paper of the pull observables that ATLAS, D0 and CMS later measured in tt̄ and H→bb̄.
- Physical picture: radiation from a colour dipole is emitted mainly in the angular region between its two ends. So a jet's soft radiation is "pulled" toward its colour partner: the other b for a colour singlet H→bb̄, the beam for g*→bb̄ (Fig. 1, Fig. 2, p. 2).
- Most of the discriminating information is in the **pull angle** θ_t, not the magnitude |t⃗| (Fig. 3, p. 3). For H→bb̄ the signal peaks toward the other b jet, while the Zbb̄ background is nearly flat (Fig. 5).
- The paper gives no quantitative significance gain, ROC curve or S/√B. The claim of discrimination power is qualitative only (Fig. 5, p. 3). The only number is a guess that "a few percent improvement" could come from optimising the jet algorithm with the experiments (p. 4).
- Proposes the experimental validation that was later carried out: hadronic W in semileptonic tt̄ as a colour-singlet control, with the b jets colour-connected to the beam as a contrasting sample (p. 4).

## Setup
- Example process: pp → ZH, H → bb̄ (m_H = 120 GeV), Z → leptons, against Zbb̄ background (p. 2–3). The LHC √s is not stated explicitly in the text.
- MC: MadGraph 4.4.26 matrix elements + Pythia 8.130 (shower, hadronization, UE) as benchmark. Cross-checks with Herwig++ 2.4.2 and Pythia 6.420 (pT-ordered) (p. 2–3).
- Fixed-kinematics study: one parton configuration, b at (y, φ) = (−0.5, −1) and (0.5, 1), p_T = 200 GeV each. It is showered 3×10⁶ times (Fig. 2) or 10⁵ times (Fig. 3, Fig. 4) with the colour connection set by hand: b–b̄ connected (signal) vs each b connected to a beam (background) (p. 2).
- Full study: parton-level p_T > 15 GeV for the b's, anti-kT R = 0.7, reconstructed mass within a 20 GeV window around 120 GeV, pull computed from the constituents of each jet, 3×10⁵ events (Fig. 5, p. 3).
- Inputs: all long-lived particles, or 0.1×0.1 calorimeter cells treated as massless (p. 3). Rapidity rather than pseudorapidity is used for the jet axis, for boost invariance (p. 3).
- Also examined: the second-moment covariance tensor C (Eq. 2), its eigenvalues a ≥ b, size g = √(a²+b²), and eccentricity (p. 4).

## Results
- Fixed-kinematics radiation maps show the colour connection clearly. For signal, radiation fills the region between the b's; for background it extends toward the beams. Contours are factors of 2 (Fig. 2).
- Pull-vector density in polar coordinates: signal is concentrated toward the other b (which the text places at θ_t ≈ 0.7; θ_t = 0 is the right-going beam); background is concentrated toward θ_t = ±π, the left-going beam (Fig. 3, p. 3).
- Pull-angle distributions for this kinematic point are "quite similar" for Herwig++ 2.4.2, Pythia 8.130 and Pythia 6.420 pT-ordered (Fig. 4, p. 3). The authors read this as low sensitivity to the MC used. The signal peak is ≈2.5× its value at θ_t = −π (≈2.2–2.4 vs ≈0.8–1.0, ≈ read from Fig. 4).
- Full ZH vs Zbb̄ with UE and hadronization: the signal Δθ_t distribution (Δθ_t = 0 pointing to the other b) peaks at 0 at ≈1.5× the near-flat background level (≈3 vs ≈2, read from Fig. 5). This holds for both the harder and the softer b jet (Fig. 5).
- In the dominant background, the alternative colour flow (left jet connected to the right-going beam, giving a signal-like pull) occurs in "about 10%" of events (p. 3).
- IRC safety: pull is linear in p_T, so it is soft-safe and collinear-safe. The authors argue it is therefore insensitive to calorimeter granularity and resolution (p. 3). Cell-based and particle-based pull distributions are "nearly identical" (p. 3).
- Higher moments: g separates quark from gluon jets but is strongly correlated with m/p_T. Eccentricity shows no significant quark/gluon difference. Pull angle is judged "the most useful moment-type observable" (p. 4).
- Jet algorithm: anti-kT beats kT, SISCone and C/A for pull. Computing pull in a larger R = 1.2 after finding R = 0.7 jets gave no obvious gain (p. 4).
- tt̄: simulated pull angles of the hadronic W daughters are said to resemble the H→bb̄ signal in Fig. 5. No figure is shown for this (p. 4).
- Colour connections are described in the large-N_C (dipole/string) picture. Subleading-colour effects are said to enter MC "through color-reconnections, which amount to a 1/N_C² ∼ 10% effect" (p. 1).

## Assessment
- The foundational, highly cited (~220 [unverified]) proposal for a jet-local colour-flow observable. Most later pull-type work starts from Eq. 1, including Hook:2011cq dipolarity, the D0 2011 W-colour measurement and ATLAS:2018olo.
- The evidence is entirely MC-based, leading-colour, and qualitative. There is no ROC, no significance gain, no detector simulation, and no pileup study. The robustness claim (Fig. 4) covers one fixed phase-space point and only parton showers of that era. Later measurements (ATLAS:2018olo) found that MC generally overpredicts the strength of colour flow and that generators disagree with each other. [ATLAS:2018olo finding unverified against that paper here.] So the "not particularly sensitive to the MC" statement should not be generalised.
- The background colour connection is imposed by hand in Figs. 2–4, so a real background is a mixture of colour flows (the ~10% other-flow fraction, p. 3, is quoted without a derivation).
- The 1/N_C² ≈ 10% statement conflates subleading-colour matrix-element and shower effects with colour-reconnection models. It is a heuristic, not a computed uncertainty.
- Pull uses a |r_i| weighting, so it is dominated by wide-angle soft radiation and therefore sensitive to UE and pileup. The paper does not examine this, although UE is included in Fig. 5. Later theory work qualified the "IR safe" claim (p. 3), which applies to the vector, not to θ_t: the pull angle is Sudakov-safe but not IRC-safe [unverified; the dedicated paper is probably Larkoski, Marzani, Wu 2019, arXiv:1903.02275, not the 2015 Larkoski–Marzani–Thaler paper].
- RQ4: the proposals were the hadronic W in tt̄ as a colour-singlet standard candle (later realised by D0 and ATLAS) and use in H→bb̄ (later used by ATLAS/CMS VH analyses and the 2015 ATLAS pull measurement).

## Leads
- Black, Gallicchio, Huth, Kagan, Schwartz, Tweedie 2010, arXiv:1010.3698, "Multivariate discrimination and the Higgs + W/Z search". Pull used in a full VH(bb̄) analysis, giving a quantitative gain the PRL lacks.
- Gallicchio & Schwartz 2011, "Quark and gluon tagging at the LHC" / "Pure samples of quark and gluon jets". Related superstructure work.
- D0 Collaboration 2011, PRD 83, 092002 (arXiv:1101.0648), "Measurement of color flow in tt̄ events". First pull measurement (RQ3).
- ATLAS 2015, Phys. Lett. B 750 (2015) 475, colour flow with jet pull in tt̄ at 8 TeV. Predecessor of ATLAS:2018olo.
- Larkoski, Marzani, Thaler 2015, "Sudakov safety in perturbative QCD". General Sudakov-safety framework. Whether it treats the pull angle explicitly is [unverified]; see also Larkoski, Marzani, Wu 2019 (arXiv:1903.02275), "Safe use of jet pull" [unverified].
- Skands & Weinzierl 2009, PRD 79 074021 (ref. [8]). Dipole-shower colour coherence, cited for the radiation picture.
- JADE 1983, Z. Phys. C 21, 37, and D0 1999, PLB 464 145. Earlier topology-specific colour-coherence measurements cited as precedents.

## Verification
Checked 2026-10-30 by an independent reader: 34 claims checked, 3 corrected, 3 unverifiable.
- Fig. 4 read-off: the signal peak is ≈2.5× its minimum (≈2.2–2.4 vs ≈0.8–1.0), not ≈2×.
- Fig. 3: θ_t ≈ 0.7 is the text's stated direction of the other b, not a measured cluster position. Reworded.
- Takeaway on missing numbers: the anchor is Fig. 5 on p. 3. Added the paper's only number, the "few percent improvement" remark on p. 4.
- Marked [unverified]: the citation count, the ATLAS:2018olo MC-overprediction statement, and the attribution of the pull-angle Sudakov-safety result to Larkoski–Marzani–Thaler 2015.
