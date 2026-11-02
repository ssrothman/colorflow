# Multiple interactions and the structure of beam remnants
- **ID / links:** Sjostrand:2004pf · INSPIRE 644134 · arXiv hep-ph/0402078 · DOI 10.1088/1126-6708/2004/03/053
- **Authors / collab, year, journal:** T. Sjöstrand, P. Z. Skands (Lund), 2004, JHEP 03 (2004) 053; LU TP 04-08
- **Type:** MC/model
- **Relevance:** 2 · RQs: 1, 2, 4
- **Full text source:** arxiv

Page numbers below are the printed page numbers. The PDF page is the printed number + 1.

## Takeaways
- This is the founding paper of the "new" Pythia 6.3 MPI framework. Several MPIs, each with its own ISR/FSR, are generated in falling p⊥. Beam remnants can have any structure: several valence quarks kicked out, sea quarks with "companion" antiquarks. Baryon number is carried by a **string junction**, so a junction-fragmentation model is needed (Secs. 4–5, pp. 20–48).
- **Colour flow between MPIs and the remnant is not fixed by perturbation theory.** With n gluons kicked out there are n! planar orderings even in the N_C → ∞ limit. These correlations arise below the shower cutoff Q₀ ~ 1 GeV (p. 40). The paper tries three initial-state orderings: random, rapidity-ordered (Δy, Eq. 67) and string-length-ordered (Δλ, Eq. 68).
- **Key negative result:** none of these initial-state colour assignments reproduces the rise of ⟨p⊥⟩(n_ch) that Tune A (and data) show. All three stay nearly flat at about 0.41–0.43 GeV out to N_ch = 150, while Tune A reaches about 0.56 (Fig. 20). The authors conclude that the colour flow "cannot be correctly described by merely arranging the colour lines present in the initial state" (p. 46). **Final-state** colour rearrangements are needed.
- **A crude final-state CR model** (Sec. 5.3, pp. 47–48) swaps colour tags at random when this lowers λ (Eqs. 69–70), with strength F. It is the precursor of the later "colour annealing" models, but the term "annealing" does not appear in this paper. With F = 1 the slope of ⟨p⊥⟩(n_ch) overshoots Tune A (Fig. 21). In the three benchmark models (Ran/Rap/Lam, Tab. 1) there are about 18–20 reconnections per Tevatron min-bias event and about 45–52 at the LHC, which is below 10% of the possible swaps (p. 50). The authors stress that this is "not … evidence for the existence of colour reconnections", only proof that changing colour structure can reach the data (p. 48).
- **Junctions and baryon-number flow.** In the new model the beam baryon number migrates to central rapidities ("baryon stopping"; Figs. 11, 26, 32). Junction baryons can carry more strangeness, with |S| = 3 possible, which is impossible in the old model (Fig. 27). The authors relate this to the heavy-ion observation Ω⁻/Ω̄⁺ > 1 (p. 54) and propose baryon-minus-antibaryon rapidity distributions as a probe (p. 54). ⟨p⊥⟩(n_ch) is promoted as "a prime test for any physical model of the colour flow" (p. 55).

## Setup
- **Collisions.** p p̄ at 1.8 TeV (Tevatron) and pp at 14 TeV (LHC). Min-bias = inelastic non-diffractive. Pure MC study: the only data comparisons are UA5/E735 multiplicity distributions in the impact-parameter section (Figs. 6–7). Everything else is compared with Pythia 6.2 "Tune A" (R. D. Field), used as a stand-in for CDF data (p. 11, p. 61).
- **MPI basics (brief).**
  - 2 → 2 QCD with a smooth regulator at p⊥0 (Eq. 7); p⊥0 ∝ E_cm^0.25 (p. 11).
  - Interactions are generated in falling p⊥ with a Sudakov-like form factor (Eq. 8).
  - Impact-parameter overlap O(b): the new option is O(b) ∝ exp(−b^d), "ExpOfPow" (Eq. 18). Tune A's double Gaussian ≈ ExpOfPow(d = 1.35) (p. 15). The new benchmark models use ExpOfPow(1.8) (p. 50).
