# Paper repositories: access, APIs, parsing

`scripts/lr.py` wraps the common operations (with rate limiting, retries, dedup). This file documents the raw APIs for anything it doesn't cover, and the gotchas it encodes.

Status markers: **[v]** verified against the live service on 2026-10-30; **[u]** documented but not yet exercised. Prefer `python3` with `json` / `xml.etree` for parsing. Keep output small (see SKILL.md). Save files only under `~/colorflow/litreview/papers/`.

## 1. INSPIRE-HEP — primary source (metadata, references, citations)

Base: `https://inspirehep.net/api/literature`. No auth. Rate limit **15 requests / 5 s per IP** (headers `X-RateLimit-Remaining`, `X-RateLimit-Reset`); on 429/502 back off and retry. [v]

```
GET /api/literature?q=<query>&sort=<mostrecent|mostcited>&size=<n≤1000>&page=<p>&fields=<comma list>
```

- **Always pass `fields=`** — full records are huge (thousand-author lists). Sub-fields allowed: `titles.title,arxiv_eprints.value`. [v]
- The single-record endpoint `/api/literature/<recid>` returned the *full* record despite `fields=`; use `q=recid:<n>&fields=...` instead. [v]
- Batch lookup: `q=recid:1 or recid:2 or ...` — 50 OR'ed recids worked, ~100 gave **HTTP 502**. `lr.py` uses batches of 40. [v]
- **Gotcha: malformed queries silently match the whole database** (~1.6M hits) instead of erroring. Observed with parentheses combined with `refersto:` (`refersto:recid:374155 and (t coherence)` → everything; without parens → 17). An empty `q` also matches everything. Avoid parentheses; treat any total > 500k as a malformed query (`lr.py` raises an error). [v] A bare `or` after `refersto:` behaves sensibly (`refersto:recid:374155 and t coherence or t jets` → 28, versus 17 for `t coherence` alone), but prefer one filter term per query. [v]
- DOIs containing parentheses (`doi 10.1016/0370-2693(81)90505-0`) resolve correctly. [v]
- Append `format=bibtex` to any search URL for BibTeX instead of JSON. [v]

Query syntax (SPIRES-style):

| Query | Meaning | |
|---|---|---|
| `doi 10.1103/PhysRevD.50.5562` | by DOI | [v] |
| `arxiv 1311.5815` | by arXiv id | [v] |
| `texkey Abe:1994nj` | by texkey (aliases resolve to the canonical record) | [v] |
| `recid:374155` | by record number | [v] |
| `t "color reconnection"`, `title coherence` | title | [v] |
| `t coherence and t jets` | boolean `and` / `or` / `not` — no parentheses | [v] |
| `refersto:recid:374155` | papers **citing** 374155 | [v] |
| `citedby:recid:374155` | papers **cited by** 374155 (its resolved references); combinable with a filter, e.g. `citedby:recid:1218394 and t coherence` → 6 of 154 | [v] |
| `k "color coherence"` | keyword | [v] |
| `fulltext "drag effect"` | full-text search (arXiv-era content) | [v] |
| `date > 2015`, `date 1990->1999` | date filter | [v] (`>`); range [u] |
| `tc r` / `tc c` / `tc p` | review / conference paper / published | [v] (`r`, `c`) |
| `a Sjostrand, T` / `cn CMS` | author / collaboration | [u] |

Useful `fields` sets:
- Triage: `control_number,texkeys,titles.title,abstracts.value,arxiv_eprints.value,dois.value,citation_count,publication_info.year,earliest_date,collaborations.value,document_type`
- Full-text locating: `arxiv_eprints.value,documents.url,documents.filename,urls.value,dois.value`
- References: `references.record,references.reference`

Response shape [v]:
```json
{"hits": {"total": 97, "hits": [{"id": "374155", "metadata": {...requested fields...}, "links": {...}}]},
 "links": {"self": "...", "next": "...", "bibtex": "..."}}
```

Parsing notes [v]:
- `control_number` = recid (int). `texkeys[0]` is canonical; later entries are aliases.
- `titles` is a list; prefer the first entry without `"source": "arXiv"` (proper LaTeX).
- `arxiv_eprints[0].value` is a bare id (`"0709.1027"`); absent for pre-arXiv papers.
- `publication_info` is a list (errata, proceedings); its first entry may lack `year`, and the whole field may be absent (e.g. ATLAS PUB notes). `earliest_date` (`"2014-11-02"` or `"1994-03"`) is a reliable fallback for the year. [v]
- `abstracts` often missing for old papers.
- `references[i] = {"record": {"$ref": ".../literature/164399"}, "reference": {...}}`; recid = last path segment. `record` is absent when INSPIRE couldn't match the reference — then only `reference.title` / `arxiv_eprint` / `publication_info` / `misc` are available (e.g. 34 refs, 33 resolved for CDF:1994zkl).
- `documents[i] = {"url", "filename", "key"}` — often scanned preprints for pre-arXiv papers (e.g. `DESY-81-009.pdf`); these typically have **no text layer**.

