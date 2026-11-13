# Weight-Centric Research: Inspirations Beyond Editing

**A companion reading series to [Awesome Weight-Space Programming](../README.md).** Not all useful ideas for programming a model originate in model-editing papers. This collection treats neural-network weights as structured objects to **understand, represent, generate, compose, localize, and preserve**. Papers here are inspirations and comparison points, **not** automatically instances of direct weight-space programming (WSP).

**Selection rule:** Include a paper when it offers a concrete, testable idea for reading or writing weights, transferring computations across networks, composing multiple updates, or preserving existing capabilities. General fine-tuning, compression, or optimization papers without such a connection are not included. A proposed connection is a research hypothesis, not an established result.

**Current selection:** 67 papers across 6 research tracks. The original 21-paper selection has been supplemented by a systematic cross-keyword search, with entries retained only when they suggest a testable weight-programming idea. Papers already listed in the [main related-work catalog](../README.md#related-research) are not duplicated here.

## Reading map

| Research track | Question for future weight programming |
| --- | --- |
| [Weight Geometry, Symmetry & Connectivity](#wcr-geometry) | When are raw coordinates misleading, and when can two checkpoints be combined? |
| [Weights as Data: Reading & Representation](#wcr-reading) | Can model properties be inferred from parameters without running the model on the original task? |
| [Weight Generation & Synthesis](#wcr-generation) | Can networks be generated as objects rather than optimized afresh for every task? |
| [Weight Arithmetic, Merging & Interference](#wcr-composition) | How can changes be combined without destroying existing capabilities? |
| [Structured Parameters, Sparsity & Mechanism Localization](#wcr-structure) | Which coordinates, directions, or subnetworks should a program modify? |
| [Continual Capability Accumulation & Preservation](#wcr-retention) | Where can new abilities live, and what should remain unchanged after many updates? |

<a id="wcr-geometry"></a>
## Weight Geometry, Symmetry & Connectivity

*When are raw coordinates misleading, and when can two checkpoints be combined?*

- **[Linear Mode Connectivity and the Lottery Ticket Hypothesis](https://arxiv.org/abs/1912.05671)** (ICML 2020). **Weight-centric idea:** Studies stability of SGD solutions and linearly connected regions. **Potential WSP inspiration:** A weight edit should be evaluated relative to the basin and stability of its host model.

- **[The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks](https://arxiv.org/abs/2110.06296)** (2021 preprint). **Weight-centric idea:** Examines how neuron permutation symmetry changes comparisons between solutions. **Potential WSP inspiration:** Weight readers and portable programs need a symmetry-aware account of parameter identity.

- **[Interpreting the Weight Space of Customized Diffusion Models](https://papers.nips.cc/paper_files/paper/2024/hash/f85364507054c257959c2011c28bfc0d-Abstract-Conference.html)** (NeurIPS 2024). **Weight-centric idea:** Studies semantic directions in a subspace of customized diffusion-model weights. **Potential WSP inspiration:** Suggests inspecting whether capability changes admit reusable, interpretable weight directions.

- **[Weight-space symmetry in deep networks gives rise to permutation saddles, connected by equal-loss valleys across the loss landscape](https://arxiv.org/abs/1907.02911)** (2019). **Weight-centric idea:** Permutation-equivalent minima can be connected through symmetry-induced saddle regions. **Potential WSP inspiration:** Portable edits must respect functional equivalence, not raw neuron indices.

- **[Improved Generalization of Weight Space Networks via Augmentations](https://arxiv.org/abs/2402.04081)** (2024). **Weight-centric idea:** Weight-space augmentation and MixUp reduce overfitting of networks trained on other networks. **Potential WSP inspiration:** Train or test weight readers against symmetry and checkpoint-distribution shortcuts.

- **[Understanding Mode Connectivity via Parameter Space Symmetry](https://arxiv.org/abs/2505.23681)** (ICML 2025). **Weight-centric idea:** Relates low-loss connectivity to continuous parameter symmetries. **Potential WSP inspiration:** Check whether edits preserve or leave a stable functional neighborhood.

- **[Generalized Linear Mode Connectivity for Transformers](https://arxiv.org/abs/2506.22712)** (2025). **Weight-centric idea:** Studies broader alignment and connectivity conditions for Transformer checkpoints. **Potential WSP inspiration:** Derive host-aware alignment rules before transferring weight programs.

- **[Beyond the Permutation Symmetry of Transformers: The Role of Rotation for Model Fusion](https://arxiv.org/abs/2502.00264)** (ICML 2025). **Weight-centric idea:** Highlights rotation symmetries beyond simple neuron permutations. **Potential WSP inspiration:** Cross-model edits may need basis-aware transformations.

- **[Universal Neural Functionals](https://arxiv.org/abs/2402.05232)** (NeurIPS 2024). **Weight-centric idea:** Builds symmetry-aware functions over parameters across network architectures. **Potential WSP inspiration:** Motivates readers and edit locators designed around valid parameter symmetries.

- **[Monomial Matrix Group Equivariant Neural Functional Networks](https://arxiv.org/abs/2409.11697)** (NeurIPS 2024). **Weight-centric idea:** Extends neural functional equivariance to monomial transformations. **Potential WSP inspiration:** A portable program should not confuse harmless rescaling with a real capability change.

- **[Scale Equivariant Graph Metanetworks](https://arxiv.org/abs/2406.10685)** (NeurIPS 2024). **Weight-centric idea:** Models networks as graphs while respecting scale transformations. **Potential WSP inspiration:** Use structured, scale-aware signatures for identifying reusable edit sites.

<a id="wcr-reading"></a>
## Weights as Data: Reading & Representation

*Can model properties be inferred from parameters without running the model on the original task?*

- **[Predicting Neural Network Accuracy from Weights](https://arxiv.org/abs/2002.11448)** (2020 preprint). **Weight-centric idea:** Predicts model accuracy from weight statistics without evaluating on task inputs. **Potential WSP inspiration:** A concrete precedent for weight-only inspection; generalization to other model families must be tested.

- **[Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction](https://arxiv.org/abs/2110.15288)** (NeurIPS 2021). **Weight-centric idea:** Learns model-level representations from populations of weights. **Potential WSP inspiration:** A possible alternative to directly giving an LLM raw tensors for edit localization and model profiling.

- **[Hyper-Representations as Generative Models: Sampling Unseen Neural Network Weights](https://arxiv.org/abs/2209.14733)** (NeurIPS 2022). **Weight-centric idea:** Uses learned weight embeddings to sample new network parameters. **Potential WSP inspiration:** Connects model-zoo knowledge to reusable parameter priors, while remaining a trained generator rather than direct WSP.

- **[Classifying the classifier: dissecting the weight space of neural networks](https://arxiv.org/abs/2002.05688)** (ECAI 2020). **Weight-centric idea:** Uses meta-classifiers on weight snapshots to infer training and model properties. **Potential WSP inspiration:** A baseline for asking which properties are actually recoverable from parameters alone.

- **[Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data](https://arxiv.org/abs/2002.06716)** (Nature Communications 2021). **Weight-centric idea:** Estimates checkpoint quality from spectral and heavy-tailed weight statistics. **Potential WSP inspiration:** Weight-only diagnostics may help screen risky edits, but cannot substitute for behavior tests.

- **[Graph Neural Networks for Learning Equivariant Representations of Neural Networks](https://arxiv.org/abs/2403.12143)** (ICLR 2024). **Weight-centric idea:** Extracts equivariant descriptions from neural-network graph structures. **Potential WSP inspiration:** Represent a host network structurally rather than passing unstructured tensors to an editor.

- **[Graph Metanetworks for Processing Diverse Neural Architectures](https://arxiv.org/abs/2312.04501)** (ICLR 2024). **Weight-centric idea:** Processes diverse neural architectures in a shared graph metanetwork. **Potential WSP inspiration:** A possible interface for architecture-aware edit localization across hosts.

- **[Towards Scalable and Versatile Weight Space Learning](https://arxiv.org/abs/2406.09997)** (ICML 2024). **Weight-centric idea:** Addresses the scale and versatility of learning representations from model weights. **Potential WSP inspiration:** Study whether compressed model fingerprints suffice for choosing edit locations.

- **[Deep Linear Probe Generators for Weight Space Learning](https://arxiv.org/abs/2410.10811)** (2024). **Weight-centric idea:** Uses generated probing operators to summarize model weights. **Potential WSP inspiration:** An alternative to costly full-tensor inspection by a reasoning editor.

- **[Learning on Model Weights using Tree Experts](https://arxiv.org/abs/2410.13569)** (CVPR 2025). **Weight-centric idea:** Builds model-weight representations with specialized tree experts. **Potential WSP inspiration:** Hierarchical inspection could route an editor toward relevant model components.

- **[Learning Model Representations Using Publicly Available Model Hubs](https://arxiv.org/abs/2510.02096)** (2025). **Weight-centric idea:** Uses model repositories to study representations of pretrained checkpoints. **Potential WSP inspiration:** Provides a route to broader training distributions for transferable weight readers.

- **[W2T: LoRA Weights Already Know What They Can Do](https://arxiv.org/abs/2603.15990)** (EMNLP 2026). **Weight-centric idea:** Canonicalizes equivalent LoRA factorizations before learning adapter representations. **Potential WSP inspiration:** Crucial reference for interpreting or selecting edits independently of arbitrary factorization.

- **[What Linear Probes Miss: Multi-View Probing for Weight-Space Learning](https://proceedings.mlr.press/v306/heo26a.html)** (ICML 2026). **Weight-centric idea:** Combines first-order probes with Gram-based higher-order interactions. **Potential WSP inspiration:** Test whether multi-view weight summaries outperform raw coordinate dumps for program planning.

- **[Weight Space Representation Learning via Neural Field Adaptation](https://arxiv.org/abs/2512.01759)** (CVPR 2026). **Weight-centric idea:** Studies weight representations through neural-field adaptation. **Potential WSP inspiration:** Potential evidence for transferable weight descriptors across fitted functions.

- **[Model Zoos: A Dataset of Diverse Populations of Neural Network Models](https://arxiv.org/abs/2209.14764)** (NeurIPS 2022). **Weight-centric idea:** Provides populations of independently trained networks and checkpoints. **Potential WSP inspiration:** Useful host-distribution benchmark for weight readers and program portability.

<a id="wcr-generation"></a>
## Weight Generation & Synthesis

*Can networks be generated as objects rather than optimized afresh for every task?*

- **[HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://arxiv.org/abs/2303.17015)** (2023 preprint). **Weight-centric idea:** Trains diffusion in the weights of implicit neural fields. **Potential WSP inspiration:** A generative prior could constrain proposed edits toward plausible functional regions.

- **[Neural Network Diffusion](https://arxiv.org/abs/2402.13144)** (2024 preprint). **Weight-centric idea:** Uses latent diffusion to synthesize performant parameter subsets. **Potential WSP inspiration:** Raises the possibility of proposing or repairing local weight blocks with a trained parameter prior.

- **[NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://proceedings.mlr.press/v306/kim26ay.html)** (ICML 2026). **Weight-centric idea:** Generates neural-network weights across widths with structural alignment. **Potential WSP inspiration:** A useful reference for reusable programs that must tolerate differences in model width or parameterization.

- **[HyperGAN: A Generative Model for Diverse, Performant Neural Networks](https://arxiv.org/abs/1901.11058)** (ICML 2019). **Weight-centric idea:** Learns to generate diverse parameter realizations for functional networks. **Potential WSP inspiration:** Explore whether valid weight regions can constrain program outputs.

- **[Graph HyperNetworks for Neural Architecture Search](https://arxiv.org/abs/1810.05749)** (ICLR 2019). **Weight-centric idea:** Generates candidate network parameters from architecture graphs. **Potential WSP inspiration:** Use architectural structure to parameterize programs across different hosts.

- **[Learning to Learn with Generative Models of Neural Network Checkpoints](https://arxiv.org/abs/2209.12892)** (2022). **Weight-centric idea:** Conditions generative checkpoint updates on desired metrics. **Potential WSP inspiration:** A direct comparison for goal-conditioned weight changes without ordinary test-time fine-tuning.

- **[Instruction-Guided Autoregressive Neural Network Parameter Generation](https://arxiv.org/abs/2504.02012)** (2025). **Weight-centric idea:** Autoregressively synthesizes parameters under instructions. **Potential WSP inspiration:** Compare instruction-to-parameters generation with executable program creation.

- **[Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights](https://arxiv.org/abs/2506.16406)** (2025). **Weight-centric idea:** Explores zero-shot prompt-conditioned parameter production. **Potential WSP inspiration:** Relevant to converting textual specifications into persistent weight changes.

- **[Scaling Up Parameter Generation: A Recurrent Diffusion Approach](https://arxiv.org/abs/2501.11587)** (NeurIPS 2025). **Weight-centric idea:** Uses recurrent diffusion to generate large parameter sets in chunks. **Potential WSP inspiration:** Suggests blockwise generation for edits too large for direct tensor writing.

- **[Text2Weight: Bridging Natural Language and Neural Network Weight Spaces](https://arxiv.org/abs/2508.13633)** (2025). **Weight-centric idea:** Generates task-conditioned weights from natural-language descriptions. **Potential WSP inspiration:** A natural-language-to-weights baseline for testing generalization to unseen tasks.

- **[Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f74d79573d71078848973009d0e99bdb-Abstract-Conference.html)** (ICLR 2025). **Weight-centric idea:** Conditionally generates weights using tasks, datasets, and architecture information. **Potential WSP inspiration:** Shows what a trained multi-condition parameter generator can provide without writing programs.

- **[DeepWeightFlow: Re-Basined Flow Matching for Generating Neural Network Weights](https://arxiv.org/abs/2601.05052)** (ICLR 2026). **Weight-centric idea:** Aligns parameterizations before flow-matching complete network weights. **Potential WSP inspiration:** Combines a portability lesson (re-basing) with a generative baseline.

- **[LoRAGen: Structure-Aware Weight Space Learning for LoRA Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fc7c087b5e965075c8946b9ff57e3d64-Abstract-Conference.html)** (ICLR 2026). **Weight-centric idea:** Handles non-identifiable LoRA factors and module-specific distributions in conditional generation. **Potential WSP inspiration:** Editing code may likewise need module-aware structure and canonical update representations.

- **[Weight-Space Linear Recurrent Neural Networks](https://arxiv.org/abs/2506.01153)** (ICLR 2026). **Weight-centric idea:** Explores recurrent modeling of parameter sequences in weight space. **Potential WSP inspiration:** An alternative structured prior when large edits must be produced sequentially.

<a id="wcr-composition"></a>
## Weight Arithmetic, Merging & Interference

*How can changes be combined without destroying existing capabilities?*

- **[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482)** (ICML 2022). **Weight-centric idea:** Combines compatible fine-tuned checkpoints by averaging weights. **Potential WSP inspiration:** Provides a simple composition baseline and a reminder that checkpoint compatibility matters.

- **[TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)** (NeurIPS 2023). **Weight-centric idea:** Addresses redundant changes and sign conflicts among parameter updates. **Potential WSP inspiration:** Multi-program installation should inspect edit conflicts, not just add deltas.

- **[Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099)** (ICML 2024). **Weight-centric idea:** Introduces DARE, random dropping and rescaling of fine-tuning deltas before merging. **Potential WSP inspiration:** Tests how much of a capability-bearing change survives sparsification; this is not equivalent to an executable program.

- **[AdaMerging: Adaptive Model Merging for Multi-Task Learning](https://arxiv.org/abs/2310.02575)** (2023 preprint). **Weight-centric idea:** Adapts task-wise or layer-wise merging coefficients using an unsupervised objective. **Potential WSP inspiration:** Suggests task- or layer-dependent arbitration when successive edits conflict.

- **[Merging Models with Fisher-Weighted Averaging](https://proceedings.neurips.cc/paper_files/paper/2022/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html)** (NeurIPS 2022). **Weight-centric idea:** Weights parameter combinations by estimated Fisher importance. **Potential WSP inspiration:** Potential protection or conflict weighting when two installed capabilities overlap.

- **[Model Breadcrumbs: Scaling Multi-Task Model Merging with Sparse Masks](https://mlanthology.org/eccv/2024/davari2024eccv-model/)** (ECCV 2024). **Weight-centric idea:** Sparsifies task deltas by removing outliers and weak updates. **Potential WSP inspiration:** Test whether sparse program effects compose better than dense changes.

- **[Model Stock: All we need is just a few fine-tuned models](https://arxiv.org/abs/2403.19522)** (ECCV 2024). **Weight-centric idea:** Approximates a beneficial weight-space center with few fine-tuned checkpoints. **Potential WSP inspiration:** Suggests low-cost reference points for evaluating update stability.

- **[Task Singular Vectors: Reducing Task Interference in Model Merging](https://openaccess.thecvf.com/content/CVPR2025/html/Gargiulo_Task_Singular_Vectors_Reducing_Task_Interference_in_Model_Merging_CVPR_2025_paper.html)** (CVPR 2025). **Weight-centric idea:** Decomposes task updates with SVD to identify and reduce interference. **Potential WSP inspiration:** An especially relevant diagnostic for multi-program capability accumulation.

- **[Model merging with SVD to tie the Knots](https://arxiv.org/abs/2410.19735)** (ICLR 2025). **Weight-centric idea:** Aligns multiple LoRA updates in a common SVD coordinate system before merging. **Potential WSP inspiration:** Compare aligned program effects against naive delta addition.

- **[RegMean++: Enhancing Effectiveness and Generalization of Regression Mean for Model Merging](https://arxiv.org/abs/2508.03121)** (TMLR 2026). **Weight-centric idea:** Models within-layer and cross-layer dependencies when constructing a merged model. **Potential WSP inspiration:** Reminds editors that local numerical changes can have downstream functional effects.

- **[Representation Surgery for Multi-Task Model Merging](https://proceedings.mlr.press/v235/yang24t.html)** (ICML 2024). **Weight-centric idea:** Repairs representation bias that arises after model merging. **Potential WSP inspiration:** Useful counterexample: parameter-compatible merging need not imply function-compatible composition.

<a id="wcr-structure"></a>
## Structured Parameters, Sparsity & Mechanism Localization

*Which coordinates, directions, or subnetworks should a program modify?*

- **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)** (ICLR 2019). **Weight-centric idea:** Identifies sparse trainable subnetworks within larger networks. **Potential WSP inspiration:** Motivates examining whether new capabilities can be installed through restricted computational substrates.

- **[Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)** (2021 preprint). **Weight-centric idea:** Uses attribution to locate neurons linked to particular factual knowledge. **Potential WSP inspiration:** Shows one route from behavior to candidate edit locations, subject to causal validation.

- **[DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353)** (ICML 2024). **Weight-centric idea:** Separates weight magnitude and direction for adaptation. **Potential WSP inspiration:** Invites explicit magnitude/direction constraints when writing local parameter changes.

- **[PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://arxiv.org/abs/2404.02948)** (NeurIPS 2024). **Weight-centric idea:** Uses principal singular components of pretrained matrices as adaptable subspaces. **Potential WSP inspiration:** Suggests selecting editing subspaces through matrix structure rather than arbitrary coordinates.

- **[SparseGPT: Massive Language Models Can be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774)** (ICML 2023). **Weight-centric idea:** Performs one-shot, retraining-free large-model pruning with reconstruction-aware updates. **Potential WSP inspiration:** Suggests controlled sparse intervention budgets and parameter redundancy probes.

- **[A Simple and Effective Pruning Approach for Large Language Models](https://arxiv.org/abs/2306.11695)** (ICLR 2024). **Weight-centric idea:** Wanda scores weights using magnitude multiplied by input activation. **Potential WSP inspiration:** Compare activation-aware editing-site choice against magnitude-only selection.

- **[SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://arxiv.org/abs/2403.07378)** (2024). **Weight-centric idea:** Uses data-aware SVD and closed-form compensation for parameter compression. **Potential WSP inspiration:** Inspires compensatory edits that preserve host outputs while changing a targeted subspace.

<a id="wcr-retention"></a>
## Continual Capability Accumulation & Preservation

*Where can new abilities live, and what should remain unchanged after many updates?*

- **[Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796)** (PNAS 2017). **Weight-centric idea:** Protects parameters estimated as important to previous tasks (EWC). **Potential WSP inspiration:** A foundation for measuring and protecting the footprint of old capabilities during edits.

- **[Progressive Neural Networks](https://arxiv.org/abs/1606.04671)** (2016 preprint). **Weight-centric idea:** Adds new network columns while retaining earlier ones and lateral transfer. **Potential WSP inspiration:** An architectural counterpart to in-place editing: preservation can come from separation, at a capacity cost.

- **[PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning](https://arxiv.org/abs/1711.05769)** (CVPR 2018). **Weight-centric idea:** Reclaims unused parameters to accommodate sequential tasks. **Potential WSP inspiration:** Suggests tracking free parameter capacity and edit occupancy across many installations.

- **[Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights](https://arxiv.org/abs/1801.06519)** (ECCV 2018). **Weight-centric idea:** Learns task-specific binary masks over fixed base weights. **Potential WSP inspiration:** Provides a non-destructive baseline for conditional capability activation and retention.

- **[Continual learning with hypernetworks](https://arxiv.org/abs/1906.00695)** (ICLR 2020). **Weight-centric idea:** Regularizes a hypernetwork to retain task-conditioned weight realizations. **Potential WSP inspiration:** A trained-generator alternative for long-horizon retention and task-conditioned recall.

- **[Memory Aware Synapses: Learning what (not) to forget](https://arxiv.org/abs/1711.09601)** (ECCV 2018). **Weight-centric idea:** Estimates online parameter importance from output sensitivity. **Potential WSP inspiration:** An empirical importance map could guide which old weights not to overwrite.

- **[InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning](https://arxiv.org/abs/2404.00228)** (CVPR 2024). **Weight-centric idea:** Constrains low-rank updates to subspaces designed to avoid old-task interference. **Potential WSP inspiration:** A strong baseline for protected subspace writing across many installations.

- **[C-LoRA: Continual Low-Rank Adaptation for Pre-trained Models](https://arxiv.org/abs/2502.17920)** (2025). **Weight-centric idea:** Routes sequential low-rank updates with orthogonality constraints. **Potential WSP inspiration:** Suggests tracking subspace usage as successive programs accumulate.

- **[BECAME: Bayesian Continual Learning with Adaptive Model Merging](https://proceedings.mlr.press/v267/li25bk.html)** (ICML 2025). **Weight-centric idea:** Derives adaptive merging coefficients from a Bayesian continual-learning view. **Potential WSP inspiration:** A principled comparator for balancing plasticity and preservation as edits accumulate.

## Surveys, maps and benchmarking resources

- **[A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)** (2026). A comprehensive overview of weight-space understanding, representation, and generation; this catalog prioritizes explicit implications for future programmable interventions.
- **[Awesome Weight-Space Learning](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning)**. An actively maintained broad reference index for weight-space research, useful for further discovery rather than one-to-one duplication.
- **[Position: Weight Space Should Be a First-Class Generative AI Modality](https://proceedings.mlr.press/v306/wang26mc.html)** (ICML 2026). A forward-looking framing of checkpoints as a generative modality.
- **[MergeBench: A Benchmark for Merging](https://proceedings.neurips.cc/paper_files/paper/2025/file/91f7f71cb04699f387dc863da42a1fe3-Paper-Datasets_and_Benchmarks_Track.pdf)** (NeurIPS 2025). A reproducible benchmark for comparing the behavior of weight-composition methods.

**Evidence note:** A trained hypernetwork or diffusion generator is not direct reasoning-driven WSP. An edit that works on one checkpoint is not evidence of program portability, and retention after one update is not evidence of long-horizon accumulation.

## Connections to the existing WSP catalog

- **Reading and alignment:** [Neural Functional Transformers](https://papers.neurips.cc/paper_files/paper/2023/hash/f4757db82a02eea015670ecca605d5cc-Abstract-Conference.html), [Git Re-Basin](https://arxiv.org/abs/2209.04836) and [Equivariant Deep Weight Space Alignment](https://arxiv.org/abs/2310.13397) are already covered in the main catalog; use them with the geometry and representation tracks above.
- **Program-to-weights and learned generators:** [Tracr](https://arxiv.org/abs/2301.05062), [Text-to-LoRA](https://arxiv.org/abs/2506.06105) and [Doc-to-LoRA](https://arxiv.org/abs/2602.15902) are already in the main catalog. They differ in supervision, parameter construction and whether an editor has to be trained.
- **Targeted changes:** [ROME](https://arxiv.org/abs/2202.05262), [MEMIT](https://arxiv.org/abs/2210.07229), [AlphaEdit](https://arxiv.org/abs/2410.02355) and [Task Arithmetic](https://arxiv.org/abs/2212.04089) remain in the main catalog rather than being duplicated here.

## Useful research questions

1. **Weight reading:** Does a method read a model property, or does it only exploit architecture, training-set, or checkpoint-family shortcuts? Test symmetry transformations and held-out networks.
2. **Portability:** Does a change transfer as fixed numeric `ΔW`, as an aligned subspace, or as an executable procedure that recomputes edits for each host?
3. **Composition:** When multiple updates are installed, are conflicts caused by shared coordinates, shared computation, or changes to activation conditions? Compare against simple addition, sparsified merging, and separation.
4. **Retention:** Measure both newly acquired ability and preservation of previously acquired abilities after sequential updates. Distinguish inference-time routing from persistent in-weight change.

**Curation note:** The list includes trained weight generators, gradient-based adapters, model merging and continual learning on purpose. Their methods should not be described as training-free WSP simply because they manipulate parameters.

[Back to Awesome Weight-Space Programming](../README.md) · [简体中文](weight-centric-research_zh.md)
