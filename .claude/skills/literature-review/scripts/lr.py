#!/usr/bin/env python3
"""Literature-review helper: INSPIRE/arXiv queries + papers.jsonl state management.

Stdlib only. Run from anywhere:  python3 .claude/skills/literature-review/scripts/lr.py <cmd> ...
All state lives in ~/colorflow/litreview/. Output is compact JSON lines (one paper per line)
so it can be piped:  lr.py citing 374155 | lr.py new | lr.py add --via "cites Abe:1994nj"

Commands (see `lr.py <cmd> -h`):
  lookup ID...        resolve doi:/arxiv:/recid:/texkey: (or bare DOI / arXiv id / recid) to records
  search QUERY        INSPIRE search (SPIRES syntax)
  refs RECID          references of a paper (resolved ones as records, unresolved listed on stderr)
  citing RECID        papers citing RECID
  arxiv QUERY         arXiv API search (for very recent preprints)
  new                 filter stdin records to those NOT already in papers.jsonl
  add                 add stdin records to papers.jsonl (default status=candidate)
  set ID k=v ...      update fields of a record (ID = recid, texkey, file ID, arXiv id, DOI or bibkey)
  setmany             batch `set` from stdin lines "ID k=v k=\"v w\" ..." (all-or-nothing)
  show ID...          print stored records
  list [--status S]   compact paginated listing (--limit/--offset; --abstract for triage)
  fetch ID            obtain full text into litreview/papers/ (Zotero -> arXiv -> INSPIRE docs)
  seed [--bib F]      import a Zotero bib export (default litreview/human_start.bib)

Output volume: keep it small (harness persists large outputs outside the project).
`refs`/`citing` on big papers emit hundreds of lines: pipe into `new | add` rather than printing.
Keyword searches (`search`, `arxiv`, filtered `citing`) are appended to litreview/searches.tsv.
  render              regenerate papers.md and queue.md from papers.jsonl
  bibtex              regenerate review.bib for relevance >= 2
"""
import argparse, fcntl, gzip, io, json, os, re, subprocess, sys, tarfile, time
import urllib.error, urllib.parse, urllib.request

ROOT = os.path.expanduser("~/colorflow")
LR = os.environ.get("LR_DIR", os.path.join(ROOT, "litreview"))  # LR_DIR override for testing
DB = os.path.join(LR, "papers.jsonl")
PAPERS = os.path.join(LR, "papers")
BIB = os.path.join(ROOT, "litreview", "human_start.bib")
LOCKDIR = os.path.join(LR, ".ratelimit")
ZOTERO = "/mnt/c/Users/simon/Zotero/storage"
INSPIRE = "https://inspirehep.net/api/literature"
UA = "colorflow-litreview/1.0"
BATCH = 40  # INSPIRE 502s on ~100 OR'ed recids; 50 tested OK

TRIAGE_FIELDS = ("control_number,texkeys,titles.title,arxiv_eprints.value,dois.value,citation_count,"
                 "publication_info.year,collaborations.value,document_type")
STATUSES = ["candidate", "queued", "blocked", "read", "skimmed", "rejected"]