## 2. arXiv — full text and very recent preprints

Search (Atom XML) [v]:
```
GET https://export.arxiv.org/api/query?search_query=<q>&start=0&max_results=<n>&sortBy=submittedDate|relevance|lastUpdatedDate&sortOrder=descending
GET https://export.arxiv.org/api/query?id_list=1311.5815,0709.1027
```
- Prefixes `ti:` `abs:` `au:` `cat:` `all:`; operators `AND` `OR` `ANDNOT` (caps); quote phrases. Categories: `hep-ph`, `hep-ex`, `hep-th`, `nucl-th`, `nucl-ex`.
- ≤ 1 request / 3 s; `max_results` ≤ 100 per page.
- Feed: `opensearch:totalResults`; each `<entry>` has `id` (`http://arxiv.org/abs/<id>v<n>`), `title`, `summary`, `published`, `author/name`, `link[@title="pdf"]`, `arxiv:primary_category`, optional `arxiv:doi`, `arxiv:journal_ref`. Namespaces: Atom `http://www.w3.org/2005/Atom`, arXiv `http://arxiv.org/schemas/atom`.
- No citation data — use INSPIRE for the graph.

Full text:
- PDF: `https://arxiv.org/pdf/<id>`. [v]
- LaTeX source: `https://arxiv.org/e-print/<id>` → **301 redirect** (use `curl -L`), then `application/gzip`, normally a `.tar.gz` (`arXiv-<id>v<n>.tar.gz`); occasionally a single gzipped `.tex`. [v] (tar case). PDF-only submissions return a PDF instead; `lr.py` checks the gzip magic bytes and reports "no LaTeX source".
- Old-style ids (`hep-ph/9405123`): keep the slash in URLs, `_` in filenames.

## 3. HEPData — experimental measurements

```
GET https://www.hepdata.net/search/?q=<terms>&format=json&size=<n>        [v]
GET https://www.hepdata.net/record/ins<recid>?format=json                   [v]
```
- Search: `results[]` with `inspire_id`, `arxiv_id`, `collaborations`, `data_abstract`, `access_urls.links` (yaml/root/yoda), `analyses` (e.g. Rivet `CMS_2013_I1265659`).
- Record: top-level `record` (with `title`), `data_tables` (list), `related_recids`, etc.
- Rivet analysis names encode the INSPIRE recid (`_I<recid>`) — handy to see which measurements feed MC tuning / CR model tests.

## 4. Secondary sources (optional)

Coverage of older HEP literature is much poorer than INSPIRE's (CDF:1994zkl: INSPIRE 97 citations, OpenAlex 58, Semantic Scholar 24) — use only as supplements.
- **OpenAlex** [v]: `https://api.openalex.org/works/doi:<doi>?select=id,title,cited_by_count,open_access,referenced_works_count`. Add `best_oa_location` to `select` for `best_oa_location.pdf_url`, a direct PDF link that is often absent. `open_access.oa_url` is usually a landing page (e.g. a DESY repository record or the publisher's DOI link), so `lr.py fetch` downloads only `pdf_url` and prints `oa_url` for a manual check. [v] Useful for non-HEP venues (nuclear physics, EIC).
- **Semantic Scholar** [v]: `https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,citationCount,influentialCitationCount`; `/citations?fields=title,isInfluential,contexts` gives citation contexts (often empty for old papers). Unauthenticated rate limits are tight.

## 5. Full-text access order (implemented by `lr.py fetch`)

1. **Zotero** (read-only). The bib `file = {...}` field holds `;`-separated Windows paths with `\\` and `\:` escapes; map `C:\Users\simon\Zotero\storage\<KEY>\<name>.pdf` → `/mnt/c/Users/simon/Zotero/storage/<KEY>/<name>.pdf`. **Gotcha** [v]: the bib export strips `{}` from filenames, so the exact path often doesn't exist; each storage `<KEY>` dir holds one attachment, so fall back to its single PDF. Never copy or modify Zotero files.
2. **arXiv** (from INSPIRE `arxiv_eprints`).
3. **INSPIRE `documents[].url`** (scans; no text layer → read the PDF pages as images).
4. **OpenAlex `best_oa_location.pdf_url`** (automatic). Otherwise `fetch` prints INSPIRE `urls` and OpenAlex `oa_url` for a manual look (CDS `cds.cern.ch` for CERN preprints, SCOAP3).
5. Otherwise the paper is `blocked` and goes into the next check-in request to the user (see SKILL.md step 11).

Reading: use the Read tool on the PDF (`pages`, ≤ 20 pages per call) so figures, tables and equations are visible; `pdftotext -layout` output (`<ID>.txt`) is for grep only.
