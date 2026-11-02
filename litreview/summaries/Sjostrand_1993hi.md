# On colour rearrangement in hadronic W⁺W⁻ events
- **ID / links:** Sjostrand:1993hi · INSPIRE 360188 · arXiv hep-ph/9310242 · DOI 10.1007/BF01560244
- **Authors / collab, year, journal:** T. Sjöstrand, V.A. Khoze, 1994, Z. Phys. C 62 (1994) 281–309
- **Type:** theory / MC model (perturbative analysis + non-perturbative string-reconnection models)
- **Relevance:** 3 · RQs: 1b, 2, 4 (context for 3)
- **Full text source:** zotero (journal scan, 29 pp; all pages read, figures legible). Page numbers below are journal pages 281–309.

## Takeaways
- **Perturbative CR in W⁺W⁻ is negligible.** It needs at least two gluons, so it is O(α_s²). The interference is colour-suppressed by 1/(N_c²−1) = 1/8 (Eq. 21). The finite W width further restricts it to gluons with ω ≲ Γ_W (Eqs. 24–27). The authors estimate ΔN^recon/N ≲ O(10⁻²) in particle flow (Eq. 41), σ^recon/σ ≪ 10⁻³ (Eq. 42 and text below it) and an m_W effect of ≲ 5 MeV (p. 306). The perturbative pattern also contains **negative-sign "dipoles"** (q₁q₃, q̄₂q̄₄; Eq. 33), which no probabilistic string/MC picture has (pp. 290–291).
- **Non-perturbative CR is likely.** Strings from the two W decays overlap in space-time: the decay vertices are only ~0.1 fm apart, while strings have r ~ 0.5–0.7 fm and τ_frag ≈ 1.5 fm (pp. 292–296; Fig. 10b). The paper defines the string-overlap models that became the LEP2 standard:
  - **Scenario I** ("elongated bags", type-I superconductor analogy): P_recon = 1 − exp(−k_I f_r³ f_t I_Σ^{+−}), with I the Gaussian flux-tube overlap integral and k_I a free parameter (Eq. 67).
  - **Scenario II** ("vortex lines", type-II superconductor analogy): reconnection with unit probability at the first crossing of two string cores that have not yet fragmented. It has no free parameter beyond τ_frag (Eqs. 68–70).
  - **Scenario II′:** as II, but reconnection is allowed only if the string length decreases, m₁₄m₂₃ < m₁₂m₃₄ (p. 299).
  - Plus a didactic scenario 0 (spherical sources; Eq. 60).
- **Reconnection probability ≈ 30 % at LEP2.** k_I = 0.6 is chosen so that I and II agree at 170 GeV (p. 300), and the authors call the result "a realistic scenario with ~30 % reconnection" (p. 301). P_recon varies by at most a factor 2 over 150–200 GeV, so the "threshold region" is very extended (Fig. 15a; p. 300). In scenario II it depends strongly on the shower cut-off m₀ and on jet multiplicity (Figs. 15b, 16).
- **m_W shifts are model- and method-dependent.** At 170 GeV: scenario I gives +14 to −10 MeV (small, sign uncertain); scenario II gives −21 to −34 MeV; II′ gives −17 to −31 MeV. The unphysical extremes are larger: "intermediate" +62 to +136 MeV, "instantaneous" +275 to +576 MeV (Tab. 1). The authors' **best estimate is ~40 MeV total CR uncertainty**: 30 MeV non-perturbative + 5 MeV perturbative + 5 MeV for the perturbative/non-perturbative interplay (pp. 306–308).
- **Observability.** The authors find inclusive observables nearly blind: ⟨n_ch⟩ changes by < 1 % and the shift sits at |p| < 1 GeV (Fig. 17a). Event shapes, dn/dy, n_jet and the azimuthal flow around jets show no usable signal for scenarios I/II (Fig. 17b; p. 302). They had no good proposal for a dedicated observable (p. 302). They suggest these handles:
  - comparing qqqq with lνqq;
  - a high-statistics Z⁰Z⁰ run, using the known m_Z to calibrate shifts;
  - Bose–Einstein correlations as a function of topology;
  - self-screening of m_W reconstruction methods against CR-sensitive regions (pp. 307–308).

