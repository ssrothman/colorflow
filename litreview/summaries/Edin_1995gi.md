# Soft colour interactions as the origin of rapidity gaps in DIS
- **ID / links:** Edin:1995gi · INSPIRE 398766 · arXiv hep-ph/9508386 · DOI 10.1016/0370-2693(95)01391-1
- **Authors / collab, year, journal:** A. Edin, G. Ingelman, J. Rathsman (Uppsala / DESY), 1996, Phys. Lett. B (per DOI; the arXiv v1 PDF gives no journal reference, so the volume and page are not stated here). Preprint TSL/ISV-95-0125, DESY-95-163.
- **Type:** MC/model (phenomenology)
- **Relevance:** 3 · RQs: 1b, 2, 4
- **Full text source:** arxiv

Page anchors are the arXiv PDF page numbers (pp. 1–11; text pp. 2–10, references p. 11). The paper has no numbered equations.

## Takeaways
- This is the original "soft colour interaction" (SCI) model, implemented in LEPTO 6.3. After the perturbative phase, every pair of colour charges, including the proton-remnant spectators, may exchange colour with probability R. Momenta are not changed. This rearranges the string topology so that colour-singlet systems can be separated in rapidity (pp. 2–3, Fig. 1). It is a colour-reconnection mechanism applied to DIS. It is the direct ancestor of Rathsman's GAL model, which ALEPH/OPAL test at LEP1 (lineage not stated in this paper; stated in Rathsman:1998tp, which takes SCI as its baseline).
- Rapidity gaps in DIS then arise without a pomeron. With R = 0.2 the model gives an η_max distribution with a "plateau" and peak that the authors say agree "reasonably" with H1/ZEUS data (Fig. 2, p. 4). The comparison is qualitative only. There is no detector simulation and no χ² is given.
- The gap rate saturates in R: above R ≈ 0.5 the gap probability does not increase and may decrease (p. 3). The gap events show diffractive-like features (exponential t, ~1/M_X², forward system dominantly a proton) without any Regge input (Fig. 3, p. 5).
- The same model plus improved sea-quark remnant treatment describes the H1 forward E_T flow at x < 10⁻³. LEPTO 6.2 falls below the data at Δη ≳ 2 (Fig. 6, p. 8). The authors argue that describing both the gaps and the high forward E_T flow is a non-trivial test (p. 8).
- The gap rate depends strongly on non-SCI ingredients: the matrix-element cut-off y_cut and the parton-shower cut-off Q₀² (Fig. 4, p. 6). The default choices (y_cut = 0.0001, Q₀² = 4 GeV²) are, of the two values compared for each, the ones that give more gaps (p. 6).

## Setup
- Process: ep DIS at HERA. Boson-gluon fusion (BGF) γg → qq̄ "constitutes a substantial part of the cross-section" at small x (10⁻⁴–10⁻²) (p. 2). The kinematic range for Fig. 2 is 7.5 < Q² < 70 GeV², 0.03 < y < 0.7, with an H1 acceptance limit η_max < 3.65 (p. 3).
- Model: LEPTO (Lund string hadronization via JETSET), ME + parton showers. Then SCI: each pair among the hard-process partons and the remnant quarks/diquark undergoes a colour exchange with probability R. Only colour changes, not momenta (p. 3). Fig. 1b shows an anticolour switch between q̄ and diquark, and Fig. 1c a colour switch between the two quarks.
- Default R = 0.2. The authors motivate it as α_s(0.5 GeV)/π ≈ 0.2 at scales below Q₀² ~ 1 GeV² (pp. 3–4).
- The gap definition mimics H1: no energy in η_max < η < 6.6 with η_max < 3.2 (p. 4, Fig. 3 caption).
- New remnant treatment: the struck quark is valence or sea according to q_val/q_sea(x₁, Q₁²). For a sea quark, the partner antiquark gets a longitudinal momentum fraction from its PDF or from P(g→qq̄). This gives a two-string configuration analogous to BGF (p. 9).
- No detector simulation and no fit. All data comparisons are by eye.

