# Contributing / 参与贡献

This is a research-oriented bibliography. We distinguish direct WSP research from related weight-centric methods and from untested future WSP hypotheses.

## One canonical source / 单一数据源

- Edit **data/entries.json** for papers, reports, projects, and resources.
- Edit **data/updates.json** to add news. Both READMEs display the **latest three** by date; older entries can remain in JSON.
- Edit **data/sections.json** for the six Weight-Centric reading tracks.
- Do not manually edit content between generated START and END comments in Markdown files.
- Text outside the generated regions stays editable.

After editing, run:

~~~bash
python3 scripts/validate.py
python3 scripts/build.py
python3 scripts/build.py --check
~~~

Commit changes to the JSON and all regenerated Markdown files.

## Data fields / 文献数据格式

Every item has an ID, original title, group, section, canonical HTTPS URL, year, and bilingual display lines. Weight-Centric records additionally have ideas, potential inspirations, and venue text in both languages. A possible WSP inspiration is a testable hypothesis, not an established result.

Groups: direct (direct WSP research), reports (original technical writeups and critiques), related (adjacent methods and foundations), resources (toolkits and data), weight-centric (separate six-track research guide).

## Evidence / 直接 WSP 的证据字段

Each direct research item includes an evidence object containing:

- level: preprint, manuscript, peer-reviewed, technical-report, or blog
- review: source_checked or metadata_only
- gradient_free: true / false / null
- source_url, target_model, intervention, claim, baselines, preservation, transfer, caveat

Keep unknown evidence values null. Do not invent outcomes or infer old-skill preservation from missing evidence. Source-checked means the primary report was inspected, **not** that its results were independently reproduced. Note whether a method repairs an existing behavior, installs a missing capability, transfers fixed numeric deltas, or reruns an executable program.

## Submission policy / 投稿规则

Authors may submit their own work but should disclose authorship, venue status, model/task, evaluation protocol, public code, and evidence scope. Prefer primary papers and first-party projects. Focus on practical research value, not raw number of papers or GitHub stars.

## Research Landscape and searchable catalog

The interactive pages are generated from **the same** `data/entries.json` used by the bilingual README. Add any new paper only once to the canonical dataset; never edit the embedded HTML data by hand.

Edit `data/navigation.json` when adding a new direct-WSP research item or changing the mutually exclusive research-map tracks. Every entry must belong to exactly one leaf (see the build validator). The pages are based on the design pattern used in [Awesome Virtual Cell](https://github.com/Boom5426/Awesome-Virtual-Cell), with a WSP-specific taxonomy.

```bash
python3 scripts/validate.py
python3 scripts/build.py
python3 scripts/build_site.py
python3 scripts/build.py --check
python3 scripts/build_site.py --check
```

The generator writes `index.html` and `landscape.html` at both repository root and under `docs/`, allowing either Pages source option. In GitHub **Settings → Pages**, publish `main` from **/(root)** or **/docs** (depending on repository setup). The public URLs are `https://boom5426.github.io/Awesome-Weight-Space-Programming/` and `.../landscape.html` after Pages deployment.

The README badges assume Pages is enabled. If not, the Markdown lists remain directly available on GitHub. GitHub Actions checks that generated pages are synchronized with JSON and HTML templates.

The research map includes a readable mobile track menu, and the catalog has bilingual UI and search. Use `?lang=zh` for Chinese and deep links such as `?branch=weight-centric&leaf=geometry` for a specific research track. To test the browser-side state (not just the HTML syntax), run:

```bash
node tests/test_site_ui.cjs
```

The catalog displays at most 24 entries initially; its **Show more** button loads the next 24. Evidence-status filters mean *the source was inspected*, never independently reproduced.
