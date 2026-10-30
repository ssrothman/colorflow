# Nonperturbative factorization breaking and color entanglement effects in dihadron and direct photon-hadron angular correlations in p+p and p+A collisions
- **ID / links:** Osborn:2018bwn · INSPIRE 1678752 · arXiv 1806.07763 · DOI none
- **Authors / collab, year, journal:** J. D. Osborn (PhD thesis, Univ. of Michigan, advisor C. Aidala; PHENIX), 2018. The p+p results are published as PHENIX, PRD 95 (2017) 072002 (√s = 510 GeV) and PHENIX, arXiv:1805.02450 (√s = 200 GeV; later PRD 98 (2018) 072004 [journal ref unverified; the thesis cites only the arXiv number]). The p+A results were PHENIX preliminary at the time.
- **Type:** experimental (with a phenomenological compilation of DY/Z/SIDIS widths)
- **Relevance:** 3 · RQs: 1e, 1d, 2, 3, 4
- **Full text source:** arxiv

## Takeaways
- This is the first dedicated experimental search for "colour entanglement", meaning TMD-factorization breaking in hadron-hadron collisions with coloured partons in both the initial and the final state. It is a colour-flow effect: soft gluons are exchanged between the hard partons and the remnants of the *other* proton (Fig. 1.9; pp. 20–22; theory Collins–Qiu 2007, Rogers–Mulders 2010). The strategy is to look for deviations from the CSS expectation that nonperturbative k_T widths **grow** with the hard scale (pp. 33–35).
- The observable is p_out = p_T^assoc sin Δφ (Eq. 1.8) in near back-to-back π⁰–h± and isolated direct γ–h± pairs at PHENIX midrapidity (|η| < 0.35). Gaussian fits to the small-p_out core isolate the nonperturbative k_T + j_T width (pp. 40–41, Fig. 1.20). γ–h± is the colour-simpler probe because the photon is colourless (p. 39).
- At √s = 510 GeV, in fixed p_T^assoc bins, the widths **decrease** with p_T^trig (slopes −0.0055 ± 0.0018 ± 0.0010 for π⁰ and −0.0109 ± 0.0039 ± 0.0016 for γ; Fig. 4.14, p. 129). This looked anti-CSS, but it was later traced to a fragmentation/kinematic artefact: at fixed p_T^assoc the away-side z falls as p_T^trig rises (p. 135, a suggestion credited to J. Collins). Binned in x_E, the √s = 200 GeV widths **increase** with p_T^trig, qualitatively like Drell–Yan (Fig. 5.4, p. 141). **Net result: no qualitative signature of colour entanglement in p+p** (abstract p. xxiii; p. 216).
- One residual oddity: at fixed p_T^trig and x_E the widths are the same at √s = 200 and 510 GeV (Fig. 5.7, p. 143–144). In DY at similar hard scale, the nonperturbative widths rise with √s (Figs. 6.6, 6.7). The author flags this as possibly due to factorization breaking, or simply because p_T^trig is not the true hard scale (the pair mass would be) (p. 144).
- p+Au shows N_coll-dependent away-side broadening, while the near-side (j_T) widths are unchanged (Figs. 5.23–5.26). This rules out final-state fragmentation modification and v2/v3 flow as the cause. Even a deliberately overestimated flow modulation is ≤ 2% of the background level and leaves the widths unchanged. The broadening could come from extra soft colour exchange ("more coloured objects"), but also from nuclear k_T, energy loss or Cronin physics, so it does not isolate colour entanglement (pp. 166–169).

## Setup
- **Data:** PHENIX central arms, |η| < 0.35.
  - p+p at √s = 510 GeV (2012 + 2013, ≈ 30 + 150 pb⁻¹).
  - p+p at √s = 200 GeV (2015, ≈ 60 pb⁻¹).
  - p+Au and p+Al at √s_NN = 200 GeV (2015, ≈ 200 and 700 nb⁻¹, equivalent to ≈ 15.8 and 9.1 pb⁻¹ of p+p) (p. 55).
