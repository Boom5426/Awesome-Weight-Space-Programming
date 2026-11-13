<h1 align="center">Awesome Weight-Space Programming</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="https://github.com/Boom5426/Awesome-Weight-Space-Programming/stargazers"><img src="https://img.shields.io/github/stars/Boom5426/Awesome-Weight-Space-Programming?style=flat-square&logo=github&label=Stars" alt="GitHub stars" /></a>
  <a href="https://github.com/Boom5426/Awesome-Weight-Space-Programming/commits/main"><img src="https://img.shields.io/github/last-commit/Boom5426/Awesome-Weight-Space-Programming?style=flat-square&logo=github&label=Updated" alt="Last update" /></a>
</p>

<p align="center">
  <a href="README.md">English</a> | <b>简体中文</b>
</p>


**权重空间编程（Weight-Space Programming, WSP）** 研究语言模型及其他推理智能体如何借助可执行的流程，直接读取、构建和修改神经网络权重。本仓库跟踪直接的 WSP 研究，并把神经程序编译、超网络和成熟的模型编辑方法单独列为相关基础，与直接 WSP 明确区分。

> 论文标题保留英文原文，便于检索和引用。


<p align="center">
  <a href="https://boom5426.github.io/Awesome-Weight-Space-Programming/"><img src="https://img.shields.io/badge/Search_%26_Filter-Browse_Catalog-0B6E99?style=for-the-badge" alt="Search and filter Weight-Space Programming research" /></a>
  <a href="https://boom5426.github.io/Awesome-Weight-Space-Programming/landscape.html"><img src="https://img.shields.io/badge/Research_Landscape-Interactive_Map-24B6A6?style=for-the-badge" alt="Explore the interactive weight-space research map" /></a>
</p>

<p align="center">
  <sub>
    <a href="#start-here">从这里开始</a> ·
    <a href="#latest-updates">最近更新</a> ·
    <a href="#research-papers">直接 WSP</a> ·
    <a href="#weight-centric-inspirations">权重相关研究</a> ·
    <a href="docs/wsp-evidence.md">证据矩阵</a>
  </sub>
</p>

<a id="start-here"></a>
## 🚀 从这里开始

刚接触 WSP？先选一个研究问题。**加粗条目**是建议的入门起点，不代表影响力排名；发表状态请见下方完整列表。

