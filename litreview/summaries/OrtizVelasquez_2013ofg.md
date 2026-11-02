# Color Reconnection and Flowlike Patterns in pp Collisions
- **ID / links:** OrtizVelasquez:2013ofg · INSPIRE 1225534 · arXiv 1303.6326 · DOI 10.1103/PhysRevLett.111.042001
- **Authors / collab, year, journal:** A. Ortiz Velasquez, P. Christiansen (Lund), E. Cuautle Flores, I. A. Maldonado Cervantes, G. Paić (UNAM), 2013, Phys. Rev. Lett. 111, 042001
- **Type:** phenomenology (MC study, Pythia 8)
- **Relevance:** 3 · RQs: 1, 2, 4
- **Full text source:** arxiv

## Takeaways
- This is the standard reference for the claim that colour reconnection (CR) in Pythia 8 produces radial-flow-like effects in pp without any medium. In events with several MPIs, CR string pieces that join partons from different mid-rapidity scatterings get a common transverse boost. The resulting hadron-mass-dependent hardening resembles radial flow (pp. 2–3, Fig. 2).
- In Pythia 8 Tune 4C, the (p+p̄)/(π⁺+π⁻) bump at p_T ≈ 2.5–3 GeV/c is attributed to CR. With CR off (RR = 0) the ratio is flat above about 1.8 GeV/c. The bump grows and moves to higher p_T in events with ≥ 20 MPIs and disappears for < 5 MPIs (Fig. 3 top, p. 2).
- The CR on/off double ratios show a mass hierarchy: p/π and Λ/K⁰_S, then φ/π, then K/π, which is almost unchanged. The effect fades at high p_T, which the authors say distinguishes CR from hydrodynamics (Fig. 3 bottom, p. 2).
- With CR on, ⟨p_T⟩ rises with multiplicity for all species and faster for heavier ones (protons fastest); with CR off it is nearly flat (Fig. 4 top). The authors say a blast-wave fit to CMS and Pythia spectra gives a T_kin–⟨β_T⟩ trend like that in heavy-ion collisions (pp. 3–4). No numbers or figure are shown for this fit.
- They speculate that the Δφ dependence of the string-length measure could also produce elliptic and triangular flow. They call this "very speculative" (p. 4).

## Setup
- Pythia 8.17, Tune 4C, pp at √s = 7 TeV, minimum bias plus multiplicity and N_MPI classes (pp. 1–2).
- Primary charged particles are defined as in ALICE: weak-decay products of strange particles are excluded. Identified hadrons are taken at |y| < 1 and event multiplicity in |η| < 2.4 (p. 2).
- CR is switched on and off with the reconnection range RR. The probability to merge a system of scale p̂_T into a harder one is (2.085·RR)²/((2.085·RR)² + p̂_T²). Tune 4C has RR = 1.5, and RR = 0 means no CR (p. 2).
- Hadron species: π, K, p, φ, Λ, K⁰_S. Observables: p/π vs p_T, CR/no-CR double ratios, ⟨p_T⟩(dN/dη / ⟨dN/dη⟩) per species, and p_T-integrated p/π vs multiplicity (Figs. 3–4).
- Data comparison: only Fig. 1, ALICE preliminary p/π at 7 TeV vs Pythia 4C and an NLO calculation (Sassot–Zurita–Stratmann FFs). For CMS ⟨p_T⟩ values the paper quotes text only and does not overlay them in Fig. 4 (p. 2).