# ---------------------------------------------------------------- HTTP / rate limiting
def _throttle(name, min_interval):
    """Cross-process rate limit: serialize requests via a lock file holding the last timestamp."""
    os.makedirs(LOCKDIR, exist_ok=True)
    with open(os.path.join(LOCKDIR, name), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            last = float(f.read().strip() or 0)
        except ValueError:
            last = 0
        wait = last + min_interval - time.time()
        if wait > 0:
            time.sleep(wait)
        f.seek(0); f.truncate(); f.write(str(time.time()))


def http_get(url, service, raw=False, tries=5):
    interval = {"inspire": 0.4, "arxiv": 3.1}.get(service, 1.0)
    for i in range(tries):
        _throttle(service, interval)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                return data if raw else data.decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(5 * (i + 1)); continue
            raise
        except urllib.error.URLError:
            if i < tries - 1:
                time.sleep(5 * (i + 1)); continue
            raise


def inspire(q, fields=TRIAGE_FIELDS, sort=None, size=25, page=1):
    if not q.strip():
        sys.exit("refusing empty INSPIRE query (it matches the whole database)")
    p = {"q": q, "size": size, "page": page, "fields": fields}
    if sort:
        p["sort"] = sort
    d = json.loads(http_get(INSPIRE + "?" + urllib.parse.urlencode(p), "inspire"))
    if d["hits"]["total"] > 500_000:
        # INSPIRE silently ignores unparseable queries (e.g. parentheses) and matches everything
        sys.exit(f"query {q!r} matched {d['hits']['total']} records: almost certainly malformed (avoid parentheses)")
    return d


def inspire_all(q, fields=TRIAGE_FIELDS, sort=None, limit=50):
    out, page = [], 1
    size = min(limit, 250)  # page size must stay constant across pages (offset = (page-1)*size)
    while len(out) < limit:
        d = inspire(q, fields, sort, size, page)
        hits = d["hits"]["hits"]
        out += hits
        if len(hits) < size or len(out) >= d["hits"]["total"]:
            break
        page += 1
    return out[:limit], d["hits"]["total"]


# ---------------------------------------------------------------- record normalisation
def norm(meta, abstract=False):
    first = lambda k, sub: (meta.get(k) or [{}])[0].get(sub)
    titles = meta.get("titles") or [{}]
    title = next((t["title"] for t in titles if t.get("source") != "arXiv" and "title" in t),
                 titles[0].get("title"))
    rec = {
        "recid": meta.get("control_number"),
        "texkey": (meta.get("texkeys") or [None])[0],
        "arxiv": first("arxiv_eprints", "value"),
        "doi": first("dois", "value"),
        "year": first("publication_info", "year"),
        "collab": first("collaborations", "value"),
        "doctype": ",".join(meta.get("document_type") or []),
        "citations": meta.get("citation_count"),
        "title": " ".join((title or "").split()),
    }
    if abstract and meta.get("abstracts"):
        rec["abstract"] = " ".join(meta["abstracts"][0]["value"].split())
    return rec


def emit(recs):
    for r in recs:
        print(json.dumps(r, ensure_ascii=False))


def read_stdin_recs():
    return [json.loads(l) for l in sys.stdin if l.strip().startswith("{")]


def fields_for(a):
    return TRIAGE_FIELDS + (",abstracts.value" if getattr(a, "abstract", False) else "")


# ---------------------------------------------------------------- DB
class db_lock:
    """Exclusive lock around load-modify-save, so parallel lr.py calls can't lose updates."""
    def __enter__(self):
        os.makedirs(LOCKDIR, exist_ok=True)
        self.f = open(os.path.join(LOCKDIR, "papers.lock"), "w")
        fcntl.flock(self.f, fcntl.LOCK_EX)
    def __exit__(self, *exc):
        self.f.close()


def load_db():
    if not os.path.exists(DB):
        return []
    with open(DB) as f:
        return [json.loads(l) for l in f if l.strip()]


def merge_missing(old, new):
    """Fill fields the stored record lacks (e.g. an arXiv-only record later found in INSPIRE)."""
    for k in ("recid", "texkey", "arxiv", "doi", "year", "collab", "doctype", "citations", "title"):
        if not old.get(k) and new.get(k):
            old[k] = new[k]


def save_db(recs):
    tmp = DB + ".tmp"
    with open(tmp, "w") as f:
        for r in sorted(recs, key=lambda r: (r.get("texkey") or str(r.get("recid")) or "")):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, DB)


def keys(r):
    ks = set()
    if r.get("recid"): ks.add(("recid", int(r["recid"])))
    if r.get("arxiv"): ks.add(("arxiv", r["arxiv"].lower()))
    if r.get("doi"): ks.add(("doi", r["doi"].lower()))
    if r.get("texkey"): ks.add(("texkey", r["texkey"]))
    return ks


