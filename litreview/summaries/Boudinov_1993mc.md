# Is there experimental evidence for coherence of soft gluons from the momentum spectra of hadrons in e⁺e⁻ data?
- **ID / links:** Boudinov:1993mc · INSPIRE 366377 · arXiv — · DOI 10.1016/0370-2693(93)91529-V
- **Authors / collab, year, journal:** E.R. Boudinov, P.V. Chliapnikov, V.A. Uvarov (IHEP Protvino), 1993, Phys. Lett. B 309 (1993) 210–221
- **Type:** phenomenology (MC study + reanalysis of published data)
- **Relevance:** 3 · RQs: 1a, 2, 3, 4
- **Full text source:** zotero

## Takeaways
- A critical paper. The authors argue that the e⁺e⁻ ξ = ln(1/x_p) spectra (shape, peak-position evolution, mass dependence) provide no evidence for soft-gluon coherence, and that their agreement with MLLA + LPHD is not proof (abstract; p. 218–220). They explicitly do not question coherence at parton level (p. 220).
- **Argument 1: shape.** The hump is a consequence of the ξ variable itself, and coherence only affects the peak position and the right-hand fall-off (p. 211).
  - In JETSET 7.3, the parton (gluon) ξ spectra with and without angular ordering differ markedly. The charged-hadron, prompt π⁰ and prompt η spectra are practically identical (Fig. 1).
  - Hence hadron spectra are set by string fragmentation (string energy), not by the last-stage parton spectrum. That contradicts local LPHD within JETSET (p. 211).
  - A retuned incoherent shower + IF (Cojets 6.12, Mazzanti–Odorico) fits the OPAL and TASSO spectra as well as JETSET/HERWIG do (p. 212).
- **Argument 2: peak evolution.** The authors attack the "b = 1 for phase space" reference used by OPAL:1990vmr:
  - pp → c⁻X spectra rebuilt from parametrized y and p_T distributions (21.7–900 GeV) give b₁ = 0.90 ± 0.03, below 1 because ⟨p_T⟩ rises (p. 213, Fig. 2).
  - Reanalysed TASSO+OPAL+L3 e⁺e⁻ data give b₁ = 0.64 ± 0.02 and width slope b₂ = 0.55 ± 0.03 (Fig. 3).
  - JETSET 7.3, 14–500 GeV (p. 214): coherent b₁ = 0.67 ± 0.01; incoherent b₁ = 0.70 ± 0.01. The authors call these "practically the same".
- **Argument 3: parton-level decomposition** (JETSET 7.3, p. 214–219, Tabs. 1–2):
  - "Primary" gluons (radiated by the quarks) without coherence follow cylindrical phase space: b₁ = 1.00 ± 0.01, b₂(R) = 0.01 ± 0.03. With coherence, b₁ depends strongly on the quark flavour and on the energy range (0.41–0.98, Tab. 2).
  - "Secondary" gluons (from g→gg) give b₁ = 0.60 ± 0.01 with or without coherence, and they dominate increasingly with energy (Tab. 1).
  - So b₁ < 1 does not require coherence, even at parton level.
- **Argument 4: particle dependence.**
  - The mass ordering of ξ_max is expected from phase space anyway.
  - In JETSET and HERWIG the ξ spectra of strange particles depend strongly on the primary-quark flavour (Figs. 4–7, Tab. 3), which MLLA ignores.
  - MLLA fits use two free parameters (normalization and Λ_eff), and Λ_eff is particle-dependent, so a good fit is not proof (p. 220).

## Setup
- Data are not new. The authors reuse published charged-particle ξ spectra (TASSO 14–44 GeV [26], OPAL [13] = OPAL:1990vmr, L3 [14]) and identified-particle spectra (π⁰ L3 [14], η L3 [17], K⁰ OPAL/DELPHI [15,16], Λ DELPHI/OPAL [16,18], Ξ⁻ OPAL [18]) (p. 210–211).
- Width variable λ = ⟨n_ch⟩σ_h/(dσ/dξ)_{ξ_max}, which equals √(2π)σ for a Gaussian (Eq. 5). Scaled variable ζ = (ξ − ξ_max)/λ (Eq. 6).
  - ξ_max and the peak height are taken from Gaussian fits near the peak.
  - λ(R) is the analogous width on the right-hand (large-ξ) side.
  - Energy evolution is fitted as ξ_max = b₁ ln√s + c₁ (Eq. 1) and λ = b₂ ln√s + c₂ (Eq. 7).
