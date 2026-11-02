# A spatially constrained QCD colour reconnection in pp, pA, and AA collisions in the Pythia8/Angantyr model
- **ID / links:** Lonnblad:2023stc · INSPIRE 2644568 · arXiv 2303.11747 · DOI 10.1140/epjc/s10052-023-11778-3
- **Authors / collab, year, journal:** L. Lönnblad, H. Shah (Lund), 2023, Eur. Phys. J. C (2023), DOI above. Read from arXiv v2, 7 Jul 2023.
- **Type:** MC/model
- **Relevance:** 2 · RQs: 1, 2
- **Full text source:** arxiv

## Takeaways
- This paper introduces a transverse-distance cut on QCD-based colour reconnection (QCD-CR, Christiansen–Skands): dipoles whose impact-parameter midpoints are more than δb_c apart may not reconnect. The cut is now the Pythia parameter `ColourReconnection:dipoleMaxDist`. It allows the first CR across different NN sub-collisions in Angantyr pA/AA events, which previously hadronised independently (pp. 2–6, Fig. 1).
- In pp, the constraint reduces CR, which raises multiplicity and flattens ⟨p⊥⟩(N_ch) (Fig. 8, Tab. 2). A retune (p⊥0^ref 2.12→2.37, m₀ 2.9→1.05 GeV, C_j 1.43→1.37, δb_c = 0.5 fm; Tab. 3) restores ⟨N_ch⟩ and ⟨p⊥⟩(N_ch) (Fig. 11). However, the high-N_ch tail drops too fast and the p⊥ spectrum becomes too hard (Fig. 12, p. 14).
- With δb_c = 7 fm (almost global CR) and no retune, mean multiplicity drops by about 10% in PbPb and about 5% in pPb, against +20% and +10% with CR switched off (Fig. 10, p. 13). After tuning, central PbPb multiplicity is still about 20% too low (Fig. 17, p. 18). Global CR makes the PbPb p⊥ spectra worse in central collisions (Fig. 18).
- Junction CR overproduces protons. p/π is far above ALICE in pp and pPb (≈0.1 vs ≈0.055; Figs. 13, 16). Λ/π, Λ/K⁰_S and partly Ξ/π, Ω/π improve over default Pythia, with a multiplicity dependence similar to rope hadronization. Multi-strange baryons are still well below the data (Figs. 13–14, 16; p. 15, p. 20).
- Physics message: spatially local CR across sub-collisions is a candidate microscopic source of collective-like effects in AA, alongside shoving, ropes and rescattering. The model is a "first attempt" and "quite naive" (p. 20). No flow observables are studied.

## Setup
- **Generator.** Pythia 8 with Angantyr (Glauber–Gribov stacking of pp-like sub-collisions; primary vs secondary non-diffractive (SND) events, p. 1–2). QCD-CR mode 0 (Tab. 1). CR candidates are swings (1/9 colour probability), junction–antijunction pairs from 2 dipoles (2/9 in implementation, 1/3 in SU(3)), and 3-dipole junctions (2/81 vs 1/27). Junction suppression is compensated by C_j through m₀j = C_j m₀. A reconnection is accepted only if the λ-measure decreases (Eq. 3; junction–junction piece Eq. 4) (pp. 4–5, 9–10, Fig. 2).
- **Spatial constraint.** Each dipole's transverse position is the midpoint of its two partons. Dipoles are assumed roughly parallel to the beam, without full 3+1D space-time (p. 6). δb_c also restricts 3-dipole junctions: all pairs must be within δb_c (p. 7).
- **Technical changes.** Improved junction hadronization, so that failed junction systems no longer veto events and skew high-N_ch tails (pp. 6, 21–23; Figs. A1, A2; new "MiniJunct2Hadrons"/"MiniJunct2Baryons"). No CR for dipoles containing diquarks in pA/AA. Beam-remnant junctions enabled (p. 22, Tab. 4).
- **SND sub-collisions.** Pomeron flux changed to Berger–Streng form with ε_pom tuned to −0.04, giving higher SND multiplicity to compensate for CR (Eq. 5, Fig. 9, pp. 11–13, Tab. 4).
- **Data.** pp 7 TeV: CMS NSD multiplicity, ⟨p⊥⟩(N_ch); ATLAS MB η, p⊥, N_ch; ALICE strangeness-enhancement ratios. pPb 5.02 TeV: ATLAS dN/dη in centrality bins; ALICE p/π and Λ/π. PbPb 2.76 TeV: ALICE dN/dη(centrality), N_part; ATLAS p⊥ spectra (refs. [26,27,33,34,36,38–40]).
- **Tuning.** Done by hand, not with Professor (p. 13). Only p⊥0^ref, m₀, C_j, δb_c in pp, then ε_pom in pPb. AA has no further tuning (p. 7).

