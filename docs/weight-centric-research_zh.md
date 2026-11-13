# 权重相关研究：超越编辑的灵感来源

**[Awesome Weight-Space Programming](../README_zh.md) 的独立阅读系列。** 权重编程的灵感不必只来自模型编辑论文。这里把神经网络权重视为可以被**理解、表征、生成、组合、定位和保护**的结构化对象。收录的研究用于提供未来的设计思路和对照，**不代表它们本身属于直接权重空间编程（WSP）**。

**收录标准：** 能够为权重读取或写入、跨模型计算迁移、多次更新的组合、旧能力保留等问题提供具体、可验证的思路。没有明确关联的一般微调、压缩与优化工作不纳入。下文的“潜在启发”是研究假设，不是已得到验证的 WSP 结论。

**首批收录：** 21 篇论文，6 条研究线。已在[主仓库相关工作](../README_zh.md#related-research)收录的论文不在此重复列出。

## 阅读路线

| 研究线 | 面向未来权重编程的关键问题 |
| --- | --- |
| [权重几何、对称性与连通性](#wcr-geometry) | 什么时候直接比较参数会产生误导？不同检查点何时可以安全组合？ |
| [权重作为数据：读取与表征](#wcr-reading) | 不运行原任务，仅靠参数能读出模型的哪些性质？ |
| [权重生成与合成](#wcr-generation) | 能否把网络作为可生成的对象，而不是每个任务都重新优化？ |
| [权重算术、合并与干扰](#wcr-composition) | 多个参数变化如何组合，才能避免破坏已有能力？ |
| [结构化参数、稀疏性与机制定位](#wcr-structure) | 程序究竟该改哪些参数、方向或子网络？ |
| [持续能力积累与旧能力保护](#wcr-retention) | 新能力应写到哪里？连续更新后哪些旧能力必须保持？ |

<a id="wcr-geometry"></a>
## 权重几何、对称性与连通性

*什么时候直接比较参数会产生误导？不同检查点何时可以安全组合？*

- **[Linear Mode Connectivity and the Lottery Ticket Hypothesis](https://arxiv.org/abs/1912.05671)**（ICML 2020）。**核心思路：**研究 SGD 解的稳定性及线性连通区域。 **对未来权重编程的启发：**判断编辑是否依赖当前网络所在的解空间区域与稳定性。

- **[The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks](https://arxiv.org/abs/2110.06296)**（2021 preprint）。**核心思路：**研究神经元置换对两个训练解之间连通性的影响。 **对未来权重编程的启发：**跨网络读取和复用权重程序时，不能把原始坐标当作稳定语义。

- **[Interpreting the Weight Space of Customized Diffusion Models](https://papers.nips.cc/paper_files/paper/2024/hash/f85364507054c257959c2011c28bfc0d-Abstract-Conference.html)**（NeurIPS 2024）。**核心思路：**在定制扩散模型的权重子空间中发现可解释的语义方向。 **对未来权重编程的启发：**探索能力变化能否表示为可理解、可复用的权重方向。

<a id="wcr-reading"></a>
## 权重作为数据：读取与表征

*不运行原任务，仅靠参数能读出模型的哪些性质？*

- **[Predicting Neural Network Accuracy from Weights](https://arxiv.org/abs/2002.11448)**（2020 preprint）。**核心思路：**从参数统计量预测模型精度，不需要执行原任务。 **对未来权重编程的启发：**为纯权重读取提供可检验的先例，但跨模型泛化仍需验证。

- **[Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction](https://arxiv.org/abs/2110.15288)**（NeurIPS 2021）。**核心思路：**从多个已训练网络的参数中学习模型级表征。 **对未来权重编程的启发：**可能为编辑位置检索与网络画像提供比原始张量更合适的输入。

- **[Hyper-Representations as Generative Models: Sampling Unseen Neural Network Weights](https://arxiv.org/abs/2209.14733)**（NeurIPS 2022）。**核心思路：**利用学习到的权重表征生成新的网络参数。 **对未来权重编程的启发：**启发从模型群体中提炼可复用先验；它属于训练式生成器，而不是直接 WSP。

<a id="wcr-generation"></a>
## 权重生成与合成

*能否把网络作为可生成的对象，而不是每个任务都重新优化？*

- **[HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://arxiv.org/abs/2303.17015)**（2023 preprint）。**核心思路：**在隐式神经场的 MLP 权重空间训练扩散生成模型。 **对未来权重编程的启发：**可以考虑用生成先验约束编辑，使修改更可能落在有效的功能区域。

- **[Neural Network Diffusion](https://arxiv.org/abs/2402.13144)**（2024 preprint）。**核心思路：**用潜在扩散模型合成性能较好的参数子集。 **对未来权重编程的启发：**启发基于参数先验生成或修复局部权重块。

- **[NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://proceedings.mlr.press/v306/kim26ay.html)**（ICML 2026）。**核心思路：**通过结构对齐，在不同宽度的网络间生成权重。 **对未来权重编程的启发：**为跨宽度、跨参数化的可移植权重程序提供设计参考。

<a id="wcr-composition"></a>
## 权重算术、合并与干扰

*多个参数变化如何组合，才能避免破坏已有能力？*

- **[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482)**（ICML 2022）。**核心思路：**通过平均兼容的微调检查点来组合模型。 **对未来权重编程的启发：**是权重组合的简单基线，也提示模型兼容性不可忽视。

- **[TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)**（NeurIPS 2023）。**核心思路：**处理多个参数增量之间的冗余修改和符号冲突。 **对未来权重编程的启发：**多程序安装不能简单叠加增量，应显式识别相互干扰。

- **[Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099)**（ICML 2024）。**核心思路：**提出 DARE，对微调增量随机丢弃和重缩放后再合并。 **对未来权重编程的启发：**提示能力增量可能有较强冗余，但稀疏增量并不等于可执行程序。

- **[AdaMerging: Adaptive Model Merging for Multi-Task Learning](https://arxiv.org/abs/2310.02575)**（2023 preprint）。**核心思路：**借助无监督目标自适应学习任务级或层级的合并系数。 **对未来权重编程的启发：**启发在连续编辑冲突时，采用任务或层级相关的组合策略。

<a id="wcr-structure"></a>
## 结构化参数、稀疏性与机制定位

*程序究竟该改哪些参数、方向或子网络？*

- **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)**（ICLR 2019）。**核心思路：**在大网络中寻找具有训练潜力的稀疏子网络。 **对未来权重编程的启发：**启发研究新能力能否安装在受限的计算子结构中。

- **[Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)**（2021 preprint）。**核心思路：**通过归因定位与特定事实知识相关的神经元。 **对未来权重编程的启发：**提供由行为定位编辑位置的路径，但仍需因果验证。

- **[DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353)**（ICML 2024）。**核心思路：**将权重分解为幅值和方向以进行适应。 **对未来权重编程的启发：**启发在编写局部参数更新时区分幅值变化与方向变化。

- **[PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://arxiv.org/abs/2404.02948)**（NeurIPS 2024）。**核心思路：**利用预训练权重矩阵的主要奇异分量构造适应空间。 **对未来权重编程的启发：**启发依据矩阵结构选择编辑子空间，而非任意参数坐标。

<a id="wcr-retention"></a>
## 持续能力积累与旧能力保护

*新能力应写到哪里？连续更新后哪些旧能力必须保持？*

- **[Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796)**（PNAS 2017）。**核心思路：**通过保护对旧任务重要的参数来缓解遗忘（EWC）。 **对未来权重编程的启发：**启发估计旧能力的参数足迹，并在编辑中进行保护。

- **[Progressive Neural Networks](https://arxiv.org/abs/1606.04671)**（2016 preprint）。**核心思路：**保留旧网络列，并通过新增网络列与侧向连接学习新任务。 **对未来权重编程的启发：**与原位编辑形成对照：隔离可保护旧能力，但会增加容量成本。

- **[PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning](https://arxiv.org/abs/1711.05769)**（CVPR 2018）。**核心思路：**通过迭代剪枝释放参数空间，依次容纳多个任务。 **对未来权重编程的启发：**启发对多次安装过程中的剩余容量和参数占用进行追踪。

- **[Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights](https://arxiv.org/abs/1801.06519)**（ECCV 2018）。**核心思路：**在固定基础权重上学习任务专属的二值掩码。 **对未来权重编程的启发：**为条件化激活新能力与保留旧能力提供非破坏式对照。

## 与主仓库已有文献的关联

- **读取与对齐：** 主目录已收录 [Neural Functional Transformers](https://papers.neurips.cc/paper_files/paper/2023/hash/f4757db82a02eea015670ecca605d5cc-Abstract-Conference.html)、[Git Re-Basin](https://arxiv.org/abs/2209.04836)、[Equivariant Deep Weight Space Alignment](https://arxiv.org/abs/2310.13397)，可结合上述几何与表征研究一起阅读。
- **程序编译与训练式生成：** [Tracr](https://arxiv.org/abs/2301.05062)、[Text-to-LoRA](https://arxiv.org/abs/2506.06105)、[Doc-to-LoRA](https://arxiv.org/abs/2602.15902) 已在主目录收录。应区分这些方法的训练需求、参数构造方式和是否需要专门训练编辑器。
- **定向修改：** [ROME](https://arxiv.org/abs/2202.05262)、[MEMIT](https://arxiv.org/abs/2210.07229)、[AlphaEdit](https://arxiv.org/abs/2410.02355)、[Task Arithmetic](https://arxiv.org/abs/2212.04089) 仍保留在主目录，不在此重复收录。

## 值得沿着这些文献提出的问题

1. **读取是否真实：** 一个方法读出的是模型机制，还是架构、训练集或检查点家族的捷径？应检验对称变换和未见网络。
2. **迁移对象是什么：** 固定数值 `ΔW`、经过对齐的子空间，还是能够在不同宿主网络上重新执行的权重程序？
3. **连续组合如何处理冲突：** 冲突来自共享参数坐标、共享计算路径，还是激活条件变化？至少与简单相加、稀疏合并、参数隔离做对照。
4. **如何衡量能力积累：** 同时检测新能力和旧能力，特别是连续更新以后；区分推理时路由与持久写入权重。

**整理说明：** 这里有意识地纳入训练式权重生成器、依赖梯度的适配器、模型合并与持续学习研究。它们会提供启发，但不应因为直接操作参数就被称为“无训练权重编程”。

[返回 Awesome Weight-Space Programming](../README_zh.md) · [English](weight-centric-research.md)