| 目标 | 推荐入口 |
| --- | --- |
| 🧠 **理解直接 WSP** | **[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)** · [WSP-Scope](https://arxiv.org/abs/2611.09382) |
| 🛠️ **安装能力与反馈适应** | **[WeightCode](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)** · [WeightLoop](https://arxiv.org/abs/2611.07319) |
| 📏 **评测权重理解与编辑** | **[IWIBench](https://arxiv.org/abs/2611.08647)** · [WSP-Scope](https://arxiv.org/abs/2611.09382) · [Weight Oracles](https://arxiv.org/abs/2610.07334) · [Orbit Audits](https://arxiv.org/abs/2611.05798) · [Clinical Network Audits](https://arxiv.org/abs/2611.05341) |
| 🧬 **生成权重与网络** | **[Physics2Weight](https://arxiv.org/abs/2611.12954)** · [Medical Imaging WSP](https://arxiv.org/abs/2611.12066) · [Game Policies](https://arxiv.org/abs/2611.09271) |
| ✅ **构建可验证的干预** | **[W-ISA](https://arxiv.org/abs/2611.13232)** · [NCP](https://arxiv.org/abs/2611.13236) · [Policy Model Checking](https://arxiv.org/abs/2611.11604) |
| 🧭 **探索权重相关研究** | **[权重相关研究](docs/weight-centric-research_zh.md)** · [English](docs/weight-centric-research.md) |
| 🔗 **了解相邻范式** | **[Program-as-Weights](https://arxiv.org/abs/2607.02512)** · [Tracr](https://arxiv.org/abs/2301.05062) · [Doc-to-LoRA](https://arxiv.org/abs/2602.15902) · [Text-to-LoRA](https://arxiv.org/abs/2506.06105) |

<a id="latest-updates"></a>
## 📰 最近更新

<!-- AUTO:START updates -->
| 日期 | 更新内容 |
| --- | --- |
| `2026-11-13` | 优化交互式研究图谱与检索页面：支持中文检索、准确的分支导航、移动端目录和分页浏览。 |
| `2026-11-13` | 引入结构化双语文献库、自动校验与证据字段，并补充早期权重编程基础和机器人策略编辑研究。 |
| `2026-11-13` | **权重相关研究**扩充至 **67 篇**，覆盖六条研究线，并补充综述和评估资源。 |
<!-- AUTO:END updates -->

<a id="research-papers"></a>
## 🔬 研究论文

<!-- AUTO:START direct -->
直接通过程序读取、构建或修改神经网络权重的研究，并标注方法与任务属性。

**19 篇论文与手稿** · [2026（19）](#2026)

**证据整理：** [WSP 证据矩阵](docs/wsp-evidence.md)

<a id="2026"></a>
### 🗓️ 2026 — 19 篇

- **[WeightCode]** `[能力植入]` `[程序复用]` WeightCode: Installing New Capabilities into Neural Networks via Weight Programming（**手稿 2026**）[[论文](https://github.com/Gen-Verse/WeightCode/blob/main/assets/WeightCode.pdf)] [[代码](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars)

- **[Mixed Signals]** `[生物信号]` `[模型构建]` Mixed Signals: Weight-Space Programming for EEG and ECG（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.13758)] [[项目](https://daravaram.github.io/)]

- **[NCP]** `[验证]` `[控制]` NCP: Verifier-Guided Optimization of Weight-Space Control Policies（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.13236)]

- **[W-ISA]** `[运行时]` `[事务式编辑]` W-ISA: Transactional Execution of Weight-Space Intervention Programs（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.13232)]

- **[Physics2Weight]** `[科学智能]` `[PDE 求解]` Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.12954)]

- **[WSP for Medical Imaging]** `[医学影像]` `[模型构建]` Weight-Space Programming for Medical Imaging: Do We Still Need Training Data?（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.12066)] [[代码](https://github.com/MaximilianLindholz/weight-space-programming-medical)] ![GitHub stars](https://img.shields.io/github/stars/MaximilianLindholz/weight-space-programming-medical.svg?logo=github&label=Stars)

- **[WSP for Policies]** `[策略合成]` `[形式化验证]` Weight-Space Programming of Policies and Their Verification via Model Checking（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.11604)]

- **[WSP for Quantum Circuits]** `[量子计算]` `[参数合成]` Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.11537)]

- **[WSP for Mathematical Optimization]** `[运筹优化]` `[打分网络]` Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.09559)]

- **[WSP-Scope]** `[基准评测]` `[LLM 编辑]` Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.09382)] [[代码](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars) [[项目](https://wsp-scope.github.io/)]

- **[Zero-Shot Game WSP]** `[博弈游戏]` `[策略合成]` Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.09271)]

- **[Can an LLM Actually Reason about Weights?]** `[权重读取]` `[可靠性]` Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.08070)]

- **[IWIBench]** `[基准评测]` `[权重内注入]` IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.08647)] [[代码](https://github.com/hcltech-robotics/iwibench)] ![GitHub stars](https://img.shields.io/github/stars/hcltech-robotics/iwibench.svg?logo=github&label=Stars)

- **[WeightLoop]** `[实验反馈]` `[持续适应]` WeightLoop: Weight-Space Programming with Experimental Feedback（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.07319)]

- **[Orbit Audits]** `[权重读取]` `[对称性]` Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.05798)]

