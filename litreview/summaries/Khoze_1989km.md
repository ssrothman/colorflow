# A Phenomenological Investigation of the String Effect
- **ID / links:** Khoze:1989km · INSPIRE 282018 · arXiv — · DOI 10.1016/0370-2693(90)91498-Z
- **Authors / collab, year, journal:** V. Khoze (LNPI Leningrad), L. Lönnblad (Lund), 1990, Phys. Lett. B 241 (1990) 123–126 (received 17 Jan 1990)
- **Type:** MC/model (phenomenology)
- **Relevance:** 3 · RQs: 1b, 2, 4
- **Full text source:** zotero (4 pp. scan; the text layer is OCR-garbled, so everything was read from page images. Fig. 2 symbols and axis values are small; numbers read off Fig. 2 are approximate and marked "≈")

## Takeaways
- The paper is an MC comparison of **ARIADNE 3.0 dipole cascade + JETSET 6.3 string fragmentation** against **JETSET string fragmentation only**, on a fixed three-fold symmetric qq̄g state (120° between jets, Fig. 1). The string effect is r = ⟨N₂⟩/⟨N₁⟩, with region 1 between q and q̄ and region 2 between q and g (p. 124). Main claim: "the perturbative phase … quickly becomes dominant as energy increases" (abstract, p. 123).
- **Discriminating signature 1: dependence on hadron mass M_H and p_out.** At lower energies r has "a fairly linear dependence" on M_H and p_out (Fig. 2a,b, p. 125). This is a Lorentz-boost effect of the azimuthally symmetric string fragmentation function (pp. 123, 125). With the dipole cascade added, these dependences are "drastically reduced already for LEP energies" (Fig. 2a,b, p. 125). At high energy r becomes independent of M_H and p_out (Fig. 2c). Without the cascade it stays species-dependent at all energies (Fig. 2d).
- **Energy dependence.** With the cascade, r₁ falls with energy: 2.74 (30 GeV) → 2.38 (93 GeV) → 2.13 (750 GeV). String-only gives 2.69 → 2.99 → 2.89 (Tab. 3). At 30 GeV the two approaches give nearly the same r₁, so the all-particle ratio alone cannot separate them at PETRA energies.
- **Discriminating signature 2: "string interaction" / antenna screening.** Take the double-inclusive ratio r₂ = ⟨N₂N₃⟩/⟨N₁N₃⟩, i.e. require extra flow in the g–q̄ valley.
  - Perturbative QCD predicts r₂ < r₁ because of "spill-over" between regions 2 and 3, plus a small O(1/N_c²) term. Asymptotic values are r₁ = 2.42 and r₂ = 2.06 (ref. [11] DKT 1988, p. 126).
  - The string model treats the two strings as uncorrelated, so r₂ ≈ r₁.
  - MC (Tab. 3): with the cascade, r₂ < r₁ already at 30 GeV (2.52 vs 2.74). String-only gives r₂ = r₁ within 0.02 at all energies.
- **Proposed LEP measurement (p. 126).** Measure r vs M_H and p_out, and r₂ vs r₁, with the gluon jet identified by heavy-quark (cc̄g, bb̄g) tagging or by leading-particle rapidity / jet broadness.

## Setup
- **Partonic state.** A fixed three-fold symmetric qq̄g configuration (all inter-jet angles 120°). Regions 1 (q–q̄), 2 (q–g) and 3 (g–q̄) are drawn in Fig. 1 as angular sectors between the jets; the figure marks 60° angles, which we read as the central 60° of each 120° gap. The paper says these events are "with smearing due to misidentification of jet species" (p. 124). How this smearing is implemented is not described.
- **MC programs.**
  - ARIADNE 3.0 colour-dipole cascade (Gustafson–Pettersson dipole formulation), which "includes the main part of the relevant QCD coherence phenomena" and can shower any string-ordered parton state (p. 124).
  - JETSET 6.3 string fragmentation (p. 124).
  - g → QQ̄ splitting is switched off. Including it lowers r slightly at very high energy, by less than the few-percent parameter uncertainty (p. 125).
- **Parameters (Tab. 2).**
  - Cascade + fragmentation: Λ = 0.25 GeV, p⊥ cut 0.50 GeV, a = 0.50, b = 0.75 GeV⁻², σ = 0.35 GeV.
  - Fragmentation only: a = 1.50, b = 0.50 GeV⁻², σ = 0.35 GeV.
  - Varying the parameters within ranges that fit event shapes and p_t data (ref. [13], Petersen et al. PRD 37 (1988) 1) changes results by no more than "a few percent" (p. 125).
