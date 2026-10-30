# String Formation Beyond Leading Colour
- **ID / links:** Christiansen:2015yqa · INSPIRE 1367312 · arXiv 1505.01681 (v2, Aug 2021) · DOI 10.1007/JHEP08(2015)003
- **Authors / collab, year, journal:** J.R. Christiansen, P.Z. Skands (Lund / CERN / Monash), 2015, JHEP 08 (2015) 003
- **Type:** MC/model
- **Relevance:** 3 · RQs: 1, 2, 3, 4
- **Full text source:** arxiv

## Takeaways
- Defines the Pythia 8 "QCD-based" CR model (ColourReconnection:mode = 1). It has two stages:
  - **Allowed connections:** a simplified SU(3) colour algebra (random colour index 1–9 per dipole) decides which string connections beyond leading colour (LC) are allowed. This includes junction (ε_ijk) connections.
  - **Chosen connection:** among the allowed ones, only reconnections that lower the string length λ are accepted, so the algorithm reaches a *local* (not global) λ minimum (§2.3.2, Eqs. 2.13–2.14, pp. 17–20).
- Central argument: subleading-colour connections are suppressed by about 1/N_C² ≈ 10% for each pair of uncorrelated partons. With many MPI it becomes unlikely that *no* such connection exists. Already for two random gluons, the LC multiplet (27) has probability only 27/64 < 50% (Eq. 2.2).
- Junction formation provides a new baryon source. The model is the first Pythia setup to describe both LEP data and CMS Λ/K⁰_S in pp (Fig. 12c, p. 28), while also fitting ⟨p⊥⟩(n_ch) (Fig. 12a). It predicts strongly enhanced heavy (c, b) and double-heavy baryons (Tab. 1). However, it fails to describe the identified-particle p⊥ spectra, ⟨p⊥⟩ vs hadron mass, and rapidity-gap survival (Figs. 20–22).
- Includes a causality/time-dilation requirement: only strings that can resolve each other between formation (about 1/m) and hadronisation (about 1 fm) may reconnect (Eq. 2.16).
- Top mass: shifts on the W-calibrated m_t stay below 200 MeV (largest +0.17 ± 0.10 GeV) for all models studied here, including an unphysical "max CR". The authors extend this to "below 300 MeV" for any λ-minimising CR, counting the models of Argyropoulos–Sjöstrand 2014 too. The raw m_t shifts by about 0.65 GeV, mostly through UE activity (Tab. 2, pp. 39–41).

## Setup
- Pythia 8 (8.2xx), starting from the Monash 2013 tune.
- **LC starting point.** CR is applied after the parton shower (and the new beam-remnant colour treatment) and before string fragmentation. The LC dipoles from the shower are the starting configuration (p. 15).
- **Colour algebra.**
  - Multiplet weights in SU(3) for two uncorrelated partons: 8⊗8, 3⊗8, 3⊗3̄, 3⊗3 (Eqs. 2.1–2.5). Three triplets form a singlet with probability 1/27 (Eq. 2.6).
  - The simplified model: each dipole gets a random index 1–9. Equal indices allow a dipole-type reconnection (P_I = 1/9). Indices equal modulo 3 but different allow junction-type reconnections (P_II = 2/9). Three different indices equal modulo 3 allow a type-III baryonic junction (P_III = 2/81 vs 1/27 in QCD) (p. 17; Fig. 3 compares weights with full SU(3)).
  - Reconnection types I–IV: dipole swap, connected J–J̄, disconnected J+J̄ from three dipoles, and "zipper" (Fig. 7).
- **String length.**
  - The positive-definite λ′ = ln(1+√2E₁/m₀)+ln(1+√2E₂/m₀) (Eqs. 2.13–2.14) replaces Eqs. 2.10–2.12, which can go negative for small masses.
  - Junction λ is scaled through m_0j = C_j·m₀, with C_j = "junctionCorrection" (Eq. 2.15).
  - Dipoles below m₀ are merged into pseudoparticles (Fig. 8).
  - The algorithm is deterministic, local and greedy: only λ-decreasing moves, ordinary reconnections first, then junctions, then iterate (pp. 19–20).
- **Beam remnant.**
  - The remnant colour multiplet is chosen with a saturation suppression p(M) = exp(−M/k_saturation) (Eq. 2.7).
  - The number of gluons added to the remnant is set by Eq. 2.9, which includes junctions.
  - A singlet remnant is forbidden to avoid double counting with diffraction (p. 14).
