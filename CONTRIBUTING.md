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