- Hadron-collider reference (p. 213; Eqs. 2–4): pp/p̄p → c⁻X ξ spectra are reconstructed, assuming y–p_T factorization, from:
  - the Uvarov–Chliapnikov rapidity parametrization exp[−a₁(y/Y)² − a₂(y/Y)⁴], with Y = ln(√s/a₃), ref. [33];
  - dσ/dp_T² ∝ exp(−a₄m_T);
  - at 21.7, 53, 200 and 900 GeV.
- MC (p. 211, 214, 216–217):
  - JETSET 7.3 tuned to DELPHI global event shapes (ref. [37]). Coherent: MSTJ(42) = 2, MSTJ(46) = 3. Incoherent: MSTJ(42) = 1, MSTJ(46) = 0.
  - The paper does not state whether the incoherent version was retuned.
  - HERWIG 5.4 with default parameters.
  - 500 000 events per program per energy (14, 22, 35, 44, 91 GeV), separately for uū+dd̄, ss̄, cc̄, bb̄.
  - Parton-level studies use the last-stage gluons before hadronization, from 14 to 500 GeV.
- The authors warn that MC flavour-separated predictions are "at best ... only qualitative" (p. 216).

## Results
- **Published ξ_max at the Z⁰ quoted** (p. 211):
  - π⁰ 4.11 ± 0.08; η 2.60 ± 0.15.
  - K⁰ 2.62 ± 0.11 and 2.91 ± 0.04.
  - Λ 2.82 ± 0.25 and 2.77 ± 0.05.
  - Ξ⁻ 2.57 ± 0.11.
  - η, K⁰, Λ and Ξ⁻ are "practically the same", although phase space would suggest ξ_max(η) ≈ ξ_max(K⁰) > ξ_max(Λ) ≥ ξ_max(Ξ⁻) (p. 216).
- **JETSET 7.3, coherence on/off** (Fig. 1): gluon spectra differ visibly in shape. Last-stage gluon spectra show a two-peak structure: primary gluons at high ξ, secondary g→gg gluons at lower ξ (p. 214). The small-print scan does not let us say reliably which curve is which in Fig. 1a. Charged-hadron, prompt π⁰ and prompt η spectra (each normalized to 1) are indistinguishable by eye.
- **pp reference** (Fig. 2, p. 213):
  - The right-hand side of (dσ/dξ)/(dσ/dξ)_max vs ξ − ξ_max nearly scales from 21.7 to 900 GeV, with a "small but noticeable" increase of the width λ(R) with energy (p. 213).
  - b₁ = 0.90 ± 0.03, b₂(R) = 0.08 ± 0.03.
  - Flat rapidity plateaus with energy-independent ⟨p_T⟩ would give b₁ = 1 exactly; the deficit is attributed to the rising ⟨p_T⟩.
- **e⁺e⁻ reanalysis, 14–91 GeV** (Fig. 3, p. 213–214):
  - b₁ = 0.64 ± 0.02. The authors call it consistent with OPAL's 0.637; the error is quoted here as ±0.014, whereas OPAL:1990vmr gives ±0.016 and this paper's own p. 212 also says ±0.016.
  - b₂ = 0.55 ± 0.03, b₂(R) = 0.26 ± 0.02.
  - Footnote 2: a fit of Eq. 7 over 22–91 GeV gives b₂ = 0.62 ± 0.03 with χ²/NDF = 0.8/3, against 7.1/4 over 14–91 GeV. The printed text reads "7 1/4"; our reading is 7.1/4.
  - Scaled ζ distributions approximately scale on the fall-off side (not shown).
  - Conclusion drawn: compared with pp, e⁺e⁻ has a slower peak evolution and a much faster growth of the right-hand width.
- **JETSET 7.3 hadron-level slopes, 14–500 GeV** (p. 214):

  | Version | b₁ | b₂ | b₂(R) |
  |---|---|---|---|
  | Coherent | 0.67 ± 0.01 | 0.51 ± 0.01 | 0.26 ± 0.01 |
  | Incoherent | 0.70 ± 0.01 | 0.45 ± 0.01 | 0.23 ± 0.01 |

  The authors summarize: "practically the same slope values … insensitivity … to the inclusion of soft gluon coherence".