## Results
- **Data comparison (Fig. 1).** ALICE preliminary p/π shows a peak of about 0.25–0.27 near p_T ≈ 3 GeV/c, falling to ≈0.10–0.13 at p_T ≈ 10–18 GeV/c (read off Fig. 1). Pythia 4C reproduces the peak qualitatively but overshoots above about 8 GeV/c (≈0.20–0.24, read off Fig. 1). The authors call this "not a major worry" (p. 1). The NLO curve rises monotonically and has no peak.
- **MPI dependence (Fig. 3 top).** With CR on (min. bias) there is a bump around 2.5 GeV/c. With CR off the ratio is flat above about 1.8 GeV/c. For N_MPI ≥ 20, the curve crosses the min-bias one at about 1.8 GeV/c and peaks at about 0.3 at 3 GeV/c. For N_MPI < 5 it looks like the no-CR curve (p. 2). Above about 5 GeV/c the curves converge: "particles inside hard jets are not sensitive to color reconnection" (p. 2).
- **Double ratios RR=1.5/RR=0 (Fig. 3 bottom).** For p/π and Λ/K⁰_S, CR lowers the ratio below about 1.5–2 GeV/c (p/π about 0.8 near 1 GeV/c) and raises it above 1 at 2.5–4 GeV/c. The maxima are ≈1.1 for p/π and ≈1.15 for Λ/K⁰_S (read off Fig. 3). The (2φ)/π bump is ≈1.07 (read off Fig. 3). K/π stays close to 1. The authors read this as a mass effect "reminiscent of radial flow" (p. 2). They note that Pythia generally underestimates strange-particle yields.
- **⟨p_T⟩ vs scaled multiplicity (Fig. 4 top).** With CR, proton ⟨p_T⟩ rises from about 0.67 to about 1.2 GeV/c over dN/dη/⟨dN/dη⟩ ≈ 0.5–6.5. Without CR it rises only from about 0.63 to about 0.75. Kaons behave the same way but less strongly (≈0.57 → ≈0.97 with CR, ≈0.57 → ≈0.65 without). Pions also rise with CR (≈0.44 → ≈0.64) but are almost flat without CR (≈0.44–0.47) (all read off Fig. 4). The authors cite CMS for a proton ⟨p_T⟩ rise from ≈0.6 to ≈1.4 GeV/c across CMS multiplicity classes. They say this "can only be accommodated" with CR (p. 2), but no direct overlay is shown.
- **p_T-integrated p/π (Fig. 4 bottom).** With CR the ratio falls with multiplicity from about 0.069 to about 0.059. Without CR it falls less, from about 0.068 to about 0.065 (read off the figure). The authors compare this qualitatively to the Pb–Pb trend. They say that in Pythia it is a phase-space redistribution: with no y cut, p̄/π is constant vs multiplicity with or without CR (p. 4).
- **Blast-wave fit.** The authors state that fits to CMS and Pythia π/K/p spectra give a T_kin–⟨β_T⟩ evolution "very similar" to heavy ions (pp. 3–4). No figure or table supports this.
- **Higher harmonics.** The string-length measure is quoted as l = √(Δη² + Δφ²), so CR could also prefer azimuthal configurations and generate v₂ and v₃. This is "very speculative" and needs further theoretical work (p. 4).

## Assessment
- This 4-page letter shows a clear proof of mechanism within one generator and one tune (4C, MPI-based CR). The CR on/off comparison isolates the effect cleanly. However, the evidence is almost entirely MC-vs-MC. Data appear only in Fig. 1, where the high-p_T description is poor, and the CMS ⟨p_T⟩ and blast-wave claims are made in the text without plots. Treat the claim that CR-induced radial flow "plays a role to explain the CMS results" (p. 4) as qualitative.
- The string-length measure l = √(Δη² + Δφ²) on p. 4 is the authors' heuristic. Pythia's actual CR criterion is the λ-measure, which is based on invariant masses, so the elliptic-flow argument is a conjecture rather than a model property. In the Lund group, azimuthal anisotropies are instead modelled with string shoving (Bierlich et al., cited in Lonnblad:2023stc). The two mechanisms should be compared.
- The baryon/meson effect depends on the CR model. The MPI-based CR has no junctions. QCD-CR (Christiansen–Skands 2015) adds junction baryons, which enhance p/π and Λ/K strongly, so later conclusions can differ (see Lonnblad:2023stc).
- The paper is still useful for RQ4. It makes clear observables (mass-ordered ⟨p_T⟩(N_ch), the p/π and Λ/K⁰_S peak vs multiplicity and N_MPI, the high-p_T fall-off of the double ratio) that can separate CR-boost from hydrodynamic radial flow. Note that the paper uses "flow-like" only for radial flow.

## Leads
- Christiansen & Skands, "String formation beyond leading colour", JHEP 08 (2015) 003, arXiv:1505.01681. The QCD-CR model whose junctions change the baryon/meson pattern, so it tests whether the flow-like signal depends on the model.
- Corke & Sjöstrand, "Interleaved parton showers and tuning prospects", JHEP 03 (2011) 032, arXiv:1011.1759 (cited in the paper as "JHEP 32 (2011)", ref. [9]). Defines Tune 4C and the RR parametrisation used here.
- CMS, "Study of the inclusive production of charged pions, kaons, and protons in pp collisions at √s = 0.9, 2.76, and 7 TeV", Eur. Phys. J. C 72 (2012) 2164, arXiv:1207.4724. The data behind the ⟨p_T⟩(N_ch) mass-ordering claim.
- G. Gustafson, "Multiple interactions, saturation, and final states in pp collisions and DIS", Acta Phys. Polon. B40 (2009) 1981, arXiv:0905.2492 (ref. [14]). Source of the CR string-boost picture (Fig. 2).
- A. Ortiz Velasquez (ALICE), QM2012 proceedings, arXiv:1210.6995. The ALICE preliminary pp p/π data in Fig. 1.
- ALICE, Phys. Lett. B 719 (2013) 29 (p–Pb double ridge, arXiv:1212.2001). The p–Pb collectivity the authors propose CR may explain.
- Follow-ups to queue via forward citations (294 cites): CR-based flow-like studies in pp and p-Pb (e.g. Ortiz et al. on "flow-like" in Pythia with transverse spherocity or N_MPI selection) and ALICE/CMS identified-particle papers that test this mechanism.