- **Triggers and pairs:** π⁰ or isolated direct-photon triggers with 4–15 GeV/c, paired with charged hadrons of p_T^assoc 0.5/0.7–10 GeV/c. The decay-photon background is removed by statistical subtraction (Sec. 3.3). The away-side window is 2π/3 < Δφ < 4π/3, with the underlying event statistically subtracted (Sec. 3.4.3).
- **Observables:**
  - p_out (Eq. 1.8) and x_E = −p_T^trig·p_T^assoc/|p_T^trig|² (Eq. 1.9), with x_E used as a proxy for z.
  - Gaussian widths of the small-p_out core of the p_out distributions.
  - √⟨p_out²⟩ from the fit function for the full away-side Δφ distribution (Eq. 4.1), which contains both perturbative and nonperturbative contributions.
  - √⟨j_T²⟩ from the near-side width (Eq. 4.3), and the k_T relation (Eq. 4.2).
- **Logic:** CSS evolution follows from the TMD factorization derivation. It predicts, independent of the nonperturbative input, that nonperturbative widths broaden with the hard scale (p. 34). The test is therefore the *rate of change* of the widths with p_T^trig or √s, in processes predicted to break factorization (dihadrons, γ-h) versus processes predicted to factorize (DY, Z, SIDIS). Sec. 6.2 compiles the latter from E288, E605, E772, CDF Z and COMPASS.
- **Models:** PYTHIA 6 (Perugia0) is used only for kinematics: ⟨z_T⟩ of π⁰ triggers (Figs. 4.15–4.17) and the x_E–z map (Figs. 6.1–6.3). No colour-entanglement calculation exists to compare to: the non-factorizing correlation function has not been studied theoretically (p. 23), and TMD calculations are too uncertain for a direct data–theory comparison (pp. 32–33).

## Results
- **√s = 510 GeV p+p**
  - The p_out distributions show a Gaussian core plus a power-law (Kaplan) tail, and PYTHIA reproduces this shape (Fig. 4.7).
  - Fixed j_T: √⟨j_T²⟩ = 0.662 ± 0.003 (stat) ± 0.012 (sys) GeV/c, flat in p_T^trig (Fig. 4.13, p. 128).
  - Gaussian widths (0.7 < p_T^assoc < 10 GeV/c) fall from ≈ 0.52 to ≈ 0.47 GeV/c over p_T^trig 4–14 GeV/c (≈ read from Fig. 4.14). The negative slopes are quoted in the Takeaways (Fig. 4.14, p. 129). With 1.2 < p_T^assoc < 10 GeV/c the slopes steepen to −0.012 ± 0.003 ± 0.001 (π⁰) and −0.023 ± 0.007 ± 0.003 (γ) (p. 130).
  - √⟨p_out²⟩ also falls with p_T^trig: only slightly for π⁰–h, and strongly but non-monotonically for γ–h. γ–h values exceed π⁰–h values. The author suggests this is because, at the same p_T^trig, the photon trigger corresponds to a lower hard scale (Fig. 4.11, p. 126).
- **Re-analysis at √s = 200 GeV in x_E bins**
  - At fixed 0.1 < x_E < 0.5 the widths rise from ≈ 0.43 to ≈ 0.55 GeV/c (π⁰) and up to ≈ 0.73 GeV/c (γ, large errors) over p_T^trig 4–14 GeV/c (≈ read from Fig. 5.4).
  - The widths rise steeply with x_E, from ≈ 0.4 to ≈ 1.1 GeV/c over x_E 0.1–0.65 (≈ read from Fig. 5.6).
  - π⁰–h and γ–h agree within uncertainties (Figs. 5.4, 5.6). This holds despite γ–h being ≈ 85% quark jets and colour-simpler (p. 174, Fig. 6.4).
  - The 510 GeV data, rebinned in x_E with only p_T^trig > 7 GeV/c, agree with the 200 GeV data (Fig. 5.7, p. 143).
  - The author concludes that the earlier decrease was due to falling z, not factorization breaking (p. 145, p. 170).
