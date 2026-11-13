#!/usr/bin/env python3
"""Build searchable catalog and interactive landscape from the canonical bibliography.

Adapted from Awesome-Virtual-Cell's template/data architecture.
Runs offline with Python standard library only.

    python3 scripts/build_site.py
    python3 scripts/build_site.py --check
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUP_LABELS = {
    "direct": "Direct WSP",
    "weight-centric": "Weight-Centric",
    "related": "Related Foundations",
    "reports": "Reports & Blogs",
    "resources": "Tools & Resources",
}
GROUP_LABELS_ZH = {
    "direct": "直接 WSP",
    "weight-centric": "权重相关研究",
    "related": "相关基础研究",
    "reports": "报告与博客",
    "resources": "工具与资源",
}


def read_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def select(items: list[dict], branch: dict, leaf: dict) -> list[dict]:
    if "ids" in leaf:
        ids = set(leaf["ids"])
        return [e for e in items if e["id"] in ids]
    group = leaf.get("group", branch.get("group", branch["id"]))
    section = leaf.get("section")
    return [e for e in items if e["group"] == group and (not section or e["section"] == section)]


def build_navigation(items: list[dict], config: dict) -> tuple[dict, dict[str, str]]:
    allocation: dict[str, str] = {}
    branches: list[dict] = []
    available = {e["id"] for e in items}
    for branch in config["branches"]:
        leaves: list[dict] = []
        branch_ids: set[str] = set()
        for leaf in branch["leaves"]:
            if "ids" in leaf and set(leaf["ids"]) - available:
                raise ValueError("Unknown IDs in " + branch["id"] + "." + leaf["id"])
            matching = select(items, branch, leaf)
            if not matching:
                raise ValueError("Empty navigation leaf: " + branch["id"] + "." + leaf["id"])
            track = branch["id"] + "." + leaf["id"]
            for entry in matching:
                if entry["id"] in allocation:
                    raise ValueError("Navigation entry assigned twice: " + entry["id"])
                allocation[entry["id"]] = track
                branch_ids.add(entry["id"])
            leaves.append({
                "id": leaf["id"], "name": leaf["name"], "name_zh": leaf["name_zh"],
                "count": len(matching),
                "examples": [e["title"] for e in matching[:4]],
            })
        branches.append({
            "id": branch["id"], "name": branch["name"],
            "name_zh": branch["name_zh"], "side": branch["side"],
            "count": len(branch_ids), "leaves": leaves,
        })
    missing = available - set(allocation)
    if missing:
        raise ValueError("Navigation must cover each canonical entry exactly once: " + ", ".join(sorted(missing)))
    return {"total": len(items), "branches": branches}, allocation


def full_title(entry: dict) -> str:
    if entry["group"] in ("weight-centric", "resources"):
        return entry["title"]
    line = entry["render_en"]
    line = re.sub(r"^- \*\*\[[^\]]+\]\*\*\s*", "", line)
    line = re.sub(r"^(?:\`[^\`]+\`\s*)+", "", line)
    line = re.split(r"\s+\(\*\*", line, maxsplit=1)[0].strip()
    return line if line and not line.startswith("[[") else entry["title"]


def code_link(entry: dict) -> str | None:
    found = re.search(r"\[\[(?:code|代码)\]\((https://[^)]+)\)\]", entry["render_en"], re.I)
    return found.group(1) if found else None


def compact_catalog(items: list[dict], allocation: dict[str, str]) -> list[dict]:
    result = []
    for index, e in enumerate(items):
        ev = e.get("evidence") or {}
        checked = ev.get("review") == "source_checked"
        result.append({
            "id": e["id"], "label": e["title"], "title": full_title(e),
            "url": e["url"], "code": code_link(e), "year": e["year"],
            "group": e["group"], "groupLabel": GROUP_LABELS[e["group"]],
            "groupLabelZh": GROUP_LABELS_ZH[e["group"]],
            "section": e["section"], "track": allocation[e["id"]],
            "idea": e.get("idea_en", ""),
            "ideaZh": e.get("idea_zh", ""),
            "inspiration": e.get("inspiration_en", ""),
            "inspirationZh": e.get("inspiration_zh", ""),
            "venue": e.get("venue_en") or ev.get("level") or "",
            "search": e["render_en"] + " " + e["render_zh"],
            "claim": ev.get("claim") if checked else None,
            "review": ev.get("review"),
            "order": index,
        })
    return result


def inline_json(obj: object) -> str:
    # Avoid accidentally terminating an embedded script.
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def render() -> dict[str, str]:
    items = read_json("data/entries.json")["entries"]
    config = read_json("data/navigation.json")
    nav, allocation = build_navigation(items, config)
    catalog = compact_catalog(items, allocation)
    source = (ROOT / "docs/site.template.html").read_text(encoding="utf-8")
    landscape = (ROOT / "docs/landscape.template.html").read_text(encoding="utf-8")
    if source.count("__CATALOG_DATA__") != 1 or source.count("__NAVIGATION_DATA__") != 1:
        raise ValueError("Missing catalog template placeholders")
    if landscape.count("__NAVIGATION_DATA__") != 1 or landscape.count("__TOTAL__") != 1:
        raise ValueError("Missing landscape template placeholders")
    catalog_html = source.replace("__CATALOG_DATA__", inline_json(catalog)).replace(
        "__NAVIGATION_DATA__", inline_json(nav))
    landscape_html = landscape.replace("__NAVIGATION_DATA__", inline_json(nav)).replace(
        "__TOTAL__", str(nav["total"]))
    return {
        "index.html": catalog_html,
        "landscape.html": landscape_html,
        "docs/index.html": catalog_html,
        "docs/landscape.html": landscape_html,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if checked-in HTML differs from canonical data")
    args = parser.parse_args()
    rendered = render()
    stale = []
    for path, content in rendered.items():
        dest = ROOT / path
        if not dest.exists() or dest.read_text(encoding="utf-8") != content:
            stale.append(path)
            if not args.check:
                dest.write_text(content, encoding="utf-8")
    if args.check and stale:
        print("Stale site files: " + ", ".join(stale) + "; run python3 scripts/build_site.py")
        return 1
    count = len(read_json("data/entries.json")["entries"])
    print(("ok" if not stale else "updated") + ": " + ", ".join(rendered)
          + " (" + str(count) + " curated entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
