# 权重相关研究：超越编辑的灵感来源

**[Awesome Weight-Space Programming](../README_zh.md) 的独立阅读系列。** 权重编程的灵感不必只来自模型编辑论文。这里把神经网络权重视为可以被**理解、表征、生成、组合、定位和保护**的结构化对象。收录的研究用于提供未来的设计思路和对照，**不代表它们本身属于直接权重空间编程（WSP）**。

**收录标准：** 能够为权重读取或写入、跨模型计算迁移、多次更新的组合、旧能力保留等问题提供具体、可验证的思路。没有明确关联的一般微调、压缩与优化工作不纳入。下文的“潜在启发”是研究假设，不是已得到验证的 WSP 结论。

**当前收录：** 67 篇论文，6 条研究线。在原有 21 篇基础上进行多关键词系统补充，仅保留能提出可检验权重编程启发的文献。已在[主仓库相关工作](../README_zh.md#related-research)收录的论文不在此重复列出。

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

- **[Weight-space symmetry in deep networks gives rise to permutation saddles, connected by equal-loss valleys across the loss landscape](https://arxiv.org/abs/1907.02911)**（2019）。**核心思路：**神经元置换产生等价极小值与对称相关的鞍点。 **对未来权重编程的启发：**跨模型程序应针对计算等价关系，而不是固定神经元编号。

- **[Improved Generalization of Weight Space Networks via Augmentations](https://arxiv.org/abs/2402.04081)**（2024）。**核心思路：**利用权重空间数据增强与 MixUp 改善模型对模型的学习泛化。 **对未来权重编程的启发：**权重读取器应经过对称变化和检查点分布偏移测试。

- **[Understanding Mode Connectivity via Parameter Space Symmetry](https://arxiv.org/abs/2505.23681)**（ICML 2025）。**核心思路：**用连续参数对称性分析低损失解之间的连通性。 **对未来权重编程的启发：**检查权重更新是否偏离宿主网络的稳定功能区域。

- **[Generalized Linear Mode Connectivity for Transformers](https://arxiv.org/abs/2506.22712)**（2025）。**核心思路：**研究 Transformer 检查点更一般的对齐及线性连通条件。 **对未来权重编程的启发：**跨 Transformer 复用权重程序前应考虑结构与对齐。

- **[Beyond the Permutation Symmetry of Transformers: The Role of Rotation for Model Fusion](https://arxiv.org/abs/2502.00264)**（ICML 2025）。**核心思路：**指出 Transformer 的模型融合还涉及置换之外的旋转对称性。 **对未来权重编程的启发：**跨模型编辑可能需要对基变换保持一致。

- **[Universal Neural Functionals](https://arxiv.org/abs/2402.05232)**（NeurIPS 2024）。**核心思路：**构造适用于多类网络架构的对称感知参数函数。 **对未来权重编程的启发：**启发设计遵循重参数化对称性的读取器与定位器。

- **[Monomial Matrix Group Equivariant Neural Functional Networks](https://arxiv.org/abs/2409.11697)**（NeurIPS 2024）。**核心思路：**将神经泛函的等变性扩展到单项矩阵群变换。 **对未来权重编程的启发：**程序不应把无害的缩放重参数化误认为能力变化。

- **[Scale Equivariant Graph Metanetworks](https://arxiv.org/abs/2406.10685)**（NeurIPS 2024）。**核心思路：**以图结构处理网络，并考虑缩放等变性。 **对未来权重编程的启发：**可考虑缩放感知的结构签名定位可复用编辑位点。

<a id="wcr-reading"></a>
## 权重作为数据：读取与表征

*不运行原任务，仅靠参数能读出模型的哪些性质？*

- **[Predicting Neural Network Accuracy from Weights](https://arxiv.org/abs/2002.11448)**（2020 preprint）。**核心思路：**从参数统计量预测模型精度，不需要执行原任务。 **对未来权重编程的启发：**为纯权重读取提供可检验的先例，但跨模型泛化仍需验证。

- **[Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction](https://arxiv.org/abs/2110.15288)**（NeurIPS 2021）。**核心思路：**从多个已训练网络的参数中学习模型级表征。 **对未来权重编程的启发：**可能为编辑位置检索与网络画像提供比原始张量更合适的输入。

- **[Hyper-Representations as Generative Models: Sampling Unseen Neural Network Weights](https://arxiv.org/abs/2209.14733)**（NeurIPS 2022）。**核心思路：**利用学习到的权重表征生成新的网络参数。 **对未来权重编程的启发：**启发从模型群体中提炼可复用先验；它属于训练式生成器，而不是直接 WSP。

- **[Classifying the classifier: dissecting the weight space of neural networks](https://arxiv.org/abs/2002.05688)**（ECAI 2020）。**核心思路：**利用权重快照上的元分类器识别网络训练与模型属性。 **对未来权重编程的启发：**为纯权重读取的可恢复信息提供基础对照。

- **[Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data](https://arxiv.org/abs/2002.06716)**（Nature Communications 2021）。**核心思路：**从谱统计与重尾特征估计模型质量，无需原训练集或测试集。 **对未来权重编程的启发：**可用于编辑前后的参数诊断，但不能替代行为评测。

- **[Graph Neural Networks for Learning Equivariant Representations of Neural Networks](https://arxiv.org/abs/2403.12143)**（ICLR 2024）。**核心思路：**将网络视为图，从中学习等变表征。 **对未来权重编程的启发：**宿主网络可先转换成结构化表示再供权重程序读取。

- **[Graph Metanetworks for Processing Diverse Neural Architectures](https://arxiv.org/abs/2312.04501)**（ICLR 2024）。**核心思路：**通过图元网络统一处理多种神经网络架构。 **对未来权重编程的启发：**为跨架构的权重程序提供结构感知接口。

- **[Towards Scalable and Versatile Weight Space Learning](https://arxiv.org/abs/2406.09997)**（ICML 2024）。**核心思路：**研究如何更高效地从较大规模模型权重中学习表征。 **对未来权重编程的启发：**检验压缩权重特征能否支持编辑位置选择。

- **[Deep Linear Probe Generators for Weight Space Learning](https://arxiv.org/abs/2410.10811)**（2024）。**核心思路：**通过探针生成器提取网络权重信息。 **对未来权重编程的启发：**为大模型权重读取提供比完整张量扫描更轻量的途径。

- **[Learning on Model Weights using Tree Experts](https://arxiv.org/abs/2410.13569)**（CVPR 2025）。**核心思路：**利用树专家结构学习网络权重的特征。 **对未来权重编程的启发：**启发分层读取与编辑位点路由。

- **[Learning Model Representations Using Publicly Available Model Hubs](https://arxiv.org/abs/2510.02096)**（2025）。**核心思路：**利用公开模型库学习检查点级表示。 **对未来权重编程的启发：**可扩大权重读取器的宿主多样性与跨模型验证范围。

- **[W2T: LoRA Weights Already Know What They Can Do](https://arxiv.org/abs/2603.15990)**（EMNLP 2026）。**核心思路：**先规范化等价 LoRA 分解，再从适配器权重读取属性与能力。 **对未来权重编程的启发：**为避免把 LoRA 因子化选择误当语义提供关键参考。

- **[What Linear Probes Miss: Multi-View Probing for Weight-Space Learning](https://proceedings.mlr.press/v306/heo26a.html)**（ICML 2026）。**核心思路：**结合一阶探针与基于 Gram 矩阵的高阶交互特征。 **对未来权重编程的启发：**检验多视角权重摘要能否提升程序规划与定位。

- **[Weight Space Representation Learning via Neural Field Adaptation](https://arxiv.org/abs/2512.01759)**（CVPR 2026）。**核心思路：**利用神经场适应学习参数空间表征。 **对未来权重编程的启发：**启发检验权重描述符能否跨已拟合函数泛化。

- **[Model Zoos: A Dataset of Diverse Populations of Neural Network Models](https://arxiv.org/abs/2209.14764)**（NeurIPS 2022）。**核心思路：**提供不同训练条件下的神经网络群体与检查点数据。 **对未来权重编程的启发：**可作为权重读取和跨宿主程序复用的测试资源。

<a id="wcr-generation"></a>
## 权重生成与合成

*能否把网络作为可生成的对象，而不是每个任务都重新优化？*

- **[HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://arxiv.org/abs/2303.17015)**（2023 preprint）。**核心思路：**在隐式神经场的 MLP 权重空间训练扩散生成模型。 **对未来权重编程的启发：**可以考虑用生成先验约束编辑，使修改更可能落在有效的功能区域。

- **[Neural Network Diffusion](https://arxiv.org/abs/2402.13144)**（2024 preprint）。**核心思路：**用潜在扩散模型合成性能较好的参数子集。 **对未来权重编程的启发：**启发基于参数先验生成或修复局部权重块。

- **[NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://proceedings.mlr.press/v306/kim26ay.html)**（ICML 2026）。**核心思路：**通过结构对齐，在不同宽度的网络间生成权重。 **对未来权重编程的启发：**为跨宽度、跨参数化的可移植权重程序提供设计参考。

- **[HyperGAN: A Generative Model for Diverse, Performant Neural Networks](https://arxiv.org/abs/1901.11058)**（ICML 2019）。**核心思路：**学习生成多样且可用的网络权重。 **对未来权重编程的启发：**启发利用有效权重分布为程序输出施加约束。

- **[Graph HyperNetworks for Neural Architecture Search](https://arxiv.org/abs/1810.05749)**（ICLR 2019）。**核心思路：**根据架构图生成候选网络参数。 **对未来权重编程的启发：**启发用网络结构而非固定张量下标参数化程序。

- **[Learning to Learn with Generative Models of Neural Network Checkpoints](https://arxiv.org/abs/2209.12892)**（2022）。**核心思路：**根据目标损失或回报条件生成检查点更新。 **对未来权重编程的启发：**为目标条件化的权重变化提供强对照范式。

- **[Instruction-Guided Autoregressive Neural Network Parameter Generation](https://arxiv.org/abs/2504.02012)**（2025）。**核心思路：**受指令条件控制，自回归生成神经网络参数。 **对未来权重编程的启发：**可比较直接生成参数与生成可复用程序的差异。

- **[Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights](https://arxiv.org/abs/2506.16406)**（2025）。**核心思路：**探索文本提示条件下的零样本参数生成。 **对未来权重编程的启发：**与将语言知识转换为持久参数变化的目标直接相关。

- **[Recurrent Diffusion for Large-Scale Parameter Generation](https://arxiv.org/abs/2501.11587)**（NeurIPS 2025）。**核心思路：**以循环扩散和参数分块扩展权重生成规模。 **对未来权重编程的启发：**启发对大模型进行分块、结构化的编辑或修复。

- **[Text2Weight: Bridging Natural Language and Neural Network Weight Spaces](https://arxiv.org/abs/2508.13633)**（2025）。**核心思路：**根据自然语言任务描述生成任务相关权重。 **对未来权重编程的启发：**适合作为文本到权重程序的泛化对照。

- **[Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f74d79573d71078848973009d0e99bdb-Abstract-Conference.html)**（ICLR 2025）。**核心思路：**利用任务、数据与架构条件生成网络参数。 **对未来权重编程的启发：**有助于界定训练式多条件生成器与权重程序的能力边界。

- **[DeepWeightFlow: Re-Basined Flow Matching for Generating Neural Network Weights](https://arxiv.org/abs/2601.05052)**（ICLR 2026）。**核心思路：**对齐参数化后，通过流匹配生成完整网络权重。 **对未来权重编程的启发：**同时提供跨网络对齐思路和完整权重生成基线。

- **[LoRAGen: Structure-Aware Weight Space Learning for LoRA Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fc7c087b5e965075c8946b9ff57e3d64-Abstract-Conference.html)**（ICLR 2026）。**核心思路：**在条件化生成中处理 LoRA 非唯一分解与模块间分布差异。 **对未来权重编程的启发：**启发程序构造规范化更新，并考虑不同模块的结构差异。


<a id="wcr-composition"></a>
## 权重算术、合并与干扰

*多个参数变化如何组合，才能避免破坏已有能力？*

- **[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482)**（ICML 2022）。**核心思路：**通过平均兼容的微调检查点来组合模型。 **对未来权重编程的启发：**是权重组合的简单基线，也提示模型兼容性不可忽视。

- **[TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)**（NeurIPS 2023）。**核心思路：**处理多个参数增量之间的冗余修改和符号冲突。 **对未来权重编程的启发：**多程序安装不能简单叠加增量，应显式识别相互干扰。

- **[Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099)**（ICML 2024）。**核心思路：**提出 DARE，对微调增量随机丢弃和重缩放后再合并。 **对未来权重编程的启发：**提示能力增量可能有较强冗余，但稀疏增量并不等于可执行程序。

- **[AdaMerging: Adaptive Model Merging for Multi-Task Learning](https://arxiv.org/abs/2310.02575)**（2023 preprint）。**核心思路：**借助无监督目标自适应学习任务级或层级的合并系数。 **对未来权重编程的启发：**启发在连续编辑冲突时，采用任务或层级相关的组合策略。

- **[Merging Models with Fisher-Weighted Averaging](https://proceedings.neurips.cc/paper_files/paper/2022/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html)**（NeurIPS 2022）。**核心思路：**根据 Fisher 重要性对模型参数进行加权合并。 **对未来权重编程的启发：**可启发多能力更新中的重要参数保护与冲突加权。

- **[Model Breadcrumbs: Scaling Multi-Task Model Merging with Sparse Masks](https://mlanthology.org/eccv/2024/davari2024eccv-model/)**（ECCV 2024）。**核心思路：**通过剔除极端值与弱更新稀疏化任务增量。 **对未来权重编程的启发：**可比较稀疏程序修改与稠密增量的可组合性。

- **[Model Stock: All we need is just a few fine-tuned models](https://arxiv.org/abs/2403.19522)**（ECCV 2024）。**核心思路：**以少量微调检查点估计有利的权重空间中心。 **对未来权重编程的启发：**可构造低成本参照点判断更新的稳定性。

- **[Task Singular Vectors: Reducing Task Interference in Model Merging](https://openaccess.thecvf.com/content/CVPR2025/html/Gargiulo_Task_Singular_Vectors_Reducing_Task_Interference_in_Model_Merging_CVPR_2025_paper.html)**（CVPR 2025）。**核心思路：**用 SVD 分解任务增量，测量并减小子空间干扰。 **对未来权重编程的启发：**尤其适合研究多个权重程序连续写入时的冲突。

- **[Model merging with SVD to tie the Knots](https://arxiv.org/abs/2410.19735)**（ICLR 2025）。**核心思路：**合并前先通过 SVD 将多个 LoRA 更新对齐到共同空间。 **对未来权重编程的启发：**可与直接相加比较，检验对齐能否降低程序冲突。

- **[RegMean++: Enhancing Effectiveness and Generalization of Regression Mean for Model Merging](https://arxiv.org/abs/2508.03121)**（TMLR 2026）。**核心思路：**在合并中显式考虑层内与跨层依赖。 **对未来权重编程的启发：**说明局部权重改动会产生跨层级的功能后果。

- **[Representation Surgery for Multi-Task Model Merging](https://proceedings.mlr.press/v235/yang24t.html)**（ICML 2024）。**核心思路：**通过轻量插件修正合并模型的表示偏移。 **对未来权重编程的启发：**提醒参数层面能合并不代表功能层面无冲突。

<a id="wcr-structure"></a>
## 结构化参数、稀疏性与机制定位

*程序究竟该改哪些参数、方向或子网络？*

- **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)**（ICLR 2019）。**核心思路：**在大网络中寻找具有训练潜力的稀疏子网络。 **对未来权重编程的启发：**启发研究新能力能否安装在受限的计算子结构中。

- **[Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)**（2021 preprint）。**核心思路：**通过归因定位与特定事实知识相关的神经元。 **对未来权重编程的启发：**提供由行为定位编辑位置的路径，但仍需因果验证。

- **[DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353)**（ICML 2024）。**核心思路：**将权重分解为幅值和方向以进行适应。 **对未来权重编程的启发：**启发在编写局部参数更新时区分幅值变化与方向变化。

- **[PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://arxiv.org/abs/2404.02948)**（NeurIPS 2024）。**核心思路：**利用预训练权重矩阵的主要奇异分量构造适应空间。 **对未来权重编程的启发：**启发依据矩阵结构选择编辑子空间，而非任意参数坐标。

- **[SparseGPT: Massive Language Models Can be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774)**（ICML 2023）。**核心思路：**利用重构感知算法对大模型进行一次性免重训练剪枝。 **对未来权重编程的启发：**启发稀疏编辑预算和参数冗余的定量分析。

- **[A Simple and Effective Pruning Approach for Large Language Models](https://arxiv.org/abs/2306.11695)**（ICLR 2024）。**核心思路：**Wanda 根据权重幅值与输入激活的乘积选择待剪参数。 **对未来权重编程的启发：**编辑位点选择可比较激活感知与纯权重幅值方法。

- **[SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://arxiv.org/abs/2403.07378)**（2024）。**核心思路：**使用数据感知 SVD 与闭式补偿减小压缩损失。 **对未来权重编程的启发：**可启发改变目标子空间时同时实施功能保持补偿。

<a id="wcr-retention"></a>
## 持续能力积累与旧能力保护

*新能力应写到哪里？连续更新后哪些旧能力必须保持？*

- **[Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796)**（PNAS 2017）。**核心思路：**通过保护对旧任务重要的参数来缓解遗忘（EWC）。 **对未来权重编程的启发：**启发估计旧能力的参数足迹，并在编辑中进行保护。

- **[Progressive Neural Networks](https://arxiv.org/abs/1606.04671)**（2016 preprint）。**核心思路：**保留旧网络列，并通过新增网络列与侧向连接学习新任务。 **对未来权重编程的启发：**与原位编辑形成对照：隔离可保护旧能力，但会增加容量成本。

- **[PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning](https://arxiv.org/abs/1711.05769)**（CVPR 2018）。**核心思路：**通过迭代剪枝释放参数空间，依次容纳多个任务。 **对未来权重编程的启发：**启发对多次安装过程中的剩余容量和参数占用进行追踪。

- **[Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights](https://arxiv.org/abs/1801.06519)**（ECCV 2018）。**核心思路：**在固定基础权重上学习任务专属的二值掩码。 **对未来权重编程的启发：**为条件化激活新能力与保留旧能力提供非破坏式对照。

- **[Continual learning with hypernetworks](https://arxiv.org/abs/1906.00695)**（ICLR 2020）。**核心思路：**通过正则化超网络保留不同任务条件下的目标权重。 **对未来权重编程的启发：**为长序列能力保留与条件化调用提供训练式对照。

- **[Memory Aware Synapses: Learning what (not) to forget](https://arxiv.org/abs/1711.09601)**（ECCV 2018）。**核心思路：**根据输出敏感度在线估计参数重要性。 **对未来权重编程的启发：**可指导程序避免覆盖对旧功能重要的参数。

- **[InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning](https://arxiv.org/abs/2404.00228)**（CVPR 2024）。**核心思路：**将低秩更新约束在减小旧任务干扰的子空间。 **对未来权重编程的启发：**适合作为连续权重写入的子空间保护基线。

- **[C-LoRA: Continual Low-Rank Adaptation for Pre-trained Models](https://arxiv.org/abs/2502.17920)**（2025）。**核心思路：**通过路由与正交约束管理顺序低秩更新。 **对未来权重编程的启发：**启发跟踪多轮程序安装的子空间占用情况。

- **[BECAME: Bayesian Continual Learning with Adaptive Model Merging](https://proceedings.mlr.press/v267/li25bk.html)**（ICML 2025）。**核心思路：**以贝叶斯持续学习推导自适应合并系数。 **对未来权重编程的启发：**为连续更新中的可塑性和保持权衡提供原则性对照。

- **[Weight-Space Linear Recurrent Neural Networks](https://arxiv.org/abs/2506.01153)**（ICLR 2026）。**核心思路：**WARP 将辅助网络的权重和偏置作为循环隐藏状态，并利用输入差异进行免梯度在线更新。 **对未来权重编程的启发：**比较输入驱动的临时参数状态更新与持久能力安装，区分在线适应与真正的能力保留。

## 综述、文献地图与评估资源

- **[A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)**（2026）。系统整理权重理解、表征和生成；本仓库的附加价值是明确其对可编程权重干预的启发。
- **[Awesome Weight-Space Learning](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning)**。覆盖面更广的权重空间研究索引，可持续查漏，但不照搬其分类与收录内容。
- **[Position: Weight Space Should Be a First-Class Generative AI Modality](https://proceedings.mlr.press/v306/wang26mc.html)**（ICML 2026）。讨论将检查点视为可生成数据模态的研究方向。
- **[MergeBench: A Benchmark for Merging](https://proceedings.neurips.cc/paper_files/paper/2025/file/91f7f71cb04699f387dc863da42a1fe3-Paper-Datasets_and_Benchmarks_Track.pdf)**（NeurIPS 2025）。为权重组合方法提供系统评价场景。

**证据边界：** 训练式超网络或扩散生成器不等于推理驱动的权重编程；单检查点编辑成功不等于程序可迁移；一次更新后的旧能力保持不等于长期能力积累。

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