- **PDF / remnant details (brief).**
  - Rescaled PDFs after each interaction (Eq. 20).
  - Valence distributions are depleted when a valence quark is used, and sea quarks get a companion distribution q_c(x; x_s) from g → q q̄ (Eqs. 25–38).
  - The sea + gluon normalisation a absorbs the momentum sum rule (Eq. 44).
  - Remnant composites (diquark, baryon or meson) are formed under four alternative rules (Fig. 10, p. 28).
  - Primordial k⊥ width σ(Q) = max(σ_min, σ∞/(1 + Q½/Q)) (Eq. 45). The fit uses 0.36 GeV (fragmentation), 0.9 GeV (EMC) and 2 GeV (Tevatron Z p⊥), giving σ∞ = 2.1 GeV and Q½ = 7 GeV (Eq. 46).
  - The k⊥ recoil is shared uniformly, by nearest colour neighbours, or along colour chains (p. 30).
- **Hadronisation.**
  - Lund strings in the planar N_C → ∞ picture (p. 35).
  - Junction topologies use the Sjöstrand–Skands 2003 BNV junction fragmentation. The junction motion is set by an effective "pull" (Eq. 66), with E_norm ≈ 1.5 GeV (p. 37).
  - Two legs are fragmented outside-in, then a diquark is formed and the last (highest-energy) leg is fragmented (p. 38).
  - Junction–antijunction systems are either kept or annihilated into two q q̄ strings, whichever has the minimal string length (Fig. 15, p. 39).
- **Benchmarks (Tab. 1).**
  - Ran: random IS ordering, p⊥0 = 2.50 GeV, F = 0.55.
  - Rap: Δy ordering, p⊥0 = 2.40 GeV, F = 0.55.
  - Lam: Δλ ordering, p⊥0 = 2.30 GeV, F = 0.65.
  - Each is tuned to Tune A's ⟨n_ch⟩ = 49.5 ± 0.5 at the Tevatron (Fig. 22).
  - Attachments that break up the remnant are suppressed by a relative factor 0.01 (p. 51).

## Results
**MPI context and evidence (Sec. 2).**
- **Old Pythia MPI colour recipes.** For interactions after the first there were three options (p. 7):
  - gg → gg as a colour-singlet closed gluon loop (roughly maximal string length);
  - gg → gg attached to existing strings so as to minimise the increase in string length;
  - gg → q q̄ as a singlet.
- **Tune A** uses PARP(85) = 0.9 and PARP(86) = 0.95, so almost all subsequent interactions are minimal-string-length gg (p. 11). The authors say that about 90% of the time Tune A picks gg → gg with colour flow chosen to minimise string length, so each extra interaction adds little multiplicity (p. 19). This is the reason Tune A gets a steep ⟨p⊥⟩(n_ch).
- **Why ⟨p⊥⟩(n_ch) probes colour.** Each new interaction must add proportionally less to n_ch than to Σp⊥. Whether it does "strongly depends on the colour connections between the interactions, i.e. whether strings tend to connect nearest neighbours in momentum space or run criss-cross in the event" (p. 11). Longer strings mean more n_ch per MPI, so fewer MPIs (larger p⊥0) are needed to match ⟨n_ch⟩, and ⟨p⊥⟩(n_ch) is flatter (p. 46).
- **Other evidence cited for MPI** (pp. 9–10):
  - double-parton scattering, with CDF σ_eff = 14.5 ± 1.7 (+1.7/−2.3) mb (p. 9);
  - KNO broadening: UA5 at 900 GeV has ⟨n_ch⟩ = 35.6 and σ(n_ch) = 19.5, vs a Poisson σ = 6.0 (p. 9);
  - large forward–backward correlation b (Eq. 11);
  - the pedestal effect, saturating at p⊥jet ≈ 10 GeV (p. 10).
- **Bose–Einstein evidence.** UA1/E735 Bose–Einstein data are cited as a hint of string–string correlations: the BE strength falls with multiplicity, but the radius grows. LEP2 W⁺W⁻ crosstalk results are called "inconclusive" (p. 35).

**Impact parameter (Sec. 3, brief).**
- ExpOfPow(d = 1.2) with p⊥0 = 1.9 GeV and Tune A both describe UA5 at 200 and 900 GeV (Fig. 6).
- Neither reproduces the E735 high-multiplicity tail at 1.8 TeV (Fig. 7). An exponential with p⊥0 = 1.6 GeV comes near E735 but then fails UA5 (p. 19). The UA5–E735 incompatibility is noted (pp. 19–20).

