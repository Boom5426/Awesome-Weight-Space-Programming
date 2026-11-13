#!/usr/bin/env python3
"""Build bilingual Markdown from canonical data/*.json (Python standard library only)."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
 "neural-compilation": ("Neural Program Compilation & Weight Generation", "Learned compilers, hypernetworks, and adapter generators that map instructions or data to model parameters, plus program-to-weight compilers.", "神经程序编译与权重生成", "学习型编译器、超网络和适配器生成器，以及将程序直接编译为网络参数的方法。"),
 "weight-foundations": ("Model Editing & Weight-Space Foundations", "Research on modifying facts or behaviors, parameter differences, symmetries, and learned weight representations.", "模型编辑与权重空间基础", "研究知识与行为修改、参数增量复用、对称性以及网络权重表征。"),
 "fast-foundations": ("Fast Weights & Self-Modifying Networks", "Dynamic parameter states and self-modification; distinguish online memory from persistent capability installation.", "快速权重与自修改网络", "关注动态参数状态和自修改机制，区分在线临时记忆与持久能力安装。"),
 "program-foundations": ("Historical Program-to-Weights & Rule Insertion", "Earlier analytical and symbolic routes to specifying neural computations through weights.", "早期程序到权重编译与规则植入", "追溯解析构造与符号规则转化为神经网络计算的历史路径。"),
 "cross-domain": ("Cross-Domain Transfer & Weight-Difference Interpretation", "Ideas from robotics and interpretability that may inform portable programs and capability tracing.", "跨领域迁移与权重变化解释", "借鉴机器人与可解释性研究，支持程序跨模型复用和能力变化追踪。"),
}
def data(name):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
def subset(entries, group, section=None):
    return [e for e in entries if e["group"] == group and (section is None or e["section"] == section)]
def rows(entries, lang):
    return "\n\n".join(e["render_" + lang] for e in entries)
def updates_view(updates, lang):
    header = "| Date | What changed |\n| --- | --- |" if lang == "en" else "| 日期 | 更新内容 |\n| --- | --- |"
    ordered = sorted(updates, key=lambda u: u["date"], reverse=True)[:3]
    return header + "\n" + "\n".join("| " + chr(96) + u["date"] + chr(96) + " | " + u[lang] + " |" for u in ordered)
def direct_view(entries, lang):
    items = subset(entries, "direct")
    n = len(items)
    if lang == "en":
        intro = "Research directly involving programmatic inspection, construction, or modification of neural-network weights, with informative method and task tags."
        stats = f"**{n} papers and manuscripts** · [2026 ({n})](#2026)"
        year = f"### 🗓️ 2026 — {n} papers"
        evidence = "**Evidence audit:** [WSP Evidence Matrix](docs/wsp-evidence.md)"
    else:
        intro = "直接通过程序读取、构建或修改神经网络权重的研究，并标注方法与任务属性。"
        stats = f"**{n} 篇论文与手稿** · [2026（{n}）](#2026)"
        year = f"### 🗓️ 2026 — {n} 篇"
        evidence = "**证据整理：** [WSP 证据矩阵](docs/wsp-evidence.md)"
    return "\n\n".join([intro, stats, evidence, '<a id="2026"></a>\n' + year, rows(items, lang)])
def related_view(entries, lang):
    intro = ("These adjacent methods inform WSP, but are not automatically instances of direct LLM-driven weight programming." if lang == "en"
             else "这些相邻方法可启发权重编程，但不应自动归类为由大模型直接完成的权重空间编程。")
    parts = [intro]
    for section, labels in LABELS.items():
        items = subset(entries, "related", section)
        if not items:
            continue
        title, desc = labels[0:2] if lang == "en" else labels[2:4]
        parts.append("### " + title + "\n\n" + desc + "\n\n" + rows(items, lang))
    return "\n\n".join(parts)
def companion_view(entries, sections, lang):
    blocks = []
    for s in sections:
        items = subset(entries, "weight-centric", s["id"])
        block = ('<a id="' + s["anchor"] + '"></a>\n## ' + s["title_" + lang] + "\n\n*" +
                 s["intro_" + lang] + "*\n\n" + rows(items, lang))
        blocks.append(block)
    return "\n\n".join(blocks)
def evidence_view(entries):
    direct = subset(entries, "direct")
    checked = [e for e in direct if e["evidence"]["review"] == "source_checked"]
    pending = [e for e in direct if e["evidence"]["review"] != "source_checked"]
    parts = [
        "# WSP Evidence Matrix / 权重编程证据矩阵",
        "This matrix summarizes source-reported evidence, not independently reproduced results. "
        "A source check is not independent replication. Repairing a defect does not automatically demonstrate a missing capability.\n\n"
        "本表整理原始来源报告的证据，并非独立复现实验。修复现有功能不等于安装此前缺失的能力。",
        f"**Coverage:** {len(direct)} direct-WSP papers; {len(checked)} source-checked examples; {len(pending)} metadata-only entries.",
        "## Source-checked examples / 已核对来源的案例",
    ]
    fields = [
      ("target_model", "Model / 对象"), ("intervention", "Intervention / 干预"),
      ("claim", "Reported outcome / 结果"), ("baselines", "Comparisons / 对照"),
      ("preservation", "Old capability / 保持"), ("transfer", "Transfer / 迁移"),
      ("caveat", "Evidence boundary / 证据边界"),
    ]
    for e in checked:
        ev = e["evidence"]
        section = "### [" + e["title"] + "](" + ev["source_url"] + ")\n\n"
        section += "\n".join("- **" + label + ":** " + (ev.get(key) or "Not established / 未证实") for key, label in fields)
        section += "\n- **Gradient-free / 免梯度:** " + ("Yes" if ev["gradient_free"] is True else "Not assessed")
        section += " · **Source level / 来源类型:** " + ev["level"]
        parts.append(section)
    parts.append("## Other direct-WSP entries / 尚待逐篇核对实证信息\n\n"
                 "These entries have bibliographic metadata but their outcomes, controls and retention evidence are not yet extracted. "
                 "Missing values must not be interpreted as negative findings.\n\n"
                 "下列条目已编目，但证据字段尚未逐篇核对；缺失不代表实验失败。")
    table = ["| Work | Source type | Verification status |", "| --- | --- | --- |"]
    table += ["| [" + e["title"] + "](" + e["url"] + ") | " + e["evidence"]["level"] + " | Metadata only / 未审查结果 |" for e in pending]
    parts.append("\n".join(table))
    parts.append("## How to read this matrix / 如何理解证据\n\n"
                 "- **Repair vs installation:** repairing existing behavior does not prove new capability acquisition.\n"
                 "- **Preservation:** absence of regression reports is not evidence of retention.\n"
                 "- **Portability:** fixed numeric deltas differ from rerunning a program on a new host.\n"
                 "- **Sequence:** one update does not establish long-horizon accumulation.\n"
                 "- **Evidence level:** a preprint, repository or blog label says what was reported, not what was independently confirmed.")
    return "\n\n".join(parts)
def replace(text, name, generated):
    begin, end = "<!-- AUTO:START " + name + " -->", "<!-- AUTO:END " + name + " -->"
    if text.count(begin) != 1 or text.count(end) != 1:
        raise ValueError("Missing or duplicate marker " + name)
    start, stop = text.index(begin) + len(begin), text.index(end)
    return text[:start] + "\n" + generated.strip() + "\n" + text[stop:]
def build():
    entries = data("entries.json")["entries"]
    updates = data("updates.json")["updates"]
    sections = data("sections.json")["sections"]
    output = {}
    count = len(subset(entries, "weight-centric"))
    for lang, path in (("en", "README.md"), ("zh", "README_zh.md")):
        txt = (ROOT / path).read_text(encoding="utf-8")
        changes = {
            "updates": updates_view(updates, lang),
            "direct": direct_view(entries, lang),
            "reports": rows(subset(entries, "reports"), lang),
            "related": related_view(entries, lang),
            "resources": rows(subset(entries, "resources"), lang),
        }
        for name, content in changes.items():
            txt = replace(txt, name, content)
        pattern = (r"\*\*\d+ curated papers across six research tracks:\*\*" if lang == "en" else
                   r"\*\*现收录 \d+ 篇，分成六条研究线：\*\*")
        new_count = (f"**{count} curated papers across six research tracks:**" if lang == "en" else
                     f"**现收录 {count} 篇，分成六条研究线：**")
        txt, n = re.subn(pattern, new_count, txt)
        if n != 1:
            raise ValueError("Missing count label in " + path)
        output[path] = txt
    for lang, path in (("en", "docs/weight-centric-research.md"),
                       ("zh", "docs/weight-centric-research_zh.md")):
        txt = (ROOT / path).read_text(encoding="utf-8")
        pattern = r"\*\*Current selection:\*\* \d+ papers" if lang == "en" else r"\*\*当前收录：\*\* \d+ 篇"
        replacement = f"**Current selection:** {count} papers" if lang == "en" else f"**当前收录：** {count} 篇"
        txt, n = re.subn(pattern, replacement, txt)
        if n != 1:
            raise ValueError("Missing companion count in " + path)
        output[path] = replace(txt, "weight-centric", companion_view(entries, sections, lang))
    path = "docs/wsp-evidence.md"
    output[path] = replace((ROOT / path).read_text(encoding="utf-8"), "evidence", evidence_view(entries))
    return output
def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--check", action="store_true", help="Fail if a generated file is stale")
    args = cli.parse_args()
    rendered = build()
    changed = []
    for name, body in rendered.items():
        path = ROOT / name
        if path.read_text(encoding="utf-8") != body:
            changed.append(name)
            if not args.check:
                path.write_text(body, encoding="utf-8")
    if args.check and changed:
        print("Stale files: " + ", ".join(changed) + "; run python3 scripts/build.py")
        return 1
    print("ok" if not changed else "updated", ": ", ", ".join(rendered))
    return 0
if __name__ == "__main__":
    sys.exit(main())