def find(db, ident):
    ident = str(ident)
    for r in db:
        if ident in (str(r["recid"]) if r.get("recid") else None, r.get("texkey"), r.get("arxiv"), r.get("doi"),
                     r.get("bibkey")) or (r.get("texkey") and ident == pid(r)):
            return r
    return None


def pid(r):
    """File-safe paper ID: texkey with ':'->'_', else arXiv/DOI fallback."""
    if r.get("texkey"): return r["texkey"].replace(":", "_")
    if r.get("arxiv"): return "arXiv_" + r["arxiv"].replace("/", "_")
    if r.get("doi"): return "doi_" + re.sub(r"[^A-Za-z0-9.-]", "_", r["doi"])
    return "recid_%s" % r.get("recid")


# ---------------------------------------------------------------- commands
def resolve_ident(s):
    s = s.strip()
    if s.startswith("doi:") or s.startswith("10."): return "doi " + s.removeprefix("doi:")
    if s.startswith("arxiv:") or re.match(r"^(\d{4}\.\d{4,5}|[a-z-]+(\.[A-Z]{2})?/\d{7})(v\d+)?$", s):
        return "arxiv " + re.sub(r"v\d+$", "", s.removeprefix("arxiv:"))
    if s.startswith("recid:") or s.isdigit(): return "recid:" + s.removeprefix("recid:")
    if s.startswith("texkey:") or re.match(r"^[^:\s]+:\d{4}[a-z]+$", s): return "texkey " + s.removeprefix("texkey:")
    return s


def cmd_lookup(a):
    for s in a.ids:
        hits, _ = inspire_all(resolve_ident(s), fields_for(a), limit=3)
        if not hits:
            print(json.dumps({"unresolved": s})); continue
        emit(norm(h["metadata"], a.abstract) for h in hits[:1])


def log_search(service, query, total):
    """Append to litreview/searches.tsv so keyword coverage is auditable and searches aren't re-run blindly."""
    with open(os.path.join(LR, "searches.tsv"), "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d')}\t{service}\t{query}\t{total}\n")


def cmd_search(a):
    hits, tot = inspire_all(a.query, fields_for(a), a.sort, a.limit)
    print(f"# {tot} total, showing {len(hits)}", file=sys.stderr)
    if not getattr(a, "nolog", False):
        log_search("inspire", a.query, tot)
    emit(norm(h["metadata"], a.abstract) for h in hits)


def cmd_citing(a):
    q = f"refersto:recid:{a.recid}" + (f" and {a.filter}" if a.filter else "")  # no parens: INSPIRE ignores them
    a.query, a.nolog = q, not a.filter  # unfiltered citation pulls are recorded via `via`, not searches.tsv
    cmd_search(a)


def resolve_recids(recids, fields):
    out = []
    for i in range(0, len(recids), BATCH):
        chunk = recids[i:i + BATCH]
        d = inspire(" or ".join(f"recid:{r}" for r in chunk), fields, size=len(chunk))
        out += [h["metadata"] for h in d["hits"]["hits"]]
    if len(out) < len(set(recids)):
        print(f"# {len(set(recids)) - len(out)} recids did not resolve (deleted/merged records)", file=sys.stderr)
    return out


def cmd_refs(a):
    d = inspire(f"recid:{a.recid}", "references.record,references.reference", size=1)
    if not d["hits"]["hits"]:
        sys.exit(f"recid {a.recid} not found")
    refs = d["hits"]["hits"][0]["metadata"].get("references", [])
    recids, unresolved = [], []
    for r in refs:
        if "record" in r:
            recids.append(int(r["record"]["$ref"].rsplit("/", 1)[1]))
        else:
            ref = r.get("reference", {})
            unresolved.append({k: ref[k] for k in ("title", "arxiv_eprint", "dois", "publication_info", "misc") if k in ref})
    print(f"# {len(refs)} references: {len(recids)} resolved, {len(unresolved)} unresolved", file=sys.stderr)
    emit(norm(m, a.abstract) for m in resolve_recids(recids, fields_for(a)))
    for u in unresolved:
        print("# unresolved: " + json.dumps(u, ensure_ascii=False)[:300], file=sys.stderr)