## Results
- **Parameter scans, pp 7 TeV vs CMS (Figs. 4, 6–8; Tab. 2).**
  - Lowering p⊥0^ref adds MPIs: multiplicity goes up and ⟨p⊥⟩ goes down (Fig. 4).
  - Raising m₀ removes small dipoles from CR (they are collapsed to pseudo-particles, Fig. 5), so multiplicity goes up. m₀ = 0.3 GeV gives too high ⟨p⊥⟩(N_ch) by about 10–20%. m₀ = 4 GeV gives too low (Fig. 6).
  - C_j < 1 increases multiplicity. C_j has a weaker effect than m₀ (Fig. 7, p. 10).
  - Reducing δb_c to 0.3 fm "reduce[s] the CR significantly", raises the high-N_ch tail and flattens ⟨p⊥⟩(N_ch). At 0.3 fm ⟨p⊥⟩ is about 10–15% below CMS at high N_ch (read off Fig. 8). δb_c = 1 fm is already large enough that the spatial effect vanishes in pp (Fig. 3, p. 6).
- **Junction handling alone (Fig. 3).** The improved junction hadronization at large δb_c (1 and 5 fm) raises the high-N_ch tail well above CMS. The authors say QCD-CR must be retuned anyway (p. 6).
- **Tuned pp (Tab. 3; Figs. 11–14).**
  - η distributions and ⟨p⊥⟩(N_ch) agree with ATLAS and CMS. SC-CR ⟨p⊥⟩ is a few % low at large N_ch (Fig. 11).
  - ATLAS N_ch distribution falls too fast above N_ch ≈ 40 (MC/data ≈ 0.6–0.7 at N_ch ≳ 70, read off the figure). Default Pythia overshoots by up to about 30% at N_ch ≈ 50–60.
  - SC-CR p⊥ spectrum is about 20% low at 1–2 GeV and >30% high above about 10 GeV (Fig. 12, read off the figure). The authors attribute this to the tuning choices: lower m₀, higher p⊥0^ref (p. 14).
  - Strangeness ratios vs ⟨dN/dη⟩ (ALICE): p/π about 0.08 rising to about 0.11 vs data ≈0.055; default Pythia ≈0.06 (Fig. 13). Λ/π and Λ/K⁰_S approach the data; default is about 30% low (Fig. 13). Ξ/π and Ω/π increase over default but stay well below data (Fig. 14). All values read off the figures. The authors note that pp ratios are insensitive to the spatial constraint (p. 15).
- **Unretuned CR effects in pA/AA (Fig. 10, p. 13).** Compared with default Angantyr (CR only within sub-collisions), switching CR off gives +20% (PbPb) and +10% (pPb) mean multiplicity. Global CR (δb_c = 7 fm) gives −10% and −5%. The effects are strongest in the highest-multiplicity tails.
- **pPb 5.02 TeV (Figs. 15–16).** SC-CR with ε_pom = 0 seriously underestimates dN/dη in central bins. ε_pom = −0.04 improves this but is still low for 0–1%, and tends to overshoot peripheral bins (p. 17). p/π is about 0.10–0.105 vs data ≈0.055 at all centralities. Default Angantyr gives about 0.06. Λ/π improves from about 0.022 (default) to about 0.03–0.035 vs data about 0.03–0.04 (Fig. 16, read off the figure).
- **PbPb 2.76 TeV (Figs. 17–18).** Central multiplicity is about 20% low with SC-CR. Peripheral bins are less affected. N_part agrees with ALICE Glauber for all setups (Fig. 17). The authors attribute the limited PbPb effect to δb_c restricting CR when sub-collisions are spread in b (p. 18). p⊥ spectra in 0–5% get worse and in 60–80% the high-p⊥ tail improves somewhat (Fig. 18). Baryon/meson ratios are deliberately not shown for PbPb because multiplicity is not reproduced (p. 20).
- **Outlook (p. 20–21).** Planned next steps: make δb_c depend on dipole density or parton p⊥; consider the perturbative swing for HI; combine with ropes, shoving and rescattering; then study flavour and collectivity in pp, pA, AA.