**Initial-state colour correlations (Sec. 5.2).**
- **Physics.** Interference terms O(1/N_C²) between colour flows already make the perturbative colour assignment non-unique. Baryon beams add a further three-fold choice of which junction leg each gluon sits on (pp. 40–41).
- **Model choice.** Only the minimal number of fictitious gluon emissions is used. As a consequence, a sea quark can never form a singlet with its own companion (p. 41).
- **Random attachment.** The junction is usually disconnected from the remnant valence quarks, so the baryon number migrates strongly (Fig. 16, p. 41). The junction-baryon p⊥ spectrum is nevertheless similar to Tune A (Fig. 17a). Two effects cancel: a softer primordial k⊥ for remnant diquarks, and a harder spectrum when no diquark forms (pp. 42–43). A free suppression of attachments to undisturbed remnant legs is introduced to limit baryon stopping (p. 43).
- **Orderings.** The paper defines:
  - Δy ordering: minimise |y_g − y₁| + |y_g − y₂|, with remnant partons placed at a fixed large rapidity (Eq. 67, Fig. 18);
  - Δλ ordering: minimise the string-length increase ln[2(p_c1·p_c̄1)(p_c2·p_c̄2)/(m₀² p_c̄1·p_c2)] (Eq. 68, Fig. 19), with a floor of m₀ on each piece because remnant kinematics are not yet fixed (p. 46).
- **⟨p⊥⟩(n_ch) at the Tevatron** (Fig. 20), with p⊥0 tuned to Tune A's ⟨n_ch⟩:

  | Model | p⊥0 | ⟨p⊥⟩ at N_ch ≈ 150 |
  |---|---|---|
  | Tune A | 2.0 GeV | ≈ 0.56 GeV |
  | random | 3.15 GeV | ≈ 0.41 GeV |
  | Δy | 3.10 GeV | ≈ 0.42 GeV |
  | Δλ | 2.95 GeV | ≈ 0.43 GeV |

  Δλ gives the most MPIs and the highest ⟨p⊥⟩, random the fewest (p. 46). The ⟨p⊥⟩ values are read off the figure. Tune A "more or less agrees" with data [CDF refs 56, 58, 61] (p. 46).
- **Interpretation.** Tune A's ordering acts on the *final-state* partons, while Δλ here acts only on initial-state colour lines (p. 46). Two candidate missing ingredients are named (pp. 46–47):
  - intertwined ISR, where two initiators share a shower ancestor above Q₀;
  - colour exchanges between showers in the initial and/or final state.

**Final-state colour (re-)connections (Sec. 5.3).**
- **Algorithm** (p. 47):
  - Les Houches colour tags are assigned; string pieces ending on junctions are excluded.
  - Pairs of tags are picked at random, and a swap i₁–j₂, i₂–j₁ is accepted if λ′ < λ (Eqs. 69–70).
  - This is iterated over a fraction F of the tags until no swap occurs.
  - It is applied only to events with ≥ 2 interactions, "to avoid the reconnections leading to large central rapidity gaps, i.e. diffractive topologies".
- **Strength.** With F = 1 and p⊥0 lowered to 1.90 GeV, ⟨p⊥⟩(n_ch) reaches ≈ 0.63 GeV at N_ch = 150, well above Tune A (≈ 0.56). The F = 0 model (p⊥0 = 3.10 GeV) stays at ≈ 0.42 (Fig. 21). The model is "very crude and should not be interpreted as representing physics per se" (p. 48).
- **Benchmark tunes (Tab. 1):**

  | Model | Tevatron ⟨n_int⟩ | Tevatron ⟨n_part⟩ | Tevatron ⟨n_rcp⟩ | LHC ⟨n_int⟩ | LHC ⟨n_part⟩ | LHC ⟨n_rcp⟩ |
  |---|---|---|---|---|---|---|
  | Ran | 3.3 | 21.5 | 18 | 4.2 | 40.2 | 45 |
  | Rap | 3.6 | 22.8 | 19 | 4.5 | 43.5 | 49 |
  | Lam | 3.9 | 24.5 | 20 | 4.8 | 45.8 | 52 |
  | Tune A | 5.7 | 19.2 | — | 6.9 | 27.7 | — |

  The new models need fewer MPIs than Tune A because each MPI showers and the string-length minimisation is less efficient (pp. 49–50).

