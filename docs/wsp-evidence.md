<!-- AUTO:START evidence -->
# WSP Evidence Matrix / 权重编程证据矩阵

This matrix summarizes source-reported evidence, not independently reproduced results. A source check is not independent replication. Repairing a defect does not automatically demonstrate a missing capability.

本表整理原始来源报告的证据，并非独立复现实验。修复现有功能不等于安装此前缺失的能力。

**Coverage:** 34 direct-WSP papers; 29 source-checked examples; 5 metadata-only entries.

## Source-checked examples / 已核对来源的案例

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