def cmd_arxiv(a):
    import xml.etree.ElementTree as ET
    p = {"search_query": a.query, "start": 0, "max_results": a.limit, "sortBy": a.sort, "sortOrder": "descending"}
    xml = http_get("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(p), "arxiv")
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml)
    tot = root.findtext("{http://a9.com/-/spec/opensearch/1.1/}totalResults")
    print(f"# {tot} total", file=sys.stderr)
    log_search("arxiv", a.query, tot)
    for e in root.findall("a:entry", ns):
        rec = {"recid": None, "texkey": None,
               "arxiv": re.sub(r"v\d+$", "", e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1]),
               "doi": e.findtext("arxiv:doi", None, ns),
               "year": int(e.findtext("a:published", "0000", ns)[:4]),
               "title": " ".join(e.findtext("a:title", "", ns).split()),
               "authors": [n.text for n in e.findall("a:author/a:name", ns)][:5]}
        if a.abstract:
            rec["abstract"] = " ".join(e.findtext("a:summary", "", ns).split())
        print(json.dumps(rec, ensure_ascii=False))


def cmd_new(a):
    seen = set().union(*(keys(r) for r in load_db())) if os.path.exists(DB) else set()
    emit(r for r in read_stdin_recs() if not (keys(r) & seen))


def cmd_add(a):
    recs = read_stdin_recs()
    with db_lock():
        db = load_db()
        n = m = 0
        for r in recs:
            r.pop("abstract", None); r.pop("authors", None)
            old = next((o for o in db if keys(o) & keys(r)), None)
            if old:
                merge_missing(old, r)
                if a.via and a.via not in old.setdefault("via", []):
                    old["via"].append(a.via); m += 1
                continue
            r.update(status=a.status, priority=a.priority, relevance=None, rqs=[], reason=a.reason or "",
                     via=[a.via] if a.via else [], fulltext=None, summary=None)
            db.append(r); n += 1
        save_db(db)
    print(f"# added {n} new; {m} existing records gained a 'via' link", file=sys.stderr)


LIST_KEYS = {"rqs", "via", "zotero"}
INT_KEYS = {"relevance", "year", "recid", "citations"}


def parse_val(k, v):
    if v in ("null", "None", ""): return [] if k in LIST_KEYS else None
    if k in LIST_KEYS: return [x.strip() for x in v.split(",") if x.strip()]
    if k in INT_KEYS: return int(v)
    return v


def apply_set(db, ident, kvs):
    r = find(db, ident)
    if not r:
        return f"{ident} not in papers.jsonl"
    new = {}
    for kv in kvs:
        if "=" not in kv:
            return f"bad assignment {kv!r} (want key=value)"
        k, v = kv.split("=", 1)
        try:
            new[k] = parse_val(k, v)
        except ValueError:
            return f"{k} must be an integer, got {v!r}"
    if "status" in new and new["status"] not in STATUSES:
        return f"bad status {new['status']}; one of {STATUSES}"
    if "priority" in new and new["priority"] not in ("next", "later"):
        return "priority must be next or later"
    if new.get("relevance") is not None and not 0 <= new["relevance"] <= 3:
        return "relevance must be 0-3"
    r.update(new)
    return r


def cmd_set(a):
    with db_lock():
        db = load_db()
        r = apply_set(db, a.id, a.kv)
        if isinstance(r, str):
            sys.exit(r)
        save_db(db)
    print(json.dumps({k: r.get(k) for k in ("texkey", "status", "priority", "relevance", "rqs", "type", "summary")}, ensure_ascii=False))