**Tevatron and LHC comparisons (Sec. 6).**
- **Agreement with Tune A.** Jet rates (Fig. 23) and charged p⊥/y spectra (Fig. 24) are close to Tune A. The new models have a slightly harder p⊥.
- **Multiplicity shape.** Not reproduced: the new models have a narrower high-n_ch tail (Fig. 22).
- **Remnant structure.** The new models have many more final-state quarks (Fig. 25a). Part of the x = 1 diquark peak moves to intermediate x (Fig. 25b).
- **Baryon number.**
  - n(p) + n(n) − n(p̄) − n(n̄) vs y is less peaked at the beam rapidity in the new models (Fig. 26a).
  - The junction-baryon rapidity distribution has a long central tail extending to negative y (Fig. 26b).
  - Without diquark formation, stopping is much stronger (Fig. 11).
  - Junction–antijunction annihilation occurs in < 1% of Tevatron events. Events with two junction–junction colour lines are rejected (p. 40).
- **Junction-baryon strangeness.** P(|S| = 2) and P(|S| = 3) rise; |S| = 3 is empty for Tune A (Fig. 27, p. 54).
- **⟨p⊥⟩(n_ch) at the Tevatron** (Fig. 28). The new models show "a too early rise to a too low plateau": about 0.49–0.52 GeV at N_ch = 150 vs Tune A ≈ 0.56. Varying the FS CR scheme can fix this, but so far only at the cost of a worse multiplicity distribution (p. 55).
- **LHC.**
  - The new models give ⟨n_ch⟩ = 87–89 vs 81 for Tune A, because of more shower activity (Fig. 29).
  - Junction baryons are harder in p⊥ at the LHC, because primordial k⊥ grows with Q (Fig. 31).
  - The central baryon-stopping tail grows with energy (Fig. 32).
  - ⟨p⊥⟩(n_ch) has the same qualitative pattern as at the Tevatron. At N_ch = 250, Tune A is ≈ 0.73 GeV and the new models ≈ 0.62–0.65 GeV (Fig. 33, read off the figure).

**Conclusions and proposed tests (Sec. 7).**
- The paper lists ten open questions (p. 60). Two of them:
  - (viii) How are interacting and remnant partons correlated in colour, and is the large-N_C limit relevant?
  - (x) How does space-time overlap of several strings modify independent string fragmentation?
- The lesson drawn from Tune A is that "the colours of final-state partons are not random but correlated, somehow, to give a reduced string length" (p. 60).
- The excess of central baryons over antibaryons in hadronic and heavy-ion data (refs [84], [85]) is cited as motivation for junction-driven baryon stopping. Suppression of multi-leg interactions should be weaker in heavy-ion collisions (pp. 60–61).
- Final-state CR is also noted as a proposed mechanism for diffractive topologies (Enberg–Ingelman–Timneanu, ref. [87]) (p. 61).
- **Proposed measurement (RQ4):** the "lumpiness" of the underlying event, i.e. n-jet rates vs a jet-resolution parameter, as in e⁺e⁻ (p. 61). The paper also points to:
  - baryon − antibaryon rapidity distributions (Fig. 26a, p. 54);
  - junction-baryon strangeness (Fig. 27, p. 54);
  - ⟨p⊥⟩(n_ch) as the prime colour-flow test (p. 55).

## Assessment
- **Historical role.** This is the origin of the argument "⟨p⊥⟩(n_ch) needs colour reconnection" in the modern Pythia lineage. It is the first explicit demonstration, within one MPI + string framework, that initial-state colour orderings alone (even Δλ-optimised) leave ⟨p⊥⟩(n_ch) flat. The argument is entirely model-internal.
  - The "data" are Tune A, not measurements. No ⟨p⊥⟩(n_ch) data points appear in any figure; Tune A is only said to "more or less agree" with CDF.
  - Neither alternatives outside the string/MPI picture (hydro, ropes) nor alternatives to CR within it are tested.