- **Gluon peak heights** (Tab. 1), incoherent / coherent:

  | √s (GeV) | Primary | Secondary |
  |---|---|---|
  | 14 | 0.65 / 0.63 | 0.46 / 0.30 |
  | 44 | 0.83 / 0.81 | 1.40 / 0.77 |
  | 91 | 0.85 / 0.84 | 2.27 / 1.14 |
  | 500 | 1.08 / 0.97 | 6.37 / 2.29 |

  - Secondary gluons grow much faster than primaries.
  - Secondary production is about 2–3× lower with coherence at 91–500 GeV. This multiplicity suppression is itself a coherence effect, although the authors do not stress it.
- **Primary-gluon slopes** (Tab. 2; p. 214–215):
  - Incoherent: b₁ = 1.00 ± 0.01, b₂ = 0.38 ± 0.02, b₂(R) = 0.01 ± 0.03, flavour-independent.
  - Coherent, by flavour and energy range:

    | √s range | Flavour | b₁ | b₂(R) | b₂ |
    |---|---|---|---|---|
    | 14–44 GeV | uū+dd̄ | 0.64 ± 0.02 | 0.32 ± 0.04 | 0.64 ± 0.02 |
    | 91–500 GeV | uū+dd̄ | 0.41 ± 0.03 | 0.30 ± 0.04 | 0.59 ± 0.03 |
    | 14–44 GeV | bb̄ | 0.98 ± 0.03 | 0.02 ± 0.04 | 0.60 ± 0.02 |
    | 91–500 GeV | bb̄ | 0.80 ± 0.04 | 0.18 ± 0.04 | 0.60 ± 0.03 |

- **Secondary-gluon slopes** (p. 215): b₁ = 0.60 ± 0.01, b₂ = 0.50 ± 0.01, b₂(R) = 0.33 ± 0.02, the same for incoherent and coherent branching and for all flavours.
  - Footnote 3 explains why: for g→gg, phase space is restricted with increasing energy in only one direction, perpendicular to the event plane (p. 216), so b₁ lies between 0.5 (spherical phase space) and 1 (cylindrical).
  - The authors conclude that b₁ ≠ 1 "cannot" establish coherence even at parton level (p. 216), and that the data–(b₁ = 1) difference says nothing about the dominance of coherence (p. 219).
- **Flavour dependence at 91 GeV** (Tab. 3; Figs. 4–6):
  - JETSET ξ_max for (u,d) quarks: π⁰ 3.91, c± 3.71, K⁰ 3.24, Λ 2.60, Ξ⁻ 2.51.
  - JETSET ξ_max for s quarks: K⁰ 2.11, Λ 1.54, Ξ⁻ 1.19.
  - HERWIG 5.4 gives a similar pattern, e.g. K⁰ 3.33 (u,d) vs 1.86 (s).
  - Both models describe OPAL/L3 summed-flavour data. Their flavour composition differs a lot, especially for bb̄, while the per-flavour shapes are similar (p. 217).
  - The mass hierarchy for (u,d) flavours, ξ_max(π⁰) > ξ_max(c±) > ξ_max(K⁰) > ξ_max(Λ) > ξ_max(Ξ⁻), is "in agreement with phase space expectations" (p. 218–219).
  - Normalized to the multiplicity of each species, the right-hand shapes are flavour-independent (p. 218).
- **Energy evolution of ξ_max by flavour** (Fig. 7): for K⁰ the flavour splitting is large in both generators. For π⁰ it is smaller. Points are read off the figure only; no numbers are tabulated.
- **Conclusions** (p. 218–220):
  - The ξ shape is not sensitive to coherence.
  - The peak evolution in MLLA is dominated by g→gg, which is coherence-insensitive, and MLLA omits the flavour dependence of primary-gluon slopes.
  - MLLA gives no quantitative mass dependence.
  - The strange-particle flavour dependence is not in MLLA, and MLLA's claimed applicability to massive particles holds only at the largest ξ.
  - Agreement with MLLA comes from fitting two free parameters (N, Λ_eff), with Λ_eff particle-dependent.

## Assessment
- **Quantitative basis.** The core claim (hadron spectra insensitive to coherence) rests on one generator, JETSET 7.3, with string fragmentation. Fig. 1 shows a visual overlap, with no χ² or ratio. The slope table on p. 214 gives b₁ = 0.67 vs 0.70 (± 0.01 each) over 14–500 GeV, against data 0.64 ± 0.02 over 14–91 GeV.
  - By the authors' own numbers the incoherent version is ≈ 2.7σ from the data and the coherent one ≈ 1.3σ (our arithmetic, quadrature sum of errors, mismatched energy ranges).
  - This matches OPAL:1990vmr Tab. 4 (0.692 vs 0.663, data 0.637). "Practically the same" is fair as a statement of weak discrimination, but it is not a demonstration of zero sensitivity. Both papers effectively agree that the separation is ≈ 1σ-level.
