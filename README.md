# Awesome Weight-Space Programming

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last Updated](https://img.shields.io/badge/updated-2026--11--11-blue)

**Weight-Space Programming (WSP)** explores how reasoning agents, especially large language models, can **inspect, construct, and edit neural-network weights** through executable procedures. Rather than ordinary gradient-based adaptation, a weight programmer can examine a network's computation, construct targeted parameter changes, and evaluate the resulting behavior. The field spans direct weight reading, weight editing, network synthesis, capability installation, reusable programs, and verification.

### Start Here: Representative Works

Selected for their **conceptual relevance**, not as a citation-count ranking:

- **[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)** (MIT CSAIL, 2026; technical blog) — Early articulation of WSP through LLM-based weight reading, construction, and editing.
- **[WeightCode](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)** (2026; manuscript) — Installs capabilities using reusable executable weight programs, while studying preservation and successive updates.
- **[WSP-Scope](https://arxiv.org/abs/2611.09382)** (2026; arXiv preprint) — Systematic evaluation of localized editing, cross-task generalization, and reliability on Qwen models.
- **[Program-as-Weights](https://arxiv.org/abs/2607.02512)** (NeurIPS 2026; **adjacent paradigm**) — Compiles specifications into reusable neural programs using a trained compiler and interpreter; distinct from direct editing of pretrained weights.

> **Scope.** The first four sections cover direct WSP, applied weight construction, evaluation, and conceptual proposals. The two **Related** sections cover learned neural compilers, hypernetworks, model editing, and weight-space learning. Works are grouped by **primary research question**, rather than by year or domain alone. Publication status is stated explicitly.

## Contents

- [Start Here: Representative Works](#start-here-representative-works)
- [Core Methods & Capability Editing](#core-methods-capability-editing)
- [Direct Weight Generation & Applications](#direct-weight-generation-applications)
- [Evaluation, Verification & Tooling](#evaluation-verification-tooling)
- [Conceptual Proposals](#conceptual-proposals)
- [Related: Neural Program Compilation & Weight Generation](#related-neural-program-compilation-weight-generation)
- [Related: Model Editing & Weight-Space Foundations](#related-model-editing-weight-space-foundations)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)

## Core Methods & Capability Editing

Direct LLM-guided inspection and modification of existing models, including reusable programs and feedback-driven updates.

- **[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)** `[Weight Reading]` `[Direct Editing]` Sparks of Weight-Space Programming: LLMs Can Natively Read & Write Neural Network Weights (**Technical Blog 2026**) [[blog](https://rikiyat.github.io/blog/weight-space-programming/)] [[logs](https://github.com/RikiyaT/lm_understand-logs)] — The MIT CSAIL research post introducing direct LLM reading, construction, and editing of neural weights, including a Qwen repair experiment.
- **[WeightCode](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)** `[Capability Installation]` `[Program Reuse]` WeightCode: Installing New Capabilities into Neural Networks via Weight Programming (**Manuscript 2026**) [[paper](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)] [[code](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars) — An LLM writes executable, gradient-free weight programs to install new capabilities; programs can be rerun on independent networks and composed across updates.
- **[WeightLoop](https://arxiv.org/abs/2611.07319)** `[Experimental Feedback]` `[Continual Adaptation]` WeightLoop: Weight-Space Programming with Experimental Feedback (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.07319)] — Uses one reusable parameter-editing program to incorporate later experimental feedback into a predictor; evaluated by offline replay.

## Direct Weight Generation & Applications

Direct construction of neural networks, policies, circuits, and task-specific scoring networks; some studies also edit existing networks.

- **[Mixed Signals](https://arxiv.org/abs/2611.13758)** `[Biosignals]` `[Model Construction]` Mixed Signals: Weight-Space Programming for EEG and ECG (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13758)] [[project](https://daravaram.github.io/)] — Studies direct construction and fault repair for EEG/ECG networks, including limitations when editing well-trained classifiers.
- **[Physics2Weight](https://arxiv.org/abs/2611.12954)** `[Scientific AI]` `[PDE Solving]` Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.12954)] — Generates neural architectures and weights from governing equations and boundary conditions for PDE solving.
- **[WSP for Medical Imaging](https://arxiv.org/abs/2611.12066)** `[Medical Imaging]` `[Model Construction]` Weight-Space Programming for Medical Imaging: Do We Still Need Training Data? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.12066)] [[code](https://github.com/MaximilianLindholz/weight-space-programming-medical)] ![GitHub stars](https://img.shields.io/github/stars/MaximilianLindholz/weight-space-programming-medical.svg?logo=github&label=Stars) — Tests LLM-written CNN weights on medical images without seeing training images, against trained and zero-shot references.
- **[WSP for Policies](https://arxiv.org/abs/2611.11604)** `[Policy Synthesis]` `[Formal Verification]` Weight-Space Programming of Policies and Their Verification via Model Checking (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11604)] — Combines LLM-generated policy weights with probabilistic model checking of task requirements.
- **[WSP for Quantum Circuits](https://arxiv.org/abs/2611.11537)** `[Quantum Computing]` `[Parameter Synthesis]` Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11537)] — Studies direct generation of variational quantum-circuit parameters and compares with optimizers.
- **[WSP for Mathematical Optimization](https://arxiv.org/abs/2611.09559)** `[Operations Research]` `[Scoring Networks]` Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09559)] — Tests directly written scoring networks inside exact optimization algorithms, including comparisons to simple heuristic baselines.
- **[Zero-Shot Game WSP](https://arxiv.org/abs/2611.09271)** `[Games]` `[Policy Synthesis]` Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09271)] — Constructs and independently verifies neural game policies across a graded ladder, probing the limits of hand-written weights.

## Evaluation, Verification & Tooling

Benchmarks and audits of weight-reading claims, plus systems for controlled, inspectable parameter interventions.

- **[WSP-Scope](https://arxiv.org/abs/2611.09382)** `[Benchmark]` `[LLM Editing]` Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09382)] [[code](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars) [[project](https://wsp-scope.github.io/)] — Examines 16 editing trajectories over seven benchmarks and two Qwen scales, including transfer and reliability.
- **[Can an LLM Actually Reason about Weights?](https://arxiv.org/abs/2611.08070)** `[Weight Reading]` `[Reliability]` Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming" (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.08070)] — Audits claimed weight understanding and distinguishes verified arithmetic from dataset priors or incomplete tracing.
- **[Orbit Audits](https://arxiv.org/abs/2611.05798)** `[Weight Reading]` `[Symmetry]` Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.05798)] — Tests whether weight readers respect function-preserving parameter permutations and rescalings.
- **[W-ISA](https://arxiv.org/abs/2611.13232)** `[Runtime]` `[Transactional Editing]` W-ISA: Transactional Execution of Weight-Space Intervention Programs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13232)] — A transactional instruction set for checked parameter edits, projections, ablations, replay, and restoration.
- **[NCP](https://arxiv.org/abs/2611.13236)** `[Verification]` `[Control]` NCP: Verifier-Guided Optimization of Weight-Space Control Policies (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13236)] — A verified control plane for temporary weight interventions; candidate policies that do not meet admission criteria are rejected.

## Conceptual Proposals

Conjectures and research proposals, separated from experimentally validated methods.

- **[Diffusion WSP Conjectures](https://arxiv.org/abs/2611.04268)** `[Diffusion Models]` `[Conjecture]` Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop (**Conjectural arXiv Preprint 2026**) [[paper](https://arxiv.org/abs/2611.04268)] — Proposes a diagnostic and iterative editing framework for restoration diffusion models; the main claims are hypotheses, not demonstrated results.

## Related: Neural Program Compilation & Weight Generation

Related paradigms that compile instructions into neural artifacts or learn generators of weights; they are not necessarily direct WSP.

- **[Program-as-Weights](https://arxiv.org/abs/2607.02512)** `[Neural Compiler]` `[Reusable Programs]` Program-as-Weights: A Programming Paradigm for Fuzzy Functions (**NeurIPS 2026**) [[paper](https://arxiv.org/abs/2607.02512)] [[code](https://github.com/programasweights/programasweights-python)] ![GitHub stars](https://img.shields.io/github/stars/programasweights/programasweights-python.svg?logo=github&label=Stars) [[project](https://programasweights.com/research/)] — A trained compiler turns natural-language function specifications into reusable parameter-efficient neural programs for a frozen interpreter.
- **[Compile by Training](https://aclanthology.org/2026.emnlp-demos.78/)** `[Neural Compiler]` `[Adapter Training]` Compile by Training: Turning Natural-Language Specifications into Local Neural Functions (**EMNLP 2026 System Demonstrations**) [[paper](https://aclanthology.org/2026.emnlp-demos.78/)] [[preprint](https://arxiv.org/abs/2609.04199)] [[code](https://github.com/programasweights/compile-by-training)] ![GitHub stars](https://img.shields.io/github/stars/programasweights/compile-by-training.svg?logo=github&label=Stars) — Compiles task specifications into local programs by synthesizing examples and training an adapter; extends Program-as-Weights.
- **[Infinite-Parameter LLMs](https://arxiv.org/abs/2609.18842)** `[Hypernetwork]` `[Online Adaptation]` Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data (**arXiv 2026**) [[paper](https://arxiv.org/abs/2609.18842)] — Proposes a live-data-conditioned hypernetwork with Bayesian updates to its latent code, yielding evolving weight modulations.
- **[DISC](https://arxiv.org/abs/2605.20856)** `[Hypernetwork]` `[Policy Generation]` DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation (**RSS 2026**) [[paper](https://arxiv.org/abs/2605.20856)] [[code](https://github.com/ReNginx/DISC)] ![GitHub stars](https://img.shields.io/github/stars/ReNginx/DISC.svg?logo=github&label=Stars) — Generates task-specific visuomotor policy weights from language instructions with a hypernetwork.
- **[Doc-to-LoRA](https://arxiv.org/abs/2602.15902)** `[Hypernetwork]` `[Context Internalization]` Doc-to-LoRA: Learning to Instantly Internalize Contexts (**ICML 2026**) [[paper](https://proceedings.mlr.press/v306/charakorn26a.html)] [[preprint](https://arxiv.org/abs/2602.15902)] [[code](https://github.com/SakanaAI/doc-to-lora)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/doc-to-lora.svg?logo=github&label=Stars) — Generates LoRA adapters from unseen contexts so the target LLM can answer later without re-reading the original context.
- **[Text-to-LoRA](https://arxiv.org/abs/2506.06105)** `[Hypernetwork]` `[Task Adaptation]` Text-to-LoRA: Instant Transformer Adaption (**ICML 2025**) [[paper](https://proceedings.mlr.press/v267/charakorn25a.html)] [[preprint](https://arxiv.org/abs/2506.06105)] [[code](https://github.com/SakanaAI/text-to-lora)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/text-to-lora.svg?logo=github&label=Stars) — Trains a hypernetwork to generate task-specific LoRA adapters from natural-language descriptions in one forward pass.
- **[Adapters as Data](https://arxiv.org/abs/2611.07775)** `[LoRA]` `[Weight Representation]` Adapters as Data: The Latent Space of LoRAs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.07775)] — Learns nonlinear representations over LoRA weights for sampling, editing, and variable-rank adapters.

## Related: Model Editing & Weight-Space Foundations

Foundational work on weight-space representations, model editing, model merging, and parameter-generating networks.

- **[A Survey of Weight Space Learning](https://arxiv.org/abs/2603.10090)** `[Survey]` `[Weight-Space Learning]` A Survey of Weight Space Learning: Understanding, Representation, and Generation (**arXiv 2026**) [[paper](https://arxiv.org/abs/2603.10090)] [[code](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning)] ![GitHub stars](https://img.shields.io/github/stars/Zehong-Wang/Awesome-Weight-Space-Learning.svg?logo=github&label=Stars) — Surveys weight-space understanding, representation, and generation; broader than LLM-driven weight-space programming.
- **[TensorMutation](https://arxiv.org/abs/2611.09650)** `[Weight-Space Learning]` `[Model Mutation]` TensorMutation: Learning Weight-Space Mutations of Deep Learning Models on Neural Graphs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09650)] — Trains a graph network to predict parameter effects of fault-informed mutations without retraining each target model.
- **[AlphaEdit](https://arxiv.org/abs/2410.02355)** `[Model Editing]` `[Knowledge Preservation]` AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (**ICLR 2025**) [[paper](https://arxiv.org/abs/2410.02355)] [[code](https://github.com/jianghoucheng/AlphaEdit)] ![GitHub stars](https://img.shields.io/github/stars/jianghoucheng/AlphaEdit.svg?logo=github&label=Stars) — Protects previously learned knowledge by projecting model edits into an appropriate null space.
- **[WISE](https://arxiv.org/abs/2405.14768)** `[Lifelong Editing]` `[Knowledge Memory]` WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models (**arXiv 2024**) [[paper](https://arxiv.org/abs/2405.14768)] [[code](https://github.com/zjunlp/EasyEdit)] ![GitHub stars](https://img.shields.io/github/stars/zjunlp/EasyEdit.svg?logo=github&label=Stars) — Studies repeated knowledge edits using separated parameter memories and sharded updates.
- **[Neural Functional Transformers](https://papers.neurips.cc/paper_files/paper/2023/hash/f4757db82a02eea015670ecca605d5cc-Abstract-Conference.html)** `[Weight-Space Learning]` `[Permutation Symmetry]` Neural Functional Transformers (**NeurIPS 2023**) [[paper](https://papers.neurips.cc/paper_files/paper/2023/hash/f4757db82a02eea015670ecca605d5cc-Abstract-Conference.html)] [[code](https://github.com/AllanYangZhou/nfn)] ![GitHub stars](https://img.shields.io/github/stars/AllanYangZhou/nfn.svg?logo=github&label=Stars) — Learns permutation-equivariant representations and transformations of neural-network weights.
- **[Git Re-Basin](https://arxiv.org/abs/2209.04836)** `[Weight Alignment]` `[Model Merging]` Git Re-Basin: Merging Models Modulo Permutation Symmetries (**ICLR 2023**) [[paper](https://arxiv.org/abs/2209.04836)] [[code](https://github.com/samuela/git-re-basin)] ![GitHub stars](https://img.shields.io/github/stars/samuela/git-re-basin.svg?logo=github&label=Stars) — Aligns independently trained networks under neuron permutation symmetries before weight-space merging.
- **[Task Arithmetic](https://arxiv.org/abs/2212.04089)** `[Task Vectors]` `[Model Merging]` Editing Models with Task Arithmetic (**ICLR 2023**) [[paper](https://arxiv.org/abs/2212.04089)] [[code](https://github.com/mlfoundations/task_vectors)] ![GitHub stars](https://img.shields.io/github/stars/mlfoundations/task_vectors.svg?logo=github&label=Stars) — Edits and combines model behavior using weight differences obtained from task-specific fine-tuning.
- **[MEMIT](https://arxiv.org/abs/2210.07229)** `[Knowledge Editing]` `[Mass Editing]` Mass-Editing Memory in a Transformer (**ICLR 2023**) [[paper](https://arxiv.org/abs/2210.07229)] [[code](https://github.com/kmeng01/memit)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/memit.svg?logo=github&label=Stars) — Applies structured parameter edits across layers to insert many factual associations into a transformer.
- **[ROME](https://arxiv.org/abs/2202.05262)** `[Knowledge Editing]` `[Causal Tracing]` Locating and Editing Factual Associations in GPT (**NeurIPS 2022**) [[paper](https://arxiv.org/abs/2202.05262)] [[code](https://github.com/kmeng01/rome)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/rome.svg?logo=github&label=Stars) — Locates factual recall computations and edits transformer MLP weights with rank-one updates.
- **[HyperNetworks](https://research.google/pubs/hypernetworks-2/)** `[Hypernetwork]` `[Weight Generation]` HyperNetworks (**ICLR 2017**) [[paper](https://research.google/pubs/hypernetworks-2/)] — Introduces trainable networks that generate the parameters of another neural network; a precursor rather than direct LLM-driven WSP.

## Additional Resources

- **MIT WSP experiment logs** — Original experiment records accompanying *Sparks of Weight-Space Programming*. [[repository](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs.svg?logo=github&label=Stars)
- **WSP-Scope project** — Evaluation materials for edits on Qwen models. [[repository](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars)
- **wsp-kit** — An independent engineering toolkit for bounded weight edits with evaluation gates; not a peer-reviewed paper. [[repository](https://github.com/AuremHQ/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AuremHQ/weight-space-programming.svg?logo=github&label=Stars)

## Contributing

Contributions are welcome. Please open an issue or pull request with:

1. The exact title, authors, first public date, and publication status (conference/journal, arXiv preprint, or technical blog).
2. A stable paper or primary-source link, plus a code link **only when verified**.
3. One or two informative tags describing the **method** and/or **task** (avoid repeating the field's name as a tag).
4. A clear distinction between **direct WSP** and a **Related** paradigm.

Please avoid duplicates, invented code repositories, unsupported venue claims, and presenting untested conjectures as empirical results.

---

**Curation snapshot: 11 November 2026.** Preprints may change; this is a curated starting collection rather than a claim of exhaustive coverage.
