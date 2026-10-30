#!/usr/bin/env python3
"""Regression tests for lr.py. Offline by default (HTTP is faked); LR_LIVE=1 adds live API smoke tests.

    python3 .claude/skills/literature-review/scripts/test_lr.py            # offline, ~1 s
    LR_LIVE=1 python3 .claude/skills/literature-review/scripts/test_lr.py  # + live INSPIRE/arXiv

State goes to a throwaway dir inside ~/colorflow (HARD RULE: no /tmp), removed afterwards.
"""
import contextlib, io, json, os, shutil, subprocess, sys, unittest
from types import SimpleNamespace as NS

HERE = os.path.dirname(os.path.abspath(__file__))
TESTDIR = os.path.expanduser(f"~/colorflow/.lrtest-{os.getpid()}")
os.environ["LR_DIR"] = TESTDIR
sys.path.insert(0, HERE)
import lr  # noqa: E402

LIVE = os.environ.get("LR_LIVE") == "1"


def meta(recid, texkey=None, arxiv=None, doi=None, year=2000, title="T", cites=0, pubinfo=None):
    m = {"control_number": recid, "texkeys": [texkey or f"A:{recid}"], "titles": [{"title": title}],
         "citation_count": cites, "publication_info": pubinfo if pubinfo is not None else [{"year": year}]}
    if arxiv: m["arxiv_eprints"] = [{"value": arxiv}]
    if doi: m["dois"] = [{"value": doi}]
    return m


class FakeInspire:
    """Stands in for lr.inspire(): serves a fixed result list with real size/page offset semantics."""
    def __init__(self, metas, total=None):
        self.metas, self.total, self.calls = metas, total, []

    def __call__(self, q, fields=None, sort=None, size=25, page=1):
        self.calls.append((q, size, page))
        lo = (page - 1) * size
        return {"hits": {"total": self.total or len(self.metas),
                         "hits": [{"metadata": m} for m in self.metas[lo:lo + size]]}}


def write(path, text):
    with open(path, "w") as f:
        f.write(text)


def run(fn, args, stdin=""):
    out, err = io.StringIO(), io.StringIO()
    old = sys.stdin
    sys.stdin = io.StringIO(stdin)
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            fn(args)
    finally:
        sys.stdin = old
    return out.getvalue(), err.getvalue()


def recs(stdout):
    return [json.loads(l) for l in stdout.splitlines() if l.startswith("{")]