- **Energies.** E_CM = 30, 45, 75, 93, 750 GeV (Tab. 3). Fig. 2c,d extends to ~500 GeV.
- **Observables.**
  - r = ⟨N₂⟩/⟨N₁⟩ for all hadrons, π, K, p, and for p_out > 0.3 GeV (Fig. 2 legend: r_all "+", r_π filled circle, r_K "×", r_p diamond, r(p_out > 0.3 GeV) open circle; the π and p symbols are hard to tell apart in the scan, but the p series is the uppermost in Fig. 2c,d).
  - r₁ = ⟨N₂⟩/⟨N₁⟩ and r₂ = ⟨N₂N₃⟩/⟨N₁N₃⟩ (p. 125).
- **Reference values.** MLLA+LPHD predictions for r in this geometry, from DKT ref. [11] (Tab. 1): r = 2.75, 2.71, 2.64 at E_CM/Λ = 90, 150, 1500.

## Results
- **Mass dependence (Fig. 2a).** At 30 GeV, r rises from ≈ 2.2 for pions (≈ 4 for kaons) to ≈ 8.5 at M_H ≈ 1 GeV (protons). At 93 GeV it rises only to ≈ 3.4. These are approximate plot readings; error bars are visible on the heavy-hadron points.
- **p_out dependence (Fig. 2b).** At 30 GeV, r rises from ≈ 2.3 to ≈ 5.5 across the plotted range. At 93 GeV it rises from ≈ 2.1 and levels off at ≈ 2.9 (approximate). The horizontal axis label is partly illegible ("Pout" with a possible superscript 2, in GeV).
- **Energy evolution with the cascade (Fig. 2c).** The species and p_out curves converge with energy to r ≈ 2–2.5 by a few hundred GeV (approximate reading). The steepest fall is for the heavy-hadron series, from ≈ 8.5 at the lowest plotted energy.
- **Energy evolution without the cascade (Fig. 2d).** The separation between series persists out to 500 GeV: the top series is at ≈ 6.5–8 (central values; error bars reach ≈ 8.8), the others at ≈ 2–4.5 (approximate).
- **Authors' conclusion (p. 125).** "The perturbative phase becomes dominant already at fairly low energies."
- **r_all vs MLLA (p. 125).** r_all decreases with energy, as in the perturbative calculation (Tab. 1). The authors say the absolute values are not directly comparable, for three reasons:
  - r_all should lie below MLLA because of non-asymptotic effects, partly light resonance-decay products not in LPHD (as explained in ref. [10] = Azimov:1985zta);
  - the dipole approximation drops the O(1/N_c²) negative q–q̄ term, which should make the MC r_all *lower* than MLLA;
  - the general behaviour should be unaffected.
- **Table 3:**

  | E_CM (GeV) | 30 | 45 | 75 | 93 | 750 |
  |---|---|---|---|---|---|
  | dipole + frag, r₁ | 2.74 | 2.65 | 2.43 | 2.38 | 2.13 |
  | dipole + frag, r₂ | 2.52 | 2.38 | 2.12 | 1.97 | 1.74 |
  | frag only, r₁ | 2.69 | 2.94 | 3.01 | 2.99 | 2.89 |
  | frag only, r₂ | 2.69 | 2.94 | 2.99 | 2.97 | 2.90 |

- **Origin of r₂ < r₁ in ARIADNE (p. 126).** The dipole cascade does not include the 1/N_c² string-interaction term, so r₂ < r₁ there comes from perturbative spill-over only. The DKT asymptotic values are r₁ = 2.42, r₂ = 2.06, i.e. r₂/r₁ ≈ 0.85 (our arithmetic). ARIADNE gives r₂/r₁ ≈ 0.83 at 93 GeV and 0.82 at 750 GeV (our arithmetic from Tab. 3).
- **Statistics.** No MC statistical errors are given in Tab. 3. Event counts are not stated.

