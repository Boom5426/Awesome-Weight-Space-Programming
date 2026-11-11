<h1 align="center">Awesome Weight-Space Programming</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="https://github.com/Boom5426/Awesome-Weight-Space-Programming/stargazers"><img src="https://img.shields.io/github/stars/Boom5426/Awesome-Weight-Space-Programming?style=flat-square&logo=github&label=Stars" alt="GitHub stars" /></a>
  <a href="https://github.com/Boom5426/Awesome-Weight-Space-Programming/commits/main"><img src="https://img.shields.io/github/last-commit/Boom5426/Awesome-Weight-Space-Programming?style=flat-square&logo=github&label=Updated" alt="Last update" /></a>
</p>



**Weight-Space Programming (WSP)** explores how language models and other reasoning agents can inspect, construct, and modify neural-network weights with executable procedures. This repository follows direct WSP research, while clearly distinguishing neural-program compilation, hypernetworks, and established model-editing methods as related foundations.


<a id="start-here"></a>
## 🚀 Start Here

New to WSP? Pick a research question. **Bold entries** are suggested starting points, not an impact ranking; publication status appears in the full lists.

| Goal | Recommended entry points |
| --- | --- |
| 🧠 **Understand direct WSP** | **[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)** · [WSP-Scope](https://arxiv.org/abs/2611.09382) |
| 🛠️ **Install and retain capabilities** | **[WeightCode](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)** · [WeightLoop](https://arxiv.org/abs/2611.07319) |
| 📏 **Evaluate weight understanding and editing** | **[IWIBench](https://arxiv.org/abs/2611.08647)** · [WSP-Scope](https://arxiv.org/abs/2611.09382) · [Weight Oracles](https://arxiv.org/abs/2610.07334) · [Orbit Audits](https://arxiv.org/abs/2611.05798) · [Clinical Network Audits](https://arxiv.org/abs/2611.05341) |
| 🧬 **Generate weights and networks** | **[Physics2Weight](https://arxiv.org/abs/2611.12954)** · [Medical Imaging WSP](https://arxiv.org/abs/2611.12066) · [Game Policies](https://arxiv.org/abs/2611.09271) |
| ✅ **Build verifiable interventions** | **[W-ISA](https://arxiv.org/abs/2611.13232)** · [NCP](https://arxiv.org/abs/2611.13236) · [Policy Model Checking](https://arxiv.org/abs/2611.11604) |
| 🔗 **Understand adjacent paradigms** | **[Program-as-Weights](https://arxiv.org/abs/2607.02512)** · [Tracr](https://arxiv.org/abs/2301.05062) · [Doc-to-LoRA](https://arxiv.org/abs/2602.15902) · [Text-to-LoRA](https://arxiv.org/abs/2506.06105) |

<a id="latest-updates"></a>
## 📰 Latest Updates

| Date | What changed |
| --- | --- |
| `2026-11-11` | Gap-filling pass: added the clinical-network auditing paper, a Claude Fable 5.2 replication, an evidence-scope critique, autoresearch experiments, the released edited Qwen checkpoint, and missing foundations (RASP, Tracr, Learning Transformer Programs, neural functionals, deep weight-space alignment, parameter decomposition, refusal-direction weight orthogonalization). |
| `2026-11-11` | Multi-keyword sweep of arXiv, alphaXiv, Hugging Face Papers and other preprint platforms: added IWIBench, Tree-Ising, Weight Oracles, SkillSmith, a diffusion-editing research report, and an independent replication resource. |
| `2026-11-11` | Adopted research-question reading tracks, a chronological direct-WSP catalog, and separate related-method sections. |
| `2026-11-11` | Initial curated collection of 33 research and technical resources, including new November preprints. |

<a id="research-papers"></a>
## 🔬 Research Papers

Research directly involving programmatic inspection, construction, or modification of neural-network weights, with informative method and task tags.

**17 papers and manuscripts** · [2026 (17)](#2026)

<a id="2026"></a>
### 🗓️ 2026 — 17 papers

- **[WeightCode]** `[Capability Installation]` `[Program Reuse]` WeightCode: Installing New Capabilities into Neural Networks via Weight Programming (**Manuscript 2026**) [[paper](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)] [[code](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars)

- **[Mixed Signals]** `[Biosignals]` `[Model Construction]` Mixed Signals: Weight-Space Programming for EEG and ECG (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13758)] [[project](https://daravaram.github.io/)]

- **[NCP]** `[Verification]` `[Control]` NCP: Verifier-Guided Optimization of Weight-Space Control Policies (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13236)]

- **[W-ISA]** `[Runtime]` `[Transactional Editing]` W-ISA: Transactional Execution of Weight-Space Intervention Programs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13232)]

- **[Physics2Weight]** `[Scientific AI]` `[PDE Solving]` Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.12954)]

- **[WSP for Medical Imaging]** `[Medical Imaging]` `[Model Construction]` Weight-Space Programming for Medical Imaging: Do We Still Need Training Data? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.12066)] [[code](https://github.com/MaximilianLindholz/weight-space-programming-medical)] ![GitHub stars](https://img.shields.io/github/stars/MaximilianLindholz/weight-space-programming-medical.svg?logo=github&label=Stars)

- **[WSP for Policies]** `[Policy Synthesis]` `[Formal Verification]` Weight-Space Programming of Policies and Their Verification via Model Checking (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11604)]

- **[WSP for Quantum Circuits]** `[Quantum Computing]` `[Parameter Synthesis]` Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11537)]

- **[WSP for Mathematical Optimization]** `[Operations Research]` `[Scoring Networks]` Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09559)]

