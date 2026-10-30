# Literature Review

## Research Questions 

The first task in this project is a comprehensive literature review. The scope for this literature review is high-energy particle physics as seen at colliders such as LEP, LHC, and EIC. The primary research questions are:

1. What is the physical origin of collective effects in high-energy QCD? Collective effects include:

    a. Color coherence inside jets
    
    b. Coherence and interference effects between multiple jets

    c. Correlations in jet substructure

    d. Correlations between multiple jets

    e. Correlations between jets and recoiling bosons
    
2. What are the theoretical results and models for these collective effects? Focused particularly on color coherence, color reconnection, and color flow.

3. What are the experimental results and constraints relevant to these effects?

4. What experimental tests have been suggested in the theoretical literature? 

### Scope notes

- Small-system collectivity (e.g. the ridge, strangeness/baryon enhancement in high-multiplicity pp and pA, rope hadronization) is **in scope**, since competing explanations (color reconnection, ropes, flow-like dynamics) bear directly on question 1. Heavy-ion collectivity is in scope only where it connects to these mechanisms or to color coherence (e.g. coherence in jet quenching).
- Non-journal sources count: LEP working-group reports, conference proceedings, CERN yellow reports, and theses where they hold unique results.
- Seed topics that must be covered even if the starting bibliography does not lead to them: color reconnection in W⁺W⁻ at LEP2 (incl. the LEP-wide combinations); color-reconnection uncertainties on the top-quark mass; jet pull and color-flow measurements (tt̄, H→bb̄, W→qq̄); rapidity gaps and color-singlet exchange; string/drag effect in e⁺e⁻ three-jet events; soft-gluon coherence and angular ordering; beyond-leading-color parton showers; EIC projections.

## Starting point

I have already started with a small manual review of some of the oldest literature. An initial list of potentially-relevant papers can be found in `litreview/human_start.bib` in `biblatex` format. This list should only be viewed as a jumping off point --- feel free to decide some of these papers are not relevant, and I expect that many more papers will be important. 

## Plan

### Basic literature review procedure

The plan for this literature review is as follows:

Start with the human_start.bib bibliography, and loop over the following steps:

1. Read and analyze potentially relevant papers. 

2. Identify additional potentially-interesting papers through any combination of the following links:

    a. Papers cited by the papers read so far

    b. Papers which cite the papers read so far

    c. Keyword searches on relevant paper repositories

3. Repeat until it is likely that all relevant data has been analyzed. Concretely: stop expanding when, in two consecutive iterations, fewer than ~10% of newly triaged candidates are judged likely relevant (expected relevance ≥ 2), and check in with the human after roughly every 150 papers read in full (the literature-review skill defines the expansion caps).

You must use the `literature-review` skill. Reading and analysis of many papers and topics should be fanned out to several subagents. 

If you can't find the full text of a paper, mark it as blocked and continue with the rest of the batch. STOP and ask for human assistance with all blocked papers at once (title, DOI, why it is needed) when any of these holds at the end of an iteration: about 10 or more papers are blocked; a blocked paper was judged essential at triage (expected relevance 3); or a ~150-paper check-in is due. Otherwise keep going. Do not summarize a paper from its abstract alone.

### Results, logs, and documentation

At each step you should maintain detailed human-readable documentation. In particular this documentation must detail:

1. A list of all the papers considered so far

2. A summary of the key relevant results, etc. for each paper (or set of papers if they are closely related)

3. A list of all the papers queued to consider next.

4. A human-readable summary of the main points, results, and answers to the research questions

5. A human-readable summary of the current open questions and ideas which do not yet have convincing experimental validation. 

6. A BibTeX file of all papers judged relevant, for later writing and Zotero import.

All of this lives under `litreview/` and is version-controlled with git (one commit per iteration).