- **Junction systems.** Multi-junction systems are split into single-junction pieces for hadronisation (Figs. 9–10).
- **Space-time.** Strings are in causal contact if γ c/(m_string r_had) < C_time, with r_had = 1 fm (Eq. 2.16). Modes 0 (none), 2 (strict) and 3 (loose) are implemented (p. 24).
- **Resonance decays.** Switch "earlyResDec": CR before or after resonance decays, which gives the extremes of CR involvement for t/W/Z decay products (p. 23).
- **Data used.**
  - L3 Z-pole multiplicity and x_p (Fig. 11).
  - CMS 7 TeV ⟨p⊥⟩(n), dn/dη, Λ/K⁰_S(y), multiplicity distributions (Figs. 12–13).
  - TOTEM forward dN/dη (Fig. 14).
  - CMS Λ p⊥ and Λ/K⁰_S(p⊥) (Fig. 20).
  - STAR 200 GeV ⟨p⊥⟩ vs mass (Fig. 21).
  - ATLAS rapidity gaps (Fig. 22).
- **Top-mass toy analysis.** Semi-leptonic tt̄ with a skewed-Gaussian 3-jet mass fit, following Argyropoulos–Sjöstrand 2014 (§4).

## Results
- **Motivation.** ⟨p⊥⟩(n_ch) rises in CDF 630/1960 GeV and ATLAS 7 TeV data. Without CR (Pythia 8.175, tune 4C, old CR switched off) it is nearly flat, ≈ 20–25% too low at high n_ch (read from Fig. 1).
- **e⁺e⁻ argument.** Effects should be small in e⁺e⁻. Coherence and angular ordering make LC dipoles already near-minimal in λ. The two W's are separated by about 1/Γ_W (pp. 2–3).
- **pp argument.**
  - Effects should be large in pp: MPI systems sit within the proton radius, and nothing aligns inter-MPI or remnant partons (p. 3).
  - Colour ambiguities are distinguished from "true" dynamical reconnections (momentum exchange). The model handles only the former, though the tune may absorb both (p. 5, p. 42).
- **Tuning (mode 2 standard).**
  - e⁺e⁻: a_Lund = 0.38 (was 0.68), b_Lund = 0.64 (was 0.98) in the text (p. 25), but Appendix A (p. 43) lists aLund = 0.36, bLund = 0.56 for all three modes; the paper is internally inconsistent here. probQQtoQ = 0.078, probStoUD = 0.2. The junction-diquark spin-1 suppression probQQ1toQQ0join is simply fixed to the string-break value (0.027 in text, 0.0275 in App. A) for lack of data (p. 26). LEP multiplicity and x_p are described about as well as Monash (Fig. 11, χ²/N_bins 0.1 vs 0.4 and 0.7 vs 0.8).
  - pp: junctionCorrection = 1.2, timeDilationPar = 0.18, pT0Ref = 2.15 (was 2.28) (p. 28). Appendix A gives the full list for modes 0/2/3 (p. 43): mode 2 has m₀ = 0.3 GeV; mode 0 has m₀ = 2.9 GeV, C_j = 1.43, pT0Ref = 2.12; mode 3 has C_j = 1.15, timeDilationPar = 0.073, pT0Ref = 2.05.
  - C_j > 1 is needed to compensate the underestimated baryon (type-III) rate (p. 17, p. 28).
- **pp observables.**
  - ⟨p⊥⟩(n), dn/dη and Λ/K⁰_S(y) agree with CMS within ≈ 5–10%. Monash underpredicts Λ/K⁰_S by ≈ 30–35% (read from Fig. 12).
  - Tails of the multiplicity distributions differ between modes and deviate from the data by 40% or more; some ratios leave the 0.6–1.4 panel (read from Fig. 13). The authors say the tails can be tuned away via the proton matter profile, which was kept fixed (p. 28).
