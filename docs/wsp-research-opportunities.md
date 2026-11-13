# Evaluating weight programs beyond benchmark gains

Research guide, 13 November 2026. The most useful next step is to test when a weight program remains effective across equivalent parameterizations, independently trained hosts, and successive edits. Existing work motivates these experiments but does not establish their general success. The [evidence matrix](wsp-evidence.md) records individual studies; this guide connects them to concrete research designs.

中文摘要：下一步值得研究的是权重程序在等价参数化、独立训练模型和连续编辑下是否仍然有效。需要区分修复已有能力、安装新能力、从零构造网络，以及请求结束后恢复权重的临时干预。下文的实验方案是研究建议，不是已经完成的结果，也不构成新颖性声明。

## Distinguish the research questions

| Question | Relevant work | What an evaluation must separate |
| --- | --- | --- |
| Can an agent read a function from weights? | [Orbit Audits](https://arxiv.org/abs/2611.05798), [Mixed Signals](https://arxiv.org/html/2611.13758v1) | Functional evidence, dataset clues, coordinate conventions and repeated-answer variance |
| Can a program install or repair behavior? | [WeightCode](https://github.com/Gen-Verse/WeightCode), [WSP-Scope](https://arxiv.org/abs/2611.09382) | New behavior, recovery of existing behavior, and changes to decoding or stopping |
| Can an agent construct a useful model? | [iWSP](https://www.alphaxiv.org/abs/2611.interpretable-weight-space-programming), [medical imaging WSP](https://arxiv.org/html/2611.12066v1), [Physics2Weight](https://arxiv.org/html/2611.12954v1) | Written weights, analytical architecture choices, evaluator fitting and hidden-set generalization |
| Can interventions execute predictably? | [W-ISA](https://arxiv.org/html/2611.13232v1), [NCP](https://arxiv.org/html/2611.13236v1) | Execution/restoration guarantees, admission decisions and actual task improvement |
| Can improvements accumulate? | [WeightLoop](https://arxiv.org/abs/2611.07319), [TIES-Merging](https://arxiv.org/abs/2306.01708) | Sequential adaptation, interference, old-task retention and numerical update composition |

The broader [Weight Space Learning survey](https://arxiv.org/abs/2603.10090) organizes work around understanding, representation and generation. These supply mechanisms and baselines for WSP, but trained weight predictors and merging algorithms should retain their own classifications.

## Findings that change experimental design

The newly source-checked entries show why a single headline score is insufficient:

- **Mixed Signals:** repair, healthy-model improvement and construction have different outcomes. Its task-reading controls make dataset familiarity a concrete alternative explanation. See Sections II–IV of the [paper](https://arxiv.org/html/2611.13758v1).
- **NCP:** the useful observation is the rejection decision: fewer repeated tokens did not satisfy its task-correctness gate. Its implemented proposer uses deterministic templates. See Sections 5–7 of the [paper](https://arxiv.org/html/2611.13236v1).
- **W-ISA:** restoring a checkpoint after execution does not establish that the intervention preserves capabilities while active. See Sections 7–8 of the [paper](https://arxiv.org/html/2611.13232v1).
- **Physics2Weight:** a finer evaluation grid exposes residual failures missed by aggregate solution accuracy. See Sections 5.4–5.6 of the [paper](https://arxiv.org/html/2611.12954v1).
- **Medical imaging WSP:** label-free construction must be compared with small-label training under explicit image-resolution and prompting choices. See Sections 3–5 of the [paper](https://arxiv.org/html/2611.12066v1).

**iWSP needs a pipeline-level distinction.** The author-released [fMRI evaluator](https://github.com/csinva/weight-space-programming-autoresearch/blob/f012b9557c8d522d58867025c0d602a04ecce38f/experiments/evolve-neuro/src/eval.py) and [ECoG evaluator](https://github.com/csinva/weight-space-programming-autoresearch/blob/f012b9557c8d522d58867025c0d602a04ecce38f/experiments/ecog/LEAN_replication_package/evolve-wave/src/eval.py) fit encoding readouts. Agent-written features without backpropagation should not be described as an entire pipeline without fitting. Its [reproduction guide](https://github.com/csinva/weight-space-programming-autoresearch/blob/f012b9557c8d522d58867025c0d602a04ecce38f/experiments/README.md) also identifies unavailable ECoG patient data and a missing story in the public fMRI release.

**EditLens adds a causal audit.** Its stopping controls recover much of the observed math gain under the tested settings. Its Gemma weight swaps and activation patches answer different causal questions; a conspicuous attention pattern does not by itself identify the parameters responsible for a behavior. These are bounded findings from a technical report, not proof that all WSP improvements are stopping effects. See the [author article](https://xxlya.github.io/editlens/) and [released repository](https://github.com/assassin808/edit-lens/tree/c274b1c58f8b0b14f8a9af4c7640360dce50bea7).

## Proposed experiment 1 Program portability under symmetry

**Question:** does a reusable edit program identify the computation it should modify, or depend on the coordinates of one checkpoint?

Start with a small reproducible target and an existing released program. WeightCode's SCAN example is a practical candidate because its [official instructions](https://github.com/Gen-Verse/WeightCode/tree/a2cefc8865f44f5dbe5ee4fce6b2282683bc3985) provide a CPU reproduction path on Linux x86-64, fixed data checksums, and separate old/new command evaluations. Establish that reproduction before changing the experiment. The published reuse result already compares rerunning a program with copying its numeric delta; simply repeating that comparison is not a new contribution.

Construct function-preserving transformations supported by the target architecture. Begin with hidden-unit permutations in a compatible feed-forward block, applying the inverse permutation to its outgoing weights and transforming biases consistently. Verify matching forward outputs before editing. ReLU rescaling is suitable only where the actual activation and surrounding operations preserve that symmetry; it must not be assumed for arbitrary Transformer blocks.

For each original and transformed checkpoint, compare:

1. The original unedited model and a no-op program.
2. The unchanged edit program rerun on the transformed host.
3. The source numeric delta copied without coordinate adjustment.
4. The same delta transformed into the correct coordinates using the known symmetry.
5. A simple deterministic repair or capability-insertion baseline, where available.

The fourth condition is essential: a copied delta can fail purely because its coordinates changed. Beating only the third condition would not establish semantic portability. [Git Re-Basin](https://arxiv.org/abs/2209.04836) motivates alignment-aware comparisons; [Orbit Audits](https://arxiv.org/abs/2611.05798) motivates separating functional correctness from invariance.

Measure new-task performance, old-task regression, editing failures, output disagreement and changed parameter count. Report all sampled transformations. Then test independently trained hosts separately: equivalent coordinate changes and independent training are different generalization problems. For the latter, disclose host-specific examples and validation access given to each program.

**Proposed contribution:** a small transformation suite, recorded baseline outputs and an evaluation table with confidence intervals grouped by source host. This would extend evaluation of executable programs rather than make another claim about raw deltas.

## Proposed experiment 2 Composition and retention

**Question:** can two individually useful programs be applied in different orders without silently destroying their gains?

Use two capabilities with disjoint selection and final-test sets. Compare applying A then B, B then A, and applying each alone. Include two forms of composition: adding deltas computed on the original host, and rerunning the second program on the already edited host. Also distinguish a frozen second program from one newly synthesized for that edited host.

Measure every capability after every step, including the untouched base tasks. Report the worst regression as well as the average. Where practical, test rollback followed by replay and compare both weights and outputs. The comparison should include an edit designed without retention constraints and one selected with them, using equal access to validation feedback.

[TIES-Merging](https://arxiv.org/abs/2306.01708) provides an interference-aware numeric baseline when the updates share a compatible base and parameterization. It does not establish that the same method will work for arbitrary executable programs. [WeightLoop](https://arxiv.org/abs/2611.07319) motivates evaluating repeated updates with feedback, while preserving the distinction between a persistent predictor and a fixed editor.

**Proposed contribution:** a sequence benchmark with separate records for synthesis, program execution, host-specific inputs and retention. Extend to longer sequences only after the two-program comparisons are stable.

## Proposed experiment 3 Evaluate edits against simple alternatives

**Question:** when does direct weight modification add value beyond a simpler intervention with the same information budget?

For reasoning-loop repair, include unchanged weights with alternate stopping rules, matched generation budgets and repeated sampling. For classification, include bias recalibration and a matched-data linear readout. For PDEs, include analytical constructions where permitted, and evaluate unseen dense grids. Do not compare an agent with rich validation feedback against a baseline denied that feedback.

Keep proposal selection and final evaluation separate. Predeclare the success criterion and allow rejection of all candidates. Record unsuccessful trials, model calls, tokens, wall-clock time, accelerator time and any post-hoc baseline changes. [WSP-Scope](https://arxiv.org/abs/2611.09382) reports retaining original weights in six of sixteen trajectories; the baseline checkpoint is a legitimate outcome.

[TensorMutation](https://arxiv.org/abs/2611.09650) is a useful adjacent source for fault-based test cases and norm-matched random controls. It uses a trained GNN to generate mutations, so it belongs among foundations rather than direct LLM-driven WSP. Its reported advantage over one mutation tool does not establish an advantage over every comparator.

**Proposed contribution:** a compact protocol with explicit information budgets and rejection criteria, followed by a reproducible pilot. None of these experiments has been executed as part of this bibliography update.

## Source audit and catalog decisions

| Entry | Sources inspected | Decision |
| --- | --- | --- |
| Mixed Signals | arXiv v1, Sections II–IV and Tables I–V | Fill evidence fields; retain construction taxonomy and record repair/reading limits |
| NCP | arXiv v1, Sections 5–7 | Fill evidence fields; distinguish deterministic synthesis, rejected candidates and temporary edits |
| W-ISA | arXiv v1, Sections 3–8 | Fill evidence fields; distinguish runtime restoration from active-edit retention |
| Physics2Weight | arXiv v1, Sections 4–5 and Tables 5–7 | Fill evidence fields; record architecture changes and residual failures |
| Medical imaging WSP | arXiv v1, Sections 3–5 | Fill evidence fields; include small-label baseline and failure case |
| iWSP | Author abstract, repository README, experiment guide and two evaluator files | Update the existing `wsp-autoresearch` record to the preprint; preserve its ID and reports link; move to direct construction |
| EditLens | Author article and repository README | Add one technical-blog record; keep it separate from peer-reviewed papers |

iWSP's alphaXiv page gives **12 November 2026** as the manuscript submission date; that is not the first date of its earlier autoresearch project. EditLens's author article identifies **November 2026** but does not specify a day; no exact first-publication day is asserted here. Neither new catalog treatment claims peer review.

The iWSP evidence check does not claim a full-PDF audit. Its repository is pinned above because results, data availability and evaluator details can change. The EditLens README says additional Gemma code/data will be added, so the linked code should not be taken as a complete reproduction package for every article result.

This update increases the direct-WSP evidence coverage from 8/19 to 14/20 source-checked records and the full catalog from 145 to 146 records. Five existing papers receive evidence summaries, one existing project is reclassified, and one report is added. The six remaining metadata-only direct entries retain unknown evidence fields. Source checking means inspecting the cited material, not independently reproducing its experiments.