## Assessment
- **What this paper adds.** It is the first quantitative statement of *how to tell the two string-effect mechanisms apart*. Andersson:1980vk and Azimov:1985zta agree on the sign and rough size of the q–q̄ depletion, and Azimov et al. note that at leading N_c the two pictures share the "2 + 2 boosted dipoles" structure. Khoze & Lönnblad identify two discriminants:
  - the M_H and p_out dependence of r and how it evolves with energy (a boost-of-string signature that the cascade washes out);
  - the double-inclusive r₂/r₁ (antenna screening, absent in independent strings).

  Both are pure MC statements, with no data comparison.
- **The comparison is not clean.**
  - The fragmentation-only and cascade setups use different Lund a, b parameters (Tab. 2), each tuned separately.
  - The partonic state is an idealised fixed symmetric configuration. "Fragmentation only" at 750 GeV is a strawman: no realistic model lacks a shower.
  - The real question, how much of the *measured* r at a given energy comes from the shower vs the string, is answered only within ARIADNE+JETSET. ARIADNE's dipoles are themselves leading-colour, string-ordered objects, so the "perturbative" r here already inherits the string colour topology. The comparison is really "string topology with vs without a perturbative cascade", not "string vs coherent pQCD".
- **The r₂ < r₁ signal in ARIADNE comes from spill-over, not from the 1/N_c² string interaction.** The authors state the latter is not in the dipole scheme. So a measured r₂ < r₁ would test the cascade's angular spread, not colour-suppressed interference. The name "string interaction" for the observable can mislead.
- **Prior settings.** The low-energy degeneracy (r₁ ≈ 2.7 for both at 30 GeV, Tab. 3) is consistent with Azimov:1985zta, where PETRA data could not discriminate. The fall of r₁ with energy in the cascade model is a falsifiable LEP prediction. Whether LEP1 found r falling toward ~2.4 and M_H/p_out-independent should be checked against the LEP string-effect papers in the queue (e.g. ALEPH:1999ad, Kneringer:1995wh, Duchesneau:1994gi). The OPAL 1991 tagged measurement (OPAL_1991xwi) uses a different geometry (ψ ≈ 130–170°), so its R̃ = 1.62 ± 0.07 is not directly comparable with r here.
- **Reliability of our reading.** Fig. 2 numbers are approximate plot readings from a small scan. Only the Tab. 1–3 values should be cited quantitatively.

## Leads
- Yu.L. Dokshitzer, S.I. Troyan, V.A. Khoze, Sov. J. Nucl. Phys. 47 (1988) 881 (ref. [11]). The MLLA predictions of r (Tab. 1) and of the double-inclusive "string interaction / antenna screening" r₂ (asymptotic r₁ = 2.42, r₂ = 2.06). Not found in the DB; high priority for RQ2/RQ4.
- G. Gustafson, Phys. Lett. B 175 (1986) 453 (= Gustafson:1986db, queued) and G. Gustafson & U. Pettersson, Nucl. Phys. B 306 (1988) 746 (= Gustafson:1987rq, queued). The colour-dipole cascade formulation underlying ARIADNE; needed to judge what coherence it includes or omits (the 1/N_c² term).
- L. Lönnblad, ARIADNE 3, LU TP 89-10 (1989); successor ARIADNE 4 (Lonnblad:1992tz, queued). Program reference.
- Yu.L. Dokshitzer, V.A. Khoze, S.I. Troyan, A.H. Mueller, Rev. Mod. Phys. 60 (1988) 373 (= Dokshitzer:1987nm, already read) and Dokshitzer, Khoze, Troyan, in Perturbative QCD, ed. A.H. Mueller (World Scientific 1989) p. 241 (= Dokshitzer:1988bq, queued). The MLLA/coherence reviews (ref. [2]); the book chapter likely contains the string-effect and antenna-screening results in detail.
- H. Aihara et al. (TPC), Z. Phys. C 28 (1985) 31 (ref. [9]; likely TPCTwoGamma:1984tkq, queued) and JADE Z. Phys. C 21 (1983) 37 (ref. [8]; likely JADE:1983ihf). The experiments that confirmed the M_H / p_out growth of r at PETRA/PEP.
- A. Petersen et al. (MARK II), Phys. Rev. D 37 (1988) 1 (= Petersen:1987bq, rejected as generic event shapes). Used here only as the tuning data, so the rejection stands.
- W. Hofmann, Lepton–Photon 1987 (Hamburg) proceedings p. 671. Experimental review of the string effect and perturbative-phase evidence. Possible review lead.
