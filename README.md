<h1 align="center">Awesome Weight-Space Programming</h1>

<p align="center">
  <a href="README_zh.md"><img src="https://img.shields.io/badge/%E8%AF%AD%E8%A8%80-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-24B6A6?style=flat-square&logo=googletranslate&logoColor=white" alt="简体中文" /></a>
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="https://github.com/Boom5426/Awesome-Weight-Space-Programming/stargazers"><img src="https://img.shields.io/github/stars/Boom5426/Awesome-Weight-Space-Programming?style=flat-square&logo=github&label=Stars" alt="GitHub stars" /></a>
  <a href="https://github.com/Boom5426/Awesome-Weight-Space-Programming/commits/main"><img src="https://img.shields.io/github/last-commit/Boom5426/Awesome-Weight-Space-Programming?style=flat-square&logo=github&label=Updated" alt="Last update" /></a>
</p>

**Weight-Space Programming (WSP)** explores how language models and other reasoning agents can inspect, construct, and modify neural-network weights with executable procedures. This repository follows direct WSP research, while clearly distinguishing neural-program compilation, hypernetworks, and established model-editing methods as related foundations.

<p align="center">
  <a href="https://boom5426.github.io/Awesome-Weight-Space-Programming/"><img src="https://img.shields.io/badge/Search_%26_Filter-Browse_Catalog-0B6E99?style=for-the-badge" alt="Search and filter Weight-Space Programming research" /></a>
  <a href="https://boom5426.github.io/Awesome-Weight-Space-Programming/landscape.html"><img src="https://img.shields.io/badge/Research_Landscape-Interactive_Map-24B6A6?style=for-the-badge" alt="Explore the interactive weight-space research map" /></a>
</p>

<p align="center">
  <sub>
    <a href="#start-here">Start Here</a> ·
    <a href="#latest-updates">Latest Updates</a> ·
    <a href="#research-papers">Direct WSP</a> ·
    <a href="#weight-centric-inspirations">Weight-Centric</a> ·
    <a href="docs/wsp-evidence.md">Evidence Matrix</a>
  </sub>
</p>


<a id="start-here"></a>
## 🚀 Start Here

New to WSP? These are **selective research entry points**, chosen for substantive experiments, useful comparisons, and clear methodological relevance—not for venue prestige, citation counts, or being the newest arXiv post. Featured does not mean peer-reviewed.

Planning an experiment? See the [evaluation research guide](docs/wsp-research-opportunities.md) for source-grounded questions on program portability, composition, retention, and matched baselines.

