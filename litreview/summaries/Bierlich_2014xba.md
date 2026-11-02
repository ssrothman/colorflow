# Effects of Overlapping Strings in pp Collisions
- **ID / links:** Bierlich:2014xba · INSPIRE 1335149 · arXiv 1412.6259 (v3, 13 Feb 2015) · DOI 10.1007/JHEP03(2015)148
- **Authors / collab, year, journal:** C. Bierlich, G. Gustafson, L. Lönnblad (Lund), A. Tarasov (JLab), 2015, JHEP 03 (2015) 148
- **Type:** MC/model
- **Relevance:** 3 · RQs: 1, 2, 3, 4
- **Full text source:** arxiv

Page numbers below are the printed page numbers (PDF page = printed + 1).

## Takeaways
- The original **rope hadronization** paper, implemented in DIPSY (BFKL dipole cascade in impact-parameter space) + ARIADNE final-state shower + Pythia 8 string fragmentation. Strings that overlap in transverse space (radius r₀ ≈ 1 fm) and rapidity add their colour charges as a random walk in SU(3) to a multiplet {p,q}. The rope tension scales with the quadratic Casimir (lattice result for an isolated rope), and each qq̄ break-up sees an **effective string tension** κ̃ equal to the *drop* in Casimir: κ̃/κ = (2p+q+2)/4 (Eq. 3.4; local form Eq. C.11). The authors stress that this is much smaller than the usual Schwinger-type assumption κ̃ = (2p−1)κ (Eq. 3.6), which is about 4× larger at large p (p. 14).
- A higher κ̃ = hκ rescales the Pythia flavour parameters as ρ → ρ^{1/h} (s/u), x → x^{1/h}, y → y^{1/h}, σ_p⊥ → σ√h, with a separate law for the diquark rate ξ (Eqs. 2.8–2.9, C.1–C.5). Total multiplicity is argued to be nearly unchanged by κ̃ (breaks happen earlier but hadrons are smaller, so b is almost invariant; p. 9). The main multiplicity effect is that only p+q ~ √(m+n) breaks are needed (Fig. 3; p. 14).
- Colour singlets from 3⊗3̄ = 8⊕1 are handled by a **final-state swing** (a colour reconnection between same-colour dipoles in ARIADNE, weight Eq. 4.3). The authors say much of the ⟨p⊥⟩-dependent, flow-like rise of p/π and Λ/K at low p⊥ comes from this CR, and the rest from rope tension (pp. 25–29).
- Against minimum-bias data (STAR 200 GeV; CMS 0.9 and 7 TeV), ropes fix the ≈ 10–40% deficit (read off Figs. 8–10) of DIPSY-without-ropes and of Pythia 8 (4C) in p/π, Λ/K⁰_S and Ξ⁻/Λ, including their weak √s dependence, with untuned new parameters r₀ = 1 fm, β = 0.25, m₀ = 0.135 GeV (Figs. 8–10, p. 20). The model **fails** to reproduce the fall of Λ/K⁰_S and p/π above p⊥ ≈ 2–3 GeV (Fig. 8 right, p. 26).
- Typical pp enhancement: ⟨h⟩ = ⟨κ̃/κ⟩ ≈ 1.13 at the low end of the plotted range (√s of a few hundred GeV) rising logarithmically to ≈ 1.22 at ≈ 14 TeV, i.e. ≈ 1.16–1.22 at LHC energies (read off Fig. 12; "around 1.2" at LHC, p. 10). Predicted ratio enhancements over plain strings (Fig. 11) are largest for baryons and multistrange hadrons and grow with √s. This is the model's main experimental test (RQ4).

## Setup
- **Event generation.**
  - DIPSY: Mueller dipole cascade with NLL-type corrections (energy-momentum conservation, running α_s, energy-scale terms), confinement via a gluon mass m_g, and saturation via the initial-state "swing" (App. A, Eqs. A.1–A.3).
  - Final-state radiation from ARIADNE (dipole shower), with the final-state swing added (§4.1).
  - Hadronization: Pythia 8, called string by string through a UserHook that changes the fragmentation parameters at each break (App. C.3).
  - Reference curve: Pythia 8.180, tune 4C (fn. 10, p. 20).