## Results
- **η_max distribution (Fig. 2, p. 4):** R = 0 gives essentially no events with η_max ≲ 1. Its curve falls to ~10⁻³ around η_max ≈ 1. R = 0.1, 0.2 and 0.5 all produce a slowly rising plateau, ≈ 10⁻² at η_max ≈ −1 to ≈ 5×10⁻² at η_max ≈ 2 (read off Fig. 2). The R dependence is weak: the R = 0.1, 0.2 and 0.5 curves lie within roughly a factor 2 of each other on the plateau. The line styles are too similar to say reliably which is highest. The text says R > 0.5 does not increase and may decrease the gap probability (p. 3). The authors claim the peak height and plateau are "in reasonable agreement" with data [1,2], but no data are overlaid in Fig. 2 (p. 4).
- **Gap-event properties (Fig. 3, p. 5):** (a) The t distribution reproduces the input primordial k⊥ Gaussian width. It follows e^{5t} for σ = 0.44 GeV and e^{t} for σ = 1 GeV, since t ≈ −k⊥² and σ² = 2⟨k⊥²⟩ (pp. 4–5). (b) M_R is dominated by the nucleon, with a sizeable Δ peak, which the authors map to pion exchange in Regge language (p. 5). The Δ fraction depends on the small-mass string hadronization model [9]. (c) dN/dM_X follows ~1/M_X², from the 1/ŝ dependence of the BGF matrix element. It is suppressed at large M_X by the gap requirement (p. 5).
- **Sensitivity to the perturbative input (Fig. 4, p. 6):** For y_cut = 0.005, which the authors call theoretically sound [10], ~10 % of events are BGF. With y_cut = 0.0001, the 2+1-jet cross section saturates the Born cross section and ~50 % are BGF (p. 6). Parton-level gaps from the BGF matrix element do not survive showering and hadronization without SCI (Fig. 4a). After SCI, Q₀² = 1 GeV² gives visibly fewer gaps than Q₀² = 4 GeV² (Fig. 4b). Defaults: y_cut = 0.0001, Q₀² = 4 GeV² (p. 6).
- **Kinematic dependence (Fig. 5, p. 7):** The gap fraction N_gap/N reaches ~0.1 at the lowest x and Q², and falls with increasing x at fixed Q² and with increasing Q² (read off the 3-D plot). The x dependence is mostly kinematic: the hard system moves forward and shrinks the possible gap. The Q² dependence is attributed to more initial-state radiation (p. 7). The authors note that the data are "within errors, essentially independent of Q² for fixed x", with "indications of some variations" of the same kind (p. 8).
- **Forward E_T flow (Fig. 6, p. 8):** H1 data [14] at x < 10⁻³ versus Δη = η − η_q/QPM. LEPTO 6.2 undershoots the data for Δη ≳ 2: ≈ 1.4–1.7 GeV vs data ≈ 1.9–2.5 GeV for 2 ≲ Δη ≲ 4.2 (read off Fig. 6). LEPTO 6.3 (new sea-quark remnant) raises the plateau. LEPTO 6.3+SCI raises it further and is described as "well described" by the authors. Strings that go "back and forth" after SCI produce more E_T per unit rapidity (p. 8).
- **Proposed tests (RQ4, pp. 5, 8–9):** compare F₂^D(β, Q²) extracted from the model with data (p. 8). Look at the forward R-system composition (N vs Δ) and vary the gap definition, where differences from pomeron models are expected (pp. 5, 9). Use higher-statistics x, Q² dependence of the gap rate (p. 8).
- The authors note that the model is similar in spirit to Buchmüller–Hebecker [17]. That model works at matrix-element level only, without showers or hadronization (pp. 9–10).

## Assessment
- This is a proof-of-concept letter. Every data comparison is qualitative. Fig. 2 has no data overlaid, and there is no detector simulation or χ² anywhere. "Reasonable agreement" cannot be quantified from this paper. That needs the later, more detailed SCI/GAL papers (e.g. Rathsman PLB 452 (1999) 364, cited by ALEPH:2006jcu as ref. [16]; the other follow-ups are not yet identified, see Leads).
- The gap rate depends at least as much on the tuned perturbative ingredients (y_cut = 0.0001 saturating the cross section with BGF; Q₀² = 4 GeV²) as on R (Figs. 4a, 4b). Both defaults are chosen because they favour gaps. So the model's success at HERA is not a clean measurement of a "colour-reconnection probability". R = 0.2 is a motivated choice, not a fit.
- Relevance to colour reconnection: this is the HERA-side origin of the idea that soft, non-perturbative colour exchanges rearrange string topology even in a single colour-singlet system. That is exactly what ALEPH:2006jcu and OPAL (EPJC 35 (2004) 293) test at LEP1 with gluon-jet rapidity gaps, and they find GAL with R₀ = 0.10 overpredicts. The tension between a HERA-motivated R and the LEP1 constraint (R₀ ≈ 0.01–0.02) is worth flagging in the synthesis. The comparison should be made with care, since SCI (this paper) and GAL (later) use different reconnection criteria.
- The x/Q² dependence prediction (Fig. 5) is a genuine falsifiable feature. Whether it distinguishes SCI from a factorized pomeron flux is our inference; the paper does not make that contrast (pp. 7–8), and it does not test the prediction.

## Leads
- A. Edin, G. Ingelman, J. Rathsman, DESY 95-145 (DIS'95 Paris proceedings) (ref. [6]): the first presentation of the SCI idea.
- W. Buchmüller, A. Hebecker, Phys. Lett. B 355 (1995) 573 (ref. [17]): parallel colour-octet → singlet rapidity-gap model, the "semiclassical" alternative.
- A. Berera, D.E. Soper, Phys. Rev. D 50 (1994) 4328 (ref. [16]): interactions before and after the hard scattering, a conceptual precursor to non-pomeron gap mechanisms.
- H1, Z. Phys. C 63 (1994) 377 (ref. [14]): forward E_T flow data used for the SCI test.
- H1, Nucl. Phys. B 429 (1994) 477 and Phys. Lett. B 348 (1995) 681; ZEUS, Phys. Lett. B 315 (1993) 481 (refs. [1,2]): the original DIS rapidity-gap observations.
- G. Ingelman, J. Rathsman, Z. Phys. C 63 (1994) 589 (ref. [10]): justification of the y_cut choice for BGF.
- Not cited here (forward-looking): Rathsman's generalized area law, PLB 452 (1999) 364 (the GAL model tested by ALEPH/OPAL), and any later Edin–Ingelman–Rathsman SCI follow-ups (e.g. applications to hadron-collider gaps). Their references are unverified here; find them via `citing 398766`.
