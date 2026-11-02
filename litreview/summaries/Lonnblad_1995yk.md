# Reconnecting coloured dipoles
- **ID / links:** Lonnblad:1995yk · INSPIRE 400768 · DOI 10.1007/s002880050087
- **Authors / collab, year, journal:** L. Lönnblad, 1996, Z. Phys. C 70 (1996) 107–113
- **Type:** MC/model
- **Relevance:** 3 · RQs: 2, 1b (also touches the seed topic "rapidity gaps and colour-singlet exchange" at HERA)
- **Full text source:** zotero (journal PDF with text layer, 7 pp; all pages read). Page numbers are journal pages 107–113.

## Takeaways
- **What the paper defines.** It defines the **colour-reconnection model of the ARIADNE dipole cascade (DCM)**. LEP2 analyses later used it as the "ARIADNE" CR model:
  - Every dipole carries a random colour index in [1, 9], which mimics the 1/N_c² chance of colour matching.
  - Two dipoles with equal index may swap partners. Of the allowed swaps, the one that most decreases the string-length measure λ = Σ ln(m²_{i,i+1}/m₀²) is performed (Eq. 2), and this is iterated after **every** emission during the perturbative cascade (p. 108).
  - Reconnection is therefore partly perturbative: the cascade continues from the reconnected dipoles.
- **WW prescription.** Each W dipole system first radiates all gluons with E_g > Γ_W independently, with reconnections only within each W. Then the cross-talk is switched on for E_g < Γ_W (p. 110). This implements the Sjöstrand–Khoze argument that the W lifetime kills interference for ω ≳ Γ_W. DELPHI_2006tie.md's description of "AR-2" matches this prescription.
- **m_W shift.** δm̄_W ≈ +32 MeV for reconnection below E_g < 2 GeV at 170 GeV. The range is +23 to +58 MeV, depending on whether the cascade continues below Γ_W and on the energy threshold (2 vs 5 GeV), and +50 MeV at 180 GeV. The statistical error is ≈ 8 MeV (Tab. 2). The author calls this consistent with Sjöstrand–Khoze's ~30 MeV estimate. The reconstruction method is MC-truth-assisted (p. 110).
- **LEP1 (Z⁰) event shapes.** Intra-system reconnections alone reduce ⟨N_ch⟩ from 21.20 to 20.84. A crude retune restores 21.16 (Tab. 1). Thrust and rapidity differences mostly vanish after retuning (Figs. 3–4). p_⊥out stays harder by up to ~10–20 % at large p_⊥out, which the author says data favour (Fig. 5; p. 109).
- **HERA rapidity gaps.** DCM + reconnections produces far fewer large-rapidity-gap DIS events than the SCI model or the pomeron-based ARIADNE default, which both describe data. Raising the p_⊥ cut-off (0.6 → 2 GeV) or dropping recoil gluons helps a little, but the 1/m_X² shape is not reproduced (Figs. 8–10; p. 112). The author concludes that CR in an *unordered* (BFKL-like) cascade cannot explain HERA gap events (p. 113).

## Setup
- **DCM basics.** Gluon emission from colour dipoles; after emission a dipole splits into two. The leading-colour approximation drops the 1/N_c²-suppressed qq̄ dipole when describing the 2nd emission (i.e. after the first). The dipole chain is equivalent to a Lund string with gluon kinks (p. 107).
- **Colour-index bookkeeping** (p. 108):
  - Indices are random in [1, 9]. Adjacent dipoles may not share an index, which would make a colour-singlet gluon.
  - For the coherently treated emission (Fig. 2) the gluon is assigned to one emitter with probability P₃ = x₁²/(x₁² + x₃²) (Eq. 1). The new dipole between the gluon and its "emitter" gets a fresh index; the other dipole keeps the old one.
  - g → qq̄ splittings keep the indices.
  - After each emission, all equal-index pairs whose swap lowers λ are considered and the largest decrease is taken. This repeats until no decrease remains, and the cascade then continues.
- **Motivation from coherence** (p. 108; Eq. 3): in the strongly ordered limit, angular ordering with a closer same-colour parton would imply the same recoupling as the λ-criterion. The author warns that ARIADNE is not always strongly ordered, so perturbative reconnection "may be somewhat overestimated".
- **Hadronisation.** JETSET string fragmentation without further reconnection (p. 109). The model "follows closely" Gustafson–Häkkinen [12] (one inter-W reconnection per event, no intra-W reconnection) but generalises it (pp. 107, 110).
- **LEP1 study.** ARIADNE + JETSET for hadronic Z⁰: default vs with reconnections vs reconnections + "crude retuning" of JETSET fragmentation parameters. Which parameters were retuned is **not specified** in the paper (p. 109).
- **LEP2 study.** e⁺e⁻ → W⁺W⁻ → 4 jets at 170 GeV (and 180 GeV), ~10⁵ events per model.
  - m_W reconstruction "similar to method 1" of Sjöstrand–Khoze [3]: jets are assigned to W's using generator-level quark directions, so the method is not experimentally feasible.
  - Observable: Δm̄_W (reconstructed − generated average mass) and δm̄_W = shift with respect to no reconnection (p. 110; Tab. 2).
  - Two-pass cascade: the DCM is ordered in p_⊥, not energy, so the cascade is run twice: first E_g > Γ_W without cross-talk, then E_g < Γ_W with cross-talk. The author notes this is "somewhat inconsistent". The alternative omits the second pass but allows inter-W reconnection before fragmentation (row e) (p. 110).
