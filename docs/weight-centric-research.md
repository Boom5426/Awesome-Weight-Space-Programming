# Weight-Centric Research: Inspirations Beyond Editing

**A companion reading series to [Awesome Weight-Space Programming](../README.md).** Not all useful ideas for programming a model originate in model-editing papers. This collection treats neural-network weights as structured objects to **understand, represent, generate, compose, localize, and preserve**. Papers here are inspirations and comparison points, **not** automatically instances of direct weight-space programming (WSP).

**Selection rule:** Include a paper when it offers a concrete, testable idea for reading or writing weights, transferring computations across networks, composing multiple updates, or preserving existing capabilities. General fine-tuning, compression, or optimization papers without such a connection are not included. A proposed connection is a research hypothesis, not an established result.

**Current selection:** 21 papers across 6 research tracks. Papers already listed in the [main related-work catalog](../README.md#related-research) are not duplicated here.

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

<a id="wcr-reading"></a>
## Weights as Data: Reading & Representation

*Can model properties be inferred from parameters without running the model on the original task?*

- **[Predicting Neural Network Accuracy from Weights](https://arxiv.org/abs/2002.11448)** (2020 preprint). **Weight-centric idea:** Predicts model accuracy from weight statistics without evaluating on task inputs. **Potential WSP inspiration:** A concrete precedent for weight-only inspection; generalization to other model families must be tested.

- **[Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction](https://arxiv.org/abs/2110.15288)** (NeurIPS 2021). **Weight-centric idea:** Learns model-level representations from populations of weights. **Potential WSP inspiration:** A possible alternative to directly giving an LLM raw tensors for edit localization and model profiling.

- **[Hyper-Representations as Generative Models: Sampling Unseen Neural Network Weights](https://arxiv.org/abs/2209.14733)** (NeurIPS 2022). **Weight-centric idea:** Uses learned weight embeddings to sample new network parameters. **Potential WSP inspiration:** Connects model-zoo knowledge to reusable parameter priors, while remaining a trained generator rather than direct WSP.

<a id="wcr-generation"></a>
## Weight Generation & Synthesis

*Can networks be generated as objects rather than optimized afresh for every task?*

- **[HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://arxiv.org/abs/2303.17015)** (2023 preprint). **Weight-centric idea:** Trains diffusion in the weights of implicit neural fields. **Potential WSP inspiration:** A generative prior could constrain proposed edits toward plausible functional regions.

- **[Neural Network Diffusion](https://arxiv.org/abs/2402.13144)** (2024 preprint). **Weight-centric idea:** Uses latent diffusion to synthesize performant parameter subsets. **Potential WSP inspiration:** Raises the possibility of proposing or repairing local weight blocks with a trained parameter prior.

- **[NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://proceedings.mlr.press/v306/kim26ay.html)** (ICML 2026). **Weight-centric idea:** Generates neural-network weights across widths with structural alignment. **Potential WSP inspiration:** A useful reference for reusable programs that must tolerate differences in model width or parameterization.

<a id="wcr-composition"></a>
## Weight Arithmetic, Merging & Interference

*How can changes be combined without destroying existing capabilities?*

- **[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482)** (ICML 2022). **Weight-centric idea:** Combines compatible fine-tuned checkpoints by averaging weights. **Potential WSP inspiration:** Provides a simple composition baseline and a reminder that checkpoint compatibility matters.

- **[TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)** (NeurIPS 2023). **Weight-centric idea:** Addresses redundant changes and sign conflicts among parameter updates. **Potential WSP inspiration:** Multi-program installation should inspect edit conflicts, not just add deltas.

- **[Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099)** (ICML 2024). **Weight-centric idea:** Introduces DARE, random dropping and rescaling of fine-tuning deltas before merging. **Potential WSP inspiration:** Tests how much of a capability-bearing change survives sparsification; this is not equivalent to an executable program.

- **[AdaMerging: Adaptive Model Merging for Multi-Task Learning](https://arxiv.org/abs/2310.02575)** (2023 preprint). **Weight-centric idea:** Adapts task-wise or layer-wise merging coefficients using an unsupervised objective. **Potential WSP inspiration:** Suggests task- or layer-dependent arbitration when successive edits conflict.

<a id="wcr-structure"></a>
## Structured Parameters, Sparsity & Mechanism Localization

*Which coordinates, directions, or subnetworks should a program modify?*

- **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)** (ICLR 2019). **Weight-centric idea:** Identifies sparse trainable subnetworks within larger networks. **Potential WSP inspiration:** Motivates examining whether new capabilities can be installed through restricted computational substrates.

- **[Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)** (2021 preprint). **Weight-centric idea:** Uses attribution to locate neurons linked to particular factual knowledge. **Potential WSP inspiration:** Shows one route from behavior to candidate edit locations, subject to causal validation.

- **[DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353)** (ICML 2024). **Weight-centric idea:** Separates weight magnitude and direction for adaptation. **Potential WSP inspiration:** Invites explicit magnitude/direction constraints when writing local parameter changes.

- **[PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://arxiv.org/abs/2404.02948)** (NeurIPS 2024). **Weight-centric idea:** Uses principal singular components of pretrained matrices as adaptable subspaces. **Potential WSP inspiration:** Suggests selecting editing subspaces through matrix structure rather than arbitrary coordinates.

<a id="wcr-retention"></a>
## Continual Capability Accumulation & Preservation

*Where can new abilities live, and what should remain unchanged after many updates?*

- **[Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796)** (PNAS 2017). **Weight-centric idea:** Protects parameters estimated as important to previous tasks (EWC). **Potential WSP inspiration:** A foundation for measuring and protecting the footprint of old capabilities during edits.

- **[Progressive Neural Networks](https://arxiv.org/abs/1606.04671)** (2016 preprint). **Weight-centric idea:** Adds new network columns while retaining earlier ones and lateral transfer. **Potential WSP inspiration:** An architectural counterpart to in-place editing: preservation can come from separation, at a capacity cost.

- **[PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning](https://arxiv.org/abs/1711.05769)** (CVPR 2018). **Weight-centric idea:** Reclaims unused parameters to accommodate sequential tasks. **Potential WSP inspiration:** Suggests tracking free parameter capacity and edit occupancy across many installations.

- **[Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights](https://arxiv.org/abs/1801.06519)** (ECCV 2018). **Weight-centric idea:** Learns task-specific binary masks over fixed base weights. **Potential WSP inspiration:** Provides a non-destructive baseline for conditional capability activation and retention.

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
