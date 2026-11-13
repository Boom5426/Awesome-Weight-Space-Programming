"""Offline smoke tests for the generated research catalog and interactive map."""
from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_site", ROOT / "scripts/build_site.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ResearchSiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))["entries"]
        cls.config = json.loads((ROOT / "data/navigation.json").read_text(encoding="utf-8"))
        cls.nav, cls.allocation = MODULE.build_navigation(cls.items, cls.config)

    def test_navigation_covers_entries_once(self):
        self.assertEqual(len(self.allocation), len(self.items))
        self.assertEqual(sum(b["count"] for b in self.nav["branches"]), len(self.items))
        self.assertEqual(len({e["id"] for e in self.items}), len(self.items))
        self.assertEqual(len(self.nav["branches"]), 4)
        self.assertEqual(sum(len(b["leaves"]) for b in self.nav["branches"]), 20)

    def test_research_tracks(self):
        self.assertEqual(self.allocation["weightcode"], "direct.install")
        self.assertEqual(self.allocation["linear-mode-connectivity-and-the-lottery-ticket-hypothesis"],
                         "weight-centric.geometry")
        self.assertEqual(self.allocation["linear-transformers-are-secretly-fast-weight-programmers"],
                         "foundations.fast")
        self.assertEqual(self.allocation["wsp-autoresearch"], "direct.synthesize")

    def test_generated_html_is_current(self):
        for path, expected in MODULE.render().items():
            with self.subTest(path=path):
                self.assertEqual((ROOT / path).read_text(encoding="utf-8"), expected)
        self.assertEqual((ROOT / "index.html").read_bytes(), (ROOT / "docs/index.html").read_bytes())
        self.assertEqual((ROOT / "landscape.html").read_bytes(), (ROOT / "docs/landscape.html").read_bytes())

    def test_catalog_json_and_accessibility(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        match = re.search(r"const PAPERS=(\[.*?\]);\s*const NAV=", html, re.S)
        self.assertIsNotNone(match)
        papers = json.loads(match.group(1))
        self.assertEqual(len(papers), len(self.items))
        self.assertEqual({e["id"] for e in papers}, {e["id"] for e in self.items})
        self.assertTrue(all(p["url"].startswith("https://") for p in papers))
        self.assertIn('aria-label="Search papers"', html)
        self.assertIn('id="review"', html)
        self.assertIn("Research Landscape", html)

    def test_map_has_deep_links_and_controls(self):
        html = (ROOT / "landscape.html").read_text(encoding="utf-8")
        self.assertIn("const MAP=", html)
        for fragment in ("Zoom out", "Zoom in", "fit", "leaf.id", "URLSearchParams",
                         "pointermove", "weight-space"):
            self.assertIn(fragment.lower(), html.lower())

    def test_updates_remain_three(self):
        for file in ("README.md", "README_zh.md"):
            text = (ROOT / file).read_text(encoding="utf-8")
            rows = re.findall(r"^\| \x6020\d\d-\d\d-\d\d\x60 \|", text, re.M)
            self.assertEqual(len(rows), 3)


if __name__ == "__main__":
    unittest.main()