- **Comparison with factorizing processes**
  - DY/Z Gaussian widths rise with M_μμ and √s: ≈ 0.85–1.3 GeV/c for M = 5–16 GeV, and ≈ 1.6 GeV/c for the CDF Z (≈ read from Fig. 6.6).
  - COMPASS ⟨p_T²⟩ rises with Q² at fixed z (Fig. 6.9). Mimicking the p+p binning (decreasing z with Q²) reproduces a *decrease* (Fig. 6.10). This supports the fragmentation explanation (p. 182).
  - Older PHENIX ⟨p_T⟩_pair (≈ 3.4 GeV/c at 200 GeV, ≈ read from Fig. 6.11) lies above the dimuon trend. This is noted as "additional p_T" in dijets/dihadrons compared with dimuons at the same √s (p. 184).
- **p+A at √s_NN = 200 GeV**
  - Away-side squared-width differences ⟨p_out⟩²_pA − ⟨p_out⟩²_pp reach ≈ 0.1 (GeV/c)² in 0–30% p+Au at 0.25 < x_E < 0.5 (≈ 0.075 centrality-integrated) and are smaller in p+Al (≈ read from Figs. 5.20, 5.23).
  - These differences grow linearly with N_coll, with slope 0.005(1) for 0.15 < x_E < 0.25 and 0.015(5) for 0.25 < x_E < 0.5 (Fig. 5.25, p. 163).
  - A zero-broadening hypothesis gives χ²/ndf = 11.8/2 and 16.5/2 (Fig. 5.26, p. 162).
  - Near-side differences are consistent with zero, all within < 2σ (Fig. 5.22, p. 160).
  - A deliberately overestimated v2/v3 modulation, taken from Au+Au, is at most ≈ 2% (on average < 1%) of the underlying-event level. Subtracting it leaves the Gaussian widths unchanged (Eq. 5.5, Figs. 5.27–5.28, pp. 165–166).
  - The extracted x̂_h is the same in p+p and p+Au (Fig. 5.18). Direct γ–h in p+Au is consistent with p+p within large errors (Figs. 5.12, 5.15).
- **Author's overall conclusion:** the nonperturbative widths "do not show any notable qualitative factorization breaking effects". Quantitative TMD calculations that assume factorization are needed to bound the size of the effect (pp. 216–217).
- **Proposals (RQ4)**
  - γ–jet p_out at sPHENIX: projections with 200–300 pb⁻¹ (Figs. 7.16–7.18).
  - Back-to-back γ + J/ψ or Υ at the LHC as a colour-singlet versus colour-octet and factorization-breaking probe (Figs. 7.19–7.20, pp. 210–214).
  - "Anti-groomed" soft-radiation jet mass as a factorization-violation observable (p. 217).
  - Linking LHC colour-coherence measurements (CMS 3-jet β, ATLAS γ+2-jet; Fig. 1.11) to colour entanglement. The author conjectures that colour coherence and colour entanglement are "likely ... the same physical phenomenon" (p. 26). On p. 209 this is softened to "qualitatively similar".

## Assessment
- **A clean null result for a qualitative test.** The method only tests the *sign* of the hard-scale evolution of the widths, and that test was nearly fooled by a kinematic bias (fixed p_T^assoc versus fixed z). The x_E-binned analysis is more sensible, but x_E is still only a proxy for z. The x_E–z correlation differs strongly between π⁰ and γ triggers in PYTHIA (Figs. 6.1–6.3), so any comparison "at fixed z" is model-dependent. The hard scale is p_T^trig, not the pair invariant mass, which further blurs the CSS comparison.
- **Sensitivity is not quantified.** No colour-entanglement calculation exists, so the absence of a qualitative difference does not bound the size of factorization breaking. The result is a constraint for future TMD fits, not a measurement of a colour effect. The slope significances (≈ 2.6–2.7σ for 0.7 < p_T^assoc < 10 GeV/c and ≈ 3–4σ for p_T^assoc > 1.2 GeV/c; these are our own stat ⊕ sys estimates, and the thesis quotes no significance) measure the "wrong-sign" trend that was later explained away.
- **The √s-independence of the widths (Fig. 5.7)** is the most interesting residual hint, given that DY widths rise with √s. It rests on few points with sizeable errors, and the DY comparison uses Gaussian fits to ⟨p_T⟩ spectra of different construction. Treat it as a hint only.
- **The p+A broadening is significant but not specific.** nPDF k_T, cold-nuclear-matter energy loss, Cronin and MPI are all viable, and the author admits this (pp. 167–168). For our RQs it is mainly a small-system data point, not evidence of colour entanglement.
- **Scope link.** This is the main experimental reference for "colour flow between initial and final states" in boson/hadron–jet correlations (RQ1e). The γ–h versus h–h comparison is a useful idea: it removes one colour line, much as colour-singlet versus octet comparisons do in jet pull. The "coherence = entanglement" claim is the author's conjecture and is not demonstrated.
- **Citations.** For citation, prefer the PHENIX journal papers (PRD 95, 072002; PRD 98, 072004). The p+A results are preliminary in the thesis.