| Research question | Selected papers |
| --- | --- |
| **What can WSP reliably do?** | **[WSP-Scope](https://arxiv.org/abs/2611.09382)** (systematic trajectories and held-out tests) · **[iWSP](https://arxiv.org/abs/2611.18114)** (transparent network construction and hidden algorithmic tests). |
| **Can programs install and preserve capabilities?** | **[WeightCode](https://arxiv.org/abs/2611.25476)** — matched fine-tuning comparisons, retention, program reuse and successive installation. |
| **Can an editing recipe transfer across checkpoints?** | **[TowerBridge](https://arxiv.org/abs/2611.31233)** — 21 CLIP checkpoints, unseen hosts and an explicit retention guard. |
| **Can scientific feedback improve an editing plan?** | **[HypoLoop](https://arxiv.org/abs/2611.23718)** (22 scientific tasks; editing locations and fitting rules) · **[WeightLoop](https://arxiv.org/abs/2611.07319)** (reusable feedback-driven weight updates). |
| **Can weight editing help practical systems?** | **[Weight Coding](https://arxiv.org/abs/2611.29613)** (held-out dates and online A/B tests) · **[Robot Foundation Model Repair](https://arxiv.org/abs/2611.31715)** (paired simulation scenes, random and sign-reversed controls). |

**Important distinction:** HypoLoop's editing *plan* is revised from experimental evidence, while numerical solvers—including gradient-based optimization in some variants—fit the actual weight changes. Its inclusion highlights valuable scientific-feedback methodology; it is **not** evidence of gradient-free weight updates. The full catalog below tracks other relevant studies, including informative failures, without endorsing every entry as a starting point.

<a id="latest-updates"></a>
## 📰 Latest Updates

<!-- AUTO:START updates -->
| Date | What changed |
| --- | --- |
| `2026-11-26` | Expanded the 26 November update with 25 additional papers/manuscripts: 11 direct-WSP items, 9 weight-centric papers and 5 related foundations. Reduced Start Here to five research questions, with up to three complementary, evidence-driven papers per question. The two search passes add 42 entries in total; see the [dated review](docs/literature-update-2026-11-26.md). Community PRs [#12](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pull/12) and [#13](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pull/13) are merged. |
| `2026-11-22` | Added [Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885) to Direct WSP and the evidence matrix: a 27B model reports gradient-free self-editing (+6.6 percentage points on held-out problems) and eight accepted improvement sessions, with scope and retention caveats. |
| `2026-11-20` | Curated a selective, evidence-driven [Start Here](#start-here): prominently featured [HypoLoop](https://arxiv.org/abs/2611.23718) for feedback-driven scientific editing, removed unsupported conjectural and preliminary diffusion entries, and kept weak or negative experimental results accessible without treating them as recommended starting points. Earlier this day, updated [WeightCode](https://arxiv.org/abs/2611.25476) and added new WSP studies. |
<!-- AUTO:END updates -->

<a id="research-papers"></a>
## 🔬 Research Papers

<!-- AUTO:START direct -->
Research directly involving programmatic inspection, construction, or modification of neural-network weights, with informative method and task tags.

**63 papers and manuscripts** · [2026 (63)](#2026)

**Evidence audit:** [WSP Evidence Matrix](docs/wsp-evidence.md)

<a id="2026"></a>
### 🗓️ 2026 — 63 papers

- **[AME]** `[Few-shot VLM Adaptation]` `[Agent-designed Programs]` Few-Shot Adaptation of Vision-Language Models via Agentic Model Editing (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.34036)]

- **[Scalpel and Brush]** `[Pruning]` `[Metric Audit]` Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.33426)]

- **[Game-Theoretic Weight Reading]** `[Exact Evaluation]` `[Read/Write/Repair]` Reading, Writing and Repairing Game-Theoretic Policies in Weight Space (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.31979)]

- **[Weight-Space Programming of JEPA World Models]** `[World Models]` `[Full-text Review Pending]` Weight-Space Programming of JEPA World Models (**alphaXiv manuscript 2026**) [[paper](https://www.alphaxiv.org/abs/2611.wsp-jepa)] [[code](https://github.com/suayptalha/wsr)] ![GitHub stars](https://img.shields.io/github/stars/suayptalha/wsr.svg?logo=github&label=Stars)

- **[Weight Coding]** `[Production Recommenders]` `[Online A/B Evaluation]` Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.29613)]

- **[Blind Deployment-Fault Repair]** `[Blind Diagnosis]` `[Script Controls]` Where Does a Weight-Editing Agent Help? Blind Diagnosis and Repair of Deployment Faults in Vision Models (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.28781)]

- **[LLM-Guided Transformer Repair]** `[Controller vs Operator]` `[Matched Search]` Can an LLM Repair a Language Model in Weight Space Without Gradient Training? (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.25613)]

- **[VLM Repair Low-Bit Audit]** `[Numerical Forensics]` `[Rounded Controls]` Weight Space Programming for Vision Language Model Repair (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.23615)]

- **[Materials-Science WSP]** `[Zero-label Construction]` `[Scientific Priors]` Weight-Space Programming for Materials Science (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.22013)] [[code](https://github.com/sheikhahnaf/weightspace-programming-for-material-science)] ![GitHub stars](https://img.shields.io/github/stars/sheikhahnaf/weightspace-programming-for-material-science.svg?logo=github&label=Stars)

- **[Diffusion Program Construction]** `[Program vs Refinement]` `[Optimizer-in-the-loop]` What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.22228)]

- **[Weight-Space Reading]** `[Behavior Forecasting]` `[No-op Controls]` Weight-Space Reading (**alphaXiv manuscript 2026**) [[paper](https://www.alphaxiv.org/abs/2611.weight-space-reading-language-models)] [[code](https://github.com/suayptalha/wsr)] ![GitHub stars](https://img.shields.io/github/stars/suayptalha/wsr.svg?logo=github&label=Stars)

- **[FWSP]** `[Deterministic Editing]` `[Capability Boundaries]` Do We Really Need an LLM for Weight-Space Programming? A Deterministic Forward-Only Paradigm and Its Capability Boundaries (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.34612)]

- **[Kolpona]** `[RTL Generation]` `[Neuron Programming]` Kolpona: An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.33973)]

- **[Closed-Form Classifiers]** `[Frozen Encoder]` `[Supervised Closed-form Heads]` Fine-Tuning Without Gradients? Closed-Form, LLM-Written Classifiers on a Frozen Encoder (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.33972)]

