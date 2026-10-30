# Colour reconnections in Herwig++
- **ID / links:** Gieseke:2012ft · INSPIRE 1116881 · arXiv 1206.0041 · DOI 10.1140/epjc/s10052-012-2225-5
- **Authors / collab, year, journal:** S. Gieseke, C. Röhr, A. Siódmok, 2012, Eur. Phys. J. C 72 (MCnet-12-06)
- **Type:** MC/model
- **Relevance:** 3 · RQs: 1, 2, 3, 4
- **Full text source:** arxiv

## Takeaways
- This is the reference paper for the Herwig++ (≥2.5) cluster-based CR models. Plain CR (PCR) swaps colour partners between two clusters if this lowers m_C + m_D, accepting with probability p_reco (Eq. 1, p. 4). Statistical CR (SCR) minimises the colour length λ = Σ m_i² by simulated annealing (Eqs. 2–4).
- Motivation: without CR, Herwig++ 2.4 MPI could not describe the ATLAS 900 GeV η distribution or ⟨p⊥⟩(N_ch), for any p_disrupt or PDF choice, even though Tevatron UE was fine (Figs. 1–2, pp. 2–3). CR "was the missing piece of the MPI model" (p. 10) and restores the rise of ⟨p⊥⟩(N_ch) (Fig. 12, p. 11).
- Physical picture is colour preconfinement. CR acts almost only on heavy clusters, in particular "n-type" clusters built from non-perturbatively extracted MPI/remnant partons, and it cuts the high-mass cluster tail by >10× (Figs. 7–9, pp. 7–8; LHC 7 TeV dijet events). In e+e- → qq̄ the colour length is essentially unchanged (Fig. 5c). LEP data are therefore insensitive, and the LEP-tuned hadronisation can be kept (Fig. 10, p. 9).
- The tuned SCR prefers fast "cooling" and ends up close to PCR (Sec. 5, p. 17; parameters in Tab. 2, p. 13). The authors conclude the data do not want a fully minimised colour length. Large reconnection probabilities are preferred: p_reco ≈ 0.54–0.61 (Tab. 2).
- MPI parameters are energy dependent: p⊥^min = 1.55/2.26/2.75 GeV at 0.9/1.8/7 TeV (Tab. 1), parametrised by a power law (Eq. 7). Diffraction-enhanced MB (N_ch ≥ 2, p⊥ > 100 MeV) is still poorly described at high N_ch (Fig. 21).

## Setup
- **Generator:** Herwig++ 2.4.2 (no CR) vs 2.5 (with CR). Cluster hadronisation. An eikonal MPI model with parameters μ² (inverse proton radius²), p⊥^min and p_disrupt, which "controls the colour structure of soft scatters" (p. 2; the precise definition as a disruption probability is not given in this paper [unverified]).
- **PCR (Sec. 2.1, p. 4):** loop over quarks in random order. For the cluster A containing the current quark, test all other clusters B. Alternative clusters C, D must satisfy m_C + m_D < m_A + m_B (Eq. 1) and must not be colour octets. Pick the configuration with the smallest m_C + m_D and accept it with probability p_reco. The authors note that it is non-deterministic and treats q and q̄ asymmetrically.
- **SCR (Sec. 2.2, pp. 4–5):** objective λ = Σ m_i² (Eq. 2). Squared masses favour evenly distributed cluster masses. Metropolis acceptance p = exp(−(λ2 − λ1)/T) (Eq. 3). Initial temperature T_init = c·median|Δλ| from dry runs (Eq. 4). T is multiplied by f each step, with αN_cl attempts per step and at most N_steps steps. The annealing parameters are said to have no physical interpretation (p. 5).
- **Diagnostics:** colour-length drop Δ_if = 1 − λ_final/λ_init (Eq. 5). Cluster classes: h-type (same hard subprocess), i-type (interconnecting perturbative partons from different subprocesses), n-type (≥1 non-perturbative parton) (Fig. 7). Cluster fraction functions f_a(m_cut) (Eq. 6).
- **Data:** LEP DELPHI event shapes and multiplicity (Fig. 10). DELPHI WW → 4q inter-jet particle flow at 189 GeV (Fig. 11). ATLAS MB at 0.9 and 7 TeV (N_ch ≥ 6, p⊥ > 500 MeV, |η| < 2.5) (Figs. 12, 20). ATLAS UE at 0.9/7 TeV and CDF UE at 1.8 TeV (toward/transverse/away) (Figs. 13–17). ATLAS diffraction-enhanced MB (N_ch ≥ 2, p⊥ > 100 MeV) (Fig. 21).
- **Tuning:** Rivet + Professor. PCR has 4 parameters (p_disrupt, p_reco, p⊥^min, μ²). SCR has 7 (p_disrupt, p⊥^min, μ², c, f, α, N_steps), i.e. p_reco is replaced by the four annealing parameters (p. 10). N_steps is handled by 50 fixed-value tunes (pp. 10–12).

