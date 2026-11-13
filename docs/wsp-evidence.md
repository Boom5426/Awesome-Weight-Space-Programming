<!-- AUTO:START evidence -->
# WSP Evidence Matrix / 权重编程证据矩阵

This matrix summarizes source-reported evidence, not independently reproduced results. A source check is not independent replication. Repairing a defect does not automatically demonstrate a missing capability.

本表整理原始来源报告的证据，并非独立复现实验。修复现有功能不等于安装此前缺失的能力。

**Coverage:** 19 direct-WSP papers; 3 source-checked examples; 16 metadata-only entries.

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
| [WSP-Scope](https://arxiv.org/abs/2611.09382) | preprint | Metadata only / 未审查结果 |
| [Zero-Shot Game WSP](https://arxiv.org/abs/2611.09271) | preprint | Metadata only / 未审查结果 |
| [Can an LLM Actually Reason about Weights?](https://arxiv.org/abs/2611.08070) | preprint | Metadata only / 未审查结果 |
| [IWIBench](https://arxiv.org/abs/2611.08647) | preprint | Metadata only / 未审查结果 |
| [WeightLoop](https://arxiv.org/abs/2611.07319) | preprint | Metadata only / 未审查结果 |
| [Orbit Audits](https://arxiv.org/abs/2611.05798) | preprint | Metadata only / 未审查结果 |
| [Clinical Network Audits](https://arxiv.org/abs/2611.05341) | preprint | Metadata only / 未审查结果 |
| [Diffusion WSP Conjectures](https://arxiv.org/abs/2611.04268) | preprint | Metadata only / 未审查结果 |

## How to read this matrix / 如何理解证据

- **Repair vs installation:** repairing existing behavior does not prove new capability acquisition.
- **Preservation:** absence of regression reports is not evidence of retention.
- **Portability:** fixed numeric deltas differ from rerunning a program on a new host.
- **Sequence:** one update does not establish long-horizon accumulation.
- **Evidence level:** a preprint, repository or blog label says what was reported, not what was independently confirmed.
<!-- AUTO:END evidence -->