## Leads
- **Rogers & Mulders, PRD 81 (2010) 094006**, "No generalized TMD-factorization in hadro-production of high transverse momentum hadrons". This is the core colour-entanglement theory paper (RQ2).
- **Collins & Qiu, PRD 75 (2007) 114014**, and **Collins, arXiv:0708.4410**. These are the original k_T-factorization-violation papers, including the 2-soft-gluon argument.
- **PHENIX, PRD 95 (2017) 072002** (510 GeV) and **PHENIX, arXiv:1805.02450 / PRD 98 (2018) 072004** (200 GeV). These are the journal versions of the thesis results (RQ3).
- **Theory extensions to boson–jet correlations (RQ1e):**
  - **Schäfer & Zhou, PRD 90 (2014) 094012**, "Color entanglement for γ-jet production in polarized pA collisions".
  - **Rogers, PRD 88 (2013) 014002**, on extra spin asymmetries from TMD-factorization breakdown.
  - **J. Zhou**, "Color entanglement like effect in collinear twist-3 factorization".
- **den Dunnen, Lansberg, Pisano, Schlegel, PRL 112 (2014) 212001** (thesis ref [179]). It proposes γ + quarkonium as a TMD and colour-octet probe (RQ4).
- **ALICE, PLB 746 (2015) 385**, "dijet k_T in p–Pb at 5.02 TeV" (thesis ref [121]). This is an LHC momentum-space acoplanarity measurement that could be reused for colour-flow and TMD tests.

## Verification
Checked 2026-10-30 by an independent reader: 62 claims checked, 6 corrected, 1 unverifiable.
- v2/v3 test: the "< 2%" figure is the size of the flow modulation relative to the underlying-event level (on average < 1%). The widths themselves are unchanged (Fig. 5.27). The earlier text said "changes the widths by < 2%".
- Fig. 4.11: the "lower hard scale for γ" explanation is the author's suggestion, not a result. The γ–h √⟨p_out²⟩ is non-monotonic.
- Slope significances: the thesis quotes none. Replaced ≈ 2.5–3σ with our own estimate: 2.6–2.7σ for the main selection, 3–4σ for p_T^assoc > 1.2 GeV/c.
- "No colour-entanglement calculation" now cites p. 23. Pages 32–33 only say that TMD calculations are too uncertain.
- The "same physical phenomenon" quote is from p. 26 only. On p. 209 the claim is softened to "qualitatively similar".
- The 510-vs-200 GeV x_E comparison is restricted to p_T^trig > 7 GeV/c. Added this.
- Plot read-offs are now marked (Figs. 4.14, 5.4, 5.6, 5.20/5.23, 6.6, 6.11). The p+Au ≈ 0.1 (GeV/c)² figure is for 0–30% centrality; the centrality-integrated value is ≈ 0.075.
- [unverified]: the PRD 98 (2018) 072004 journal reference. The thesis cites only arXiv:1805.02450.
- All other quoted numbers match the thesis exactly: slopes, j_T, χ² values, N_coll fits, luminosities, the 85% quark fraction, and the page anchors (printed page = PDF page − 24).