- **Status of the CR model.** The FS CR here is explicitly a toy: a random-pair λ-descent with a free F. The authors repeatedly disclaim it as evidence for CR. Its legacy is the class of λ-minimising "colour annealing" models (Sandhoff–Skands 2005, already queued) and the Pythia 6.4 Perugia CR. The reconnection counts in Tab. 1 are model-specific and should not be quoted as physical.
- **Tension with later work.** Sjöstrand 2013 (already summarised) says colour correlations between MPIs reduce the remnant charge "but nowhere near enough", so CR is still required. That is consistent with Figs. 20/21 here.
- **Figure-caption inconsistency.** The Fig. 20 caption calls the rapidity-ordered curve "solid", but the legend shows it dotted (Tune A is solid). This does not affect the conclusion.
- **Baryon-stopping predictions.** These are qualitative and parameter-dependent: the remnant-break suppression of 0.01 and the diquark-formation rules strongly change Fig. 11. They are relevant for RQ1 small-system/baryon-number discussions (junction baryons, later junction CR in Pythia 8), but they are not a test of colour coherence per se. The Ω⁻/Ω̄⁺ heavy-ion link is only suggestive.
- **What is not here.** The paper has nothing on perturbative colour coherence or jet observables. It belongs to the RQ2 "colour flow / CR modelling" strand and partly to RQ1, as an argument for a non-perturbative origin of MPI colour correlations.

## Leads
- **Sjöstrand & Skands, "Baryon number violation and string topologies", Nucl. Phys. B659 (2003) 243, hep-ph/0212264** (Sjostrand:2002ip, queued "later"). Defines junction fragmentation and the junction pull (Eq. 66), which this paper relies on. Worth raising to "next" for the junction/baryon strand.
- **Sjöstrand & Skands, "Transverse-momentum-ordered showers and interleaved multiple interactions", EPJC 39 (2005) 129, hep-ph/0408302** (Sjostrand:2004ef, queued). Direct follow-up promised here: p⊥-ordered ISR interleaved with MPI. It addresses the "intertwined showers" question and is the model on which colour annealing was built.
- **Sandhoff & Skands, "Colour annealing – a toy model of colour reconnections"** (Sandhoff:2005jh, recid 700706, queued). The successor to the Sec. 5.3 toy CR model and the actual "colour annealing" paper.
- **Sjöstrand & van Zijl, Phys. Rev. D36 (1987) 2019** (Sjostrand:1987su, queued). Original MPI model and the original ⟨p⊥⟩(n_ch) colour-connection argument (ref. [1]).
- **R. D. Field (CDF), Tune A / underlying event, hep-ph/0201192, and CDF D. Acosta et al., Phys. Rev. D65 (2002) 072005** (ref. [58]). Field:2001aok is currently *rejected*. The CDF ⟨p⊥⟩(n_ch) measurement (PRD65, 072005) is the actual data behind Tune A's ⟨p⊥⟩(n_ch) and should be checked for presence in the queue (RQ3).
- **UA1, C. Albajar et al., Nucl. Phys. B335 (1990) 261, and E735, T. Alexopoulos et al., Phys. Lett. B336 (1994) 599** (ref. [58]). Early ⟨p⊥⟩(n_ch) data (RQ3).
- **UA1, Phys. Lett. B226 (1989) 410, and E735, Phys. Rev. D48 (1993) 1931** (ref. [80]). BE strength decreasing and radius increasing with multiplicity, cited as a hint of inter-string correlations (RQ1/RQ3, small-system collectivity).
- **Enberg, Ingelman & Timneanu, Phys. Rev. D64 (2001) 114015, hep-ph/0106246** (Enberg:2001vq, queued). Final-state soft colour interactions as an origin of diffraction at the Tevatron (ref. [87]).
- **Andersson, Gustafson & Söderberg, Z. Phys. C20 (1983) 317, and Andersson, Mohanty & Söderberg, Nucl. Phys. B646 (2002) 102** (ref. [81]). The λ string-length measure used for all CR ordering here. Lower priority, but foundational for "λ-minimisation" CR.
- **Baryon stopping / junction literature** (ref. [85]): Kharzeev, Phys. Lett. B378 (1996) 238; Kopeliovich & Povh, Z. Phys. C75 (1997) 693; Vance, Gyulassy & Wang, Phys. Lett. B443 (1998) 45. Only relevant if the review covers baryon-number flow and junction CR in small systems; low priority.
- **Skands & Sjöstrand, proceedings hep-ph/0310315 (HEP 2003) and hep-ph/0401060 (Les Houches 2003).** Short companion write-ups. They are likely redundant with this paper, so skip unless the review needs a complete record.