## Results
- **Without CR (Herwig++ 2.4.2):** at 900 GeV, dN/dη depends strongly on p_disrupt: a central dip for p_disrupt = 1, overshoot by up to ≈25–30% for 0 (≈, read from Fig. 1). ⟨p⊥⟩(N_ch) is ≈10–20% too low and too flat for all settings and PDFs (CTEQ6L1, MRST LO**) (≈, read from Figs. 1–2, p. 3).
- **Colour-length drop:** in soft-inclusive 7 TeV pp, Δ_if is bimodal with peaks at 0 and 1, similar for PCR and SCR (Fig. 5a). The fraction with Δ_if ≈ 1 decreases with a higher parton-level jet p⊥ cut, because remnants carry less momentum in hard events (Fig. 5b, p. 6). In LEP dijets CR has "no impact on the colour length in the bulk". WW → 4j has a "slightly higher" fraction with non-vanishing drop (in the plot the 0<Δ_if<1 plateau is ≈0.4 vs ≲0.1 for dijets, ≈ read from Fig. 5c), but "the vast majority" of WW events are unaffected (pp. 6–7).
- **Cluster masses:** CR enhances the 1–2 GeV peak and suppresses the high-mass tail (Fig. 6). In 7 TeV LHC dijet events, f_i(100 GeV) = 0.15, and n-type clusters exceed 50% of clusters above m_cut ≈ 70 GeV (Fig. 8, p. 7). n-type clusters dominate the tail but contribute little below ~6 GeV. After CR the tail is suppressed by a factor >10 (Fig. 9, p. 8).
- **LEP:** Herwig with CR (UE-EE-3, UE-EE-SCR tunes) matches DELPHI y_S and ⟨N_ch⟩ as well as without CR (Fig. 10). The full comparison is on the Herwig/MCplots pages (p. 9). This allows factorised tuning: LEP hadronisation fixed, MPI+CR tuned on hadron data.
- **WW particle flow:** PCR with p_reco = 0.54 gives "a slight improvement" over no CR for the DELPHI inter-W/intra-W flow. The CR envelope (p_reco varied) reaches ≈+10–30% in some bins (≈, read from Fig. 11). Apparent outliers in the data and "too optimistic systematic errors" mean no constraint can be derived (Fig. 11, p. 9). No extra WW-specific suppression is introduced. The authors note that the finite W width lets the W's travel apart before decaying, so large CR "should" be suppressed; they justify omitting an explicit suppression by the moderate observed sensitivity and the mostly vanishing Δ_if in WW (Fig. 5c) (p. 9).
- **MB tune at 900 GeV (MB900-CTEQ6L1, PCR):** η, N_ch, p⊥ spectrum and ⟨p⊥⟩(N_ch) are all described. ⟨p⊥⟩(N_ch) improves from ≈0.8–0.9 of data to ≈1 (≈, read from Fig. 12, p. 11).
- **UE:** the UE7-2 tune (ATLAS 7 TeV, PCR) describes all regions. The p⊥ > 100 MeV UE data, not used in the tune, are also well described (Fig. 16c, p. 10). The azimuthal N_ch and Σp⊥ profiles are described, improving with p⊥^lead (Fig. 17, p. 15; text p. 11).
- **Energy dependence:** one parameter set cannot describe 900 GeV and 7 TeV together; the data prefer different p⊥^min (p. 12). μ² and p⊥^min are strongly correlated and poorly constrained individually (Fig. 18). Energy-extrapolated tunes: Tab. 1 (p⊥^min values) and Tab. 2. UE-EE-3: μ² = 1.11 GeV², p_disrupt = 0.80, p_reco = 0.54. UE-EE-3-CTEQ6L1: 1.35, 0.75, 0.61. UE-EE-SCR-CTEQ6L1: μ² = 1.5, p_disrupt = 0.8, c = 0.01, f = 0.21, N_steps = 10, α = 0.66. The p⊥^min(s) power law (Eq. 7, p. 17) has p⊥,0^min = 3.11/2.81/2.64 GeV and b = 0.21/0.24/0.21 at E0 = 7 TeV (Tab. 2, p. 13; Fig. 19). PCR and SCR UE descriptions are of the same quality (Figs. 13–15). The authors favour SCR for its "clearer physics picture" (p. 12).
- **7 TeV MB (not in the UE-EE tunes):** SCR is slightly better than PCR. The PCR multiplicity overshoots by up to ≈50% at N_ch ≈ 50–70. ⟨p⊥⟩(N_ch) is within a few % for SCR and ≈5–10% low at high N_ch for PCR (≈, read from Fig. 20, p. 18; text p. 17).
- **Diffraction-enhanced MB (N_ch ≥ 2, p⊥ > 100 MeV):** both tunes fail. ⟨p⊥⟩(N_ch) for PCR falls increasingly low above N_ch ≈ 60, ≈20–30% low at N_ch ≳ 120; SCR is closer up to N_ch ≈ 120 but drops to ≈0.6 of data in the highest bin. The PCR multiplicity overshoots strongly above N_ch ≈ 80, while SCR is closer (≈, read from Fig. 21, p. 18). The authors attribute the low-N_ch failure to the absent soft-diffraction model. They say the high-N_ch failure "may indicate missing physics" or need a dedicated MB tune (p. 17).
- **Conclusion:** because the tuned SCR cools fast, PCR is a special case of SCR. Data demand a final state "that does not obey a perfectly minimized colour length", which the authors interpret as a limitation of the leading-N_c colour-line picture (p. 17).