- **Beam-remnant saturation.** No saturation vs maximal saturation differ by about 10% in TOTEM forward dN/dη with no shape change. saturation = 5 is chosen (Fig. 14a). Forward baryons may trace remnant junctions (Fig. 14b, p. 29).
- **LEP three-jet test.** The rapidity-gap / zero-charge gluon-jet observable (Friberg–Gustafson–Häkkinen; OPAL/L3/ALEPH) shows a negligible difference between the new CR and no CR. The model therefore should not be excluded by LEP. An unphysical "max CR" (1/N_C² → 1) would be excluded (Fig. 16, p. 31). The model ignores g→gg octet history, so it may overestimate CR in three-jet events (p. 30).
- **Baryon multiplicity scaling.** Baryon multiplicity rises faster than linearly with hadron multiplicity in the new model, driven by junction baryons. Diquark baryons scale linearly (Fig. 17).
- **String masses.** The new model gives many low-mass strings, whereas the old model's mass distribution is flat. Low-mass junction systems strongly suppress diquark production: a 10 GeV junction is about 5× less likely than a 10 GeV dipole string to make an extra diquark pair (Fig. 18).
- **Identified yields at 7 TeV (Tab. 1).**
  - Most light and strange baryons rise 20–50% compared with the old CR model (p, Λ, Σ). Ξ⁻ rises about 60% and Ω⁻ about ×4. Λ_c⁺ and Λ_b⁰ rise only about ×2.
  - Σ_c⁰, Σ_c⁺⁺ and Σ_b rise by factors of about 20–30, because junctions avoid the spin-1 dd/uu diquark penalty.
  - Double-heavy (ccq) baryons go from about 1e-7 to 2e-4 per event (pp. 33–35).
- **Failures.**
  - Λ p⊥ spectrum: overshoots at very low p⊥, ≈ 30% low at 2–3 GeV, and too high above ≈ 5 GeV (read from Fig. 20a; p. 37). Λ/K⁰_S(p⊥) is good below ≈ 3 GeV but too high at high p⊥ (read from Fig. 20b).
  - ⟨p⊥⟩ vs hadron mass (STAR 200 GeV): no improvement over the old model, with heavier hadrons ≈ 15–30% low and π slightly high (read from Fig. 21). The authors call this "disappointing" and point to flow, rescattering or ropes as possible additional physics (p. 37–38).
  - Rapidity-gap cross section at low p⊥ cut (200 MeV): overshot by ≈ 50–60% at Δη^F ≈ 4–5.5, because CR creates singlet subsystems; the old CR model also overshoots, by ≈ 35% (read from Fig. 22a). The effect vanishes for the 800 MeV cut. Diffractive parameters would need retuning (p. 38).
- **Top mass (Tab. 2).**
  - Raw m_t shifts relative to no CR: default −0.67, default ERD −0.36, new −0.66, new ERD −0.45, max CR ERD −0.22, max CR (tuned) +0.66 GeV, ±0.09 each. Max CR (tuned) is more than 1 GeV above the tuned no-CR value, though W calibration removes most of it (p. 40).
  - After rescaling by 80.385/m̂_W, all shifts are ≤ 0.17 GeV in magnitude (largest: default +0.17, new +0.14).
  - The raw shift comes mainly from UE activity: the retuned "no CR (tuned)" gives −0.63 GeV raw but −0.06 GeV rescaled.
  - ERD (CR with top decay products) narrows jets and raises m_t (p. 40).
  - Claim: whenever CR is λ-minimising, shifts stay below 300 MeV (including the models of Argyropoulos–Sjöstrand 2014), because shower coherence protects jet structure and W-mass calibration cancels shifts (pp. 40–41).
- **Proposed tests (RQ4).**
  - Baryon/meson ratio vs multiplicity; the scaling shape distinguishes junction from diquark baryons (Fig. 17).
  - Σ_c⁰/Σ_c⁺⁺, Σ_b and Λ_b yields, Ω⁻, and Σ_c*/Σ_c as a probe of junction diquark spin (pp. 33–35).
  - Double-heavy baryons (p. 35).
  - Forward baryons as beam-remnant tracers (p. 29).
  - ⟨p⊥⟩ vs mass at LHC energies in high- and low-multiplicity and UE samples (p. 38).
  - Rapidity-gap survival (Fig. 22).
  - Top-specific in-situ CR observables (p. 41).
  - A future dedicated e⁺e⁻ (WW) study is announced (p. 30).

## Assessment
- **Importance.** This is the most influential modern CR model, now the standard "QCD CR" variation in LHC top-mass systematics [unverified: not in this paper], with 516 citations [unverified]. Its strength is a principled, if simplified, link between SU(3) multiplet weights and string topology, plus a unified account of strangeness/baryon ratios in ee and pp. Compared with the old Pythia 8 CR, it makes baryon production in pp a genuine colour-flow observable. This bears directly on RQ1 (collectivity in small systems), as an alternative to ropes and hydro.
- **Caveats.**
  - The index model treats colour-unconnected partons as fully uncorrelated, and it ignores shower history (e.g. g→gg octets). The authors admit this may overestimate CR in jets.
  - Minimisation is greedy and local, not a full area-law probability.
  - The type-III rate is 2/3 of the QCD value, and is compensated by a tuned C_j = 1.2.
  - The causality criterion (Eq. 2.16) is not Lorentz-invariant, and the variants (modes 0/2/3) differ noticeably in multiplicity tails.
  - Λ/K⁰_S is tuned (C_j), so the y-integrated agreement is not a prediction. The p⊥ dependence and heavy-baryon rates are predictions, but the heavy-baryon rates (and especially Σ_c*/Σ_c) depend on the junction-diquark spin suppression, which was fixed by hand to the string-break value without data (pp. 26, 35).
