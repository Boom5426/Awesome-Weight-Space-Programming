#!/usr/bin/env python3
"""Validate canonical bilingual bibliography data (Python stdlib only)."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {"direct", "reports", "related", "resources", "weight-centric"}
LEVELS = {"manuscript", "preprint", "peer-reviewed", "technical-report", "blog"}
REVIEWS = {"source_checked", "metadata_only"}
EVIDENCE_FIELDS = {"level", "review", "gradient_free", "source_url", "target_model",
                   "intervention", "claim", "baselines", "preservation", "transfer", "caveat"}
TRACKS = {"geometry", "reading", "generation", "composition", "structure", "retention"}
RELATED = {"neural-compilation", "weight-foundations", "fast-foundations", "program-foundations", "cross-domain"}
def load(name):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
def errors():
    entries = load("entries.json")["entries"]
    updates = load("updates.json")["updates"]
    sections = load("sections.json")["sections"]
    problems, ids, urls = [], set(), {}
    for i, e in enumerate(entries):
        key = e.get("id") or "item-" + str(i)
        for field in ("id", "group", "section", "title", "url", "render_en", "render_zh", "year"):
            if not e.get(field):
                problems.append(key + ": missing " + field)
        if key in ids:
            problems.append(key + ": duplicate id")
        ids.add(key)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key):
            problems.append(key + ": invalid ID")
        group = e.get("group")
        if group not in GROUPS:
            problems.append(key + ": invalid group")
        if group == "weight-centric" and e.get("section") not in TRACKS:
            problems.append(key + ": invalid weight-centric section")
        if group == "related" and e.get("section") not in RELATED:
            problems.append(key + ": invalid related section")
        year = e.get("year")
        if not isinstance(year, int) or year < 1900 or year > 2100:
            problems.append(key + ": invalid year")
        link = e.get("url", "")
        if urlparse(link).scheme != "https" or not urlparse(link).netloc:
            problems.append(key + ": invalid HTTPS source URL")
        if group != "resources":
            canonical = link.lower().split("#")[0].rstrip("/")
            if canonical in urls:
                problems.append(key + ": duplicate primary URL with " + urls[canonical])
            urls[canonical] = key
        for lang in ("en", "zh"):
            raw = e.get("render_" + lang, "")
            if not raw.startswith("- **["):
                problems.append(key + ": malformed " + lang + " display line")
            if group == "weight-centric":
                for field in ("idea_" + lang, "inspiration_" + lang, "venue_" + lang):
                    if not e.get(field):
                        problems.append(key + ": missing " + field)
                if link not in raw:
                    problems.append(key + ": missing companion source in " + lang)
        if group == "direct":
            ev = e.get("evidence")
            if not isinstance(ev, dict):
                problems.append(key + ": missing evidence object")
                continue
            missing = EVIDENCE_FIELDS - set(ev)
            if missing:
                problems.append(key + ": missing evidence fields " + str(sorted(missing)))
            if ev.get("level") not in LEVELS:
                problems.append(key + ": invalid evidence level")
            if ev.get("review") not in REVIEWS:
                problems.append(key + ": invalid review state")
            if ev.get("gradient_free") not in (True, False, None):
                problems.append(key + ": gradient_free must be true/false/null")
            if ev.get("review") == "source_checked" and any(not ev.get(k) for k in
                    ("target_model", "intervention", "claim", "baselines", "preservation", "transfer", "caveat")):
                problems.append(key + ": source-checked evidence incomplete")
            if ev.get("review") == "metadata_only" and ev.get("claim") is not None:
                problems.append(key + ": metadata-only result must remain null")
    track_ids = [x.get("id") for x in sections]
    if len(track_ids) != 6 or set(track_ids) != TRACKS:
        problems.append("sections: expected six distinct tracks")
    for section in sections:
        for key in ("id", "anchor", "title_en", "title_zh", "intro_en", "intro_zh"):
            if not section.get(key):
                problems.append("sections: missing " + key)
    for i, update in enumerate(updates):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", update.get("date", "")):
            problems.append("update " + str(i) + ": bad date")
        if not update.get("en") or not update.get("zh"):
            problems.append("update " + str(i) + ": both languages required")
    if not updates:
        problems.append("updates: must be nonempty")
    return problems
if __name__ == "__main__":
    issues = errors()
    if issues:
        print("\n".join(issues))
        sys.exit(1)
    print("ok: " + str(len(load("entries.json")["entries"])) + " canonical bilingual records")