- **Final-state swing.** Two dipoles with the same colour index (probability 1/N_c²) may swap, (12)(34) → (14)(32). It competes with gluon emission, dP_s/dρ = λ·(p₁+p₂)²(p₃+p₄)²/[(p₁+p₄)²(p₃+p₂)²] (Eq. 4.3), which favours small dipole masses, in the spirit of the λ-measure (Eq. 4.1). Only dipoles closer than ∝ 1/m_g in impact parameter can swing (p. 17). A junction ("antitriplet") swing (Fig. 6) is sketched but deferred. Its effect is mimicked inside the rope model instead (p. 17).
- **Rope formation.** SU(3) multiplets {p,q} with dimension N = (p+1)(q+1)(p+q+2)/2 (Eq. 3.1). Random-walk steps follow Eq. 3.2, recursions Eqs. B.3–B.5. The tension ratio is C₂({p,q})/C₂({1,0}) = (p²+pq+q²+3p+3q)/4 (Eq. 3.3). The {1,0}⊗{0,1}→{0,0} step is excluded from the walk because the swing has already taken it (p. 19).
- **Two overlap schemes.**
  - **Pipe-based (App. C.1):** each string is replaced by a straight cylinder along y, with radius r_pipe² = r₀² + spread (Eq. C.7). m and n come from geometric overlaps (Eq. C.8). One average h = (p²+pq+q²+3p+3q)/[4(p+q)] is used per string (Eq. C.9). Strings are randomly discarded with probability 1−(p+q)/(m+n), which the authors note breaks energy-momentum conservation (p. 37).
  - **Dipole-based (App. C.2), the default "Rope":** each dipole is taken in its rest frame. m_i and n_i are the summed rapidity-overlap fractions of parallel and antiparallel dipoles within r₀ (Eq. C.10), after the partons have propagated for a time 1/m₀. Dipoles are broken with probability (1+m_i+n_i−p_i−q_i)/(1+m_i+n_i). Two gluons are replaced by a diquark–antidiquark pair to emulate junctions, or by quarks with probability β (p. 39). The local κ̃ comes from Eq. C.11. Gluon loops use a string-averaged κ̃ (p. 40).
- **Tuning (App. D).**
  - ARIADNE + Pythia 8 are tuned to DELPHI LEP data with and without the swing (Fig. 18). LEP fragmentation parameters: a = 0.42, b = 0.4 (p. 7).
  - DIPSY is tuned with Professor to σ_tot, σ_el and ATLAS 0.9 and 7 TeV min-bias data (Figs. 19–21), separately with and without ropes, so that the total multiplicity is the same. Only flavour ratios are then changed by the ropes (p. 23).
  - DIPSY has no diffraction model, so only particle ratios are compared. The authors' justification is that in Pythia 8 diffraction changes the Λ yield but not Λ/K⁰_S (Fig. 22, pp. 41–44).
- **Data.** STAR p/π⁺(p⊥) at 200 GeV; CMS Λ/K⁰_S(p⊥) at 7 TeV, Λ/K⁰_S(|y|) and Ξ⁻/Λ(|y|) at 0.9 and 7 TeV (Figs. 8–10).

## Results
- **Parameter scaling (Fig. 2).** As h goes from 1 to 8, ρ̃ rises from ≈ 0.19 to ≈ 0.8 and ξ̃ from ≈ 0.09 to ≈ 1. ã falls from ≈ 0.3 to ≈ 0.1, and b̃ rises from ≈ 0.8 to ≈ 1.0 (read from Fig. 2). In pp, h < 1.5 (Fig. 2 caption, p. 9).
  - At h ≈ 1.2, the changes in a and b would naively reduce multiplicity by ≈ 5%. This is absorbed by retuning in pp (p. 10).
  - For AA at LHC, the authors *predict* a 15–20% multiplicity decrease from ã, b̃, without retuning (p. 10).
- **Random walk (Fig. 3).** ⟨p+q⟩ ≈ 7 for m+n = 16 (1σ band ≈ 5–9), consistent with p+q ~ √(m+n) (p. 14).
- **Worked example (App. B.2).** Three random triplets give a decuplet, two octets and a singlet with probabilities 10/27, 8/27, 8/27, 1/27.
  - The decuplet breaks with κ̃/κ = 2, 3/2, 1.
  - An octet breaks with κ̃/κ = 5/4, then 1 (pp. 34–35).
- **p/π at 200 GeV (Fig. 8 left).** DIPSY and Pythia undershoot STAR. MC/data is ≈ 0.6–0.9 at low p⊥, Pythia lowest (read from ratio panel). Rope is closer to the data in normalization and p⊥ shape (p. 21). The STAR errors are large.
- **Λ/K⁰_S vs p⊥ at 7 TeV (Fig. 8 right).**
  - Data peak at ≈ 1.1 near p⊥ ≈ 2.5 GeV. DIPSY and Pythia peak at ≈ 0.65–0.8, with MC/data ≈ 0.6–0.7 around 2 GeV.
  - Rope reaches ≈ 1.0 and describes the rise up to ≈ 3 GeV. It does not fall at high p⊥: MC/data > 1.4 (off scale) above ≈ 4.5 GeV (read from Fig. 8).