## Setup
- **Process.** e⁺e⁻ → W⁺W⁻ → q₁q̄₂q₃q̄₄ near and above threshold (mostly √s = 170 GeV; energy scans 150–200 GeV). It is generated with PYTHIA 5.6 (Breit–Wigner W's, correlated decay angles, no ISR), the JETSET 7.3 shower (m₀ ≈ 1 GeV) and Lund string fragmentation (pp. 283–284).
- **Sect. 2 toy scenarios.** Deliberately extreme and later rejected by the authors (p. 282–283):
  1. no reconnection;
  2. the GPZ-style "instantaneous" reconnection into q₁q̄₄ + q₃q̄₂ singlets before the shower, i.e. showers with ~20 GeV rather than 80 GeV scale;
  3. "intermediate": original showers, then reconnection before fragmentation.
  - First tested for two W's at rest with a 30° opening angle between u and ū (Fig. 1–2), then for realistic 170 GeV kinematics (Fig. 3).
- **Sect. 3 perturbative analysis.**
  - Soft-gluon currents for single emission (Eqs. 7–15): at O(α_s) there is no decay–decay interference in colour (Fig. 5).
  - Double emission (Eqs. 16–22): the interference term carries 1/(N_c²−1) and the "profile function" χ₁₂ (Eq. 20). χ₁₂ → 0 for Γ_W → 0 and → 1 for Γ_W → ∞. Near threshold χ₁₂ = Γ_W²/(Γ_W² + (ω₁−ω₂)²) (Eq. 27).
  - At high energy the effective cut is k_max^recon ~ Γ_W m_W/E_W (Eq. 28).
  - Inclusive particle flow is the antenna pattern of Eq. 33: 2[(12)+(34)] N′_q(m_W/2) + R[(14)+(23)−(13)−(24)] N′_q(k_max^recon), with R ≲ O(α_s/N_c²) (Eq. 37).
  - QED analogue γγ → Z⁰Z⁰ → e⁺e⁻μ⁺μ⁻ (Eqs. 39–40).
- **Sect. 4 non-perturbative space-time picture.**
  - Lund string with κ ≈ 1 GeV/fm. Fragmentation proper-time distribution P(τ)dτ = exp(−τ²/τ_frag²) 2τdτ/τ_frag², with τ_frag ≈ 1.5 fm, from a = 0 and b ≈ 0.4 GeV⁻² (Eqs. 44–46).
  - The W lifetime is Breit–Wigner-weighted (Eq. 47–48). Average W decay separations at LEP2 are ~0.08 fm in time and 0.05 fm in space (Fig. 10b; p. 294).
  - Parton lifetimes: partons with m ≳ 10 GeV decay within ~0.1 fm, so the jet structure is fixed before the W-decay separation matters (pp. 294–295, Eq. 49–53).
  - String pieces move as in Eq. 50, and the boosted colour field is used for the overlap integral (Eqs. 55–58, 61–62).
  - Scenario I uses a transverse Gaussian with r_had ≈ 0.5 fm (p. 296). Its overlap integral is computed by MC with 100 sampled space-time points per event (Eqs. 65–66, f_r = 2.5, f_t = 2), with at most one reconnection per event (p. 298).
- **Sect. 5 predictions.**
  - Reconnection probability vs √s, m₀, n_jet and n_ch (Figs. 15–16).
  - Event properties (Fig. 17).
  - Reconnection position d_rec and string-length change Δλ (Eqs. 71–72; Fig. 18).
  - W-mass systematics with four jet-pairing methods (p. 304–305):
    - Common reconstruction: LUCLUS with d_join = 8 GeV, exactly 4 jets, E_jet ≥ 20 GeV, all inter-jet angles > 0.5 rad; ~60 % of events survive.
    - Methods: 1 = MC-truth parton matching; 2 = minimise |m̄_W − 80|; 3 = minimise |m_W⁽¹⁾−80| + |m_W⁽²⁾−80|; 4 = maximise the opening angles.
    - Perfect detector assumed. 160k events per scenario, ~100k after cuts (p. 306).

## Results
**Maximal (toy) effects, Sect. 2**
- W's at rest, 30° opening: ⟨n_ch⟩ = 21.8 (instantaneous), 40.0 (no reconnection) and 37.8 (intermediate) (p. 283). The instantaneous case has a deep central rapidity dip and suppressed flow at 90° (Fig. 2b–d; p. 284). The authors take the central-region deficit as a sign of how strongly 80 GeV-scale radiation broadens jets (p. 284).
- At 170 GeV with realistic kinematics: ⟨n_ch⟩ = 36.6 / 36.2 / 33.7 (no / intermediate / instantaneous) (p. 285; Fig. 3a).
  - Δm̄_W (reconstructed − generated, in a ±10 GeV window) = −0.28 ± 1.57, −0.14 ± 1.60 and +0.30 ± 1.55 GeV (mean ± spread). That is a shift of > 100 MeV (intermediate) and ~500 MeV (instantaneous), against an aimed-for statistical error of ~50 MeV (p. 285; Fig. 3d).
  - The effect shrinks far above threshold, where reconnection *raises* system masses (p. 285).

**Perturbative suppression, Sect. 3**
- Colour factor of the decay–decay interference: Tr(TᵃTᵇ)Tr(TᵃTᵇ)/[Tr(TᵃTᵃ)Tr(TᵇTᵇ)] = 1/(N_c²−1) (Eq. 21).
- Only gluons with ω ≲ Γ_W contribute (Eq. 27; p. 289), with Γ_W ≈ 2.1 GeV (p. 294). The reconnection-sensitive multiplicity is N_q(k_max^recon)/N_q(m_W/2) ~ O(10⁻¹) (Eq. 38).
- The authors conclude: ΔN^recon/N^no-recon ≲ O(10⁻²) (Eq. 41); Δσ^recon/σ ≲ (C_Fα_s)²/N_c² · Γ_W/m_W (Eq. 42), numerically ≪ 10⁻³ (p. 291).
- The (13) and (24) dipoles enter with negative sign and *increase* string-like anisotropies of the (14), (23) dipoles (p. 291). The effect is visible only inclusively, because the reconnection terms are not positive-definite (p. 291).

**Reconnection probabilities, Sects. 4–5**
- **Scenario 0.**
  - Overlap I(β)/I(0) falls by a factor 3–4 from threshold to 200 GeV (Fig. 12). P_recon = ½(1 − exp(−k₀ I(β)/I(0))) saturates at ½ (Eq. 60).
  - For k₀ = 0.2–5, P_recon at 150 GeV ranges from ≈0.1 to ≈0.5 and falls slowly with √s (Fig. 13; read off the plot, ≈).
- **Scenarios I and II** (k_I = 0.6 tuned to match II at 170 GeV; p. 300):
  - P_recon ≈ 0.27–0.40 throughout 150–200 GeV, peaking near ~163 GeV and decreasing slowly above. The variation is at most a factor 2 over 150–200 GeV (Fig. 15a, ≈; p. 300).
  - Scenario II falls faster with √s than I, because II needs head-on core crossings (p. 300).
- **Shower cut-off m₀** (Fig. 15b; pp. 300–301):
  - Scenario I is nearly flat. Scenario II falls towards 0 at large m₀, since with no shower the qq̄ strings recede and cannot cross.
  - The authors take the realistic m₀ range (1 → 2–3 GeV) to imply a factor ≤ 2 uncertainty in P_recon for II.
- **Event activity** (Fig. 16; p. 301):
  - P_recon roughly doubles from few to many jets (LUCLUS d_join = 2.5 GeV) and rises with n_ch. II is more sensitive than I.
  - Thrust and T₄ are insensitive to P_recon, because they reflect the 4-parton topology.
- About 20 % of string crossings at 170 GeV would *increase* string length (topology of Fig. 14c; p. 299).
- Reconnection position: ⟨d_rec⟩ ≈ 0.18, so reconnections typically occur near the middle of the strings. ⟨d_rec⟩ ≈ 0.06 even in the "intermediate" scenario, because shower asymmetries move it off zero (Fig. 18a; p. 303).
- String-length change ⟨Δλ⟩ (with ⟨λ⟩ ≈ 20) is roughly flat in d_rec for I. II shows a trend to smaller |Δλ| at larger d_rec; II′ behaves like I (Fig. 18b; pp. 303–304).

**Event properties, Sect. 5.2**
- ⟨n_ch⟩ = 36.63 (no CR), 36.31 (I), 36.45 (II), with a statistical error of 0.04 from 40k events. The difference sits essentially entirely at |p| < 1 GeV. The authors judge it below LEP2 observability given statistics, backgrounds, QED radiation and the need to extrapolate from Z⁰ (p. 302; Fig. 17a).
- Azimuthal particle density around jet axes (0.3 < p_⊥ < 0.8 GeV, nearest-jet angle > 1 rad) shows no detectable effect for I/II. The unphysical instantaneous case changes it visibly (Fig. 17b; p. 302).
- **Large-x excess** (x > 1/2 forbidden for independent W's at rest): not seen in the scenarios, and swamped by γ*/Z⁰ → qq̄g (pp. 302–303).
- **J/ψ from cs̄c̄s reconnection:** 1 event in 50,000 scenario-II events, against a ~10× larger shower background (p. 303).

**W mass, Sect. 5.3 (Tab. 1, 170 GeV)**
- No-CR offsets ⟨Δm̄_W⟩ are −276, +158, −355 and +471 MeV, with spreads σ ≈ 1.6–2.2 GeV, for methods 1–4 (Tab. 1). Method 2 gives the smallest offset and method 1 the narrowest distribution (p. 305). 2–4 % of events lie in far wings with |Δm̄_W| > 10 GeV (p. 305).
- ⟨δm̄_W⟩ = CR − no-CR (MeV); the statistical error is ≈ 10 MeV per entry (Tab. 1 caption):

| Method | I | II | II (m₀=2) | II′ | Intermediate | Instantaneous |
|---|---|---|---|---|---|---|
| 1 | +14 | −21 | −23 | −17 | +136 | +576 |
| 2 | −10 | −34 | −33 | −28 | +62 | +286 |
| 3 | +14 | −34 | −31 | −27 | +88 | +496 |
| 4 | +1 | −27 | −28 | −31 | +74 | +275 |

- **Interpretation.** The authors argue that jet masses compensate the inward shift of jet directions from string boosts (Eqs. 73–74). A reconnection that randomises the colour partner leaves θ₁₂ unchanged on average, so m_W is overestimated (intermediate/instantaneous). In I/II reconnections occur away from the event centre, and the sign may differ. The I vs II difference is tentatively attributed to grazing (I) vs head-on (II) overlaps (p. 306).
- **Error budget.** "Non-perturbative effects are bounded by 30 MeV, say". This is consistent with the intermediate shifts scaled by P_recon ≈ 1/3. Adding ≤ 5 MeV perturbative and 5 MeV interplay linearly gives "roughly like 40 MeV" (pp. 306–308).
  - If P_recon were halved, the total would still be 25 MeV (p. 308).
  - CR "may well be the largest individual source of systematic error" in the qqqq channel. The value depends on the reconstruction method (p. 307).

**Proposed tests / outlook (RQ4)** (pp. 307–308)
- Check every experimental m_W method against the scenarios. Look for CR "traces" so that data can self-screen and mass corrections can be applied as a function of observed deviations.
- Use the mixed lνqq channel, which is free of reconnection ambiguity.
- A high-statistics run above the Z⁰Z⁰ threshold: m_Z is known, so any systematic shift is unambiguous and could amount to a direct observation of CR. Z⁰ data predict Z⁰Z⁰ properties such as the n_ch distribution.
- Bose–Einstein correlations: if the W strings stay separate sources, BE effects should be weaker in W⁺W⁻ than in Z⁰ and vary with topology in step with P_recon (p. 308; UA1 precedent [27]).
- Wanted: an observable sensitive at the per-cent level where the no-CR prediction is well under control (p. 308).
- The ideas extend to tt̄ and to colour-singlet resonances at hadron colliders. Further listed effects (p. 308–309):
  - 1-string vs 3-string tt̄ scenarios;
  - the b-quark "attraction effect";
  - tb̄/t̄b/bb̄ interactions in the forward–backward asymmetry;
  - the azimuthal asymmetry of b-jets in tt̄.

## Assessment
- **Scope.** This is the foundational paper for the SK-I / SK-II / SK-II′ models that all four LEP experiments and the LEP combination used (ALEPH_2013dgf.md). Its qualitative conclusion holds up against the final LEP2 outcome:
  - CR is small in inclusive observables but a leading systematic on m_W(qqqq).
  - The paper's ~40 MeV estimate is close to the final 35 MeV CR systematic on m_W(qqqq) (Tab. 7.3 of ALEPH_2013dgf). The match is partly coincidental: LEP obtained 35 MeV only *after* soft-particle de-weighting/cone reconstruction, which the paper did not consider, and with k_I at the 68 % CL upper limit (2.10). With standard reconstruction LEP found shifts up to ~100 MeV (ALEPH_2013dgf, p. 137).
- **Reconnection fraction vs LEP.** The paper's reference k_I = 0.6 gives P_recon ≈ 30 % at 170 GeV. LEP's combined fit is k_I = 1.26 (+0.84 −0.64), i.e. ~51 % at 189 GeV. DELPHI's default κ = 0.66 (DELPHI_2006tie.md) is close to, but not identical with, this paper's k_I = 0.6 (p. 300) [unverified: origin of the 0.66 value is not in this paper]. LEP data prefer roughly twice the paper's reference strength. This is still well inside the ~factor-2 model uncertainty the authors themselves allow. Caveat: k_I depends on implementation details (f_r, f_t, the choice of Ω_trial; Eqs. 66–67), so absolute k_I values transfer only within the same PYTHIA implementation.
- **SK-II/II′ were never directly constrained by LEP.** The combination is SK-I specific (ALEPH_2013dgf). SK-II has no free strength parameter. Its m_W shift here is consistently negative, while SK-I's is small and of uncertain sign (Tab. 1; p. 306), so the LEP SK-I-based systematic does not automatically cover it. Still, the magnitudes (≤ 34 MeV) are below the assigned 35 MeV.
- **Perturbative argument.** The suppression factors (α_s², 1/(N_c²−1), Γ_W/m_W) are robust order-of-magnitude statements. The 5 MeV figures for the perturbative and "interplay" contributions are estimates, the second explicitly "out of thin air" (p. 308). The negative-dipole (13)+(24) structure is a genuine sub-leading-colour prediction with no MC counterpart. It links to Khoze_1996dn.md and the beyond-leading-colour shower seed topic.
- **Limitations the authors acknowledge.**
  - The two-step treatment: reconnection decided from an inclusive space-time picture, then momentum-space fragmentation.
  - At most one reconnection per event.
  - No colour-matching suppression: they assume 1/N_c² does not apply non-perturbatively because many soft gluons make colour available locally (p. 291). The paper itself flags this as a "first guess".
  - Kinematics: no ISR, perfect detector, MC-truth-assisted jet pairing in method 1.
  - Δm̄_W statistical errors ~6–10 MeV are comparable to the scenario-I shifts. Scenario-I signs are therefore not significant.
- **Observability.** The authors' pessimism about dedicated observables was partly overtaken by events: the LEP particle-flow (inter-/intra-W region ratio R_N) and m_W-estimator-difference methods did gain sensitivity, giving the 2.8σ combined preference for CR (ALEPH_2013dgf). The m_W-estimator method is close in spirit to the paper's "self-screening" suggestion.
- **Plot read-offs.** Figs. 13, 15, 16 and 18 are read by eye (≈); tabulated and in-text numbers are exact.

## Leads
- G. Gustafson, U. Pettersson, P.M. Zerwas, Phys. Lett. B 209 (1988) 90: the original "instantaneous" WW colour-rearrangement proposal that this paper rebuts (seed topic).
- T. Sjöstrand, V.A. Khoze, Phys. Rev. Lett. 72 (1994) 28 (arXiv number from memory, verify: hep-ph/9310276): the companion letter. Check for any numbers that differ.
- G. Gustafson, J. Häkkinen, Z. Phys. C 64 (1994) 659: alternative λ-based WW reconnection model; LEP never constrained it directly.
- V.A. Khoze, L.H. Orr, W.J. Stirling, Nucl. Phys. B 378 (1992) 413; Yu.L. Dokshitzer, V.A. Khoze, L.H. Orr, W.J. Stirling, Nucl. Phys. B 403 (1993) 65: soft-gluon radiation and decay–decay interference in tt̄ / unstable-particle production, the origin of the χ₁₂ profile-function argument (relevant for CR in top-mass).
- V.S. Fadin, V.A. Khoze, A.D. Martin, Phys. Lett. B 311 (1993) 311 and Phys. Lett. B 320 (1994) 141 (Durham DTP/93/18): W-width suppression of interference in W⁺W⁻.
- Ya.I. Azimov, Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, Phys. Lett. B 165 (1985) 147: perturbative "drag" effect, the antenna picture of the string effect (seed topic: string/drag effect).
- Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, Sov. J. Nucl. Phys. 50 (1990) 505: colour-suppressed interference phenomena (negative antennae).
- T. Sjöstrand, P.M. Zerwas, in "e⁺e⁻ Collisions at 500 GeV: The Physics Potential", DESY 92-123A, p. 463: 1-string vs 3-string tt̄ scenarios (CR in top).
- L. Lönnblad, T. Sjöstrand, Phys. Lett. B 351 (1995) 293 (cited by Lonnblad_1995yk): BE effects in WW as the other "cross-talk" source. The BE-vs-topology test was proposed here.
- JADE, Phys. Lett. B 157 (1985) 340: the string-effect jet-direction shift used to explain the m_W shift sign (p. 306).
- Follow-ups, forward citations: the LEP2 "QCD event generators" / "W mass" Yellow-report contributions (CERN 96-01, 1996), which define the SK-I/II/II′, AR-1/2/3 and HERWIG CR variants as used by the experiments. Also later SK-model energy-dependence and Z⁰Z⁰ studies.