- **[Clinical Network Audits]** `[临床 AI]` `[审计与修复]` Weight-space programming for auditing clinical decision networks（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.05341)] [[代码](https://github.com/hnusrat1/weightspace-rt)] ![GitHub stars](https://img.shields.io/github/stars/hnusrat1/weightspace-rt.svg?logo=github&label=Stars)

- **[Diffusion WSP Conjectures]** `[扩散模型]` `[猜想]` Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop（**猜想性 arXiv 预印本 2026**）[[论文](https://arxiv.org/abs/2611.04268)]

- **[Robot Policy Debugging]** `[机器人基础模型]` `[词汇修复]` Can LLMs Debug Robots by Editing Their Weights?（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.09376)]

- **[Instruction Distillation]** `[机器人策略]` `[闭式编辑]` Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.11894)]
<!-- AUTO:END direct -->

<a id="reports-and-blogs"></a>
## 📝 报告与博客

<!-- AUTO:START reports -->
- **[Fable WSP Replication]** `[复现]` `[跨模型对比]` Claude Fable 5.2 can do "weight-space-programming" about as well as GPT-6 Astra（**LessWrong 帖子 2026**）[[帖子](https://www.lesswrong.com/posts/wg3K6xFFTdM6RmRgn/claude-fable-5-2-can-do-weight-space-programming-about-as)] [[数据](https://huggingface.co/datasets/shawnghu/fable-weight-space-programming)]

- **[Gradient-Free Diffusion Weight Editing]** `[LLM 编辑]` `[概念擦除]` An LLM Erases a Concept by Editing Diffusion Weights Directly, Without Gradients（**alphaXiv 研究报告 2026**）[[报告](https://www.alphaxiv.org/abs/2611.gradient-free-diffusion-weight-editing)] [[博客](https://huggingface.co/blog/javadtaghia/an-llm-erases-a-concept-by-editing-diffusion-weigh)]

- **[Sycophancy Repair by Weight Editing]** `[直接编辑]` `[迎合行为]` `[预注册]` Repairing sycophancy in Qwen2.5-0.5B by editing its weights, with Claude Opus 5.5 as the editor and a blind test split（**技术博客 2026**）[[博客](https://say43.github.io/2026/11/05/repairing-sycophancy.html)] [[代码](https://github.com/Say43/Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/Say43/Weight-Space-Programming.svg?logo=github&label=Stars)

- **[Evidence-Scope Critique]** `[批评]` `[证据范围]` The 'Astra can read and write weights to improve Qwen' post is misleading（**技术博客 2026**）[[博客](https://honnibal.dev/blog/astra-read-write-misleading)]

- **[WSP Autoresearch]** `[自主研究]` `[手写 Transformer]` Weight-Space Programming Autoresearch：智能体为算术、算法和 NLP 任务手写 Transformer 权重（**技术报告 2026**）[[报告](https://csinva.io/weight-space-programming-autoresearch/analyze)] [[代码](https://github.com/csinva/weight-space-programming-autoresearch)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch.svg?logo=github&label=Stars)

- **[Sparks of Weight-Space Programming]** `[权重读取]` `[直接编辑]` Sparks of Weight-Space Programming: LLMs Can Natively Read & Write Neural Network Weights（**技术博客 2026**）[[博客](https://rikiyat.github.io/blog/weight-space-programming/)] [[日志](https://github.com/RikiyaT/lm_understand-logs)]

- **[Independent Edit Composition]** `[独立复现]` `[组合]` Independently Discovered Weight Edits Compose: A Replication and Extension of Weight-Space Programming（**GitHub 报告 2026**）[[代码](https://github.com/ajaygrover/weight-space-programming-stacking)]

- **[Robot VLA Weight Editing]** `[机器人策略]` `[直接编辑]` Opus 5.5 makes π0.5 move faster and smoother by editing its weights（**技术报告 2026**）[[代码](https://github.com/Cuzyoung/robotics-weight-editing)]

- **[Policy Surgery]** `[强化学习控制]` `[权重编辑]` Policy Surgery：对已有控制策略进行程序化权重修复（**GitHub 项目 2026**）[[代码](https://github.com/latentpaths/policy-surgery)]
<!-- AUTO:END reports -->

<a id="weight-centric-inspirations"></a>
## 🧭 权重相关研究：超越编辑的灵感来源

未来的权重编程不必只从模型编辑论文中寻找灵感。新增的 **[权重相关研究](docs/weight-centric-research_zh.md)** 系列把权重作为可理解、可表征、可生成、可组合和可保护的对象。这些论文提供**方法启发与比较基线**，不等于直接 WSP。

**现收录 67 篇，分成六条研究线：**

| 研究线 | 关键问题 |
| --- | --- |
| 权重几何与对称性 | 等价参数化的网络如何比较、对齐与迁移计算？ |
| 权重读取与表征 | 不依赖原任务数据，能从权重中读出什么？ |
| 权重生成与合成 | 能否直接生成可用的网络或参数子块？ |
| 权重算术与合并 | 多次参数更新如何组合、为何相互干扰？ |
| 结构化参数与机制定位 | 应该修改哪些权重方向、神经元或子空间？ |
| 持续能力积累与保护 | 如何引入新能力而不破坏已有能力？ |

[**进入中文阅读系列**](docs/weight-centric-research_zh.md) · [English](docs/weight-centric-research.md)

<a id="related-research"></a>
## 🔗 相关研究

<!-- AUTO:START related -->
这些相邻方法可启发权重编程，但不应自动归类为由大模型直接完成的权重空间编程。

### 神经程序编译与权重生成

学习型编译器、超网络和适配器生成器，以及将程序直接编译为网络参数的方法。

- **[Adapters as Data]** `[LoRA]` `[权重表征]` Adapters as Data: The Latent Space of LoRAs（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.07775)]

- **[SkillSmith]** `[参数化技能合成]` `[前缀微调]` SkillSmith: Learning to Compose Parametric Skills and Textual Knowledge（**arXiv 2026**）[[论文](https://arxiv.org/abs/2607.27497)]

- **[Program-as-Weights]** `[神经编译器]` `[可复用程序]` Program-as-Weights: A Programming Paradigm for Fuzzy Functions（**NeurIPS 2026**）[[论文](https://arxiv.org/abs/2607.02512)] [[代码](https://github.com/programasweights/programasweights-python)] ![GitHub stars](https://img.shields.io/github/stars/programasweights/programasweights-python.svg?logo=github&label=Stars) [[项目](https://programasweights.com/research/)]

- **[Compile by Training]** `[神经编译器]` `[适配器训练]` Compile by Training: Turning Natural-Language Specifications into Local Neural Functions（**EMNLP 2026 System Demonstrations**）[[论文](https://aclanthology.org/2026.emnlp-demos.78/)] [[预印本](https://arxiv.org/abs/2609.04199)] [[代码](https://github.com/programasweights/compile-by-training)] ![GitHub stars](https://img.shields.io/github/stars/programasweights/compile-by-training.svg?logo=github&label=Stars)

- **[Infinite-Parameter LLMs]** `[超网络]` `[在线适应]` Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data（**arXiv 2026**）[[论文](https://arxiv.org/abs/2609.18842)]

- **[DISC]** `[超网络]` `[策略生成]` DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation（**RSS 2026**）[[论文](https://arxiv.org/abs/2605.20856)] [[代码](https://github.com/ReNginx/DISC)] ![GitHub stars](https://img.shields.io/github/stars/ReNginx/DISC.svg?logo=github&label=Stars)

- **[Doc-to-LoRA]** `[超网络]` `[上下文内化]` Doc-to-LoRA: Learning to Instantly Internalize Contexts（**ICML 2026**）[[论文](https://proceedings.mlr.press/v306/charakorn26a.html)] [[预印本](https://arxiv.org/abs/2602.15902)] [[代码](https://github.com/SakanaAI/doc-to-lora)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/doc-to-lora.svg?logo=github&label=Stars)

- **[Text-to-LoRA]** `[超网络]` `[任务适应]` Text-to-LoRA: Instant Transformer Adaption（**ICML 2025**）[[论文](https://proceedings.mlr.press/v267/charakorn25a.html)] [[预印本](https://arxiv.org/abs/2506.06105)] [[代码](https://github.com/SakanaAI/text-to-lora)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/text-to-lora.svg?logo=github&label=Stars)

- **[Neural Programs in Weight Space]** `[程序合成]` `[元学习]` End-to-End Synthesis of Neural Programs in Weight Space（**ICLR 2025 Workshop on Neural Network Weights as a New Data Modality**）[[论文](https://openreview.net/forum?id=tzf3XUg0Q5)]

- **[Learning Transformer Programs]** `[可解释设计]` `[程序提取]` Learning Transformer Programs（**NeurIPS 2023**）[[论文](https://arxiv.org/abs/2306.01128)] [[代码](https://github.com/princeton-nlp/TransformerPrograms)] ![GitHub stars](https://img.shields.io/github/stars/princeton-nlp/TransformerPrograms.svg?logo=github&label=Stars)

- **[Tracr]** `[程序编译]` `[手工构造权重]` Tracr: Compiled Transformers as a Laboratory for Interpretability（**NeurIPS 2023**）[[论文](https://arxiv.org/abs/2301.05062)] [[代码](https://github.com/google-deepmind/tracr)] ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/tracr.svg?logo=github&label=Stars)

- **[PPUDA]** `[参数预测]` `[图超网络]` Parameter Prediction for Unseen Deep Architectures（**NeurIPS 2021**）[[论文](https://arxiv.org/abs/2110.13100)] [[代码](https://github.com/facebookresearch/ppuda)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/ppuda.svg?logo=github&label=Stars)

- **[RASP]** `[编程语言]` `[Transformer 计算]` Thinking Like Transformers（**ICML 2021**）[[论文](https://arxiv.org/abs/2106.06981)] [[代码](https://github.com/tech-srl/RASP)] ![GitHub stars](https://img.shields.io/github/stars/tech-srl/RASP.svg?logo=github&label=Stars)

### 模型编辑与权重空间基础

研究知识与行为修改、参数增量复用、对称性以及网络权重表征。

- **[Tree-Ising]** `[免训练编辑]` `[离散优化]` Tree-Ising: Repairing Language Models with Bit-Level Ising Edits（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.14210)]

- **[A Survey of Weight Space Learning]** `[综述]` `[权重空间学习]` A Survey of Weight Space Learning: Understanding, Representation, and Generation（**arXiv 2026**）[[论文](https://arxiv.org/abs/2603.10090)] [[代码](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning)] ![GitHub stars](https://img.shields.io/github/stars/Zehong-Wang/Awesome-Weight-Space-Learning.svg?logo=github&label=Stars)

- **[TensorMutation]** `[权重空间学习]` `[模型变异]` TensorMutation: Learning Weight-Space Mutations of Deep Learning Models on Neural Graphs（**arXiv 2026**）[[论文](https://arxiv.org/abs/2611.09650)]

- **[Weight Oracles]** `[权重读取]` `[安全审计]` Weight Oracles: Reading Neural Network Weights with Language Models（**arXiv 2026；NeurIPS 2026 NeuralArtifacts Workshop Spotlight**）[[论文](https://arxiv.org/abs/2610.07334)]

- **[Targeted Parameter Decomposition]** `[机制恢复]` `[定向重连]` Targeted Recovery of Weight-Space Mechanisms From Neural Networks（**ICML 2026 Mechanistic Interpretability Workshop**）[[论文](https://arxiv.org/abs/2607.13047)] [[代码](https://github.com/Antovigo/targeted-parameter-decomposition)] ![GitHub stars](https://img.shields.io/github/stars/Antovigo/targeted-parameter-decomposition.svg?logo=github&label=Stars)

- **[Weight Space as a Modality]** `[立场论文]` `[权重生成]` Position: Weight Space Should Be a First-Class Generative AI Modality（**ICML 2026**）[[论文](https://arxiv.org/abs/2605.18632)]

- **[AlphaEdit]** `[模型编辑]` `[知识保持]` AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models（**ICLR 2025**）[[论文](https://arxiv.org/abs/2410.02355)] [[代码](https://github.com/jianghoucheng/AlphaEdit)] ![GitHub stars](https://img.shields.io/github/stars/jianghoucheng/AlphaEdit.svg?logo=github&label=Stars)

- **[Refusal Direction]** `[权重正交化]` `[行为编辑]` Refusal in Language Models Is Mediated by a Single Direction（**NeurIPS 2024**）[[论文](https://arxiv.org/abs/2406.11717)] [[代码](https://github.com/andyrdt/refusal_direction)] ![GitHub stars](https://img.shields.io/github/stars/andyrdt/refusal_direction.svg?logo=github&label=Stars)

- **[WISE]** `[终身编辑]` `[知识记忆]` WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models（**arXiv 2024**）[[论文](https://arxiv.org/abs/2405.14768)] [[代码](https://github.com/zjunlp/EasyEdit)] ![GitHub stars](https://img.shields.io/github/stars/zjunlp/EasyEdit.svg?logo=github&label=Stars)

- **[Deep Weight Space Alignment]** `[权重对齐]` `[等变网络]` Equivariant Deep Weight Space Alignment（**ICML 2024**）[[论文](https://arxiv.org/abs/2310.13397)] [[代码](https://github.com/AvivNavon/deep-align)] ![GitHub stars](https://img.shields.io/github/stars/AvivNavon/deep-align.svg?logo=github&label=Stars)

- **[Neural Functional Transformers]** `[权重空间学习]` `[置换对称性]` Neural Functional Transformers（**NeurIPS 2023**）[[论文](https://papers.neurips.cc/paper_files/paper/2023/hash/f4757db82a02eea015670ecca605d5cc-Abstract-Conference.html)] [[代码](https://github.com/AllanYangZhou/nfn)] ![GitHub stars](https://img.shields.io/github/stars/AllanYangZhou/nfn.svg?logo=github&label=Stars)

- **[NFN]** `[权重空间学习]` `[置换等变]` Permutation Equivariant Neural Functionals（**NeurIPS 2023**）[[论文](https://arxiv.org/abs/2302.14040)] [[代码](https://github.com/AllanYangZhou/nfn)] ![GitHub stars](https://img.shields.io/github/stars/AllanYangZhou/nfn.svg?logo=github&label=Stars)

- **[DWSNets]** `[权重空间学习]` `[等变网络]` Equivariant Architectures for Learning in Deep Weight Spaces（**ICML 2023**）[[论文](https://arxiv.org/abs/2301.12780)] [[代码](https://github.com/AvivNavon/DWSNets)] ![GitHub stars](https://img.shields.io/github/stars/AvivNavon/DWSNets.svg?logo=github&label=Stars)

- **[Git Re-Basin]** `[权重对齐]` `[模型合并]` Git Re-Basin: Merging Models Modulo Permutation Symmetries（**ICLR 2023**）[[论文](https://arxiv.org/abs/2209.04836)] [[代码](https://github.com/samuela/git-re-basin)] ![GitHub stars](https://img.shields.io/github/stars/samuela/git-re-basin.svg?logo=github&label=Stars)

- **[Task Arithmetic]** `[任务向量]` `[模型合并]` Editing Models with Task Arithmetic（**ICLR 2023**）[[论文](https://arxiv.org/abs/2212.04089)] [[代码](https://github.com/mlfoundations/task_vectors)] ![GitHub stars](https://img.shields.io/github/stars/mlfoundations/task_vectors.svg?logo=github&label=Stars)

- **[MEMIT]** `[知识编辑]` `[批量编辑]` Mass-Editing Memory in a Transformer（**ICLR 2023**）[[论文](https://arxiv.org/abs/2210.07229)] [[代码](https://github.com/kmeng01/memit)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/memit.svg?logo=github&label=Stars)

- **[ROME]** `[知识编辑]` `[因果追踪]` Locating and Editing Factual Associations in GPT（**NeurIPS 2022**）[[论文](https://arxiv.org/abs/2202.05262)] [[代码](https://github.com/kmeng01/rome)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/rome.svg?logo=github&label=Stars)

- **[Transformer Circuits Framework]** `[机制可解释性]` `[权重读取]` A Mathematical Framework for Transformer Circuits（**Transformer Circuits Thread 2021**）[[文章](https://transformer-circuits.pub/2021/framework/index.html)]

- **[HyperNetworks]** `[超网络]` `[权重生成]` HyperNetworks（**ICLR 2017**）[[论文](https://research.google/pubs/hypernetworks-2/)]

### 快速权重与自修改网络

关注动态参数状态和自修改机制，区分在线临时记忆与持久能力安装。

- **[Learning to control fast-weight memories: An alternative to dynamic recurrent networks]** `[历史基础]` Learning to control fast-weight memories: An alternative to dynamic recurrent networks（**经典研究 1992**）[[论文](https://doi.org/10.1162/neco.1992.4.1.131)] — 早期 Fast Weight 控制器：一个网络在线编程另一个网络的临时权重。

- **[A 'self-referential' weight matrix]** `[历史基础]` A 'self-referential' weight matrix（**经典研究 1993**）[[论文](https://doi.org/10.1007/978-1-4471-2063-6_107)] — 提出读取并修改网络自身参数的早期自指机制。

- **[Using Fast Weights to Attend to the Recent Past]** `[历史基础]` Using Fast Weights to Attend to the Recent Past（**预印本 2016**）[[论文](https://arxiv.org/abs/1610.06258)] — 将快速权重用作短期联想记忆，不等同于持久能力安装。

- **[Linear Transformers Are Secretly Fast Weight Programmers]** `[历史基础]` Linear Transformers Are Secretly Fast Weight Programmers（**预印本 2021**）[[论文](https://arxiv.org/abs/2102.11174)] — 揭示线性注意力与快速权重编程的形式关系。

- **[A Modern Self-Referential Weight Matrix That Learns to Modify Itself]** `[历史基础]` A Modern Self-Referential Weight Matrix That Learns to Modify Itself（**预印本 2022**）[[论文](https://arxiv.org/abs/2202.05780)] — 探索运行时能修改自身参数状态的网络结构。

- **[Learning to (Learn at Test Time): RNNs with Expressive Hidden States]** `[历史基础]` Learning to (Learn at Test Time): RNNs with Expressive Hidden States（**预印本 2024**）[[论文](https://arxiv.org/abs/2407.04620)] — 把网络组件当作测试时动态更新的状态；应与持久编辑区分。

### 早期程序到权重编译与规则植入

追溯解析构造与符号规则转化为神经网络计算的历史路径。

- **[Neural networks and physical systems with emergent collective computational abilities]** `[历史基础]` Neural networks and physical systems with emergent collective computational abilities（**经典研究 1982**）[[论文](https://doi.org/10.1073/pnas.79.8.2554)] — Hopfield 网络展示由解析规则构造的联想记忆权重。

- **[Knowledge-based artificial neural networks]** `[历史基础]` Knowledge-based artificial neural networks（**经典研究 1994**）[[论文](https://doi.org/10.1016/0004-3702(94)90105-8)] — 先将命题规则编译进初始权重，再利用梯度优化完善。

- **[A neural compiler]** `[历史基础]` A neural compiler（**经典研究 1995**）[[论文](https://doi.org/10.1016/0304-3975(94)00200-3)] — 把高级程序编译成网络拓扑与参数。

### 跨领域迁移与权重变化解释

借鉴机器人与可解释性研究，支持程序跨模型复用和能力变化追踪。

- **[Learning to Interpret Weight Differences in Language Models]** `[历史基础]` Learning to Interpret Weight Differences in Language Models（**预印本 2025**）[[论文](https://arxiv.org/abs/2510.05092)] — 训练 Diff Interpretation Tuning 描述微调产生的权重变化，不是直接 WSP。

- **[Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts]** `[历史基础]` Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts（**预印本 2026**）[[论文](https://arxiv.org/abs/2607.00666)] — 利用带子空间对齐的权重向量算术实现 VLA 领域适应。

- **[Robotic Policy Adaptation via Weight-Space Meta-Learning]** `[历史基础]` Robotic Policy Adaptation via Weight-Space Meta-Learning（**预印本 2026**）[[论文](https://arxiv.org/abs/2606.07217)] — 学习型元网络为机器人策略生成适应性权重。
<!-- AUTO:END related -->

<a id="resources"></a>
## 🧰 资源与工具

<!-- AUTO:START resources -->
- **[WeightCode]** 可执行程序、复现脚本和一个智能体技能（agent skill）。[[代码](https://github.com/Gen-Verse/WeightCode)] ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/WeightCode.svg?logo=github&label=Stars)

- **[Weights-Only Replication]** 对 MIT WSP 部分权重读取实验的独立复现，包含缩减上下文的对照实验。[[代码](https://github.com/jhpark94/weights-only-replication)] ![GitHub stars](https://img.shields.io/github/stars/jhpark94/weights-only-replication.svg?logo=github&label=Stars)

- **[MIT WSP Logs]** *Sparks of Weight-Space Programming* 的一手实验记录。[[代码](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs.svg?logo=github&label=Stars)

- **[Edited Qwen3.5-0.8B]** *Sparks* 中数学推理死循环修复实验发布的检查点，模型卡附有独立的基准重测结果。[[模型](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)]

- **[WSP-Scope]** 系统性评测的代码与实验。[[代码](https://github.com/WSP-Scope/WSP-Scope-Project)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project.svg?logo=github&label=Stars)

- **[wsp-kit]** 用于有界编辑的独立工具包；并非同行评审论文。[[代码](https://github.com/AuremHQ/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AuremHQ/weight-space-programming.svg?logo=github&label=Stars)
<!-- AUTO:END resources -->

<a id="scope"></a>
## 🎯 收录范围

- **直接 WSP：** 通过推理智能体或可执行程序进行的权重读取、构建、编辑、能力植入、程序复用、评测与验证。
- **相关方法：** 神经程序编译、学习型权重生成器、模型编辑、权重合并和权重空间表征学习——前提是它们有助于阐明重要机制或提供对比。
- **权重相关研究系列：** 权重几何、表征、生成、结构化操作与持续能力保护等方向，只要能为未来的权重编程提供具体、可检验的启发。
- **通常不收录：** 与可编程权重没有明确联系的通用 PEFT 和纯梯度适应方法。

<a id="inclusion-rules"></a>
## ✅ 收录规则

- 优先收录原始研究论文、作者一手的预印本与项目主页，以及官方代码仓库。
- 明确区分同行评审论文、预印本、未发表手稿和技术博客。
- 收录有实质贡献的新方法、评测、基准和有实证支撑的结果；猜想性工作需明确标注。
- 使用简洁的方法 / 任务标签，不重复整个领域的名称。
- 仅在确实存在时提供 `[论文]`、`[预印本]`、`[代码]` 等一手来源链接；只为可识别的 GitHub 仓库显示 star 徽章。
- 将密切相关的基础工作与直接 WSP 分开列出，避免重复引用。

<a id="contributing"></a>
## 🤝 参与贡献

欢迎补充和勘误。请提交 [Issue](https://github.com/Boom5426/Awesome-Weight-Space-Programming/issues) 或 [Pull Request](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pulls)，并附上完整标题、论文一手链接、首次公开日期、发表状态、已核实的代码 / 项目链接，以及一段简短的相关性说明。

<a id="star-history"></a>
## ⭐ Star 历史

<p align="center">
  <a href="https://star-history.com/#Boom5426/Awesome-Weight-Space-Programming&Date">
    <img src="https://api.star-history.com/svg?repos=Boom5426/Awesome-Weight-Space-Programming&type=Date" alt="Star History Chart" />
  </a>
</p>