- **Λ/K⁰_S vs |y| (Fig. 9).** Data are ≈ 0.52 at 0.9 TeV and ≈ 0.54 at 7 TeV. Rope matches within errors at both energies. DIPSY gives ≈ 0.38–0.39 and Pythia ≈ 0.38–0.42, i.e. MC/data ≈ 0.7–0.8 (Pythia up to ≈ 0.9 at |y| > 1.5, 0.9 TeV) with no energy dependence (read from Fig. 9). The authors say the rope captures the "albeit weak" energy dependence (caption).
- **Ξ⁻/Λ vs |y| (Fig. 10).** Data are ≈ 0.10–0.12. Rope is ≈ 0.11–0.12, within errors. DIPSY is ≈ 0.09 and Pythia ≈ 0.08, i.e. MC/data ≈ 0.6–0.85 (read from Fig. 10).
- **Predicted √s dependence (Fig. 11; p⊥ > 200 MeV, rope/no-rope ratios, from ≈ 0.9 TeV to the top of the axis, ≈ 14 TeV, as read).**

  | Ratio | Enhancement |
  |---|---|
  | p/π | ≈ 1.29 → ≈ 1.45 |
  | Ξ⁻/Λ | ≈ 1.18 → ≈ 1.36 |
  | Λ/K⁰_S | ≈ 1.38 → ≈ 1.40 |
  | K/π | ≈ 1.11 → ≈ 1.17 |

  The strangeness and baryon effects do not factorize simply (p. 21).
- **Model behaviour.**
  - ⟨h⟩ rises from ≈ 1.13 to ≈ 1.22 over the plotted √s range, with event-by-event 1σ of ≈ ±0.07–0.09. Junctions per unit λ rise from ≈ 0.009 to ≈ 0.021 (Fig. 12; log rise attributed to BFKL gluon growth, p. 23).
  - In r₀ at 900 GeV, ⟨h⟩ saturates at ≈ 1.22 for r₀ ≳ 1.5–2 fm, when strings become larger than the proton (Fig. 13; p. 24). Near r₀ ≈ 1 fm, small r₀ changes move ⟨h⟩ by up to 5%, the largest expected uncertainty (p. 25).
  - In m₀ from 0.05 to 0.25 GeV, ⟨h⟩ goes from ≈ 1.09 to ≈ 1.17 (Fig. 14).
  - Results have "very little sensitivity" to β (p. 24, no figure shown).
  - Changes in the rope tension can be compensated by changes in r₀ (p. 13).
- **Flow-like effects and high-p⊥ tails (Fig. 15, p⊥ in |y| < 2).**
  - At 7 TeV, the swing alone already lowers the high-p⊥ tail of p/π relative to DIPSY. Full Rope raises the ratio to a ≈ 0.37 plateau that stays flat out to 8 GeV.
  - A modified "Pipe" variant switches ropes off (κ̃/κ = 1) for strings with any parton or hadron at |y| < 2 and p⊥ > 4 GeV. It peaks at ≈ 0.31 near 1.5 GeV and then falls to ≈ 0.2, closer in shape to the expected data trend.
  - However, Pipe's √s dependence is "not nearly as good" as the dipole scheme's (pp. 26–27).
  - The authors cite Ortiz et al. [80] for flow-like effects from Pythia CR (p. 26).
- **K/π (Fig. 16).** There is only a small rope effect and no intermediate-p⊥ bump, consistent with ALICE [81] according to the authors (p. 27).
- **e⁺e⁻ (App. D.1, Fig. 18).** Thrust is equally well described with and without the swing. The out-of-plane p⊥ tail improves with the swing: MC/data ≈ 0.75 vs ≈ 0.6 at the highest bins (read from Fig. 18). The total χ²/Ndf is "somewhat improved". Ropes give no change in the tuned LEP observables (p. 41).
- **DIPSY limitations (App. D.2).**
  - Charged-particle p⊥ spectra are too hard above a few GeV: MC/data > 1.4 above ≈ 3 GeV (Figs. 19–20). There are no hard matrix elements and no quarks in the evolution.
  - The √s dependence of multiplicity is too flat, so separate per-energy tunes were also made. Results shown use the global tune, since the ratios were insensitive to the choice (p. 41).
- **Pythia diffraction check (Fig. 22).** Including diffraction lowers the Λ dN/dy normalization: MC/data ≈ 0.55 vs ≈ 0.7 non-diffractive only. Λ/K⁰_S is unchanged at ≈ 0.7 of the data (read from Fig. 22).
- **Conclusions (pp. 28–29).** The authors list several sources of flow-like behaviour: plasma; rope tension; CR into low multiplets; and transverse expansion from rope pressure, which is neglected here. They call for pp/pA/AA studies of angular flow, fluctuations and correlations to separate these sources. They claim "rather firm predictions" for LHC Run 2.