- **HERA study.** Boson–gluon fusion in DIS, ARIADNE 4.07 vs LEPTO 6.3 SCI (soft colour interactions with fixed probability R ≈ 0.2 and a virtuality cut-off of 4 GeV²).
  - Here inter-system reconnections are allowed only *after* the perturbative cascade; intra-system ones are allowed throughout (p. 111).
  - Observables: η_max of the most forward particle and the m_X distribution for η_max < 3.2 (Figs. 8–10). No data are overlaid.

## Results
**LEP1 (Z⁰)**
- ⟨N_ch⟩: default 21.20, reconnected 20.84, reconnected + retuned 21.16, statistical error ≈ 0.02 (Tab. 1). All reconnections shorten strings (decrease λ), so multiplicity drops (p. 109).
- Relative to default: thrust differences are within ~±(few %) after retuning, with statistical fluctuations up to ±0.2 at low T (Fig. 3). Rapidity along the thrust axis drops by up to ~2–3 % before retuning and returns to ~0 after (Fig. 4).
- p_⊥out (out of the event plane) is harder with reconnections: a relative excess growing to ~+0.1–0.2 at p_⊥out ~ 2–3 GeV, which retuning does not remove (Fig. 5; ≈ read-off). The author notes ARIADNE underdescribes data here and the hardening "is favoured by data", but "no firm conclusions" are possible before a full retune (p. 109).

**LEP2 W mass (Tab. 2; 170 GeV unless noted; δ errors ≈ 8 MeV, Δ errors ≈ 6 MeV)**

| Row | Model | ⟨Δm̄_W⟩ (MeV) | ⟨δm̄_W⟩ (MeV) |
|---|---|---|---|
| a | No reconnections | 98 | – |
| b | Reconnections within each W | 103 | 5 |
| c | (b) retuned | 97 | −1 |
| d | (c) + inter-W reconnection for E_g < 2 GeV | 130 | 32 |
| e | (d) but no gluons with E_g < 2 GeV (no second cascade) | 121 | 23 |
| f | (d) but threshold E_g < 5 GeV | 156 | 58 |
| g | No reconnections, 180 GeV | 140 | – |
| h | (d) at 180 GeV | 190 | 50 |

- Intra-W reconnection alone has no significant effect on m_W (rows b, c).
- Inter-W reconnection shifts m_W **upwards** by ~25–60 MeV. The shift is sensitive to the E_g threshold and to √s. Whether the cascade continues below Γ_W matters little (d vs e) (p. 110).
- The text says the "realistic scenarios (d), (e) and (g)" give 30–50 MeV. Row (g) is the 180 GeV no-reconnection baseline, so this is presumably a typo for (h) (our reading).
- The author stresses that the effects "depend heavily on the details of the method" and that realistic reconstructions "will most likely smear out these effects" (p. 110). The reconnected fraction of events is **not** quoted in the paper.

**HERA rapidity gaps (Figs. 7–10)**
- ARIADNE's unordered dipole cascade radiates far more gluons at forward lab rapidities (y ≳ 3–8) than LEPTO's DGLAP shower (Fig. 7).
- η_max distribution: the gap-event rate (η_max small) for DCM+reconnections is roughly an order of magnitude below SCI and the default pomeron model (Fig. 8, log scale; ≈).
- p_⊥cut raised to 2 GeV or recoil gluons removed: a modest increase in gaps (Fig. 9). The m_X spectrum of gap events (η_max < 3.2) does not follow the 1/m_X² behaviour seen at HERA (Fig. 10; p. 112).