- **Later developments [unverified].** The heavy-baryon predictions have since been tested by ALICE Λ_c⁺/D⁰ and Σ_c measurements. In later literature QCD-CR (mode 2) is the main Pythia model describing the Λ_c enhancement in pp. That evidence lies outside this paper and should be confirmed from those papers.
- **Top-mass result.** The "≤ 300 MeV for λ-minimising models" result rests on one toy calibration (W-mass rescaling) with about 0.1 GeV statistical precision. It explicitly excludes non-λ-minimising "devil's advocate" models. The authors warn that the unresolved p⊥ spectra may signal further dynamical non-perturbative uncertainties (p. 41).
- **LEP.** The "consistent with LEP" claim rests only on no-CR vs new-CR MC differences in the three-jet gap observable, not a direct data comparison. LEP2 WW was not studied here.
- **Physics picture.** The model frames CR as *colour-space ambiguity* resolved by potential-energy minimisation, not dynamical reconnection. This distinction is useful for the synthesis. Ropes (Bierlich et al.) and EPOS hydro are the named competitors for the same data.

## Leads
- Sjöstrand & Skands, Nucl. Phys. B659 (2003) 243 (hep-ph/0212264): junction string topologies and λ for junctions, the basis of the junction hadronisation used here.
- Sjöstrand & Khoze, Z. Phys. C62 (1994) 281 and Khoze & Sjöstrand PLB 328 (1994) 466: SK models; CR in top events.
- Friberg, Gustafson, Häkkinen, Nucl. Phys. B490 (1997) 289: colour connections in e⁺e⁻, the gluon-jet rapidity-gap observable.
- OPAL, EPJ C35 (2004) 293; L3, PLB 581 (2004) 19; ALEPH, EPJ C48 (2006) 685: LEP three-jet CR tests (seed topic).
- Bierlich, Gustafson, Lönnblad, Tarasov, JHEP 1503 (2015) 148: rope hadronisation, the competing explanation for strangeness/baryons.
- Ortiz Velasquez et al., PRL 111 (2013) 042001: CR mimicking flow.
- Gieseke, Röhr, Siodmok, EPJ C72 (2012) 2225: Herwig++ CR.
- CMS, JHEP 1105 (2011) 064 (Λ/K⁰_S) and STAR, PRC 75 (2007) 064901: identified-particle data that the model partly fails.
- Forward citations: ALICE Λ_c/D⁰ and Σ_c in pp; Christiansen–Sjöstrand ee/WW follow-up (2015); Bierlich–Christiansen ropes + CR.

## Verification
Checked 2026-10-30 by an independent reader: 74 claims checked, 13 corrected, 3 unverifiable.
- Takeaway: λ selection is a local greedy minimisation (only λ-lowering moves), not "the smallest λ".
- Takeaway: "≤ 200 MeV" applies to the models studied here; the "< 300 MeV for all λ-minimising models" claim includes the Argyropoulos–Sjöstrand models.
- Lund a/b: the text (0.38/0.64) and Appendix A (0.36/0.56) disagree; flagged. Added mode-2 m₀ = 0.3 GeV and the mode-0/3 values.
- Table 2: added default ERD (−0.36) and max CR (tuned) (+0.66 raw, > 1 GeV above tuned no CR).
- Table 1: the 20–50% rise does not hold for Ξ⁻ (+60%) or Ω⁻ (×4); Λ_c and Λ_b rise only ×2.
- Fig. 20a: Λ overshoots (it is not too soft) at very low p⊥. Fig. 22a: overshoot ≈ 50–60%, and the old CR also overshoots. Fig. 13: tail deviations exceed 40%.
- Heavy-baryon "genuine predictions" qualified: they depend on the hand-fixed probQQ1toQQ0join.
- Citation count, top-systematics status and later ALICE developments marked [unverified].
