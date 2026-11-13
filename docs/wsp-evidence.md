<!-- AUTO:START evidence -->
# WSP Evidence Matrix / 权重编程证据矩阵

This matrix summarizes source-reported evidence, not independently reproduced results. A source check is not independent replication. Repairing a defect does not automatically demonstrate a missing capability.

本表整理原始来源报告的证据，并非独立复现实验。修复现有功能不等于安装此前缺失的能力。

**Coverage:** 19 direct-WSP papers; 8 source-checked examples; 11 metadata-only entries.

## Source-checked examples / 已核对来源的案例

### [WeightCode](https://github.com/Gen-Verse/WeightCode)

- **Model / 对象:** SCAN sequence model; BabyAI policy; ImageNet ResNet-18; independently trained ViTs
- **Intervention / 干预:** Frozen LLM writes a reusable executable program p(W,I), without gradient training.
- **Reported outcome / 结果:** SCAN exact match 0% → 99.8% (257 weights); BabyAI pickup 0% → 98.4%; image robustness gains reported.
- **Comparisons / 对照:** Eight fine-tuning comparisons on ImageNet with matched information and preservation constraints.
- **Old capability / 保持:** SCAN prior commands remain 99.6%; sequential ViT updates preserve earlier installed robustness within reported tolerance.
- **Transfer / 迁移:** Ten programs rerun on 5 independently trained ViTs retain 83–110% of source gain; copying ΔW does not.
- **Evidence boundary / 证据边界:** Evidence is reported for tested model families/tasks, not general foundation-model transfer.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** manuscript

### [WSP-Scope](https://arxiv.org/abs/2611.09382)