- **[Tool-Free Quantization Repair]** `[Quantization]` `[Tool-free Weight Reading]` Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.33031)] [[code](https://github.com/urbste/weight-space-programming-ptq)] ![GitHub stars](https://img.shields.io/github/stars/urbste/weight-space-programming-ptq.svg?logo=github&label=Stars)

- **[Robot Foundation Model Repair]** `[Robot Foundation Model]` `[Physical Execution Repair]` Sparks of Weight-Space Programming for Robot Foundation Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.31715)]

- **[TowerBridge]** `[Cross-checkpoint Recipe]` `[Multimodal Retrieval]` TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.31233)]

- **[Self-Upgrading Embodied Agents]** `[Self-Editing]` `[Text Embodied Environment]` Self-Upgrading Embodied Agents (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.31117)]

- **[IR-ODWSP]** `[Object Detection]` `[Inverse Reparameterization]` Reparameterizing Your Object Detectors for Weight Space Programming (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.29882)] [[code](https://github.com/WongKinYiu/ODWSP)] ![GitHub stars](https://img.shields.io/github/stars/WongKinYiu/ODWSP.svg?logo=github&label=Stars)

- **[SELFWRITE]** `[Recursive Self-Editing]` `[Hidden Acceptance Gate]` Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.29513)]

- **[PAWP-TTS]** `[Speech Synthesis]` `[Negative Evidence]` PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.29455)] [[code](https://github.com/Firojpaudel/PAWP_TTS)] ![GitHub stars](https://img.shields.io/github/stars/Firojpaudel/PAWP_TTS.svg?logo=github&label=Stars)

- **[Self-WSP]** `[Self-Editing]` `[Random-search Controls]` Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.28833)]

- **[Autonomous Parameter Surgery]** `[Security Evaluation]` `[Selective Weight Tampering]` Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.27920)]

- **[TrojanMaxxing]** `[Security Evaluation]` `[Vision-Language Models]` TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.27425)]

- **[Spatial WSP vs LoRA]** `[Matched Backbone]` `[Retention Trade-off]` Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.27089)]

- **[Particle-Physics WSP]** `[Scientific Model Repair]` `[Mechanistic Controls]` Weight-space programming and mechanistic interpretability for model editing in particle physics (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.27079)] [[code](https://github.com/rbonnetguerrini/WSP-mech-interp-for-model-editing-in-particle-physics)] ![GitHub stars](https://img.shields.io/github/stars/rbonnetguerrini/WSP-mech-interp-for-model-editing-in-particle-physics.svg?logo=github&label=Stars)

- **[ICL-to-Weights]** `[Context Internalization]` `[Knowledge-matched Controls]` Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.26841)] [[code](https://github.com/y3nk0/weight-space-programming-study)] ![GitHub stars](https://img.shields.io/github/stars/y3nk0/weight-space-programming-study.svg?logo=github&label=Stars)

- **[Edit-Ready Vision Training]** `[Editability Preparation]` `[Gradient-trained Backbone]` Training Vision Models for LLM-Driven Weight-Space Programming (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.26408)]

- **[Self-Rewriting]** `[Self-Rewriting]` `[Continual Improvement]` Language Models Can Rewrite Their Own Weights (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.21885)] [[project](https://www.jiajunfan.com/projects/self-rewriting/)]

- **[WeightCode]** `[Capability Installation]` `[Program Reuse]` WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.25476)] [[code](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars)

- **[WSP Beyond Transformers]** `[Architecture Design]` `[Sparse Associative Memory]` Weight-Space Programming Doesn't Need Transformers (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.22055)] [[code](https://github.com/effl-lab/Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/effl-lab/Weight-Space-Programming.svg?logo=github&label=Stars)

- **[Tractor Guidance WSP]** `[Real-world Control]` `[Network Construction]` Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.21958)]

- **[Same Fix, Different Weights]** `[Replication]` `[Repair Mechanism]` Same Fix, Different Weights: Replicating Weight-Space Programming with Claude (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.20953)] [[code](https://github.com/Cenrax/weight-space-programming-claude)] ![GitHub stars](https://img.shields.io/github/stars/Cenrax/weight-space-programming-claude.svg?logo=github&label=Stars)

- **[Weights & Caches]** `[Tabular Foundation Models]` `[Weights & KV Cache]` Weights & Caches: LLMs Can Program Tabular Foundation Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.20174)]

- **[Zero-Shot Structured-Data WSP]** `[Zero-shot Construction]` `[Structured Data]` Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.19292)]