- **Retuning ambiguity.** It is not stated whether the incoherent JETSET was retuned. OPAL retuned its incoherent options to ⟨n_ch⟩ (OPAL:1990vmr p. 623). An untuned incoherent shower would have a different multiplicity, so the Fig. 1 comparison (normalized to 1) may hide normalization differences.
- **Cojets argument.** The claim that incoherent + IF (Cojets 6.12) matches OPAL/TASSO spectra rests on ref. [32] (Mazzanti–Odorico), not on new work here. OPAL:1992lzb shows Cojets 6.20 failing the TPAC azimuthal correlations by 5.0–5.2σ (and Cojets 6.12 having the wrong shape), and OPAL_1991xwi shows Cojets fails the string effect (R̃ ≈ 1.02). Cojets's ξ success therefore does not generalize to other observables.
- **The pp "phase space" reference.** It is a parametrization-based reconstruction (factorized y, p_T), and pp minimum-bias events contain multiple-scattering/colour effects of their own. So b₁ = 0.90 is a heuristic benchmark, not a coherence-free control.
  - The paper's strongest genuine point is the parton-level decomposition. Within JETSET, secondary g→gg gluons have b₁ ≈ 0.60 regardless of coherence and dominate at high energy, so a slope well below 1 is not unique to angular ordering.
  - Caveat: this is model-internal. Coherence does strongly suppress the secondary-gluon multiplicity (Tab. 1), which affects the peak height and the multiplicity evolution, and the paper does not examine those.
- **Consistency with other critiques.** The paper is consistent with the later admission in Khoze_1996dn (p. 42) that the ξ spectrum alone, after retuned string hadronization, is not evidence for coherence within MCs. It anticipates the community's move to observables such as azimuthal correlations (OPAL:1992lzb), the string/drag effect, and the multiplicity ratio and q/g jet differences.
- **Minor issues.**
  - OPAL's slope error is quoted inconsistently (±0.016 on p. 212, ±0.014 on p. 213).
  - The flavour-dependence discussion is explicitly qualitative.
  - No uncertainty is attached to the JETSET-vs-HERWIG ξ_max values in Tab. 3.

## Leads
- P. Mazzanti, R. Odorico, Nucl. Phys. B 370 (1992) 23 (ref. [32]): the claim that a tuned incoherent IF model (Cojets 6.12) fits LEP/TASSO ξ spectra, which carries much of the critique. Also cited by OPAL:1992lzb as the Cojets 6.20 tune.
- V.A. Uvarov, P.V. Chliapnikov, Yad. Fiz. 50 (1989) 1689 [Sov. J. Nucl. Phys. 50 (1989) 1048] (ref. [33]): the pp rapidity parametrization and width analysis underlying the "phase space" reference.
- Ya.I. Azimov, Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, Z. Phys. C 31 (1986) 213 (ref. [11]): the LPHD/resonance-duality statement the authors challenge.
- Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, Lund preprint LU TP 90-12 (ref. [12]): MLLA for massive/identified particles.
- Identified-particle ξ_max measurements at the Z⁰:
  - L3, B. Adeva et al., Phys. Lett. B 259 (1991) 199 (π⁰);
  - L3, O. Adriani et al., Phys. Lett. B 286 (1992) 403 (η);
  - OPAL, G. Alexander et al., Phys. Lett. B 264 (1991) 219 (K⁰);
  - DELPHI, P. Abreu et al., Phys. Lett. B 275 (1992) 231;
  - OPAL, P.D. Acton et al., Phys. Lett. B 291 (1992) 503 (Λ, Ξ⁻).
  - These are the data behind the mass-dependence argument; relevance probably 2.
- TASSO, W. Braunschweig et al., Z. Phys. C 47 (1990) 187: the 14–44 GeV spectra.
- Forward: rebuttals and later analyses of ξ* vs √s with coherence on/off, e.g. limiting-spectrum fits with Q₀ ≈ Λ and full-energy-range (LEP2, HERA Breit frame) tests. Run `citing 366377` to find direct responses.