## Assessment
- This is a model and implementation paper (with a Pythia-release technical appendix), not a test of collectivity. It matters for RQ2 because it documents the current Pythia option (`dipoleMaxDist`) for space-time-local CR. It also shows a clear trade-off: spatial locality weakens CR in pp, and the ⟨p⊥⟩(N_ch) slope then has to be recovered by retuning, at the cost of the N_ch tail and the p⊥ spectrum.
- The quality of the tune is limited. It is done by hand with 4 parameters, flavour parameters are left at QCD-CR mode-0 values, and the authors call it "a bit naive" (p. 14). The δb_c = 0.5 fm value is a compromise between pp (favouring larger) and pA (favouring smaller) (p. 13), so it is not a measurement of a physical CR range.
- The geometry is simplistic. Midpoint position in the transverse plane ignores longitudinal and time separation, and the authors acknowledge this (p. 6). The value of δb_c relative to the proton radius (~0.8–0.9 fm) and string width is not discussed in detail.
- The proton overproduction from junction CR (p/π ≈ 2× data in pp and pPb) is a significant tension with QCD-CR as used here. It is relevant when CR models are used to explain baryon enhancement (cf. Bierlich & Christiansen 2015). Ortiz Velasquez et al. 2013 used the MPI-based CR instead, so the two should not be compared directly.
- The paper does not compute flow coefficients or ridge observables, so it gives no direct evidence on CR-driven collectivity in AA.

## Leads
- Christiansen & Skands, "String formation beyond leading colour", JHEP 08 (2015) 003, arXiv:1505.01681. Defines QCD-CR, the base model here (ref. [17]).
- Bierlich & Christiansen, "Effects of color reconnection on hadron flavor observables", Phys. Rev. D 92 (2015) 094010, arXiv:1507.02091. QCD-CR effects on baryon/strangeness ratios vs multiplicity (ref. [41]).
- Bierlich, Gustafson, Lönnblad, Shah, "The Angantyr model for heavy-ion collisions in Pythia8", JHEP 10 (2018) 134, arXiv:1806.10820. The base HI framework (ref. [6]). Context for SND treatment and no-cross-talk default.
- Bierlich, Chakraborty, Gustafson, Lönnblad, "Strangeness enhancement across collision systems without a plasma", Phys. Lett. B 835 (2022) 137571, arXiv:2205.11170. Rope hadronization comparison (ref. [35]).
- Bierlich, Chakraborty, Gustafson, Lönnblad, "Setting the string shoving picture in a new frame", JHEP 03 (2021) 270, arXiv:2010.07595. The Lund alternative for flow-like effects (ref. [11]).
- Bierlich, Gustafson, Lönnblad, Tarasov, "Effects of overlapping strings in pp collisions", JHEP 03 (2015) 148, arXiv:1412.6259. Ropes (ref. [12]). Also mentions the perturbative swing for HI CR (p. 21).
- L. Lönnblad, "Reconnecting coloured dipoles", Z. Phys. C 70 (1996) 107. Swing/dipole CR origin, suggested for HI (ref. [23]).
- Gustafson & Häkkinen, Z. Phys. C 64 (1994) 659, and Friberg, Gustafson & Häkkinen, Nucl. Phys. B 490 (1997) 289, arXiv:hep-ph/9604347. LEP-era CR in WW and e⁺e⁻ (refs. [22, 24]).
- Sjöstrand & Utheim, EPJC 80 (2020) 907, arXiv:2005.05658, and Bierlich, Sjöstrand & Utheim, EPJA 57 (2021) 227, arXiv:2103.09665. Hadronic rescattering in pp/pA/AA, which raises central multiplicity and could offset the CR reduction (refs. [14, 15]).
- Forward: later Shah/Lönnblad papers applying SC-CR to flavour and collectivity in pp, pA, AA (promised on p. 21). Check INSPIRE citations (23).