- **[WeightBench]** `[Benchmark]` `[42 Tasks]` WeightBench: Evaluating Language Models as Weight-Space Programmers (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.18553)] [[code](https://github.com/Aayush-Marasini/WeightBench)] ![GitHub stars](https://img.shields.io/github/stars/Aayush-Marasini/WeightBench.svg?logo=github&label=Stars)

- **[Computational-Biology Python WSP]** `[Computational Biology]` `[Behavior Repair]` Weight-Space Programming Changes How an LLM Uses Python for Computational Biology (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.20566)] [[repository; code pending](https://github.com/satouma7/bioWSP)] ![GitHub stars](https://img.shields.io/github/stars/satouma7/bioWSP.svg?logo=github&label=Stars)

- **[YOLO26 Weight Editing Study]** `[Object Detection]` `[Negative Evidence]` Can Large Language Models Optimize Pretrained Neural Network Weights? A Multi-Phase Empirical Evaluation of Gradient-Free Editing in YOLO26 Object Detection (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.17789)]

- **[Just Sort It!]** `[Mechanism Test]` `[Closed-form Edit]` Just sort it! A note on the LP behind rank-one anti-loop edits (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.21432)]

- **[SGNE-CC v2]** `[Spherical Rotation]` `[Sparse Anti-Loop Edit]` SGNE-CC v2: Training-Free Spherical Rotation of 205 `down_proj` Columns (0.0177%) in DeepSeek-R1-Distill-Qwen-1.5B (**Zenodo 2026**) [[preprint](https://doi.org/10.5281/zenodo.24398165)] [[code](https://github.com/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2)] [[weights](https://huggingface.co/Nondual-Observer/DeepSeek-R1-Distill-Qwen-1.5B-SGNE-CC-v2)] ![GitHub stars](https://img.shields.io/github/stars/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2.svg?logo=github&label=Stars)

- **[SGNE-CC]** `[Mechanistic Audit]` `[Norm-Preserving Edit]` Weight-Space Audit of MIT-p50c and DNA Weight Editing (SGNE-CC) on Qwen3.5-0.8B at a 32,768-Token Generation Limit (**Zenodo 2026**) [[preprint](https://doi.org/10.5281/zenodo.24235218)] [[code](https://github.com/Nondual-Observer/dna-weight-editing)] [[weights](https://huggingface.co/Nondual-Observer/Qwen3.5-0.8B-SGNE-CC)] ![GitHub stars](https://img.shields.io/github/stars/Nondual-Observer/dna-weight-editing.svg?logo=github&label=Stars)

- **[WSP Backdoor Security Study]** `[Security Audit]` `[Weight Editing]` Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.17395)]

- **[Computation, Not Weight Access]** `[Audit Controls]` `[Black-box Comparison]` Computation, not weight access: large language models as auditors of clinical prediction networks (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.07847)] [[code](https://github.com/Chth1z/llm-clinical-network-audit)] ![GitHub stars](https://img.shields.io/github/stars/Chth1z/llm-clinical-network-audit.svg?logo=github&label=Stars)

- **[iWSP]** `[Interpretable Construction]` `[Neuroscience]` Interpretable Weight-Space Programming Builds Transparent Transformers and Brain Encoding Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.18114)] [[code](https://github.com/csinva/weight-space-programming-autoresearch)] [[reports](https://csinva.io/weight-space-programming-autoresearch/analyze)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch.svg?logo=github&label=Stars)

- **[Replicating and Extending WSP]** `[Replication]` `[Weight Reading]` Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.21449)]

- **[Rule-to-Network Compilation]** `[Rule Compilation]` `[Program Baselines]` Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.16981)] [[code](https://github.com/JensLehmann/weight-space-programming-games)] ![GitHub stars](https://img.shields.io/github/stars/JensLehmann/weight-space-programming-games.svg?logo=github&label=Stars)

- **[Mixed Signals]** `[Biosignals]` `[Model Construction]` Mixed Signals: Weight-Space Programming for EEG and ECG (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13758)] [[project repository](https://github.com/DaraVaram/BioWSP)] ![GitHub stars](https://img.shields.io/github/stars/DaraVaram/BioWSP.svg?logo=github&label=Stars) [[project](https://daravaram.github.io/BioWSP/)]

- **[NCP]** `[Verification]` `[Control]` NCP: Verifier-Guided Optimization of Weight-Space Control Policies (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13236)] [[code](https://github.com/eax/w-isa/tree/main/NCP)] ![GitHub stars](https://img.shields.io/github/stars/eax/w-isa.svg?logo=github&label=Stars)

- **[W-ISA]** `[Runtime]` `[Transactional Editing]` W-ISA: Transactional Execution of Weight-Space Intervention Programs (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.13232)] [[code](https://github.com/eax/w-isa)] ![GitHub stars](https://img.shields.io/github/stars/eax/w-isa.svg?logo=github&label=Stars)

- **[Physics2Weight]** `[Scientific AI]` `[PDE Solving]` Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.12954)]

- **[WSP for Medical Imaging]** `[Medical Imaging]` `[Model Construction]` Weight-Space Programming for Medical Imaging: Do We Still Need Training Data? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.12066)] [[code](https://github.com/MaximilianLindholz/weight-space-programming-medical)] ![GitHub stars](https://img.shields.io/github/stars/MaximilianLindholz/weight-space-programming-medical.svg?logo=github&label=Stars)

- **[WSP for Policies]** `[Policy Synthesis]` `[Formal Verification]` Weight-Space Programming of Policies and Their Verification via Model Checking (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11604)] [[code](https://github.com/LAVA-LAB/COOL-MC/tree/wsp_verified)] ![GitHub stars](https://img.shields.io/github/stars/LAVA-LAB/COOL-MC.svg?logo=github&label=Stars)

- **[WSP for Quantum Circuits]** `[Quantum Computing]` `[Parameter Synthesis]` Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11537)] [[code](https://github.com/DebarshiKunduPSU/Quantum-Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/DebarshiKunduPSU/Quantum-Weight-Space-Programming.svg?logo=github&label=Stars)

- **[WSP for Mathematical Optimization]** `[Operations Research]` `[Scoring Networks]` Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09559)] [[code](https://github.com/butkeraites/llm-written-weights-or)] ![GitHub stars](https://img.shields.io/github/stars/butkeraites/llm-written-weights-or.svg?logo=github&label=Stars)

- **[WSP-Scope]** `[Benchmark]` `[LLM Editing]` Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09382)] [[code](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars) [[project](https://wsp-scope.github.io/)]

- **[Zero-Shot Game WSP]** `[Games]` `[Policy Synthesis]` Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09271)]

- **[Can an LLM Actually Reason about Weights?]** `[Weight Reading]` `[Reliability]` Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming" (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.08070)]

- **[IWIBench]** `[Benchmark]` `[Intra-weight Injection]` IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.08647)] [[code](https://github.com/hcltech-robotics/iwibench)] ![GitHub stars](https://img.shields.io/github/stars/hcltech-robotics/iwibench.svg?logo=github&label=Stars)

- **[WeightLoop]** `[Experimental Feedback]` `[Continual Adaptation]` WeightLoop: Weight-Space Programming with Experimental Feedback (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.07319)] [[code](https://github.com/limengran98/WeightLoop)] ![GitHub stars](https://img.shields.io/github/stars/limengran98/WeightLoop.svg?logo=github&label=Stars)

- **[Orbit Audits]** `[Weight Reading]` `[Symmetry]` Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.05798)]

- **[Clinical Network Audits]** `[Clinical AI]` `[Auditing & Repair]` Weight-space programming for auditing clinical decision networks (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.05341)] [[code](https://github.com/hnusrat1/weightspace-rt)] ![GitHub stars](https://img.shields.io/github/stars/hnusrat1/weightspace-rt.svg?logo=github&label=Stars)

- **[Robot Policy Debugging]** `[Robot Foundation Model]` `[Lexical Repair]` Can LLMs Debug Robots by Editing Their Weights? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.09376)]

- **[Instruction Distillation]** `[Robot Policy]` `[Closed-Form Editing]` Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.11894)] [[code](https://github.com/adeeb10abbas/weightsmith)] ![GitHub stars](https://img.shields.io/github/stars/adeeb10abbas/weightsmith.svg?logo=github&label=Stars)
<!-- AUTO:END direct -->

<a id="reports-and-blogs"></a>
## 📝 Reports and Blogs

<!-- AUTO:START reports -->
- **[EditLens]** `[Mechanistic Audit]` `[Replication]` What Did Astra's Edit Actually Do? (**Technical Blog 2026**) [[blog](https://xxlya.github.io/editlens/)] [[code](https://github.com/assassin808/edit-lens)] ![GitHub stars](https://img.shields.io/github/stars/assassin808/edit-lens.svg?logo=github&label=Stars) — Tests loop-repair explanations and contrasts weight swaps with activation patches.

- **[Fable WSP Replication]** `[Replication]` `[Cross-Model Comparison]` Claude Fable 5.2 can do "weight-space-programming" about as well as GPT-6 Astra (**LessWrong Post 2026**) [[post](https://www.lesswrong.com/posts/wg3K6xFFTdM6RmRgn/claude-fable-5-2-can-do-weight-space-programming-about-as)] [[data](https://huggingface.co/datasets/shawnghu/fable-weight-space-programming)]

- **[Gradient-Free Diffusion Weight Editing]** `[LLM Editing]` `[Concept Erasure]` An LLM Erases a Concept by Editing Diffusion Weights Directly, Without Gradients (**alphaXiv Research Report 2026**) [[report](https://www.alphaxiv.org/abs/2611.gradient-free-diffusion-weight-editing)] [[blog](https://huggingface.co/blog/javadtaghia/an-llm-erases-a-concept-by-editing-diffusion-weigh)]

- **[Sycophancy Repair by Weight Editing]** `[Direct Editing]` `[Sycophancy]` `[Preregistered]` Repairing sycophancy in Qwen2.5-0.5B by editing its weights, with Claude Opus 5.5 as the editor and a blind test split (**Technical Blog 2026**) [[blog](https://say43.github.io/2026/11/05/repairing-sycophancy.html)] [[code](https://github.com/Say43/Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/Say43/Weight-Space-Programming.svg?logo=github&label=Stars)

- **[Evidence-Scope Critique]** `[Critique]` `[Evidence Scope]` The 'Astra can read and write weights to improve Qwen' post is misleading (**Technical Blog 2026**) [[blog](https://honnibal.dev/blog/astra-read-write-misleading)]

- **[Sparks of Weight-Space Programming]** `[Weight Reading]` `[Direct Editing]` Sparks of Weight-Space Programming: LLMs Can Natively Read & Write Neural Network Weights (**Technical Blog 2026**) [[blog](https://rikiyat.github.io/blog/weight-space-programming/)] [[logs](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs.svg?logo=github&label=Stars)

- **[Independent Edit Composition]** `[Replication]` `[Composition]` Independently Discovered Weight Edits Compose: A Replication and Extension of Weight-Space Programming (**GitHub Report 2026**) [[code](https://github.com/ajaygrover/weight-space-programming-stacking)] ![GitHub stars](https://img.shields.io/github/stars/ajaygrover/weight-space-programming-stacking.svg?logo=github&label=Stars)

- **[Robot VLA Weight Editing]** `[Robot Policy]` `[Direct Editing]` Opus 5.5 makes π0.5 move faster and smoother by editing its weights (**Technical Report 2026**) [[code](https://github.com/Cuzyoung/robotics-weight-editing)] ![GitHub stars](https://img.shields.io/github/stars/Cuzyoung/robotics-weight-editing.svg?logo=github&label=Stars)

- **[Policy Surgery]** `[RL Control]` `[Weight Editing]` Policy Surgery: Programmatic repair of learned control policies (**GitHub Project 2026**) [[code](https://github.com/latentpaths/policy-surgery)] ![GitHub stars](https://img.shields.io/github/stars/latentpaths/policy-surgery.svg?logo=github&label=Stars)
<!-- AUTO:END reports -->

<a id="weight-centric-inspirations"></a>
## 🧭 Weight-Centric Inspirations (Beyond Editing)

Not all useful ideas for future weight programming come from editing papers. Our new **[Weight-Centric Research](docs/weight-centric-research.md)** reading series explores neural weights as objects to understand, represent, generate, compose, and protect. These studies are **inspirations and baselines**, not automatically direct WSP.

**76 curated papers across six research tracks:**

| Track | Research question |
| --- | --- |
| Weight geometry & symmetry | Can we compare or transfer computations across equivalent parameterizations? |
| Weight reading & representation | What can weights reveal without original task data? |
| Weight generation & synthesis | Can we generate a functional network or parameter block? |
| Weight arithmetic & merging | How do multiple updates interact or interfere? |
| Structured parameters & localization | Which weight directions, units, or subspaces should be changed? |
| Continual capability retention | How can new capabilities accumulate without erasing old ones? |

[**Browse the reading series (English)**](docs/weight-centric-research.md) · [简体中文](docs/weight-centric-research_zh.md)

<a id="related-research"></a>
## 🔗 Related Research

<!-- AUTO:START related -->
These adjacent methods inform WSP, but are not automatically instances of direct LLM-driven weight programming.

### Neural Program Compilation & Weight Generation

Learned compilers, hypernetworks, and adapter generators that map instructions or data to model parameters, plus program-to-weight compilers.

- **[CLAM]** `[Parametric Memory]` `[Recurrent Hypernetwork]` Instant Weight-Space Consolidation for Long-Term Memory in LLMs (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.20759)] — A trained recurrent hypernetwork compiles session activations into a carried LoRA memory, alongside an episodic buffer. Deployment uses no gradients; the generator requires per-base-model training.

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

Research on modifying facts or behaviors, parameter differences, symmetries, and learned weight representations.

- **[Tiny Gradient Loop Repair]** `[Gradient Baseline]` `[Looping Mechanism]` A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.33133)] — Sparse gradient edits and constant residual shifts complement a published WSP patch; a trained baseline, not gradient-free WSP. Gains depend strongly on decoding budget.

- **[Ethical-Priority Weight Edits]** `[Exploratory Control]` `[Exposed Trade-off Mechanism]` Can Weight-Space Programming Alter Learned Ethical Priorities? (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.24330)] — Hand-specified edits change fitted trade-offs in concept-supervised readers. The independent blinded editor has not run; this is not evidence of discovering ethical mechanisms in general LLMs.

- **[HypoLoop]** `[Feedback-driven Editing]` `[Numerical Solvers]` HypoLoop: Revising Weight-Editing Plans from Scientific Feedback (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.23718)] [[code](https://github.com/limengran98/HypoLoop)] ![GitHub stars](https://img.shields.io/github/stars/limengran98/HypoLoop.svg?logo=github&label=Stars) — Revises editable locations and fitting rules from sequential scientific feedback across 22 tasks. Patches are fitted by numerical solvers (including gradient-based optimization); related model editing, not gradient-free capability installation.

- **[SWEET]** `[Training-free Editing]` `[Mechanistic Localization]` SWEET: Mitigating Spurious Feature Reliance in LLM Reasoning via Weight Editing (**arXiv 2026**) [[paper](https://arxiv.org/abs/2611.10974)] — Uses counterfactual activation directions to localize and suppress spurious behavior; related mechanistic editing, not necessarily agent-authored programs.

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

### Fast Weights & Self-Modifying Networks

Dynamic parameter states and self-modification; distinguish online memory from persistent capability installation.

- **[BaseRSI]** `[Harness Internalization]` `[Closed-form Regression]` BaseRSI: Recursive Self-Improvement of a Base Vision-Language Model via Training-Free Harness Internalization (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2611.24578)] [[code](https://github.com/beita6969/BaseRSI)] ![GitHub stars](https://img.shields.io/github/stars/beita6969/BaseRSI.svg?logo=github&label=Stars) — ReGap/ReKey distill activation differences into selected neurons via regression and measured edit strength; distinguish this specified fitting rule from unrestricted agent-authored programs.

- **[AutoHebb]** `[Hebbian Plasticity]` `[Meta-learning]` AutoHebb: Self-Modifying Neural Networks that Zero-Shot Infer and Continually Learn (**arXiv preprint 2026**) [[paper](https://arxiv.org/abs/2610.40757)] — Meta-learned fixed weights control local Hebbian plasticity for online learning. This supplies a self-modification foundation rather than an LLM writing persistent edit programs.

- **[Learning to control fast-weight memories: An alternative to dynamic recurrent networks]** `[Historical Foundation]` Learning to control fast-weight memories: An alternative to dynamic recurrent networks (**Classic 1992**) [[paper](https://doi.org/10.1162/neco.1992.4.1.131)] — Early fast-weight controllers in which one network programs transient weights of another.

- **[A 'self-referential' weight matrix]** `[Historical Foundation]` A 'self-referential' weight matrix (**Classic 1993**) [[paper](https://doi.org/10.1007/978-1-4471-2063-6_107)] — Early explicit self-referential mechanisms for reading and modifying the network's own parameters.

- **[Using Fast Weights to Attend to the Recent Past]** `[Historical Foundation]` Using Fast Weights to Attend to the Recent Past (**Preprint 2016**) [[paper](https://arxiv.org/abs/1610.06258)] — Fast weights as transient associative memory; distinct from permanent capability installation.

- **[Linear Transformers Are Secretly Fast Weight Programmers]** `[Historical Foundation]` Linear Transformers Are Secretly Fast Weight Programmers (**Preprint 2021**) [[paper](https://arxiv.org/abs/2102.11174)] — Shows the formal relation between linear attention and fast-weight programming.

- **[A Modern Self-Referential Weight Matrix That Learns to Modify Itself]** `[Historical Foundation]` A Modern Self-Referential Weight Matrix That Learns to Modify Itself (**Preprint 2022**) [[paper](https://arxiv.org/abs/2202.05780)] — Explores networks with runtime self-modifying parameter state.

- **[Learning to (Learn at Test Time): RNNs with Expressive Hidden States]** `[Historical Foundation]` Learning to (Learn at Test Time): RNNs with Expressive Hidden States (**Preprint 2024**) [[paper](https://arxiv.org/abs/2407.04620)] — Test-time training treats part of a model as a learned, dynamically updated state.

### Historical Program-to-Weights & Rule Insertion

Earlier analytical and symbolic routes to specifying neural computations through weights.

- **[Neural networks and physical systems with emergent collective computational abilities]** `[Historical Foundation]` Neural networks and physical systems with emergent collective computational abilities (**Classic 1982**) [[paper](https://doi.org/10.1073/pnas.79.8.2554)] — Hopfield networks illustrate analytically constructed synaptic memories.

- **[Knowledge-based artificial neural networks]** `[Historical Foundation]` Knowledge-based artificial neural networks (**Classic 1994**) [[paper](https://doi.org/10.1016/0004-3702(94)90105-8)] — Compiles propositional prior rules into initial weights before gradient refinement.

- **[A neural compiler]** `[Historical Foundation]` A neural compiler (**Classic 1995**) [[paper](https://doi.org/10.1016/0304-3975(94)00200-3)] — Compiles high-level programs into network topology and weights.

### Cross-Domain Transfer & Weight-Difference Interpretation

Ideas from robotics and interpretability that may inform portable programs and capability tracing.

- **[Learning to Interpret Weight Differences in Language Models]** `[Historical Foundation]` Learning to Interpret Weight Differences in Language Models (**Preprint 2025**) [[paper](https://arxiv.org/abs/2510.05092)] — Trains Diff Interpretation Tuning to describe finetuning-induced weight changes; not direct WSP.

- **[Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts]** `[Historical Foundation]` Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts (**Preprint 2026**) [[paper](https://arxiv.org/abs/2607.00666)] — Uses weight-vector arithmetic with subspace alignment for VLA domain shifts.

- **[Robotic Policy Adaptation via Weight-Space Meta-Learning]** `[Historical Foundation]` Robotic Policy Adaptation via Weight-Space Meta-Learning (**Preprint 2026**) [[paper](https://arxiv.org/abs/2606.07217)] — A learned meta-network predicts adaptation weights for robot policies.
<!-- AUTO:END related -->

<a id="resources"></a>
## 🧰 Resources & Tools

<!-- AUTO:START resources -->
- **[WeightCode]** Executable programs, reproduction scripts, and an agent skill. [[code](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars)

- **[Weights-Only Replication]** Independent replication of selected MIT WSP weight-reading experiments, including reduced-context controls. [[code](https://github.com/jhpark94/weights-only-replication)] ![GitHub stars](https://img.shields.io/github/stars/jhpark94/weights-only-replication.svg?logo=github&label=Stars)

- **[MIT WSP Logs]** First-party experiment records for *Sparks of Weight-Space Programming*. [[code](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs.svg?logo=github&label=Stars)

- **[Edited Qwen3.5-0.8B]** Released checkpoint from the *Sparks* math-looping repair experiment, with an independent benchmark re-run on the model card. [[model](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)]

- **[WSP-Scope]** Code and experiments for systematic evaluation. [[code](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars)

- **[wsp-kit]** Independent toolkit for bounded edits; not a peer-reviewed paper. [[code](https://github.com/AuremHQ/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AuremHQ/weight-space-programming.svg?logo=github&label=Stars)
<!-- AUTO:END resources -->

### Related lists

- **[Awesome Weight Editing]** The umbrella list: five families of direct weight modification (knowledge editing, steering & abliteration, task arithmetic & merging, unlearning, WSP), bilingual, with a daily arXiv radar and a transactional toolkit ([modifyllm](https://github.com/vicfei/modifyllm)). [[code](https://github.com/vicfei/awesome-weight-editing)]

<a id="scope"></a>
## 🎯 Scope

- **Direct WSP:** weight reading, construction, editing, capability installation, program reuse, evaluation, and verification through reasoning agents or executable programs.
- **Related methods:** neural-program compilation, learned weight generators, model editing, weight merging, and weight-space representation learning when they clarify an important mechanism or comparison.
- **Weight-centric inspirations:** broader work on parameter geometry, representation, generation, structured manipulation, and continual retention when it offers a concrete, testable idea for future weight programming.
- **Usually out of scope:** generic PEFT and gradient-only adaptation without a clear connection to programmable weights.

<a id="inclusion-rules"></a>
## ✅ Inclusion Rules

- Prefer original research papers, first-party preprints and project pages, and official repositories.
- Clearly distinguish peer-reviewed papers, preprints, unpublished manuscripts, and technical blogs.
- Include substantive new methods, evaluations, benchmarks, and empirically grounded results; exclude unsupported conjecture-only proposals from the main curated catalog.
- Assign concise method/task tags rather than repeating the name of the whole field.
- Provide `[paper]`, `[preprint]`, `[code]`, and other primary-source links only when available; show star badges only for identifiable GitHub repositories.
- Keep closely related foundations separate from direct WSP, and avoid duplicate references.
- Feature work in **Start Here** only when it offers a useful methodological contribution and convincing task comparisons, preservation analysis, failure controls, or reproducible evidence. A paper's inclusion in the wider catalog is not an endorsement.

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