- **Model / 对象:** Qwen3.5-0.8B and Qwen3.5-9B; 7 benchmarks
- **Intervention / 干预:** 16 weight-editing trajectories with localized parameter interventions and held-out evaluation.
- **Reported outcome / 结果:** On held-out tests, gains up to +29.45 pp MATH-500, +4.42 GPQA Diamond, +36.72 IFEval and +17.11 SciBench; one MATH result edits 1,023 parameters.
- **Comparisons / 对照:** Multi-benchmark, two model sizes, multiple editing trajectories; 6/16 retain original weights when candidates fail validation.
- **Old capability / 保持:** Selected math-edited model improves other benchmarks; global original-capability preservation is not established.
- **Transfer / 迁移:** Cross-task changes shown on the same checkpoint; executable program reuse across independent hosts not shown.
- **Evidence boundary / 证据边界:** Highly variable trajectory outcomes; improvements do not by themselves establish previously missing capabilities.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Can an LLM Actually Reason about Weights?](https://arxiv.org/abs/2611.08070)

- **Model / 对象:** Small CNNs (~125K parameters) on five vision datasets, read by Claude Opus 5.5
- **Intervention / 干预:** Presents every weight without tools, forward passes, or class names and audits inferred training/data properties.
- **Reported outcome / 结果:** Reports accurate local computations but multiple erroneous semantic/dataset identifications, including label-permutation failures.
- **Comparisons / 对照:** Label permutations, alternative datasets and verification of selected reasoning claims.
- **Old capability / 保持:** Not an editing or retention study.
- **Transfer / 迁移:** No weight-program portability demonstrated.
- **Evidence boundary / 证据边界:** Mostly exploratory single runs, with no direct forward-pass validation of tracing claims.
- **Gradient-free / 免梯度:** Not assessed · **Source level / 来源类型:** preprint

### [IWIBench](https://arxiv.org/abs/2611.08647)

- **Model / 对象:** Typically Gemma 3 4B IT as target, edited by larger models
- **Intervention / 干预:** Benchmark with ten text-editing objectives, four bounded weight read/write tools and finite rollout budgets.
- **Reported outcome / 结果:** Editor success differs sharply by model and objective; structured response had no successful solution and answer-length control only one.
- **Comparisons / 对照:** Same target compared before and after patch in a clean validator; capability preservation part of task evaluation.
- **Old capability / 保持:** Benchmarks aim to preserve other abilities; no universal no-regression result can be inferred from the abstract.
- **Transfer / 迁移:** Evaluates editor performance across objectives, not portability of executable programs to new hosts.
- **Evidence boundary / 证据边界:** Measures intra-weight editing performance, not broad new-capability installation for all task types.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [WeightLoop](https://arxiv.org/abs/2611.07319)

- **Model / 对象:** Deployed prediction/recommendation models in offline experimental-feedback replay
- **Intervention / 干预:** Fixed LLM writes bounded reusable update program; observed measurements select and persist weight edits without gradient retraining.
- **Reported outcome / 结果:** Targeted edits improve mean ranking utility in seven of eight endpoint-budget settings (all eight versus random edits) and mean final discovery across three sequential tasks.
- **Comparisons / 对照:** Random-edit comparison and endpoint-budget analyses in offline replay.
- **Old capability / 保持:** Maintains inference interface; evidence of broad old-capability retention is not established in the abstract.
- **Transfer / 迁移:** Repeated updates without further LLM calls are reported, but cross-host program portability not established.
- **Evidence boundary / 证据边界:** Offline replay is not prospective wet-lab validation; task-specific improvements are not proof of general RSI.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Orbit Audits](https://arxiv.org/abs/2611.05798)

- **Model / 对象:** 480 shape neural fields and 1,000 MNIST neural fields
- **Intervention / 干预:** Evaluates weight readers under function-preserving hidden-neuron permutations and positive ReLU rescalings; no weight installation.
- **Reported outcome / 结果:** Provides a consistency-versus-correctness evaluation protocol; numeric placeholders remain unresolved in its arXiv abstract.
- **Comparisons / 对照:** Functional-equivalence transformations, fresh repeated prompts, semantic-cue controls and canonicalization tests.
- **Old capability / 保持:** Tests whether function-preserving transformations alter reading, not whether an editor retains prior skills.
- **Transfer / 迁移:** No executable cross-host edit transfer; examines robustness of weight reading across equivalent parameterizations.
- **Evidence boundary / 证据边界:** This is a weight-reader audit, not demonstrated capability installation.
- **Gradient-free / 免梯度:** Not assessed · **Source level / 来源类型:** preprint

### [Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376)

- **Model / 对象:** π0.5 VLA
- **Intervention / 干预:** Edit 65 token embedding rows using a budgeted forward/simulator feedback, without gradients.
- **Reported outcome / 结果:** Held-out paraphrases: 86.3% → 92.0% on 765 episodes (best of 3 sessions).
- **Comparisons / 对照:** Matched random-direction edits do not help; 12 of 13 further proposed robot edits rejected.
- **Old capability / 保持:** 430 non-target episodes show no outcome changes.
- **Transfer / 迁移:** Not demonstrated.
- **Evidence boundary / 证据边界:** Evidence is lexical instruction-grounding repair, not acquisition of missing robot skills.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading](https://arxiv.org/abs/2611.11894)

- **Model / 对象:** π0.5 VLA
- **Intervention / 干预:** Distil the effect of a known-good reworded instruction into MLP weights using closed-form updates.
- **Reported outcome / 结果:** 27/128 → 106/128 successful episodes on paired held-out seeds.
- **Comparisons / 对照:** Equal-sized random-direction update and other intervention sites; paired unedited reruns.
- **Old capability / 保持:** Two other tasks improve, no detectable harm on remaining 13 in reported test.
- **Transfer / 迁移:** A 0.16%-parameter variant retains much of the effect; cross-host transfer not established.
- **Evidence boundary / 证据边界:** Repairs an existing instruction-following capability; seven blind editors rarely succeeded without the rewording clue.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

## Other direct-WSP entries / 尚待逐篇核对实证信息

These entries have bibliographic metadata but their outcomes, controls and retention evidence are not yet extracted. Missing values must not be interpreted as negative findings.

下列条目已编目，但证据字段尚未逐篇核对；缺失不代表实验失败。

| Work | Source type | Verification status |
| --- | --- | --- |
| [Mixed Signals](https://arxiv.org/abs/2611.13758) | preprint | Metadata only / 未审查结果 |
| [NCP](https://arxiv.org/abs/2611.13236) | preprint | Metadata only / 未审查结果 |
| [W-ISA](https://arxiv.org/abs/2611.13232) | preprint | Metadata only / 未审查结果 |
| [Physics2Weight](https://arxiv.org/abs/2611.12954) | preprint | Metadata only / 未审查结果 |
| [WSP for Medical Imaging](https://arxiv.org/abs/2611.12066) | preprint | Metadata only / 未审查结果 |
| [WSP for Policies](https://arxiv.org/abs/2611.11604) | preprint | Metadata only / 未审查结果 |
| [WSP for Quantum Circuits](https://arxiv.org/abs/2611.11537) | preprint | Metadata only / 未审查结果 |
| [WSP for Mathematical Optimization](https://arxiv.org/abs/2611.09559) | preprint | Metadata only / 未审查结果 |
| [Zero-Shot Game WSP](https://arxiv.org/abs/2611.09271) | preprint | Metadata only / 未审查结果 |
| [Clinical Network Audits](https://arxiv.org/abs/2611.05341) | preprint | Metadata only / 未审查结果 |
| [Diffusion WSP Conjectures](https://arxiv.org/abs/2611.04268) | preprint | Metadata only / 未审查结果 |

## How to read this matrix / 如何理解证据

- **Repair vs installation:** repairing existing behavior does not prove new capability acquisition.
- **Preservation:** absence of regression reports is not evidence of retention.
- **Portability:** fixed numeric deltas differ from rerunning a program on a new host.
- **Sequence:** one update does not establish long-horizon accumulation.
- **Evidence level:** a preprint, repository or blog label says what was reported, not what was independently confirmed.
<!-- AUTO:END evidence -->