class Base(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(TESTDIR, ignore_errors=True)
        os.makedirs(TESTDIR)
        self._orig = (lr.inspire, lr.http_get, lr.ZOTERO)

    def tearDown(self):
        lr.inspire, lr.http_get, lr.ZOTERO = self._orig

    def add(self, *metas, via="v", status="candidate"):
        lines = "\n".join(json.dumps(lr.norm(m)) for m in metas)
        return run(lr.cmd_add, NS(status=status, priority="later", via=via, reason=""), lines)


class TestQueries(Base):
    def test_pagination_constant_page_size(self):
        fake = FakeInspire([meta(i) for i in range(1, 601)])
        lr.inspire = fake
        hits, _ = lr.inspire_all("q", limit=260)
        ids = [h["metadata"]["control_number"] for h in hits]
        self.assertEqual(ids, list(range(1, 261)))
        self.assertEqual({c[1] for c in fake.calls}, {250})

    def test_guard_raises_not_exits(self):
        lr.http_get = lambda *a, **k: json.dumps({"hits": {"total": 1_600_000, "hits": []}})
        with self.assertRaises(lr.QueryError):
            lr.inspire("refersto:recid:1 and (t x)")
        with self.assertRaises(lr.QueryError):
            lr.inspire("  ")

    def test_year_from_any_publication_info(self):
        m = meta(1, pubinfo=[{"journal_title": "Proc"}, {"year": 1994}])
        self.assertEqual(lr.norm(m)["year"], 1994)
        self.assertIsNone(lr.norm(meta(2, pubinfo=[]))["year"])

    def test_title_prefers_non_arxiv(self):
        m = meta(1); m["titles"] = [{"source": "arXiv", "title": "plain"}, {"title": "$\\LaTeX$"}]
        self.assertEqual(lr.norm(m)["title"], "$\\LaTeX$")

    def test_resolve_ident(self):
        self.assertEqual(lr.resolve_ident("10.1103/X"), "doi 10.1103/X")
        self.assertEqual(lr.resolve_ident("1311.5815v2"), "arxiv 1311.5815")
        self.assertEqual(lr.resolve_ident("hep-ph/9405123"), "arxiv hep-ph/9405123")
        self.assertEqual(lr.resolve_ident("374155"), "recid:374155")
        self.assertEqual(lr.resolve_ident("CDF:1994zkl"), "texkey CDF:1994zkl")


class TestDB(Base):
    def test_add_dedups_and_counts_via(self):
        self.add(meta(1), meta(2), via="ref of X")
        _, err = self.add(meta(2), meta(3), via="ref of Y")
        self.assertIn("added 1 new; 1 existing", err)
        db = {r["recid"]: r for r in lr.load_db()}
        self.assertEqual(db[2]["via"], ["ref of X", "ref of Y"])
        self.assertEqual(len(db), 3)

    def test_list_ranks_by_nvia(self):
        self.add(meta(1, cites=100), meta(2, cites=1), via="ref of recid:7")
        self.add(meta(2), via="cites recid:8")
        out, _ = run(lr.cmd_list, NS(status="candidate", priority=None, limit=10, offset=0, abstract=False))
        self.assertEqual([r["recid"] for r in recs(out)], [2, 1])

    def test_arxiv_stub_merges_with_inspire_record(self):
        run(lr.cmd_add, NS(status="candidate", priority="later", via="arxiv", reason=""),
            json.dumps({"recid": None, "texkey": None, "arxiv": "1311.5815", "title": "t", "authors": ["x"]}))
        self.add(meta(1265659, "CMS:2013cvx", arxiv="1311.5815"), via="inspire")
        (r,) = lr.load_db()
        self.assertEqual((r["recid"], r["texkey"], r["via"]), (1265659, "CMS:2013cvx", ["arxiv", "inspire"]))
        self.assertNotIn("authors", r)

    def test_records_without_ids_are_ignored(self):
        _, err = run(lr.cmd_add, NS(status="candidate", priority="later", via="v", reason=""),
                     '{"unresolved": "foo"}\n' + json.dumps(lr.norm(meta(1))))
        self.assertIn("ignored 1", err)
        self.assertEqual(len(lr.load_db()), 1)

    def test_set_validation(self):
        self.add(meta(1, "A:2000a"))
        for bad in (["relevance=7"], ["expect=4"], ["status=bogus"], ["priority=soon"], ["relevence=3"],
                    ["type=experiment"], ["relevance=high"], ["noequals"]):
            self.assertIsInstance(lr.apply_set(lr.load_db(), "A:2000a", bad), str, bad)
        db = lr.load_db()
        r = lr.apply_set(db, "A_2000a", ["reason=a,b", "rqs=3", "relevance=2", "expect=3", "type=exp"])
        self.assertEqual((r["reason"], r["rqs"], r["relevance"], r["expect"]), ("a,b", ["3"], 2, 3))

    def test_setmany_all_or_nothing(self):
        self.add(meta(1, "A:2000a"))
        with self.assertRaises(SystemExit):
            run(lr.cmd_setmany, NS(), 'A:2000a status=read\nNope:1999x status=read\n')
        self.assertEqual(lr.load_db()[0]["status"], "candidate")
        run(lr.cmd_setmany, NS(), 'A:2000a status=read reason="first read, good"\n# comment\n')
        r = lr.load_db()[0]
        self.assertEqual((r["status"], r["reason"]), ("read", "first read, good"))

    def test_parallel_adds_lose_nothing(self):
        lines = lambda rng: "\n".join(json.dumps(lr.norm(meta(i))) for i in rng)
        cmd = [sys.executable, os.path.join(HERE, "lr.py"), "add", "--via"]
        env = dict(os.environ, LR_DIR=TESTDIR)
        ps = [subprocess.Popen(cmd + [f"p{k}"], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL, env=env, text=True)
              for k in range(4)]
        for k, p in enumerate(ps):
            p.stdin.write(lines(range(k * 50, k * 50 + 60))); p.stdin.close()  # overlapping ranges
        for p in ps:
            p.wait()
        db = lr.load_db()
        self.assertEqual(len(db), 210)
        self.assertEqual(len({r["recid"] for r in db}), 210)


class TestFetch(Base):
    def setUp(self):
        super().setUp()
        self.zot = os.path.join(TESTDIR, "zotero")
        os.makedirs(os.path.join(self.zot, "KEY1"))
        write(os.path.join(self.zot, "KEY1", "Abe - 1994 - ensuremath{.pdf"), "x")
        lr.ZOTERO = self.zot

    def test_zotero_brace_fallback(self):
        field = (r"C\:\\Users\\simon\\Zotero\\storage\\KEY1\\Abe - 1994 - ensuremath .pdf;"
                 r"C\:\\Users\\simon\\Zotero\\storage\\KEY2\\x.html")
        self.assertEqual(lr.zotero_pdfs(field), [os.path.join(self.zot, "KEY1", "Abe - 1994 - ensuremath{.pdf")])

    def _fetch(self, ident):
        out, err = run(lr.cmd_fetch, NS(id=ident, source=False))
        return json.loads(out), err

    def test_blocked_then_status_rules(self):
        lr.inspire = FakeInspire([{"control_number": 5, "urls": [{"value": "https://pub/x"}]}])
        self.add(meta(5, "B:1980a"), status="queued")
        res, _ = self._fetch("B:1980a")
        self.assertTrue(res["blocked"]); self.assertEqual(res["urls"], ["https://pub/x"])
        self.assertEqual(lr.load_db()[0]["status"], "blocked")
        # read papers must not be demoted to blocked by a failed re-fetch
        db = lr.load_db(); db[0]["status"] = "read"; lr.save_db(db)
        res, _ = self._fetch("B:1980a")
        self.assertNotIn("blocked", res)
        self.assertEqual(lr.load_db()[0]["status"], "read")

    def test_non_pdf_download_rejected(self):
        lr.http_get = lambda *a, **k: b"<!DOCTYPE html>"
        dest = os.path.join(TESTDIR, "x.pdf")
        self.assertFalse(lr.download_pdf("u", "arxiv", dest))
        self.assertFalse(os.path.exists(dest))

    def test_arxiv_fetch_and_unblock(self):
        pdf = b"%PDF-1.4 fake"
        lr.http_get = lambda *a, **k: pdf
        self.add(meta(7, "C:2014a", arxiv="1311.5815"), status="queued")
        db = lr.load_db(); db[0]["status"] = "blocked"; lr.save_db(db)
        res, _ = self._fetch("C:2014a")
        self.assertEqual(res["source"], "arxiv")
        r = lr.load_db()[0]
        self.assertEqual((r["status"], r["fulltext"]), ("queued", "arxiv"))

    def test_missing_zotero_file_falls_through(self):
        lr.http_get = lambda *a, **k: b"<html>"
        lr.inspire = FakeInspire([{"control_number": 8}])
        self.add(meta(8, "D:1990a"), status="queued")
        db = lr.load_db(); db[0]["zotero"] = ["/nonexistent.pdf"]; lr.save_db(db)
        res, err = self._fetch("D:1990a")
        self.assertIn("no longer exist", err)
        self.assertTrue(res.get("blocked"))


class TestSeed(Base):
    BIB = r"""@article{good2014,
  title = {Good {{Paper}}},
  doi = {10.1/good},
  file = {C\:\\Users\\simon\\Zotero\\storage\\KEY1\\Abe - 1994 - ensuremath .pdf}
}
@article{orphan1980,
  title = {Nothing Matches This},
  date = {1980-01-01}
}
"""

    def test_seed_idempotent_and_unblocks(self):
        bib = os.path.join(TESTDIR, "zotero_new.bib")
        write(bib, self.BIB)
        os.makedirs(os.path.join(TESTDIR, "zotero", "KEY1"))
        write(os.path.join(TESTDIR, "zotero", "KEY1", "Abe - 1994 - ensuremath{.pdf"), "x")
        lr.ZOTERO = os.path.join(TESTDIR, "zotero")

        def fake(q, fields=None, sort=None, size=25, page=1):
            hit = [{"metadata": meta(11, "G:2014a", doi="10.1/good")}] if q == "doi 10.1/good" else []
            return {"hits": {"total": len(hit), "hits": hit}}
        lr.inspire = fake
        # pre-existing blocked record for the good paper
        self.add(meta(11, "G:2014a", doi="10.1/good"), status="blocked")
        run(lr.cmd_seed, NS(bib=bib))
        run(lr.cmd_seed, NS(bib=bib))  # second run must not duplicate
        db = {r.get("bibkey"): r for r in lr.load_db()}
        self.assertEqual(len(lr.load_db()), 2)
        self.assertEqual(db["good2014"]["status"], "queued")
        self.assertEqual(len(db["good2014"]["zotero"]), 1)
        self.assertTrue(db["orphan1980"]["unresolved"])
        self.assertEqual(db["orphan1980"]["year"], 1980)

    def test_parse_bib_nested_braces(self):
        (e,) = lr.parse_bib("@article{k1,\n  title = {A {{B}} c},\n  doi = {10.1/x}\n}\n")
        self.assertEqual((e["bibkey"], e["title"], e["doi"]), ("k1", "A {{B}} c", "10.1/x"))


class TestPass3(Base):
    def test_year_falls_back_to_earliest_date(self):
        m = meta(1, pubinfo=[]); m["earliest_date"] = "2014-11-02"
        self.assertEqual(lr.norm(m)["year"], 2014)

    def test_setmany_reports_unbalanced_quotes(self):
        self.add(meta(1, "A:2000a"))
        with self.assertRaises(SystemExit) as cm:
            run(lr.cmd_setmany, NS(), "A:2000a reason=Sjostrand's model\n")
        self.assertIn("cannot parse line", str(cm.exception.code))
        run(lr.cmd_setmany, NS(), 'A:2000a reason="Sjostrand\'s model"\n')
        self.assertEqual(lr.load_db()[0]["reason"], "Sjostrand's model")

    def test_parse_bib_ignores_assignments_inside_values(self):
        (e,) = lr.parse_bib("@article{k,\n  abstract = {we set doi = {fake} here},\n  doi = {10.1/real}\n}\n")
        self.assertEqual(e["doi"], "10.1/real")

    def test_seed_clears_unresolved_once_resolved(self):
        bib = os.path.join(TESTDIR, "b.bib")
        write(bib, "@article{k,\n  title = {Some Long Title Words},\n  doi = {10.1/x}\n}\n")
        lr.inspire = lambda *a, **k: {"hits": {"total": 0, "hits": []}}
        run(lr.cmd_seed, NS(bib=bib))
        self.assertTrue(lr.load_db()[0]["unresolved"])
        lr.inspire = lambda q, *a, **k: {"hits": {"total": 1, "hits": [{"metadata": meta(9, "K:2001a", doi="10.1/x")}]}}
        run(lr.cmd_seed, NS(bib=bib))
        (r,) = lr.load_db()
        self.assertEqual((r["recid"], r.get("unresolved")), (9, None))

    def test_source_not_gzip_is_reported(self):
        lr.http_get = lambda url, *a, **k: b"%PDF-1.4 only"
        self.add(meta(3, "S:2010a", arxiv="1001.0001"), status="queued")
        out, err = run(lr.cmd_fetch, NS(id="S:2010a", source=True))
        self.assertIn("no LaTeX source", err)
        self.assertNotIn("latex_dir", json.loads(out))

    def test_openalex_pdf_used_when_others_fail(self):
        def http(url, service, raw=False, **k):
            if "openalex" in url:
                return json.dumps({"open_access": {"oa_url": "https://land"}, "best_oa_location": {"pdf_url": "https://oa.pdf"}})
            return b"%PDF-1.4 oa" if url == "https://oa.pdf" else b"<html>"
        lr.http_get = http
        lr.inspire = FakeInspire([{"control_number": 4}])
        self.add(meta(4, "O:1985a", doi="10.1/oa"), status="queued")
        res = json.loads(run(lr.cmd_fetch, NS(id="O:1985a", source=False))[0])
        self.assertEqual(res["source"], "openalex")
        self.assertEqual(lr.load_db()[0]["status"], "queued")

    def test_openalex_landing_page_reported_when_blocked(self):
        lr.http_get = lambda url, *a, **k: (json.dumps({"open_access": {"oa_url": "https://land"}, "best_oa_location": None})
                                             if "openalex" in url else b"<html>")
        lr.inspire = FakeInspire([{"control_number": 6}])
        self.add(meta(6, "L:1985a", doi="10.1/land"), status="queued")
        res = json.loads(run(lr.cmd_fetch, NS(id="L:1985a", source=False))[0])
        self.assertEqual((res.get("blocked"), res.get("oa_url")), (True, "https://land"))

    def test_list_abstracts_for_arxiv_only_records(self):
        run(lr.cmd_add, NS(status="candidate", priority="later", via="v", reason=""),
            json.dumps({"recid": None, "texkey": None, "arxiv": "2610.00001", "title": "t"}))
        lr.inspire = FakeInspire([])
        atom = ('<feed xmlns="http://www.w3.org/2005/Atom" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">'
                '<opensearch:totalResults>1</opensearch:totalResults><entry><id>http://arxiv.org/abs/2610.00001v1</id>'
                '<title>t</title><summary>An abstract.</summary><published>2026-10-01T00:00:00Z</published></entry></feed>')
        lr.http_get = lambda *a, **k: atom
        out, _ = run(lr.cmd_list, NS(status="candidate", priority=None, limit=5, offset=0, abstract=True, abstract_chars=50))
        self.assertEqual(recs(out)[0]["abstract"], "An abstract.")

    def test_cli_errors_are_one_line(self):
        env = dict(os.environ, LR_DIR=TESTDIR)
        cmd = [sys.executable, os.path.join(HERE, "lr.py")]
        p = subprocess.run(cmd + ["search", "x", "--sort", "bogus"], env=env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)  # argparse rejects bad sort
        p = subprocess.run(cmd + ["set", "Nope:1999x", "status=read"], env=env, capture_output=True, text=True)
        self.assertNotIn("Traceback", p.stderr)

    def test_add_scales(self):
        import time as _t
        self.add(*[meta(i) for i in range(1, 5001)])
        t0 = _t.time()
        self.add(*[meta(i) for i in range(4500, 5500)], via="w")
        self.assertLess(_t.time() - t0, 5)
        self.assertEqual(len(lr.load_db()), 5499)


class TestVia(Base):
    def test_citing_pulls_count_once_and_refs_add(self):
        lr.inspire = FakeInspire([meta(1), meta(2)])
        out1, _ = run(lr.cmd_citing, NS(recid=99, filter=None, abstract=False, limit=2, sort="mostcited"))
        out2, _ = run(lr.cmd_citing, NS(recid=99, filter=None, abstract=False, limit=2, sort="mostrecent"))
        for out in (out1, out2):
            run(lr.cmd_add, NS(status="candidate", priority="later", via="ignored", reason=""), out)
        r = lr.find(lr.load_db(), "1")
        self.assertEqual((r["via"], lr.nvia(r)), (["cites recid:99"], 1))
        lr.inspire = FakeInspire([{"control_number": 98, "references": [{"record": {"$ref": "x/literature/1"}}]}])
        refs_meta = FakeInspire([meta(1)])
        calls = iter([lr.inspire, refs_meta])
        lr.inspire = lambda *a, **k: next(calls)(*a, **k)
        out, _ = run(lr.cmd_refs, NS(recid=98, abstract=False, show_unresolved=0))
        run(lr.cmd_add, NS(status="candidate", priority="later", via=None, reason=""), out)
        r = lr.find(lr.load_db(), "1")
        self.assertEqual(lr.nvia(r), 2)

    def test_search_hits_do_not_count_toward_nvia(self):
        lr.inspire = FakeInspire([meta(1)])
        out, _ = run(lr.cmd_search, NS(query="t x", abstract=False, limit=1, sort="mostcited"))
        run(lr.cmd_add, NS(status="candidate", priority="later", via=None, reason=""), out)
        r = lr.load_db()[0]
        self.assertEqual((r["via"], lr.nvia(r)), (["search: t x"], 0))

class TestPass3b(Base):
    def test_refs_filter_uses_citedby_and_ref_label(self):
        fake = FakeInspire([meta(1)])
        lr.inspire = fake
        out, _ = run(lr.cmd_refs, NS(recid=5, abstract=False, show_unresolved=0, filter="t coherence"))
        self.assertEqual(fake.calls[0][0], "citedby:recid:5 and t coherence")
        self.assertEqual(recs(out)[0]["_via"], "ref of recid:5")

    def test_list_ranks_expect_first(self):
        self.add(meta(1, cites=999), meta(2, cites=1), via="ref of recid:7", status="queued")
        db = lr.load_db(); lr.apply_set(db, "2", ["expect=3"]); lr.save_db(db)
        out, _ = run(lr.cmd_list, NS(status="queued", priority=None, limit=10, offset=0, abstract=False))
        self.assertEqual([r["recid"] for r in recs(out)], [2, 1])

class TestRender(Base):
    def test_render_mixed_years_and_pipes(self):
        self.add(meta(1, title="a | b"), meta(2, pubinfo=[]))
        db = lr.load_db(); db[0]["year"] = "1999"; lr.save_db(db)
        run(lr.cmd_render, NS())
        with open(os.path.join(TESTDIR, "papers.md")) as f:
            md = f.read()
        self.assertIn("a \\| b", md)
        self.assertTrue(os.path.exists(os.path.join(TESTDIR, "queue.md")))


class TestHook(unittest.TestCase):
    HOOK = os.path.join(HERE, "..", "..", "..", "hooks", "path_guard.py")
    P = os.path.expanduser("~/colorflow")

    def code(self, tool, **inp):
        ev = json.dumps({"tool_name": tool, "tool_input": inp, "cwd": self.P})
        return subprocess.run([sys.executable, self.HOOK], input=ev, text=True, capture_output=True).returncode

    def test_cases(self):
        z = "/mnt/c/Users/simon/Zotero/storage/X/a.pdf"
        self.assertEqual(self.code("Read", file_path=f"{self.P}/litreview.md"), 0)
        self.assertEqual(self.code("Read", file_path="litreview.md"), 0)
        self.assertEqual(self.code("Read", file_path=z), 0)
        self.assertEqual(self.code("Write", file_path=z), 2)
        self.assertEqual(self.code("Read", file_path=os.path.expanduser("~/.bashrc")), 2)
        self.assertEqual(self.code("Edit", file_path="../colorflow2/x"), 2)
        self.assertEqual(self.code("Read", file_path=f"{self.P}/../.ssh/id"), 2)
        self.assertEqual(self.code("Glob", pattern="/etc/**"), 2)
        self.assertEqual(self.code("Glob", pattern="**/*.md"), 0)
        self.assertEqual(self.code("Grep", pattern="x", path="/etc"), 2)


@unittest.skipUnless(LIVE, "set LR_LIVE=1 for live API tests")
class TestLive(Base):
    def test_inspire_lookup_refs_citing(self):
        (r,) = recs(run(lr.cmd_lookup, NS(ids=["10.1103/PhysRevD.50.5562"], abstract=False))[0])
        self.assertEqual((r["recid"], r["texkey"]), (374155, "CDF:1994zkl"))
        out, err = run(lr.cmd_refs, NS(recid=374155, abstract=False, show_unresolved=0))
        self.assertGreater(len(recs(out)), 25)
        out, _ = run(lr.cmd_citing, NS(recid=374155, filter="t coherence", abstract=False, limit=5, sort="mostcited"))
        self.assertEqual(len(recs(out)), 5)
        with self.assertRaises(lr.QueryError):
            lr.inspire("refersto:recid:374155 and (t coherence)")

    def test_arxiv_search(self):
        out, _ = run(lr.cmd_arxiv, NS(query="id:1311.5815", limit=1, sort="relevance", abstract=False))
        self.assertEqual(recs(out)[0]["arxiv"], "1311.5815")


if __name__ == "__main__":
    try:
        unittest.main(verbosity=1)
    finally:
        shutil.rmtree(TESTDIR, ignore_errors=True)