- **[WSP-Scope]** `[Benchmark]` `[LLM Editing]` Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09382)] [[code](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars) [[project](https://wsp-scope.github.io/)]

- **[Zero-Shot Game WSP]** `[Games]` `[Policy Synthesis]` Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09271)]

- **[Can an LLM Actually Reason about Weights?]** `[Weight Reading]` `[Reliability]` Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming" (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.08070)]

- **[IWIBench]** `[Benchmark]` `[Intra-weight Injection]` IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.08647)] [[code](https://github.com/hcltech-robotics/iwibench)] ![GitHub stars](https://img.shields.io/github/stars/hcltech-robotics/iwibench.svg?logo=github&label=Stars)

- **[WeightLoop]** `[Experimental Feedback]` `[Continual Adaptation]` WeightLoop: Weight-Space Programming with Experimental Feedback (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.07319)]

- **[Orbit Audits]** `[Weight Reading]` `[Symmetry]` Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.05798)]

- **[Clinical Network Audits]** `[Clinical AI]` `[Auditing & Repair]` Weight-space programming for auditing clinical decision networks (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.05341)] [[code](https://github.com/hnusrat1/weightspace-rt)] ![GitHub stars](https://img.shields.io/github/stars/hnusrat1/weightspace-rt.svg?logo=github&label=Stars)

- **[Diffusion WSP Conjectures]** `[Diffusion Models]` `[Conjecture]` Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop (**Conjectural arXiv Preprint 2026**) [[paper](https://arxiv.org/abs/2611.04268)]


<a id="reports-and-blogs"></a>
## 📝 Reports and Blogs

- **[Fable WSP Replication]** `[Replication]` `[Cross-Model Comparison]` Claude Fable 5.2 can do "weight-space-programming" about as well as GPT-6 Astra (**LessWrong Post 2026**) [[post](https://www.lesswrong.com/posts/wg3K6xFFTdM6RmRgn/claude-fable-5-2-can-do-weight-space-programming-about-as)] [[data](https://huggingface.co/datasets/shawnghu/fable-weight-space-programming)]

- **[Gradient-Free Diffusion Weight Editing]** `[LLM Editing]` `[Concept Erasure]` An LLM Erases a Concept by Editing Diffusion Weights Directly, Without Gradients (**alphaXiv Research Report 2026**) [[report](https://www.alphaxiv.org/abs/2611.gradient-free-diffusion-weight-editing)] [[blog](https://huggingface.co/blog/javadtaghia/an-llm-erases-a-concept-by-editing-diffusion-weigh)]

- **[Evidence-Scope Critique]** `[Critique]` `[Evidence Scope]` The 'Astra can read and write weights to improve Qwen' post is misleading (**Technical Blog 2026**) [[blog](https://honnibal.dev/blog/astra-read-write-misleading)]

- **[WSP Autoresearch]** `[Autoresearch]` `[Hand-Written Transformers]` Weight-Space Programming Autoresearch: agents hand-writing transformer weights for arithmetic, algorithmic, and NLP tasks (**Technical Report 2026**) [[report](https://csinva.io/weight-space-programming-autoresearch/analyze)] [[code](https://github.com/csinva/weight-space-programming-autoresearch)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch.svg?logo=github&label=Stars)

- **[Sparks of Weight-Space Programming]** `[Weight Reading]` `[Direct Editing]` Sparks of Weight-Space Programming: LLMs Can Natively Read & Write Neural Network Weights (**Technical Blog 2026**) [[blog](https://rikiyat.github.io/blog/weight-space-programming/)] [[logs](https://github.com/RikiyaT/lm_understand-logs)]

<a id="related-research"></a>
## 🔗 Related Research

These adjacent methods inform WSP, but are not automatically instances of direct LLM-driven weight programming.

### Neural Program Compilation & Weight Generation

Learned compilers, hypernetworks, and adapter generators that map instructions or data to model parameters, plus program-to-weight compilers that construct networks by hand.

- **[Adapters as Data]** `[LoRA]` `[Weight Representation]` Adapters as Data: The Latent Space of LoRAs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.07775)]

- **[SkillSmith]** `[Parametric Skill Synthesis]` `[Prefix Tuning]` SkillSmith: Learning to Compose Parametric Skills and Textual Knowledge (**arXiv 2026**) [[paper](https://arxiv.org/abs/2607.27497)]

- **[Program-as-Weights]** `[Neural Compiler]` `[Reusable Programs]` Program-as-Weights: A Programming Paradigm for Fuzzy Functions (**NeurIPS 2026**) [[paper](https://arxiv.org/abs/2607.02512)] [[code](https://github.com/programasweights/programasweights-python)] ![GitHub stars](https://img.shields.io/github/stars/programasweights/programasweights-python.svg?logo=github&label=Stars) [[project](https://programasweights.com/research/)]

- **[Compile by Training]** `[Neural Compiler]` `[Adapter Training]` Compile by Training: Turning Natural-Language Specifications into Local Neural Functions (**EMNLP 2026 System Demonstrations**) [[paper](https://aclanthology.org/2026.emnlp-demos.78/)] [[preprint](https://arxiv.org/abs/2609.04199)] [[code](https://github.com/programasweights/compile-by-training)] ![GitHub stars](https://img.shields.io/github/stars/programasweights/compile-by-training.svg?logo=github&label=Stars)

- **[Infinite-Parameter LLMs]** `[Hypernetwork]` `[Online Adaptation]` Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data (**arXiv 2026**) [[paper](https://arxiv.org/abs/2609.18842)]

- **[DISC]** `[Hypernetwork]` `[Policy Generation]` DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation (**RSS 2026**) [[paper](https://arxiv.org/abs/2605.20856)] [[code](https://github.com/ReNginx/DISC)] ![GitHub stars](https://img.shields.io/github/stars/ReNginx/DISC.svg?logo=github&label=Stars)

- **[Doc-to-LoRA]** `[Hypernetwork]` `[Context Internalization]` Doc-to-LoRA: Learning to Instantly Internalize Contexts (**ICML 2026**) [[paper](https://proceedings.mlr.press/v306/charakorn26a.html)] [[preprint](https://arxiv.org/abs/2602.15902)] [[code](https://github.com/SakanaAI/doc-to-lora)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/doc-to-lora.svg?logo=github&label=Stars)

- **[Text-to-LoRA]** `[Hypernetwork]` `[Task Adaptation]` Text-to-LoRA: Instant Transformer Adaption (**ICML 2025**) [[paper](https://proceedings.mlr.press/v267/charakorn25a.html)] [[preprint](https://arxiv.org/abs/2506.06105)] [[code](https://github.com/SakanaAI/text-to-lora)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/text-to-lora.svg?logo=github&label=Stars)

- **[Neural Programs in Weight Space]** `[Program Synthesis]` `[Meta-Learning]` End-to-End Synthesis of Neural Programs in Weight Space (**ICLR 2025 Workshop on Neural Network Weights as a New Data Modality**) [[paper](https://openreview.net/forum?id=tzf3XUg0Q5)]

- **[Learning Transformer Programs]** `[Interpretable by Design]` `[Program Extraction]` Learning Transformer Programs (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2306.01128)] [[code](https://github.com/princeton-nlp/TransformerPrograms)] ![GitHub stars](https://img.shields.io/github/stars/princeton-nlp/TransformerPrograms.svg?logo=github&label=Stars)

- **[Tracr]** `[Program Compilation]` `[Hand-Constructed Weights]` Tracr: Compiled Transformers as a Laboratory for Interpretability (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2301.05062)] [[code](https://github.com/google-deepmind/tracr)] ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/tracr.svg?logo=github&label=Stars)

- **[PPUDA]** `[Parameter Prediction]` `[Graph Hypernetwork]` Parameter Prediction for Unseen Deep Architectures (**NeurIPS 2021**) [[paper](https://arxiv.org/abs/2110.13100)] [[code](https://github.com/facebookresearch/ppuda)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/ppuda.svg?logo=github&label=Stars)

- **[RASP]** `[Programming Language]` `[Transformer Computation]` Thinking Like Transformers (**ICML 2021**) [[paper](https://arxiv.org/abs/2106.06981)] [[code](https://github.com/tech-srl/RASP)] ![GitHub stars](https://img.shields.io/github/stars/tech-srl/RASP.svg?logo=github&label=Stars)

### Model Editing & Weight-Space Foundations

Research on modifying facts or behaviors, reusing parameter differences, and reasoning about symmetries or learned weight representations.

- **[Tree-Ising]** `[Training-Free Editing]` `[Discrete Optimization]` Tree-Ising: Repairing Language Models with Bit-Level Ising Edits (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.14210)]

- **[A Survey of Weight Space Learning]** `[Survey]` `[Weight-Space Learning]` A Survey of Weight Space Learning: Understanding, Representation, and Generation (**arXiv 2026**) [[paper](https://arxiv.org/abs/2603.10090)] [[code](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning)] ![GitHub stars](https://img.shields.io/github/stars/Zehong-Wang/Awesome-Weight-Space-Learning.svg?logo=github&label=Stars)

- **[TensorMutation]** `[Weight-Space Learning]` `[Model Mutation]` TensorMutation: Learning Weight-Space Mutations of Deep Learning Models on Neural Graphs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09650)]

- **[Weight Oracles]** `[Weight Reading]` `[Safety Auditing]` Weight Oracles: Reading Neural Network Weights with Language Models (**arXiv 2026; NeurIPS 2026 NeuralArtifacts Workshop Spotlight**) [[paper](https://arxiv.org/abs/2610.07334)]

- **[Targeted Parameter Decomposition]** `[Mechanism Recovery]` `[Targeted Rewiring]` Targeted Recovery of Weight-Space Mechanisms From Neural Networks (**ICML 2026 Mechanistic Interpretability Workshop**) [[paper](https://arxiv.org/abs/2607.13047)] [[code](https://github.com/Antovigo/targeted-parameter-decomposition)] ![GitHub stars](https://img.shields.io/github/stars/Antovigo/targeted-parameter-decomposition.svg?logo=github&label=Stars)

- **[Weight Space as a Modality]** `[Position]` `[Weight Generation]` Position: Weight Space Should Be a First-Class Generative AI Modality (**ICML 2026**) [[paper](https://arxiv.org/abs/2605.18632)]

- **[AlphaEdit]** `[Model Editing]` `[Knowledge Preservation]` AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (**ICLR 2025**) [[paper](https://arxiv.org/abs/2410.02355)] [[code](https://github.com/jianghoucheng/AlphaEdit)] ![GitHub stars](https://img.shields.io/github/stars/jianghoucheng/AlphaEdit.svg?logo=github&label=Stars)

- **[Refusal Direction]** `[Weight Orthogonalization]` `[Behavior Editing]` Refusal in Language Models Is Mediated by a Single Direction (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2406.11717)] [[code](https://github.com/andyrdt/refusal_direction)] ![GitHub stars](https://img.shields.io/github/stars/andyrdt/refusal_direction.svg?logo=github&label=Stars)

- **[WISE]** `[Lifelong Editing]` `[Knowledge Memory]` WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models (**arXiv 2024**) [[paper](https://arxiv.org/abs/2405.14768)] [[code](https://github.com/zjunlp/EasyEdit)] ![GitHub stars](https://img.shields.io/github/stars/zjunlp/EasyEdit.svg?logo=github&label=Stars)

- **[Deep Weight Space Alignment]** `[Weight Alignment]` `[Equivariant Networks]` Equivariant Deep Weight Space Alignment (**ICML 2024**) [[paper](https://arxiv.org/abs/2310.13397)] [[code](https://github.com/AvivNavon/deep-align)] ![GitHub stars](https://img.shields.io/github/stars/AvivNavon/deep-align.svg?logo=github&label=Stars)

- **[Neural Functional Transformers]** `[Weight-Space Learning]` `[Permutation Symmetry]` Neural Functional Transformers (**NeurIPS 2023**) [[paper](https://papers.neurips.cc/paper_files/paper/2023/hash/f4757db82a02eea015670ecca605d5cc-Abstract-Conference.html)] [[code](https://github.com/AllanYangZhou/nfn)] ![GitHub stars](https://img.shields.io/github/stars/AllanYangZhou/nfn.svg?logo=github&label=Stars)

- **[NFN]** `[Weight-Space Learning]` `[Permutation Equivariance]` Permutation Equivariant Neural Functionals (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2302.14040)] [[code](https://github.com/AllanYangZhou/nfn)] ![GitHub stars](https://img.shields.io/github/stars/AllanYangZhou/nfn.svg?logo=github&label=Stars)

- **[DWSNets]** `[Weight-Space Learning]` `[Equivariant Networks]` Equivariant Architectures for Learning in Deep Weight Spaces (**ICML 2023**) [[paper](https://arxiv.org/abs/2301.12780)] [[code](https://github.com/AvivNavon/DWSNets)] ![GitHub stars](https://img.shields.io/github/stars/AvivNavon/DWSNets.svg?logo=github&label=Stars)

- **[Git Re-Basin]** `[Weight Alignment]` `[Model Merging]` Git Re-Basin: Merging Models Modulo Permutation Symmetries (**ICLR 2023**) [[paper](https://arxiv.org/abs/2209.04836)] [[code](https://github.com/samuela/git-re-basin)] ![GitHub stars](https://img.shields.io/github/stars/samuela/git-re-basin.svg?logo=github&label=Stars)

- **[Task Arithmetic]** `[Task Vectors]` `[Model Merging]` Editing Models with Task Arithmetic (**ICLR 2023**) [[paper](https://arxiv.org/abs/2212.04089)] [[code](https://github.com/mlfoundations/task_vectors)] ![GitHub stars](https://img.shields.io/github/stars/mlfoundations/task_vectors.svg?logo=github&label=Stars)

- **[MEMIT]** `[Knowledge Editing]` `[Mass Editing]` Mass-Editing Memory in a Transformer (**ICLR 2023**) [[paper](https://arxiv.org/abs/2210.07229)] [[code](https://github.com/kmeng01/memit)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/memit.svg?logo=github&label=Stars)

- **[ROME]** `[Knowledge Editing]` `[Causal Tracing]` Locating and Editing Factual Associations in GPT (**NeurIPS 2022**) [[paper](https://arxiv.org/abs/2202.05262)] [[code](https://github.com/kmeng01/rome)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/rome.svg?logo=github&label=Stars)

- **[Transformer Circuits Framework]** `[Mechanistic Interpretability]` `[Weight Reading]` A Mathematical Framework for Transformer Circuits (**Transformer Circuits Thread 2021**) [[article](https://transformer-circuits.pub/2021/framework/index.html)]

- **[HyperNetworks]** `[Hypernetwork]` `[Weight Generation]` HyperNetworks (**ICLR 2017**) [[paper](https://research.google/pubs/hypernetworks-2/)]

<a id="resources"></a>
## 🧰 Resources & Tools

- **[WeightCode]** Executable programs, reproduction scripts, and an agent skill. [[code](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars)
- **[Weights-Only Replication]** Independent replication of selected MIT WSP weight-reading experiments, including reduced-context controls. [[code](https://github.com/jhpark94/weights-only-replication)] ![GitHub stars](https://img.shields.io/github/stars/jhpark94/weights-only-replication.svg?logo=github&label=Stars)

- **[MIT WSP Logs]** First-party experiment records for *Sparks of Weight-Space Programming*. [[code](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs.svg?logo=github&label=Stars)
- **[Edited Qwen3.5-0.8B]** Released checkpoint from the *Sparks* math-looping repair experiment, with an independent benchmark re-run on the model card. [[model](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)]
- **[WSP-Scope]** Code and experiments for systematic evaluation. [[code](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars)
- **[wsp-kit]** Independent toolkit for bounded edits; not a peer-reviewed paper. [[code](https://github.com/AuremHQ/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AuremHQ/weight-space-programming.svg?logo=github&label=Stars)

<a id="scope"></a>
## 🎯 Scope

- **Direct WSP:** weight reading, construction, editing, capability installation, program reuse, evaluation, and verification through reasoning agents or executable programs.
- **Related methods:** neural-program compilation, learned weight generators, model editing, weight merging, and weight-space representation learning when they clarify an important mechanism or comparison.
- **Usually out of scope:** generic PEFT and gradient-only adaptation without a clear connection to programmable weights.

<a id="inclusion-rules"></a>
## ✅ Inclusion Rules

- Prefer original research papers, first-party preprints and project pages, and official repositories.
- Clearly distinguish peer-reviewed papers, preprints, unpublished manuscripts, and technical blogs.
- Include substantive new methods, evaluations, benchmarks, and empirically grounded results; clearly label conjectural work.
- Assign concise method/task tags rather than repeating the name of the whole field.
- Provide `[paper]`, `[preprint]`, `[code]`, and other primary-source links only when available; show star badges only for identifiable GitHub repositories.
- Keep closely related foundations separate from direct WSP, and avoid duplicate references.

<a id="contributing"></a>
## 🤝 Contributing

Contributions and corrections are welcome. Open an [Issue](https://github.com/Boom5426/Awesome-Weight-Space-Programming/issues) or [Pull Request](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pulls) with the full title, primary paper link, first public date, publication status, verified code/project links, and a short explanation of relevance.

<a id="star-history"></a>
## ⭐ Star History

<p align="center">
  <a href="https://star-history.com/#Boom5426/Awesome-Weight-Space-Programming&Date">
    <img src="https://api.star-history.com/svg?repos=Boom5426/Awesome-Weight-Space-Programming&type=Date" alt="Star History Chart" />
  </a>
</p>