## Assessment
- CR here is a purely kinematic "repair" of colour assignments that the MPI model makes arbitrarily between scatters. There is no colour-algebra weight (no 1/N_c² suppression as in Rathsman's GAL or SCI). The large p_reco ~0.5–0.6 means most heavy clusters reconnect. That is a strong statement about the non-perturbative colour structure of hadron collisions, and it rests only on ⟨p⊥⟩(N_ch) and η shape.
- The evidence for CR in pp is indirect: the ⟨p⊥⟩(N_ch) rise is the same signal that drove Pythia's CR (Sandhoff–Skands). Other mechanisms (ropes, collective flow, MPI p⊥ dependence) are not considered. Degeneracy with p_disrupt, μ², p⊥^min (Fig. 18) weakens any quantitative claim about CR strength.
- The universality test is weak. LEP Z data are insensitive by construction (Fig. 5c), and the WW particle-flow comparison is inconclusive (Fig. 11). So the model is effectively tuned only in pp, and the same p_reco is assumed in e+e- WW without a physics argument. The space-time separation argument for WW (p. 9) is not implemented: there is no space-time information in the model.
- The SCR annealing parameters are tuning knobs with "no physical interpretation". The finding that the data prefer an incompletely minimised λ is interesting, but it may be an artefact of the annealing schedule. Several Professor issues (N_steps integer, interpolation failures, excluded regions) are reported (p. 12).
- Relevant for top-mass CR uncertainties (Herwig PCR/SCR variations used by ATLAS/CMS) and as a precursor of the Herwig 7 baryonic/space-time CR models. It is complementary to Rathsman's GAL: both minimise invariant masses (A_ij ≈ 2p_i·p_j vs Σm²), but GAL includes a colour-suppression factor and was validated on DIS diffraction. No rapidity-gap or DIS observables are studied here.

## Leads
- Sandhoff & Skands, hep-ph/0604120 (2005), and Skands & Wicke, EPJC 52 (2007) 133: Pythia CR models driven by ⟨p⊥⟩(N_ch); the top-mass CR uncertainty.
- Wicke & Skands, Nuovo Cim. B123 (2008) S1: CR and the top mass at the Tevatron.
- DELPHI, EPJC 51 (2007) 249: WW → 4q particle-flow CR measurement used in Fig. 11.
- D. Duchesneau, LAPP-EXP-2000-02 (2000): particle-flow method for WW CR studies, which became the LEP standard.
- Gieseke, Röhr, Siódmok, arXiv 1110.2675 (2011), and Gieseke et al. (Herwig++ 2.5 release), arXiv 1102.1672: the first CR implementation and MB tuning.
- Schulz & Skands, EPJC 71 (2011) 1644: energy scaling of MB tunes, the context for the p⊥^min(s) issue.
- Gieseke, Kirchgaeßer, Plätzer, EPJC 78 (2018) 99, "Baryon production from cluster hadronisation": Herwig 7 baryonic CR follow-up.
- Bellm, Duncan, Gieseke, Myska, Siódmok, EPJC 79 (2019) 1003, "Spacetime colour reconnection in Herwig 7": the space-time CR follow-up and top-mass impact.

## Verification
Checked 2026-10-30 by an independent reader: 58 claims checked, 9 corrected, 1 unverifiable.
- SCR parameter list fixed: 7 parameters with p_reco replaced by c, f, α, N_steps (not PCR's 4 plus 4).
- WW (p. 9): the finite-W-width remark was misrendered as the authors' justification; their actual justification is the moderate observed sensitivity plus Fig. 5c.
- Fig. 21: "less so for SCR" was wrong; SCR is worse than PCR in the highest-N_ch ⟨p⊥⟩ bin.
- Fig. 20 PCR multiplicity overshoot ≈50% (not ~40%) at N_ch ≈ 50–70; Fig. 11 envelope up to ≈+30%.
- Page anchors fixed: Figs. 1–2 on p. 3, Fig. 12 on p. 11, Tab. 2 on p. 13, Figs. 20–21 on p. 18, Fig. 17 on p. 15; Figs. 8–9 are 7 TeV dijet events.
- p_disrupt definition not given in this paper: marked [unverified]. Plot read-offs marked ≈.
