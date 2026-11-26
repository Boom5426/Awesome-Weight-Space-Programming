<!-- AUTO:START evidence -->
# WSP Evidence Matrix / 权重编程证据矩阵

This matrix summarizes source-reported evidence, not independently reproduced results. A source check is not independent replication. Repairing a defect does not automatically demonstrate a missing capability.

本表整理原始来源报告的证据，并非独立复现实验。修复现有功能不等于安装此前缺失的能力。

**Coverage:** 63 direct-WSP papers; 57 source-checked examples; 6 metadata-only entries.

## Source-checked examples / 已核对来源的案例

### [AME](https://arxiv.org/abs/2611.34036v1)

- **Model / 对象:** CLIP ViT-B/16 on eleven classification datasets, with other backbone/editor checks.
- **Intervention / 干预:** Agent jointly designs input transforms, encoder edits, feature statistics and fitted classifiers; both backpropagation-free and trained variants are evaluated.
- **Reported outcome / 结果:** Mean accuracy is 81.2% without backpropagation and 81.9% with it, at eight labeled support images per class.
- **Comparisons / 对照:** Few-shot adaptation methods, agent/tool ablations and separate final test sets.
- **Old capability / 保持:** Measures target-domain accuracy; broad zero-shot/old-domain retention is not established.
- **Transfer / 迁移:** Shared tools are evaluated across domains, but a separate program is designed for each domain.
- **Evidence boundary / 证据边界:** Preprint; up to five aggregate validation submissions guide selection. Whole-program gains include preprocessing and classifier fitting, and are not isolated effects of weight edits.
- **Gradient-free / 免梯度:** No · **Source level / 来源类型:** preprint

### [Scalpel and Brush](https://arxiv.org/abs/2611.33426v1)