def cmd_setmany(a):
    """stdin lines: ID key=value key="value with spaces" ...  (all-or-nothing)"""
    import shlex
    with db_lock():
        db = load_db()
        errors, n = [], 0
        for line in sys.stdin:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = shlex.split(line)
            r = apply_set(db, parts[0], parts[1:])
            if isinstance(r, str):
                errors.append(r)
            else:
                n += 1
        if errors:
            sys.exit("no changes saved; errors:\n" + "\n".join(errors))
        save_db(db)
    print(f"# updated {n} records", file=sys.stderr)


def cmd_show(a):
    db = load_db()
    for i in a.ids:
        print(json.dumps(find(db, i) or {"missing": i}, ensure_ascii=False))


def cmd_list(a):
    """Compact, paginated listing. Candidates are ranked by how many reviewed papers point to them (len(via))."""
    rs = [r for r in load_db() if (not a.status or r.get("status") == a.status)
          and (a.priority is None or r.get("priority") == a.priority)]
    rs.sort(key=lambda r: (-len(r.get("via") or []), -(r.get("citations") or 0)))
    page = rs[a.offset:a.offset + a.limit]
    print(f"# {len(rs)} matching; showing {a.offset}-{a.offset + len(page)}", file=sys.stderr)
    abstracts = {}
    if a.abstract:
        ids = [r["recid"] for r in page if r.get("recid")]
        abstracts = {m["control_number"]: " ".join(m["abstracts"][0]["value"].split())
                     for m in resolve_recids(ids, "control_number,abstracts.value") if m.get("abstracts")}
    for r in page:
        out = {"id": r.get("texkey") or r.get("arxiv") or r.get("doi"), "recid": r.get("recid"), "year": r.get("year"),
               "cites": r.get("citations"), "nvia": len(r.get("via") or []), "status": r.get("status"),
               "rel": r.get("relevance"), "title": (r.get("title") or "")[:150]}
        if a.abstract:
            out["abstract"] = abstracts.get(r.get("recid"), "")[:a.abstract_chars]
        print(json.dumps(out, ensure_ascii=False))


# ---- full text
def zotero_pdfs(file_field):
    out = []
    for p in file_field.split(";"):
        p = p.replace("\\:", ":").replace("\\\\", "\\").strip()
        if p.lower().endswith(".pdf") and p.startswith("C:\\Users\\simon\\Zotero\\storage\\"):
            key, name = p.split("\\")[5:7]
            path = os.path.join(ZOTERO, key, name)
            if not os.path.exists(path):
                # the bib export strips {} from filenames; one storage dir == one attachment, so take its pdf
                cands = [f for f in os.listdir(os.path.join(ZOTERO, key))
                         if f.lower().endswith(".pdf")] if os.path.isdir(os.path.join(ZOTERO, key)) else []
                path = os.path.join(ZOTERO, key, cands[0]) if len(cands) == 1 else None
            if path:
                out.append(path)
    return out


def pdftotext(pdf, txt):
    subprocess.run(["pdftotext", "-layout", pdf, txt], check=False)
    return os.path.exists(txt) and os.path.getsize(txt) > 2000  # tiny => probably a scan without text layer


def download_pdf(url, service, dest):
    """Download atomically; reject non-PDF responses (HTML error/captcha pages). Returns True on success."""
    if os.path.exists(dest):
        return True
    try:
        data = http_get(url, service, raw=True)
    except urllib.error.HTTPError as e:
        print(f"# download failed ({e.code}): {url}", file=sys.stderr)
        return False
    if not data.startswith(b"%PDF"):
        print(f"# not a PDF ({data[:40]!r}...): {url}", file=sys.stderr)
        return False
    with open(dest + ".tmp", "wb") as f:
        f.write(data)
    os.replace(dest + ".tmp", dest)
    return True