## Assessment
- **Why it matters.** This is the primary reference for the ARIADNE CR model that, together with SK-I and HERWIG CR, formed the trio of CR models in the LEP2 W analyses (ALEPH_2013dgf.md, DELPHI_2006tie.md).
  - The LEP combination constrains only SK-I. ARIADNE-2 (this paper's E_g < Γ_W prescription, reported at ~22 % reconnected at 189 GeV) enters only through the "equal reconnection fraction" heuristic (ALEPH_2013dgf, p. 67).
  - ALEPH_2013dgf reports that "ARIADNE-1" is ruled out by Z → 3-jet data. AR-1 appears to be the variant with inter-W reconnection at all scales; this paper does not use the AR-1/2/3 labels. DELPHI_2006tie identifies only AR-2 (E_g < Γ_W); the AR-1 identification is our inference [unverified: not stated in this paper or in DELPHI_2006tie.md] and should be confirmed against the LEP2 generator Yellow report.
  - The paper's own LEP1 check (Figs. 3–5) concerns only intra-system reconnection and finds it retunable. The later gluon-jet rapidity-gap tests were what constrained these models.
- **m_W shifts in context.** +23 to +58 MeV at 170–180 GeV with MC-truth jet assignment; the sign is the same as SK-I in method 1 but larger (Sjostrand_1993hi Tab. 1: +14 MeV). LEP's final 35 MeV CR systematic (with soft-particle de-weighting, SK-I at k_I = 2.10) is of the same order. DELPHI_2006tie later found only ΔM_W(std, cone) = 7.2 ± 4.1 MeV for ARIADNE. This supports the author's expectation that realistic reconstructions dilute the effect, though the observables differ.
- **Model-dependence and weaknesses.**
  - The λ-minimisation criterion forces every reconnection to shorten strings. The model can therefore only reduce multiplicity (contrast SK-I, which allows length-increasing reconnections).
  - The 1/9 colour-index rule is a crude stand-in for SU(3) colour algebra, with no colour-octet/sextet structure and no negative-weight terms. Christiansen_2015yqa.md's QCD-based CR later improves on this.
  - The E_g < Γ_W cut is a step function at a fixed 2 GeV. Tab. 2 shows a 32 → 58 MeV sensitivity to moving it to 5 GeV, so the cut-off is effectively a hidden parameter.
  - The reconnection fraction is not given, which makes direct comparison with SK-I P_recon impossible from this paper alone.
  - The retuning is described only as "crude", with unspecified parameters.
- **HERA conclusion.** It is a model-internal negative result: CR within an unordered DCM cannot give the gap rate or the m_X shape. It does not exclude SCI-type models with ordered showers, as the author notes (p. 113). The comparison is MC vs MC; no data points are shown. Relevant to the "rapidity gaps / colour-singlet exchange" seed topic as a cautionary counterpoint to Edin–Ingelman–Rathsman SCI (cf. Rathsman_1998tp.md).
- **Read-offs.** Figs. 3–10 read-offs are approximate (≈). Table values are exact.

## Leads
- G. Gustafson, J. Häkkinen, Z. Phys. C 64 (1994) 659 [12]: the λ-based WW reconnection model this one generalises (seed topic CR in WW).
- A. Edin, G. Ingelman, J. Rathsman, "Rapidity gaps in DIS through soft colour interactions", DESY 95-145 → Phys. Lett. B 366 (1996) 371 [8]: SCI model, the main competitor in the HERA comparison (seed topic: rapidity gaps).
- W. Buchmüller, A. Hebecker, DESY 95-077 → Phys. Lett. B 355 (1995) 573 (journal ref. from memory, verify) [7]: "LOR" soft-colour model of diffractive DIS.
- J. Ellis, D.A. Ross (cited as "I.A. Ross"), "Search for large rapidity gap events in e⁺e⁻ annihilation", CERN-TH/95-84 → Phys. Lett. B 384 (1996) 293 (journal ref. from memory, verify) [35]: proposed e⁺e⁻ gap test of CR (RQ4).
- L. Lönnblad, T. Sjöstrand, Phys. Lett. B 351 (1995) 293 [22]: Bose–Einstein effects as W⁺W⁻ cross-talk / m_W systematic.
- B. Andersson, P. Dahlqvist, G. Gustafson, Phys. Lett. B 214 (1988) 604; Z. Phys. C 44 (1989) 455 [15, 16]: the λ measure underlying λ-minimising CR models (also used in Christiansen_2015yqa).
- L. Lönnblad, Z. Phys. C 65 (1995) 285 [23]: the pomeron-inspired DCM model for HERA rapidity gaps (ARIADNE default).
- K. Hamacher, M. Weierstall, WU B 95-07 (1995) [21]: DELPHI generator tuning, needed for any retune with CR.
- Follow-up, not cited: the LEP2 Yellow Report "QCD event generators" (CERN 96-01; hep-ph/9601212) and the "Determination of the mass of the W boson" chapter (hep-ph/9602352) (arXiv numbers from memory, verify). They should define the AR-1/AR-2/AR-3 variants and compare all CR models on common m_W methods. Needed to pin down the AR-1/AR-2 mapping used in ALEPH_2013dgf.
- Follow-up, forward citations: Friberg, Gustafson, Häkkinen, Nucl. Phys. B 490 (1997) 289 (gluon-jet rapidity-gap test of CR in Z⁰ → 3 jets) and the ALEPH/L3/OPAL Z → 3-jet CR tests that ruled out AR-1 (ALEPH_2013dgf refs [108–110]).