## Assessment
- **Key model for the RQ1 small-system debate.** It shows that strangeness and baryon enhancement in pp, and part of the low-p⊥ "radial-flow-like" baryon/meson rise, can come from string-overlap and CR mechanisms without a QGP. It is the precursor of Pythia 8 rope hadronization and string shoving (Bierlich:2017vhg).
- **Evidence is ratio-based and limited in scope.**
  - Only identified-particle ratios in min-bias events at 0.2–7 TeV are compared. There is no multiplicity-binned comparison, which is the observable that later became decisive (ALICE 2017 strangeness vs multiplicity).
  - There is no azimuthal or flow observable and no comparison with Pythia CR modes beyond 4C.
  - Agreement is qualitative: no χ² is given, and the new parameters are "set to reasonable physical estimates" rather than tuned (p. 22).
- **The high-p⊥ failure is significant.** The rope Λ/K⁰_S keeps rising where data fall (Fig. 8). The fix (Pipe + p⊥ > 4 GeV cut) is ad hoc and spoils the √s behaviour. Since DIPSY's own p⊥ spectrum is too hard (Figs. 19–20), part of the high-p⊥ mismodelling may come from the generator rather than the rope concept. The authors do not disentangle the two.
- **Approximations change multiplicity and kinematics.** Strings are fragmented one at a time. The pipe scheme deletes strings, violating energy-momentum conservation (p. 37). The dipole scheme converts gluon pairs to diquarks to fake junctions. These are implementation approximations, not physics.
- **Internal inconsistencies.**
  - App. C.2 says m₀ ∝ 1/r₀ ~ 0.2 GeV (p. 38). The results use m₀ = 0.135 GeV (p. 20), and p. 25 says 1/r₀ ≈ 0.2 GeV gives worse √s dependence.
  - The Fig. 14 caption says "as a function of r₀" for the right panel, but the axis is m₀.
  - Fig. 11's caption mentions "Ξ⁻ to ΛΛ̄" and "ΛΛ̄ to K⁰_s", so the exact ratio definitions there are slightly ambiguous.
- **Theoretical uncertainty acknowledged by the authors.** The Casimir scaling is for isolated static ropes. Surrounding strings or bag pressure could change the tension (pp. 12–13). Rope pressure and expansion is neglected (p. 29).
- **Connections to the CR literature.** The final-state swing is a λ-minimising CR in the ARIADNE lineage (Lönnblad 1996). It is conceptually close to Pythia QCD-CR (Christiansen:2015yqa): both use 1/N_c² colour-index matching and junction-like baryon production. This paper adds spatial (impact-parameter) information. Disentangling "CR" from "rope" contributions to flow-like effects remains open; the authors say both contribute (p. 29).

## Leads
- Biró, Nielsen, Knoll, Nucl. Phys. B 245 (1984) 449 (Biro:1984cf): the original colour-rope random-walk model the paper builds on.
- Ortiz Velasquez et al., PRL 111 (2013) 042001, arXiv:1303.6326 (OrtizVelasquez:2013ofg): CR producing flow-like patterns in pp; directly relevant to "CR vs. ropes vs. flow".
- CMS, JHEP 05 (2011) 064, arXiv:1102.4282 (CMS:2011jlm): strange-particle ratios at 0.9 and 7 TeV, the key data here.
- STAR, Phys. Lett. B 637 (2006) 161, nucl-ex/0601033: identified p/π at 200 GeV used in Fig. 8.
- Bierlich, Gustafson, Lönnblad, "Collectivity without plasma in hadronic collisions", PLB 779 (2018), arXiv:1710.09725 (Bierlich:2017vhg): follow-up adding string shoving (the rope "pressure" this paper neglects); found via lookup, not cited here.
- Lönnblad, Z. Phys. C 70 (1996) 107: the ARIADNE colour-reconnection model behind the final-state swing.
- Andersson, Henning, Nucl. Phys. B 355 (1991) 82: alternative rope fragmentation (early breakup, multiplicity).
- Flensburg, Gustafson, Lönnblad, JHEP 08 (2011) 103, arXiv:1103.4321: DIPSY final states; needed to judge the generator underlying the rope results.
- Bali, PRD 62 (2000) 114503, hep-lat/0006022: lattice Casimir scaling of the flux-tube tension; the basis of κ_rope ∝ C₂.
- Werner, Guiot, Karpenko, Pierog, arXiv:1411.1048 (Werner:2014xoa): EPOS core–corona, the competing "plasma in pp" explanation cited for high-p⊥ behaviour.
- ALICE, PLB 736 (2014) 196, arXiv:1401.1250 (ALICE:2014juv): identified π/K/p at large p⊥, cited for the absence of a K/π bump.
- Forward citations (295): expect the Pythia 8 rope implementation, the multiplicity-dependent strangeness comparisons, and pA/AA rope studies. Recommend `citing 1335149 --filter "t rope"`.