def cmd_fetch(a):
    with db_lock():
        r = find(load_db(), a.id)
    if not r:
        sys.exit(f"{a.id} not in papers.jsonl")
    os.makedirs(PAPERS, exist_ok=True)
    base = os.path.join(PAPERS, pid(r))
    res = {"id": pid(r)}
    if r.get("zotero"):
        pdf = r["zotero"][0]
        res.update(source="zotero", pdf=pdf, text_layer=pdftotext(pdf, base + ".txt"))
    if not res.get("source") and r.get("arxiv") and download_pdf(f"https://arxiv.org/pdf/{r['arxiv']}", "arxiv", base + ".pdf"):
        res.update(source="arxiv", pdf=base + ".pdf", text_layer=pdftotext(base + ".pdf", base + ".txt"))
    if a.source:
        if r.get("arxiv"):
            data = http_get(f"https://arxiv.org/e-print/{r['arxiv']}", "arxiv", raw=True)
            os.makedirs(base, exist_ok=True)
            try:
                tarfile.open(fileobj=io.BytesIO(data), mode="r:gz").extractall(base, filter="data")
            except tarfile.ReadError:
                with open(os.path.join(base, "main.tex"), "wb") as f:
                    f.write(gzip.decompress(data))
            res["latex_dir"] = base
        else:
            print("# --source ignored: no arXiv id", file=sys.stderr)
    if not res.get("source") and r.get("recid"):
        d = inspire(f"recid:{r['recid']}", "documents.url,documents.filename,urls.value", size=1)
        m = d["hits"]["hits"][0]["metadata"] if d["hits"]["hits"] else {}
        for doc in (x for x in m.get("documents", []) if x.get("filename", "").lower().endswith(".pdf")):
            if download_pdf(doc["url"], "inspire", base + ".pdf"):
                res.update(source="inspire-doc", pdf=base + ".pdf", text_layer=pdftotext(base + ".pdf", base + ".txt"))
                break
        if not res.get("source"):
            res["urls"] = [u["value"] for u in m.get("urls", [])]
    if res.get("source"):
        res["txt"] = base + ".txt" if os.path.exists(base + ".txt") else None
    with db_lock():  # re-load: other lr.py calls may have written while we were downloading
        db = load_db()
        rr = find(db, a.id)
        if res.get("source"):
            rr["fulltext"] = res["source"]
            if rr.get("status") == "blocked":
                rr["status"] = "queued"
        else:
            rr["status"] = "blocked"
            res["blocked"] = True
        save_db(db)
    print(json.dumps(res, ensure_ascii=False))