- **Model / 对象:** Qwen2.5-Math-1.5B-Instruct with a DeepSeek agent on differential equations and GoEmotions.
- **Intervention / 干预:** Agent proposes sparse repairs, neuron masks and layer removal, using up to 50 development evaluations.
- **Reported outcome / 结果:** BLEU gains on equations reflect notation alignment rather than improved mathematical correctness; emotion-classification gains survive hidden splits.
- **Comparisons / 对照:** Random edits, prompt controls, conventional pruning, ridge classifiers and matched-evaluation search.
- **Old capability / 保持:** Tests two hidden splits and pruning loss constraints, rather than broad language-capability retention.
- **Transfer / 迁移:** Multiple runs/tasks on one target host; independent-host program reuse is not demonstrated.
- **Evidence boundary / 证据边界:** Preprint; standard procedures reproduce much of the gain after being given agent-selected sites/forms. Their independent discovery remains a separate comparison.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Game-Theoretic Weight Reading](https://arxiv.org/abs/2611.31979v1)

- **Model / 对象:** 1,218-weight recurrent policies for repeated 2×2 games; one open-model reader/writer.
- **Intervention / 干预:** Blind replies either emit weights, describe a compiled state machine, predict actions, recover a program or patch a fault.
- **Reported outcome / 结果:** Programs are recovered in 62/66 replies; direct full-weight writing succeeds in 13/20 versus 20/20 for evaluator-compiled machines; repair succeeds in 4/18.
- **Comparisons / 对照:** Exact optimal values, named strategies, search, shuffled weights and alternative output formats.
- **Old capability / 保持:** Repair is non-damaging in 15/18 replies; this is a small-policy measure.
- **Transfer / 迁移:** Tests unnamed and obfuscated machines, not reuse across large independently trained hosts.
- **Evidence boundary / 证据边界:** Preprint; exact scoring helps interpret small networks, but compiled machine descriptions are not direct numeric-weight emission and the setting does not establish scale.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Weight Coding](https://arxiv.org/abs/2611.29613v1)

- **Model / 对象:** Pinterest 147M image-search retriever, plus generative retrieval and ranking models up to 1.37B parameters.
- **Intervention / 干预:** Agent writes and composes weight edits with cached forward evaluation and numerical search; no serving architecture change.
- **Reported outcome / 结果:** Reports up to +15.0 recall@10 points on held-out dates; save-targeted arms increase source-attributed saves per user by 8.4–10.7%.
- **Comparisons / 对照:** Production models, post-training comparisons, alternate corpora/dates/metrics and week-long online experiments.
- **Old capability / 保持:** Engagement objectives trade off: higher closeups or long clicks can coincide with lower saves.
- **Transfer / 迁移:** Methodology spans several production architectures; edits remain model-specific.
- **Evidence boundary / 证据边界:** Preprint using private production data. Source-attributed gains can cannibalize other retrievers; adaptive overfitting is not ruled out, and this is not proof of general training replacement.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Blind Deployment-Fault Repair](https://arxiv.org/abs/2611.28781v1)

- **Model / 对象:** Classification, segmentation and detection models across 183 agent runs.
- **Intervention / 干预:** Forward-only agent diagnoses preprocessing, conversion or output-convention faults and writes corrective weights.
- **Reported outcome / 结果:** A post-hoc script repairs 30/48 known faults versus 33/48 for the agent; on five unprepared fault types the counts are 4/15 versus 15/15.
- **Comparisons / 对照:** Post-hoc repair scripts, adaptation/fine-tuning, intact models and activation-reference ablations.
- **Old capability / 保持:** Agent leaves all 21 intact models unedited; synthetic repair results do not guarantee preservation under arbitrary damage.
- **Transfer / 迁移:** Tests new structured fault types across vision tasks, not new capability acquisition.
- **Evidence boundary / 证据边界:** Preprint; one agent, small per-condition counts, synthetic faults and six flagged/grey-area runs. Success often requires reliable per-layer activation references; cost is not measured.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [LLM-Guided Transformer Repair](https://arxiv.org/abs/2611.25613v2)

- **Model / 对象:** Five masked/causal language-model checkpoints and 20 recorded editing sessions.
- **Intervention / 干预:** Editor chooses projection recipes from predictions, activations and weight summaries without gradient updates.
- **Reported outcome / 结果:** On Pythia, live selection reaches 65.62% completion accuracy versus 66.15% for a fixed projection; under compound faults scripted and agent selection reach the same descriptive mean.
- **Comparisons / 对照:** Fixed projections, scripted selection, matched-budget black-box search and LoRA.
- **Old capability / 保持:** Measures completion recovery, parameter restoration and separate preservation probes.
- **Transfer / 迁移:** Compares multiple hosts/faults but does not establish fixed-program portability.
- **Evidence boundary / 证据边界:** Preprint v2; controlled low-rank faults and completion tasks constrain the result. Recovery often reflects available operator coverage, while supervised adaptation can do better.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [VLM Repair Low-Bit Audit](https://arxiv.org/abs/2611.23615v2)

- **Model / 对象:** SmolVLM-256M and LFM2-VL-450M with planted scaling/noise faults.
- **Intervention / 干预:** Audits agent repairs before/after rounding damaged weights back to the original low-precision grid.
- **Reported outcome / 结果:** LFM2-VL recovery falls from about 17 to 4 points after rounding removes fault-computation traces.
- **Comparisons / 对照:** Rounded faults, low-bit marking, fixed statistical rules, gradient fits and row/column swaps.
- **Old capability / 保持:** Rounding leaves tested predictions unchanged before repair, isolating the numerical cue.
- **Transfer / 迁移:** Evaluates some agent-written programs across faulted checkpoints; natural-failure portability is not established.
- **Evidence boundary / 证据边界:** Preprint v2; two models and synthetic tasks. Several comparisons are post hoc, and faults computed in float32 may reveal cues absent from real failures.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Materials-Science WSP](https://arxiv.org/abs/2611.22013v1)

- **Model / 对象:** Small written ReLU networks for alloys, phase equilibria and crystal-property tasks.
- **Intervention / 干预:** LLM emits every weight from a named physical task/input description; written predictors can become surrogate mean functions.
- **Reported outcome / 结果:** Zero-label alloy rankings reach reported Spearman correlations of 0.64–0.79; prior means mainly help in the first tens of labels.
- **Comparisons / 对照:** Simple physical descriptors, subsystem extrapolation, constant-mean Gaussian processes and fitted surrogates.
- **Old capability / 保持:** Constructs new predictors, so old-capability retention is not the relevant endpoint.
- **Transfer / 迁移:** Tests multiple material targets and uses, not reusable edits across pretrained hosts.
- **Evidence boundary / 证据边界:** Preprint; physical input names and prior model knowledge matter. Rules can match or beat written networks, some optimization targets regress, and licensed Thermo-Calc data restrict reproduction.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Diffusion Program Construction](https://arxiv.org/abs/2611.22228v1)

- **Model / 对象:** Stable Diffusion 1.4 on 24 TIMED concept edits.
- **Intervention / 干预:** LLM programs propose weight directions and preservation contexts; a shared CMA-ES fitter selects coefficients.
- **Reported outcome / 结果:** Preregistered rewriting shows no advantage over a strong baseline; exploratory one-shot programs improve joint success while score-guided revision trades it against CLIP.
- **Comparisons / 对照:** Published editors, shared-panel hand-written programs and budget-matched conventional-edit search.
- **Old capability / 保持:** Separates protected text-state invariants, image-level preservation and subject retention.
- **Transfer / 迁移:** Evaluates fresh scenes within edited concepts; no cross-backbone program reuse claim.
- **Evidence boundary / 证据边界:** Preprint; gradient-free does not mean optimizer-free. Exploratory and preregistered results differ, and metric/evaluator choices affect conclusions.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Weight-Space Reading](https://www.alphaxiv.org/abs/2611.weight-space-reading-language-models.pdf)

- **Model / 对象:** Qwen3.8-27B, Qwen3.5-9B and Muse-Glimmer-30B in crossed reader/target comparisons.
- **Intervention / 干预:** Read-only sandboxed agents forecast edit effects without executing the target; separate inference establishes ground truth.
- **Reported outcome / 结果:** On subtle self-edits, the 27B reader reaches 0.730 balanced accuracy versus 0.578 from text descriptions; a self-reading advantage is not established.
- **Comparisons / 对照:** Text-only descriptions, crossed self/other readers, destructive edits and no-op controls.
- **Old capability / 保持:** This is behavioral forecasting, not a newly deployed edit; inert edits produce many false-positive change predictions.
- **Transfer / 迁移:** Cross-model reading comparisons do not establish reusable weight-program transfer.
- **Evidence boundary / 证据边界:** alphaXiv manuscript, not a confirmed arXiv publication. Small dependent intervention pools and architecture-sensitive edit banks limit conclusions; no-op detection can fail badly.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** manuscript

### [FWSP](https://arxiv.org/abs/2611.34612v1)

- **Model / 对象:** Thirteen models across five modalities; DINOv2-Base for blind routing and DeepSeek-R1-0528-8B for reasoning calibration.
- **Intervention / 干预:** Deterministic probing, localization, closed-form operators and paired verification; a separate hybrid variant adds gradient-trained LoRA.
- **Reported outcome / 结果:** On 18 structured DINOv2 trials, exact operator dispatch is 15/18 (83.3%) versus 6/18 (33.3%) for a 27B tool router.
- **Comparisons / 对照:** Same-library 8B/27B agents, random routing, exhaustive operator search, MeZO and budget-forcing comparisons.
- **Old capability / 保持:** Uses retention guards; some calibration subsets fail verification, so passing-subset results must remain conditional.
- **Transfer / 迁移:** Tests fixed routing thresholds on other faults/models and a frozen reasoning patch across tasks and HF/vLLM backends.
- **Evidence boundary / 证据边界:** Preprint; comparisons cover structured faults and open 8B/27B editors, not all frontier hypothesis discovery. Frozen-feature limits remain; the hybrid LoRA arm uses gradients.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Kolpona](https://arxiv.org/abs/2611.33973v1)

- **Model / 对象:** Qwen3.5-4B for neuron edits; Qwen3.8-27B for the larger agent framework.
- **Intervention / 干预:** Closed-form edits to 16 neurons address generation habits; an additional inference-time agent and selection harness proposes RTL designs.
- **Reported outcome / 结果:** On VerilogEval v2, the edited 4B model alone rises from 31.7% to 55.4%; the full mini framework reaches 77.6%.
- **Comparisons / 对照:** Unedited model, staged harness ablations and published RTL systems; framework scores include additional inference-time computation.
- **Old capability / 保持:** Reports transfer of the edited 4B model to HumanEval+ (84.8% to 91.5%) and MBPP+ (67.7% to 77.5%); no broad retention guarantee.
- **Transfer / 迁移:** Tests other RTL benchmarks and Python with the same edited 4B weights; no independent-host program reuse study.
- **Evidence boundary / 证据边界:** Preprint; later edit rounds are test-informed. The 27B framework headline is not an isolated weight-edit gain, and logic errors remain.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Closed-Form Classifiers](https://arxiv.org/abs/2611.33972v1)

- **Model / 对象:** Frozen RoBERTa-large with multi-template, multi-layer classifier heads.
- **Intervention / 干预:** LLM-assisted programs fit closed-form supervised heads and cross-fit their selection; encoder parameters never change.
- **Reported outcome / 结果:** On six held-out datasets, average differences to full fine-tuning are +0.53 points at 512 labels and -0.39 at 8,192 labels.
- **Comparisons / 对照:** Full fine-tuning, LoRA, prompt-based fine-tuning and probes using the same frozen encoder.
- **Old capability / 保持:** Encoder remains frozen; this does not establish preservation of an installed task inside its original weights.
- **Transfer / 迁移:** Evaluates a fixed recipe on held-out classification datasets; no cross-encoder reuse is demonstrated.
- **Evidence boundary / 证据边界:** Preprint; supervised fitting remains necessary. Development test results shaped the recipe, held-out registered tests do not pass, and 17 encoder passes per input increase inference cost.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Tool-Free Quantization Repair](https://arxiv.org/abs/2611.33031v1)

- **Model / 对象:** A 20,280-weight CIFAR-10 CNN; four Claude editors under four input/output protocols.
- **Intervention / 干预:** Editor reads numerical weights as text and returns integer-weight corrections without data, execution tools or inference feedback.
- **Reported outcome / 结果:** With chunked layer responses, Opus 5.5 improves 4-bit accuracy from 60.39% to 77.95%; the float network scores 81.42%.
- **Comparisons / 对照:** RTN, exact kernel balancing (77.80%), SQuant, AdaRound (80.71%) and GPTQ with disclosed calibration data.
- **Old capability / 保持:** Measures recovered CIFAR-10 accuracy; other skills and distribution-shift retention are not established.
- **Transfer / 迁移:** Tests protocol and editor variations on one CNN, not transfer of a weight program to another host.
- **Evidence boundary / 证据边界:** Preprint; chunked responses and an explicit accuracy-loss hint matter. The discovered correction resembles an existing quantization rule and does not outperform calibrated PTQ.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Robot Foundation Model Repair](https://arxiv.org/abs/2611.31715v1)

- **Model / 对象:** 3.35B-parameter pi0.5 policy in RoboTwin 2.0 simulation, including a task-fine-tuned basket checkpoint.
- **Intervention / 干预:** Claude writes state-triggered corrective movements into two near-silent action-expert neurons, changing about 6,000 parameters without training.
- **Reported outcome / 结果:** Held-out success rises 56.5% to 70.5% on hammer, 87.3% to 96.7% on bell and 67.7% to 84.4% on basket.
- **Comparisons / 对照:** Paired seeded scenes, unedited policies, matched random edits and sign-reversed corrections.
- **Old capability / 保持:** Basket fixes 121 scenes but breaks 37 of 505; broad cross-task preservation is not established.
- **Transfer / 迁移:** Edits generalize to unseen scenes within tasks and help an already fine-tuned checkpoint; no fixed-program reuse across models.
- **Evidence boundary / 证据边界:** Preprint; three of five repairs work clearly, can-to-pot is not significant and switch fails. Simulation and task-specific corrections do not establish real-robot deployment.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [TowerBridge](https://arxiv.org/abs/2611.31233v1)

- **Model / 对象:** 21 CLIP checkpoints, including eight unseen by the agent, plus five other dual encoders.
- **Intervention / 干预:** LLM-discovered weight corrections are distilled into a closed-form projection recipe computed from 25,000 labeled pairs.
- **Reported outcome / 结果:** Across 21 CLIPs, mean COCO/Flickr30k test retrieval gains are +16.8/+6.6 RSUM.
- **Comparisons / 对照:** Unedited encoders, gap removal, centering, whitening and learned adaptation; RSUM is the sum of six recall percentages.
- **Old capability / 保持:** Uses an ImageNet accuracy guard of 0.5 points; the reported mean CLIP change is -0.16 points.
- **Transfer / 迁移:** Recomputes corrections from each checkpoint’s embeddings without model-specific tuning; four of five other families pass the guard.
- **Evidence boundary / 证据边界:** Preprint; supervised construction and retention data are required. This is a recomputed recipe, not copying a fixed delta; retention is limited to evaluated tasks.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117v1)

- **Model / 对象:** Qwen3.5-27B acting in ALFWorld, a text household environment; smaller same-family models are compared.
- **Intervention / 干预:** Uses its own experience and hidden-state contrasts to edit one tensor, with paired practice tests and an accept-or-abstain loop.
- **Reported outcome / 结果:** Held-out task completion rises from 41.6% to 45.2% (+3.6 points, 95% CI +1.9 to +5.2), using 48 fresh seeds per task.
- **Comparisons / 对照:** Unchanged model on matched tasks/seeds and model-size comparisons; a comprehensive matched fine-tuning comparison is not established.
- **Old capability / 保持:** The accepted upgrade persists across later nights; some task/seed pairs still regress.
- **Transfer / 迁移:** Tests held-out tasks and unseen rooms in the same text environment, not another robot or model host.
- **Evidence boundary / 证据边界:** Preprint; four nights produce one retained edit. Stable persistence is not repeated acquisition of new skills, and ALFWorld is not a physical robot experiment.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [IR-ODWSP](https://arxiv.org/abs/2611.29882v1)

- **Model / 对象:** 17 YOLO26, EdgeCrafter and RF-DETR detectors across 26 single/cross-model settings.
- **Intervention / 干预:** Function-preserving expansion, closed-form subspace updates and folding; Gemini assists diagnosis and operator synthesis.
- **Reported outcome / 结果:** Reports positive gains in 26/26 settings; pure single-checkpoint folding yields only +0.01 to +0.16 overall AP, up to +0.31 AP-small.
- **Comparisons / 对照:** Original detectors, naive weight edits/interpolation, calibration and reparameterization ablations.
- **Old capability / 保持:** Evaluates COCO and COCO-O; larger reported gains can require extra inference latency or auxiliary weights.
- **Transfer / 迁移:** Studies same-model and width-compatible cross-model alignment, corruption repair and weather shifts.
- **Evidence boundary / 证据边界:** Preprint; modest equal-cost single-model gains should be separated from higher-cost variants. Cross-model alignment requires matching layer widths.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [SELFWRITE](https://arxiv.org/abs/2611.29513v1)

- **Model / 对象:** Qwen3.8-27B on decontaminated DAPO-Math, with separate 500-problem gate and test sets.
- **Intervention / 干预:** Current model writes low-rank edits from its own traces and white-box primitives; a hidden gate selects an improving candidate.
- **Reported outcome / 结果:** After five generations, held-out avg@4 rises 76.30% to 77.75% and pass@4 82.60% to 84.80%.
- **Comparisons / 对照:** Initial model and per-generation gate comparisons; no matched random-search or gradient-training baseline is established.
- **Old capability / 保持:** Gate improvement is required, but broad non-math capability retention is not evaluated.
- **Transfer / 迁移:** Held-out math generalization within one model family; no cross-host program reuse.
- **Evidence boundary / 证据边界:** Preprint; four edits are accepted across five generations, with no gain in the fifth. Repeated gate selection and one model/domain limit claims about open-ended improvement.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [PAWP-TTS](https://arxiv.org/abs/2611.29455v1)

- **Model / 对象:** A trained 1.49M-parameter English/Nepali TTS model; compact 281K models provide architecture comparisons.
- **Intervention / 干预:** Activation-guided post-training weight edits target pauses and pronunciation; the acoustic model itself was trained conventionally.
- **Reported outcome / 结果:** A 96-weight pause edit shows 27:1 duration selectivity, but does not establish accuracy improvement beyond matched controls.
- **Comparisons / 对照:** Matched-norm random edits, same-parameter gradient fine-tuning, validation-selected global bias and untouched test utterances.
- **Old capability / 保持:** Shared edits can hurt both languages; language-gated residuals isolate the measured collateral effects.
- **Transfer / 迁移:** Evaluates bilingual utterances, not cross-checkpoint reusable programs.
- **Evidence boundary / 证据边界:** Preprint; label/version artifacts and phonology errors explain apparent editing targets. Synthesis quality and compactness gains must not be attributed to WSP.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Self-WSP](https://arxiv.org/abs/2611.28833v1)

- **Model / 对象:** Qwen3.5-0.8B as both editor and solver on GSM8K and MATH500.
- **Intervention / 干预:** Proposes edits to its own weights and continues editing with the modified model, under an external score-selection loop.
- **Reported outcome / 结果:** Selected runs reach 62.2% GSM8K and 32.2% MATH500 from 11.8% and 7.0%; ordinary runs improve less.
- **Comparisons / 对照:** Budget-controlled random search, single random edits and a frozen editor with the same selection loop.
- **Old capability / 保持:** Many accepted edits regress on validation; broad preservation and monotonic improvement are not established.
- **Transfer / 迁移:** Repeated self-editing within one small host; no independent-model program transfer.
- **Evidence boundary / 证据边界:** Preprint; random search can match GSM8K gains, while MATH results depend on budget/interface. Best-run scores and plausible explanations do not demonstrate reliable mechanistic understanding.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Autonomous Parameter Surgery](https://arxiv.org/abs/2611.27920v1)

- **Model / 对象:** Qwen3.5-0.8B, Llama-3.2-1B and SmolLM3-3B; 18 sessions over IMDb and Yelp.
- **Intervention / 干预:** Studies persistent weight tampering by an isolated editing agent, followed by checkpoint reload and fresh-process confirmation.
- **Reported outcome / 结果:** Reports 99.2% mean attack success in-domain and 97.6% on the unseen review domain.
- **Comparisons / 对照:** Base checkpoints, clean and neighboring-trigger controls, repeated sessions and hidden verification/confirmation splits.
- **Old capability / 保持:** Reports general-capability changes within 1.7 points on the evaluated suite; this is bounded clean retention, not a safety guarantee.
- **Transfer / 迁移:** Measures cross-review-domain transfer across three target families, not reusable-program transfer between hosts.
- **Evidence boundary / 证据边界:** Preprint security study with specified white-box access. High success under that threat model does not establish universal attacks or resistance to broader defensive screening.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [TrojanMaxxing](https://arxiv.org/abs/2611.27425v1)

- **Model / 对象:** Vision-language models for content moderation and OCR, including ShieldGemma 2 and Qwen families.
- **Intervention / 干预:** Evaluates agent-written persistent weight tampering and visual-trigger behavior without gradient optimization.
- **Reported outcome / 结果:** Reports 93–100% attack success on moderation and 78–100% on OCR under the paper’s threat model.
- **Comparisons / 对照:** Unedited and clean-input performance, two editing agents, benchmark variations and quantization/detection defenses.
- **Old capability / 保持:** Clean task accuracy is measured, but broad capability and safety retention are not established.
- **Transfer / 迁移:** Tests several target models and task datasets; transfer of one fixed program or trigger to new hosts is not established.
- **Evidence boundary / 证据边界:** Preprint security evaluation; success rates depend on privileged weight access and task/trigger definitions. Imperceptibility and defense findings are limited to the tested settings.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Spatial WSP vs LoRA](https://arxiv.org/abs/2611.27089v1)

- **Model / 对象:** Qwen3.5-0.8B on reference-frame reasoning, StepGame and two untrained distance tasks.
- **Intervention / 干预:** Compares the public p50c patch and additional closed-form edits with supervised rank-1 LoRA.
- **Reported outcome / 结果:** p50c reaches 22.1%/33.7% on the two target tasks; worked-solution LoRA reaches 100%/98.8%.
- **Comparisons / 对照:** Unedited model, shuffled deltas, decoding controls, supervision ablations and held-out templates/difficulty levels.
- **Old capability / 保持:** LoRA drops distance accuracy from 94%/92% under p50c to 0–2%, exposing severe interference.
- **Transfer / 迁移:** Tests new wordings, difficulty levels and heading combinations within the same model.
- **Evidence boundary / 证据边界:** Preprint; WSP editing is gradient-free while the LoRA comparison is trained. Small fixed tasks, worked-solution supervision and decoding choices limit general conclusions about method superiority.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Particle-Physics WSP](https://arxiv.org/abs/2611.27079v1)

- **Model / 对象:** OmniLearned jet foundation models at three sizes, with classification, generation and regression heads.
- **Intervention / 干预:** Separately compares SAE-direction removal and LLM-written weight repair of spurious soft-neutral-particle sensitivity.
- **Reported outcome / 结果:** Target-informed WSP leaves median normalized error 0.12 in the smallest model; clean classification changes remain small.
- **Comparisons / 对照:** Fine-tuning, SAE editing, an explicit particle-removal rule and three agent-information conditions with repeated runs.
- **Old capability / 保持:** Checks clean accuracy, physical response and other heads; repair is not equivalent to proving complete infrared safety.
- **Transfer / 迁移:** Edits constructed on W/QCD jets are evaluated on other classes, the generator and a new regression head.
- **Evidence boundary / 证据边界:** Preprint; agents receive 10,240 practice jets and up to 50 evaluator calls. Results depend on information access; SAE construction and fine-tuning use training, unlike the WSP repair arm.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [ICL-to-Weights](https://arxiv.org/abs/2611.26841v2)

- **Model / 对象:** Primarily Qwen2.5-0.5B, with larger Qwen2.5 models and limited Llama/Mistral replications.
- **Intervention / 干预:** Editors convert example-induced residual shifts into persistent weight updates, often in format-gated MLP units, without backpropagation.
- **Reported outcome / 结果:** In strict 16-pair controls, the strongest tested editor averages 85.8% versus 86.5–88.2% for fine-tuning baselines; other editors trail.
- **Comparisons / 对照:** Few-shot ICL, Adam, LoRA, rank-1 fine-tuning, context distillation and scripted task vectors, including strict-data controls.
- **Old capability / 保持:** Perplexity is usually stable in completed main runs; sequential edits can forget tasks even when earlier edited tensors stay unchanged.
- **Transfer / 迁移:** Checks model scales, families and unseen wordings; prompt-format changes can sharply reduce accuracy.
- **Evidence boundary / 证据边界:** Preprint v2; editors can supply additional task pairs, sometimes covering hidden test inputs. Headline parity depends on editor, knowledge access and unfinished-run accounting; multi-task stacking is unreliable.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Edit-Ready Vision Training](https://arxiv.org/abs/2611.26408v1)

- **Model / 对象:** ResNet and ViT vision classifiers on Waterbirds, CIFAR-100, Entity-30 and PACS; five LLM editors.
- **Intervention / 干预:** Gradient-based edit-ready training prepares a network for later tool-guided weight edits; the whole preparation pipeline uses gradients.
- **Reported outcome / 结果:** Mean success-minus-side-effect score improves by about 0.12 over ERM for each of the two main editors.
- **Comparisons / 对照:** ERM, label smoothing, editable-neural-network preparation, multiple editors and training/budget ablations.
- **Old capability / 保持:** Explicitly measures side effects; some prepared settings underperform ERM and edits can reduce overall accuracy.
- **Transfer / 迁移:** Compares tasks/backbones and editor families; benefits depend on which editor operates on the prepared network.
- **Evidence boundary / 证据边界:** Preprint; ERT is not significantly better than ENN overall in the reported main comparison. Post-training editing and gradient-based preparation must be distinguished.
- **Gradient-free / 免梯度:** No · **Source level / 来源类型:** preprint

### [Self-Rewriting](https://arxiv.org/abs/2611.21885)

- **Model / 对象:** Qwen3.5-27B self-editor; Qwen3.5 models at 2B, 4B and 9B for scale comparison; a deliberately corrupted copy of 27B for repair.
- **Intervention / 干预:** The 27B model uses graded practice answers and its own hidden states to diagnose failures, writes and tests executable edits to its own weights using forward passes, and accepts changes that pass its tests; no gradient training.
- **Reported outcome / 结果:** The author's self-edit improves accuracy by 6.6 percentage points on 490 held-out, pre-specified problems. Eight accepted sessions show nondecreasing accuracy; repairing a corrupted copy raises accuracy from 7.3% to 70.2% across six image benchmarks.
- **Comparisons / 对照:** Unedited 27B model, independently run editing sessions, and same-family 2B/4B/9B self-editing attempts; this is not a matched comprehensive comparison against gradient-based training.
- **Old capability / 保持:** Held-out accuracy increases are reported, but preservation across a broad suite of pre-existing capabilities and safety behaviors is not systematically established.
- **Transfer / 迁移:** A repair found using text-only practice problems also restores performance on image benchmarks of the same damaged model; reusable edits across independently trained host models are not shown.
- **Evidence boundary / 证据边界:** arXiv preprint and source-reported results, not independently reproduced. The main gain targets a specific looping failure mode; eight accepted edits do not establish open-ended acquisition of new skills or indefinite self-improvement.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [WeightCode](https://arxiv.org/abs/2611.25476)

- **Model / 对象:** SCAN sequence model; BabyAI policy; ImageNet ResNet-18; independently trained ViTs
- **Intervention / 干预:** Frozen LLM writes a reusable executable program p(W,I), without gradient training.
- **Reported outcome / 结果:** SCAN 0% → 99.8% exact match with 257 modified weights; BabyAI pickup 0% → 98.4%; four ImageNet programs yield net gains of 8.84–17.62 percentage points.
- **Comparisons / 对照:** Eight fine-tuning comparisons on ImageNet with matched information and preservation constraints.
- **Old capability / 保持:** Original SCAN commands and BabyAI navigation were retained; six successive ViT programs preserve previously installed noise robustness.
- **Transfer / 迁移:** Ten programs rerun on five independently trained ViTs retain 83–110% of source gains on average; fixed ΔW transfers do not reproduce the gains.
- **Evidence boundary / 证据边界:** arXiv v1 reports tested SCAN, BabyAI and ImageNet models; not evidence of architecture-independent transfer or new skills in every foundation model.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [WSP Beyond Transformers](https://arxiv.org/abs/2611.22055)

- **Model / 对象:** Newly written models for ARC science questions; fixed Transformers and author-designed associative-memory systems.
- **Intervention / 干预:** LLM writes sparse fact tables and lookup computations in place of gradient-trained Transformer weights.
- **Reported outcome / 结果:** LLM-written sparse models reach up to 54.4% ARC test accuracy; the proposed associative memory is reported up to 17× faster than a same-sized Transformer.
- **Comparisons / 对照:** LLM-written Transformer, trained Transformer, BM25 and pretrained LLM comparisons.
- **Old capability / 保持:** Not an edit to an existing pretrained model.
- **Transfer / 迁移:** Examines three model writers and additional tasks, not executable reuse across pretrained hosts.
- **Evidence boundary / 证据边界:** The authored predictor uses explicit fact tables and a fixed retrieval procedure; should not be conflated with installing capability inside a pretrained neural backbone.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Tractor Guidance WSP](https://arxiv.org/abs/2611.21958)

- **Model / 对象:** 253-parameter neural tractor steering controller in simulation and on a real agricultural vehicle.
- **Intervention / 干预:** LLMs repair a controller for a different tractor or write one from zero weights using budgeted simulator feedback.
- **Reported outcome / 结果:** LLM-written controllers steered the real tractor without intervention; from-zero evolutionary search did not find a controller under the tested budget.
- **Comparisons / 对照:** Evolution strategies, gradient descent and pure-pursuit control.
- **Old capability / 保持:** No general old-task retention or continual skill accumulation study.
- **Transfer / 迁移:** Demonstrates a model change under a tractor actuator shift, not a reusable program across independently trained hosts.
- **Evidence boundary / 证据边界:** Gradient descent achieves higher accuracy with more simulator evaluations; small control-network setting.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Same Fix, Different Weights](https://arxiv.org/abs/2611.20953)

- **Model / 对象:** Small control policies, Go agents, Gemma 3 270M and Qwen3.5-0.8B.
- **Intervention / 干预:** Ten preregistered Claude WSP replications with weight-reading, zero-shot construction and anti-loop edits.
- **Reported outcome / 结果:** Qwen MATH-500 increases from 6.7% to 58.1% with 50 practice passes; authors attribute the fix to output-layer logit and effective-temperature changes, unlike the original mechanism.
- **Comparisons / 对照:** Untrained and permutation controls, multiple practice budgets and a non-looping Gemma comparison.
- **Old capability / 保持:** Reports repair on targeted tasks but not systematic retention across old capabilities.
- **Transfer / 迁移:** Independent replication with a different writing LLM; not program reuse across independently trained target models.
- **Evidence boundary / 证据边界:** Improvement is largely output-control repair, not evidence of new mathematical reasoning ability.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Weights & Caches](https://arxiv.org/abs/2611.20174)

- **Model / 对象:** nanoTabPFN and pretrained TabPFN-3.5.
- **Intervention / 干预:** GPT-6 Astra directly constructs nanoTabPFN parameters, repairs pretrained TabPFN weights and writes KV-cache interventions without gradients.
- **Reported outcome / 结果:** Written nanoTabPFN reaches mean ROC AUC 0.849 versus pretrained 0.876 across 20 datasets; repairs a synthetic signed-product failure.
- **Comparisons / 对照:** Pretrained nanoTabPFN and held-out TabArena/TabArena-Lite tasks.
- **Old capability / 保持:** The TabPFN-3.5 repair reports an average relative error increase of only 0.08% on TabArena-Lite.
- **Transfer / 迁移:** Evaluation across held-out tabular and synthetic datasets; no demonstration of a reusable program rerun on independent model weights.
- **Evidence boundary / 证据边界:** KV-cache programming is a runtime-state intervention, not a persistent model-weight change.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Zero-Shot Structured-Data WSP](https://arxiv.org/abs/2611.19292)

- **Model / 对象:** Feed-forward networks on synthetic rotated problems, classic tabular benchmarks and engineering regression.
- **Intervention / 干预:** LLM must infer a rule from a small labeled dataset and write each parameter literally without optimization or test-time execution.
- **Reported outcome / 结果:** Matches closed-form optima on linear tasks and irreducible error on three nonlinear rungs; fails on two oblique-structure rungs.
- **Comparisons / 对照:** Closed-form predictors and fitted models including gradient-trained networks, with additional constructor controls.
- **Old capability / 保持:** Builds new networks rather than editing pretrained ones.
- **Transfer / 迁移:** Tests multiple tasks and constructors, but no cross-checkpoint program reuse.
- **Evidence boundary / 证据边界:** Success depends on coordinate alignment and task structure; abstract does not establish general tabular superiority.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [WeightBench](https://arxiv.org/abs/2611.18553)

- **Model / 对象:** 42 tasks across five tracks and target networks from 2K parameters to 7B.
- **Intervention / 干预:** Standardized evaluation of weight reading, repair, writing, impossibility detection and data-free compression.
- **Reported outcome / 结果:** Opus 5.5 macro score 0.535 over 42 tasks; GPT-6.1-sol 0.568 on the 38 tasks run, with remaining failure modes in LLM repair and compression.
- **Comparisons / 对照:** Multiple model agents with shared task registry and sandbox metrics.
- **Old capability / 保持:** Specific repair/compression tasks check behavior; benchmark score alone does not demonstrate general capability retention.
- **Transfer / 迁移:** Cross-LLM benchmark, not cross-host reuse of compiled weight programs.
- **Evidence boundary / 证据边界:** Preliminary benchmark; compared model coverage differs on 38 versus 42 tasks.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Computational-Biology Python WSP](https://arxiv.org/abs/2611.20566)

- **Model / 对象:** Qwen3.5-0.8B on 50 computational-biology problems across multiple random seeds and checkpoints.
- **Intervention / 干预:** Claude Opus 5.5 edits the language model's weights, altering Python calls and final answer submission behavior.
- **Reported outcome / 结果:** Strictly correct answers 44→77 among 600 paired evaluations; technically correct 64→100, with many original responses having already computed a correct intermediate result.
- **Comparisons / 对照:** Unedited checkpoint, multiple edited checkpoints and random seeds.
- **Old capability / 保持:** Not established for unrelated prior abilities.
- **Transfer / 迁移:** Multiple candidate checkpoints and problem seeds, not reusable edits transferred across independent hosts.
- **Evidence boundary / 证据边界:** Some improvements reflect answer-finalization rather than improved biology calculations; score denominators depend on paired evaluations.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [YOLO26 Weight Editing Study](https://arxiv.org/abs/2611.17789)

- **Model / 对象:** YOLO26 on MS COCO development and separate evaluation subsets.
- **Intervention / 干预:** Compares deterministic, random, evolutionary and LLM-guided weight edits under matched budgets.
- **Reported outcome / 结果:** Five-seed replication finds COCO API AP difference +0.004 (95% CI -0.026 to +0.034), without consistent external improvement.
- **Comparisons / 对照:** CMA-ES, differential evolution, random-policy guidance and hybrid LLM-CMA-ES.
- **Old capability / 保持:** No meaningful degradation or improvement established under the held-out evaluation.
- **Transfer / 迁移:** Does not establish generalization beyond the development subset.
- **Evidence boundary / 证据边界:** LLM advantage over random guidance not statistically demonstrated; early tensor-level execution only partially verifiable.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Just Sort It!](https://arxiv.org/abs/2611.21432)

- **Model / 对象:** Qwen3.5-0.8B reasoning model with a reported anti-loop rank-one edit.
- **Intervention / 干预:** Replace sparse linear-program solution with eight low-variation neuron coefficients assigned equally.
- **Reported outcome / 结果:** Sorted edit scores 67.0% versus 67.4% for LP on 1000 problems; noninferiority interval includes zero and stays within prespecified 5-point margin.
- **Comparisons / 对照:** Original LP-based anti-loop edit and unedited model (9.5%).
- **Old capability / 保持:** No general unrelated-task retention measured.
- **Transfer / 迁移:** Single target model; no new-host program transfer.
- **Evidence boundary / 证据边界:** Indicates a nearly constant directional bias may explain the edit; does not establish a broader capability installation mechanism.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [SGNE-CC v2 (DeepSeek-R1-1.5B)](https://doi.org/10.5281/zenodo.24398165)

- **Model / 对象:** DeepSeek-R1-Distill-Qwen-1.5B (dense 28-layer Qwen2 transformer with no recurrent layers).
- **Intervention / 干预:** Exact norm-preserving spherical rotation of 205 mlp.down_proj columns (0.0177% of parameters; 603 KB patch) calibrated on 200 MATH-500 items with zero gradient steps.
- **Reported outcome / 结果:** Across 1,054 problems on five benchmarks at T=0 (32,768 tokens, no penalties), overall accuracy rises from 60.5% to 69.5% (MATH-500 65.4% -> 76.4%, MBPP 53.3% -> 67.5%, BBH 68.3% -> 77.5%, ARC 52.7% -> 59.3%), unclosed traces drop 87% (28.9% -> 3.9%, 305 -> 41 of 1,054), and mean token count drops 2.7x.
- **Comparisons / 对照:** Unedited DeepSeek-R1-Distill-Qwen-1.5B evaluated under greedy T=0, recommended T=0.6 sampling, and T=0.3 low-noise sampling, with 42/42 SHA-256 trace verification.
- **Old capability / 保持:** Four of five benchmarks (MBPP, HumanEval, BBH Logic, ARC-Challenge; 554 tasks) are completely untouched during calibration and all improve or preserve accuracy at T=0.
- **Transfer / 迁移:** Extends column-norm-preserving spherical editing from hybrid GatedDeltaNet Qwen3.5-0.8B to a pure dense attention-MLP transformer without architecture-specific recurrent gates.
- **Evidence boundary / 证据边界:** Under recommended T=0.6 sampling, gains are smaller (+2.0pp on MATH-500, -0.7pp on ARC-Challenge, though T=0.3 reaches 66.0% on ARC vs. 57.3% base at T=0.6); evaluated on one 1.5B distilled model.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [SGNE-CC (Qwen3.5-0.8B Audit)](https://doi.org/10.5281/zenodo.24235218)

- **Model / 对象:** Qwen3.5-0.8B (752M text parameters; 18 GatedDeltaNet + 6 attention layers) compared directly against MIT-p50c.
- **Intervention / 干预:** 3.13 MiB gradient-free spherical rotation of selected output columns preserving Euclidean column norms within BF16 rounding (<= 0.1625% drift vs. up to +114.3% norm inflation in MIT-p50c).
- **Reported outcome / 结果:** Under greedy decoding without repetition penalties (T=0, 32,768-token budget), MATH-500 rises from 0% (base) and 5.0% (MIT-p50c) to 43.0%, cutting 32k cutoffs from 95.0% to 18.4% and mean length 3.7x across 1,128 tasks on five suites.
- **Comparisons / 对照:** Unedited Qwen3.5-0.8B and MIT-p50c evaluated under both greedy decoding (T=0, pp=0) and model-card sampling (T=0.6, pp=1.5).
- **Old capability / 保持:** Tested on held-out MGSM-240, BBH-160, HumanEval-164, and MultiSpeech-64; under T=0.6, pp=1.5 matches vLLM MATH-500 (47.0% vs. 48.2%) and improves BBH Web of Lies (45% vs. 35%), but trails MIT-p50c on MGSM-240 (41.7% vs. 57.1%).
- **Transfer / 迁移:** Evaluated on Qwen3.5-0.8B; companion study SGNE-CC v2 tests the same column-norm-preserving formulation on a dense 1.5B Qwen2 transformer.
- **Evidence boundary / 证据边界:** Constructed via mechanistic weight-geometry calibration rather than an autonomous LLM prompt loop; shorter generations occasionally terminate verbal checks early under T=0.6, pp=1.5 on MGSM-240 and MATH L1-2.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [WSP Backdoor Security Study](https://arxiv.org/abs/2611.17395)

- **Model / 对象:** MNIST MLP, CIFAR-10 ResNet-18 and Qwen2.5-0.5B classifier.
- **Intervention / 干预:** Evaluate whether models can be altered through data-free, no-forward-pass, gradient-free LLM weight-editing prompts.
- **Reported outcome / 结果:** The paper reports feasibility of targeted malicious behavior changes on some architectures, with performance differences across five editing LLMs.
- **Comparisons / 对照:** Five editor models and three target architectures.
- **Old capability / 保持:** Paper reports broadly preserved clean performance in tested conditions, not guarantees.
- **Transfer / 迁移:** Compares architectures and editor models; not cross-host executable program reuse.
- **Evidence boundary / 证据边界:** Security-motivated failure analysis; reported results are not a recommendation to apply edits.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Computation, Not Weight Access](https://arxiv.org/abs/2611.07847)

- **Model / 对象:** Simulated clinical prediction networks from 105 to 38,401 weights.
- **Intervention / 干预:** Separate weights-only prompting from computation tools and black-box versus white-box access for LLM audits.
- **Reported outcome / 结果:** With tools, planted relationships recovered in 39/39 audits; black-box access performs as well as white-box access.
- **Comparisons / 对照:** Calculation scripts, no-tool prompts, black-box and white-box audit access.
- **Old capability / 保持:** Mainly an audit study; no evidence of continuing capability retention.
- **Transfer / 迁移:** Tests multiple network sizes, but no executable weight edits transferred.
- **Evidence boundary / 证据边界:** Results challenge interpretations that success demonstrates native raw-weight comprehension; simulated data setting.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Interpretable Weight-Space Programming Builds Transparent Transformers and Brain Encoding Models](https://arxiv.org/abs/2611.18114)

- **Model / 对象:** Handwritten transformers for 13 algorithmic and four NLP tasks; visual, language and auditory brain-encoding models.
- **Intervention / 干预:** Agent iteratively writes weights/features from validation feedback without backpropagation; released neuroscience evaluators fit ridge readouts.
- **Reported outcome / 结果:** All 26 reported Opus algorithmic runs attain 100% hidden accuracy; short-description rebuilds preserve algorithmic accuracy and lose about 1.4 points on NLP on average.
- **Comparisons / 对照:** Majority-class, interpretable feature and pretrained neural-encoding baselines, plus description-and-rebuild audits.
- **Old capability / 保持:** New model construction; not sequential retention of capabilities in an existing host.
- **Transfer / 迁移:** Visual features evaluated across datasets; text-mediated rebuilding is distinct from rerunning an edit on independent pretrained hosts.
- **Evidence boundary / 证据边界:** Source check uses the author abstract, repository and evaluators, not independent replication. Gradient-free feature writing does not mean a fitting-free pipeline; ECoG data are not public.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Replicating and Extending WSP](https://arxiv.org/html/2611.21449v1)

- **Model / 对象:** Small MinAtar/Breakout policies, MNIST classifiers, three newly designed games, poisoned Olmo 3 190M models and Qwen3.5-0.8B adapters.
- **Intervention / 干预:** Independent replication of Sparks: GPT-6 Astra, Claude Opus 5.5 and open-weight models write weights in one reply, decompile networks, read raw weights and audit models without executing code.
- **Reported outcome / 结果:** Astra's Breakout networks score 514/550/307 (original 517); written MNIST networks average 49.6% vs 82.0% for a template classifier. Decompiled Python matches Astra's network on all 49,189 tested states. On new games Astra recovers board layout but mostly misses mechanics; audits flag poisoned models (10/10, 7/10; adapters 23/32) but never identify the trigger.
- **Comparisons / 对照:** Shuffled-weight controls, rotated-digit and modified-game variants, code-versus-weights comparison across model generations, template and trained MNIST classifiers; PPO numbers are reused from the original report and likely under-tuned.
- **Old capability / 保持:** Not a retention study; constructs new networks and audits existing ones.
- **Transfer / 迁移:** The standard Breakout network scores 0.5/0.0 on swapped/upside-down variants; networks written for each variant average 515. Decompiled programs reproduce network actions.
- **Evidence boundary / 证据边界:** Three-day sprint with one to five runs per condition; analysis code written mainly by the evaluated model families and not independently reviewed; no repository URL; original networks and logs are public, so contamination is possible.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Rule-to-Network Compilation](https://arxiv.org/html/2611.16981v1)

- **Model / 对象:** Fixed 57,289-parameter recurrent actor and free-architecture networks for 20 unpublished ARC-AGI-3-style game families.
- **Intervention / 干预:** Nine LLM writers receive redacted simulator source and write all weights without fitting or search, one-shot or with up to three feedback rounds.
- **Reported outcome / 结果:** Strongest writer (GPT-6 Astra) reaches 0.56 [0.40, 0.71] held-out-level success with feedback in the fixed actor; free architectures reach 68–90%. Python players reach 97–100%; capped NumPy programs 91% vs 79% for networks. Written networks are 93% zeros.
- **Comparisons / 对照:** Python and NumPy program controls; behaviour cloning, distillation and PPO in the same actor (best non-privileged 11%); retraining Astra's architectures from scratch solves about 1%; weight-noise and random-update controls.
- **Old capability / 保持:** Not a host-retention study. Standard PPO fine-tuning drives held-out success from 0.50 to 0.01; written weights do not survive subsequent gradient updates.
- **Transfer / 迁移:** Within-family generalisation to held-out levels, renderings and start states (held-out templates cost 1 point); no transfer to new games or independently trained hosts.
- **Evidence boundary / 证据边界:** Writers read source code while learned baselines see only support levels, so the comparison is mainly about information access. Per-family estimates use 3–6 levels; games were authored with LLM assistance and an evaluated writer helped design the harness; private games limit outside reproduction.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Mixed Signals](https://arxiv.org/html/2611.13758v1)

- **Model / 对象:** TinyEEGNet (2,730 weights) and ECGResNet (941,189 weights); EEG and ECG tasks.
- **Intervention / 干预:** Three LLMs read, repair and construct networks with bounded feedback; no gradient optimization; one-shot linear algebra allowed in ECG experiments.
- **Reported outcome / 结果:** No reliable task reading or healthy-network improvement. With feedback, Opus/DeepSeek recover 0.99/0.96 of lost EEG accuracy; Opus constructs an eyes-state classifier with 0.834 balanced accuracy.
- **Comparisons / 对照:** Random/shuffled-label controls, placebo edits, recalibration, fine-tuning, textbook ECG correction, and handcrafted EEG pipelines.
- **Old capability / 保持:** Opus ECG swap repair leaves correct-ECG macro-AUC near baseline (0.9167 vs 0.9169); not a general retention result.
- **Transfer / 迁移:** EEG construction evaluated on 65 unseen subjects; no executable-program transfer across independently trained hosts established.
- **Evidence boundary / 证据边界:** ECG repair misses the textbook baseline; shortcut repairs miss the best standard fix. Several settings use one run; public-dataset familiarity and post-hoc EEG baselines limit interpretation.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [NCP](https://arxiv.org/html/2611.13236v1)

- **Model / 对象:** SmolLM-135M-Instruct; nine-question fixture split 3/3/3 and separate WikiText-2 slices.
- **Intervention / 干预:** Deterministic Python templates propose activation-conditioned temporary weight interventions; a verifier controls admission to a persistent rule table.
- **Reported outcome / 结果:** Projection reduces validation repetition 0.4133 to 0.2191, but all three candidates correct zero new answers and are rejected; no rule is admitted.
- **Comparisons / 对照:** Original policy versus projection, head ablation and their combination, on separate development/validation examples and a 4,095-target verifier corpus.
- **Old capability / 保持:** Every trial restores base weights. Candidates satisfy the 0.5% perplexity budget; this bounded check does not establish broad capability preservation.
- **Transfer / 迁移:** Fresh-process and saved-table replay reproduce outcomes; not program transfer to a new model.
- **Evidence boundary / 证据边界:** Architectural microbenchmark with deterministic synthesis, not a demonstrated LLM editor or sustained recursive capability improvement.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [W-ISA](https://arxiv.org/html/2611.13232v1)

- **Model / 对象:** SmolLM-135M-Instruct and Qwen2.5-1.5B-Instruct.
- **Intervention / 干预:** Shape-checked parameter instructions execute in request-scoped transactions with snapshots, restoration and optional activation-based routing.
- **Reported outcome / 结果:** Reports undo/replay and interruption restoration. Materialized rank-one updates and equivalent hooks yield identical greedy sequences in 45 timed Qwen requests.
- **Comparisons / 对照:** Original inference, direct weight materialization and equivalent PyTorch hooks; separate ablation/projection conditions.
- **Old capability / 保持:** Restores parameter digests after requests; combined SmolLM intervention raises full WikiText-2 perplexity by 0.3754%. Restoration is not preservation while an edit is active.
- **Transfer / 迁移:** Runtime exercised on two model families; useful edit transfer across models is not established.
- **Evidence boundary / 证据边界:** Execution infrastructure for supplied interventions, not autonomous capability discovery. The hook comparison uses one fixed prompt across three generation lengths.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [Physics2Weight](https://arxiv.org/html/2611.12954v1)

- **Model / 对象:** Small networks for heat, advection, Burgers and Allen-Cahn PDEs; Claude Opus 5.5 writes architectures and weights.
- **Intervention / 干预:** Physics-constrained prompts, architecture editing and five refinement rounds using external residual/constraint feedback without reference solutions.
- **Reported outcome / 结果:** Lower relative solution error than the tested PINN baseline on four PDEs; near-machine precision on heat/advection, but worse PDE residuals on nonlinear problems.
- **Comparisons / 对照:** PINN, direct WSP, and prompting/architecture/refinement ablations; medians of three runs.
- **Old capability / 保持:** Constructs task-specific solutions; prior-capability retention is not evaluated.
- **Transfer / 迁移:** Separate constructions for four equations; unchanged executable-program transfer across trained hosts is not shown.
- **Evidence boundary / 证据边界:** Architecture changes embed analytical structure. For one Burgers run, residual MSE rises from 5.45e-2 to 6.6e9 on a finer grid; low solution error does not certify physical consistency.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

### [WSP for Medical Imaging](https://arxiv.org/html/2611.12066v1)

- **Model / 对象:** LeNet-style CNNs with at most 7,000 weights on seven 28x28 medical-imaging classification tasks.
- **Intervention / 干预:** Opus 5.5 and GPT-6 Astra write weights in one reply without tools, images or task-specific training.
- **Reported outcome / 结果:** Mean MedMNIST test AUC is 0.719/0.711; both beat zero-shot MedSigLIP on 5/6 tasks, but Adam with 256 labels wins on all six (mean 0.828).
- **Comparisons / 对照:** Zero-shot MedSigLIP and the same CNN architecture trained with Adam at different label budgets; three calls per LLM/task.
- **Old capability / 保持:** Constructs new classifiers; retention of a pretrained model is not evaluated.
- **Transfer / 迁移:** Seven task-specific constructions, not reuse of a fixed edit program on independent hosts.
- **Evidence boundary / 证据边界:** Astra reaches 0.136 AUC on SynthUterus. Public-dataset prior knowledge, tiny images, and upsampled inputs/untuned prompts for MedSigLIP constrain comparisons; no clinical deployment claim.
- **Gradient-free / 免梯度:** Yes · **Source level / 来源类型:** preprint

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
| [Weight-Space Programming of JEPA World Models](https://www.alphaxiv.org/abs/2611.wsp-jepa) | manuscript | Metadata only / 未审查结果 |
| [WSP for Policies](https://arxiv.org/abs/2611.11604) | preprint | Metadata only / 未审查结果 |
| [WSP for Quantum Circuits](https://arxiv.org/abs/2611.11537) | preprint | Metadata only / 未审查结果 |
| [WSP for Mathematical Optimization](https://arxiv.org/abs/2611.09559) | preprint | Metadata only / 未审查结果 |
| [Zero-Shot Game WSP](https://arxiv.org/abs/2611.09271) | preprint | Metadata only / 未审查结果 |
| [Clinical Network Audits](https://arxiv.org/abs/2611.05341) | preprint | Metadata only / 未审查结果 |

## How to read this matrix / 如何理解证据

- **Repair vs installation:** repairing existing behavior does not prove new capability acquisition.
- **Preservation:** absence of regression reports is not evidence of retention.
- **Portability:** fixed numeric deltas differ from rerunning a program on a new host.
- **Sequence:** one update does not establish long-horizon accumulation.
- **Evidence level:** a preprint, repository or blog label says what was reported, not what was independently confirmed.
<!-- AUTO:END evidence -->