# ---- seeding
def parse_bib(text):
    entries = []
    for m in re.finditer(r"@(\w+)\{([^,]+),", text):
        i, depth, start = m.end(), 1, m.end()
        while depth and i < len(text):
            depth += {"{": 1, "}": -1}.get(text[i], 0); i += 1
        body, fields = text[start:i - 1], {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", body):
            j, d = fm.end(), 1
            while d and j < len(body):
                d += {"{": 1, "}": -1}.get(body[j], 0); j += 1
            fields.setdefault(fm.group(1).lower(), body[fm.end():j - 1])
        entries.append({"bibkey": m.group(2), **fields})
    return entries


def clean_title(t):
    t = re.sub(r"\\[a-zA-Z]+|[{}$\\^_]", " ", t)
    return " ".join(t.split())


def cmd_seed(a):
    """Import a Zotero biblatex export. New entries -> queued/next; existing ones gain Zotero paths
    (and blocked -> queued). Use with --bib for Zotero exports of papers the user downloaded on request."""
    bib = a.bib or BIB
    tag = os.path.splitext(os.path.basename(bib))[0]
    resolved = []
    for e in parse_bib(open(bib, encoding="utf-8").read()):  # network part outside the DB lock
        hits, match = [], None
        if e.get("doi"):
            hits, _ = inspire_all("doi " + e["doi"], limit=1); match = "doi"
        if not hits and e.get("eprint"):
            hits, _ = inspire_all("arxiv " + e["eprint"], limit=1); match = "arxiv"
        if not hits and e.get("title"):
            words = [w for w in clean_title(e["title"]).split() if len(w) > 3][:8]
            if words:
                hits, _ = inspire_all(" and ".join(f"t {w}" for w in words), limit=2); match = "title"
        if hits:
            r = norm(hits[0]["metadata"])
            if match == "title":
                r["match"] = "title-search: verify"
        else:
            y = (e.get("date") or e.get("year") or "")[:4]
            r = {"recid": None, "texkey": None, "arxiv": e.get("eprint"), "doi": e.get("doi"),
                 "year": int(y) if y.isdigit() else None, "title": clean_title(e.get("title", "")), "unresolved": True}
        r["bibkey"] = e["bibkey"]
        r["zotero"] = zotero_pdfs(e.get("file", ""))
        resolved.append(r)
    with db_lock():
        db = load_db()
        for r in resolved:
            old = next((o for o in db if keys(o) & keys(r)), None)
            if old:
                merge_missing(old, r)
                old["bibkey"] = r["bibkey"]
                if r["zotero"]:
                    old["zotero"] = r["zotero"]
                    if old.get("status") == "blocked":
                        old["status"] = "queued"
                if tag not in old.setdefault("via", []):
                    old["via"].append(tag)
                state = "updated"
            else:
                r.update(status="queued", priority="next", relevance=None, rqs=[], reason=tag,
                         via=[tag], fulltext=None, summary=None)
                db.append(r)
                state = "new"
            print(json.dumps({k: r.get(k) for k in ("bibkey", "recid", "texkey", "unresolved", "match") if r.get(k) is not None}
                             | {"zotero_pdfs": len(r["zotero"]), "state": state}, ensure_ascii=False))
        save_db(db)


# ---- rendering
def md_escape(s):
    return str(s if s is not None else "").replace("|", "\\|")


def cmd_render(a):
    db = load_db()
    order = {s: i for i, s in enumerate(["read", "skimmed", "queued", "blocked", "candidate", "rejected"])}
    db.sort(key=lambda r: (order.get(r.get("status"), 9), -(r.get("relevance") or 0), int(r.get("year") or 0)))
    counts = {s: sum(r.get("status") == s for r in db) for s in STATUSES}
    L = ["# Papers considered", "", "_Generated by `lr.py render` from `papers.jsonl` — do not edit by hand._", "",
         "Counts: " + ", ".join(f"{s} {n}" for s, n in counts.items() if n), "",
         "| ID | Year | Title | Type | Status | Rel | RQs | Summary / reason |", "|---|---|---|---|---|---|---|---|"]
    for r in db:
        ident = r.get("texkey") or r.get("arxiv") or r.get("doi") or "?"
        link = f"[{md_escape(ident)}](https://inspirehep.net/literature/{r['recid']})" if r.get("recid") else md_escape(ident)
        summ = f"[summary]({r['summary']})" if r.get("summary") else md_escape(r.get("reason"))
        L.append(f"| {link} | {md_escape(r.get('year'))} | {md_escape(r.get('title'))} | {md_escape(r.get('type'))} | "
                 f"{r.get('status')} | {md_escape(r.get('relevance'))} | {md_escape(','.join(map(str, r.get('rqs') or [])))} | {summ} |")
    open(os.path.join(LR, "papers.md"), "w").write("\n".join(L) + "\n")

    Q = ["# Reading queue", "", "_Generated by `lr.py render` from `papers.jsonl` — do not edit by hand._", ""]
    def section(title, rs):
        Q.extend([f"## {title} ({len(rs)})", ""])
        for r in rs:
            ident = r.get("texkey") or r.get("arxiv") or r.get("doi")
            extra = f" — DOI {r['doi']}" if title.startswith("Blocked") and r.get("doi") else ""
            Q.append(f"- **{ident}** ({r.get('year')}) {r.get('title')} — _{r.get('reason') or '; '.join(r.get('via') or [])}_{extra}")
        Q.append("")
    q = [r for r in db if r.get("status") == "queued"]
    section("Next", [r for r in q if r.get("priority") == "next"])
    section("Later", [r for r in q if r.get("priority") != "next"])
    section("Blocked: needs full text", [r for r in db if r.get("status") == "blocked"])
    section("Candidates awaiting triage", [r for r in db if r.get("status") == "candidate"])
    open(os.path.join(LR, "queue.md"), "w").write("\n".join(Q))
    print(f"# rendered papers.md ({len(db)} rows) and queue.md", file=sys.stderr)


def cmd_bibtex(a):
    rel = [r for r in load_db() if (r.get("relevance") or 0) >= a.min_rel]
    db = [r for r in rel if r.get("recid")]
    if len(db) < len(rel):
        print(f"# skipped {len(rel) - len(db)} relevant records without INSPIRE recid: "
              + ", ".join(pid(r) for r in rel if not r.get("recid")), file=sys.stderr)
    chunks = []
    for i in range(0, len(db), BATCH):
        q = " or ".join(f"recid:{r['recid']}" for r in db[i:i + BATCH])
        url = INSPIRE + "?" + urllib.parse.urlencode({"q": q, "size": BATCH, "format": "bibtex"})
        chunks.append(http_get(url, "inspire"))
    out = os.path.join(LR, a.out)
    open(out, "w").write("\n".join(chunks))
    print(f"# wrote {len(db)} entries to {out}", file=sys.stderr)


def main():
    P = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    S = P.add_subparsers(dest="cmd", required=True)
    def sp(name, fn, **kw):
        p = S.add_parser(name, **kw); p.set_defaults(fn=fn); return p
    def common(p, sort="mostcited"):
        p.add_argument("--abstract", action="store_true", help="include abstracts (verbose!)")
        p.add_argument("--limit", type=int, default=25)
        p.add_argument("--sort", default=sort)
    p = sp("lookup", cmd_lookup); p.add_argument("ids", nargs="+"); p.add_argument("--abstract", action="store_true")
    p = sp("search", cmd_search); p.add_argument("query"); common(p)
    p = sp("refs", cmd_refs); p.add_argument("recid", type=int); p.add_argument("--abstract", action="store_true")
    p = sp("citing", cmd_citing); p.add_argument("recid", type=int); p.add_argument("--filter"); common(p)
    p = sp("arxiv", cmd_arxiv); p.add_argument("query"); common(p, sort="submittedDate")
    sp("new", cmd_new)
    p = sp("add", cmd_add); p.add_argument("--status", default="candidate", choices=STATUSES)
    p.add_argument("--priority", default="later", choices=["next", "later"]); p.add_argument("--via"); p.add_argument("--reason")
    p = sp("set", cmd_set); p.add_argument("id"); p.add_argument("kv", nargs="+", help="key=value; lists as a,b,c")
    p = sp("show", cmd_show); p.add_argument("ids", nargs="+")
    sp("setmany", cmd_setmany, help="stdin lines: ID key=value ...")
    p = sp("list", cmd_list); p.add_argument("--status"); p.add_argument("--priority")
    p.add_argument("--limit", type=int, default=40); p.add_argument("--offset", type=int, default=0)
    p.add_argument("--abstract", action="store_true", help="fetch abstracts from INSPIRE (for triage)")
    p.add_argument("--abstract-chars", type=int, default=600)
    p = sp("fetch", cmd_fetch); p.add_argument("id"); p.add_argument("--source", action="store_true", help="also fetch arXiv LaTeX source")
    p = sp("seed", cmd_seed); p.add_argument("--bib", help="biblatex file (default: litreview/human_start.bib)")
    sp("render", cmd_render)
    p = sp("bibtex", cmd_bibtex); p.add_argument("--min-rel", type=int, default=2); p.add_argument("--out", default="review.bib")
    a = P.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
