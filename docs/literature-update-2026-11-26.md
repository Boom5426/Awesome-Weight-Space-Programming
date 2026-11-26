# WSP 文献更新与社区贡献整理

截至 2026 年 11 月 26 日，两轮检索共补充 42 条论文/手稿：第一轮 17 条，扩展检索再补 25 条。直接 WSP 目录现为 63 篇，权重相关研究 76 篇，相关基础 51 篇；加上报告和资源，结构化目录共 205 条。已同步中英文 README、证据矩阵、检索目录和研究图谱。完整标题、模型、对照、能力保持及局限保存在 [entries.json](../data/entries.json) 和[证据矩阵](wsp-evidence.md)。

The additions are preprints or manuscripts, not confirmed peer-reviewed publications. Source-checked means the primary report was inspected, not independently reproduced. The JEPA manuscript remains metadata-only, with outcome fields left null. arXiv dates below are in UTC; repository updates follow Asia/Shanghai.

## 检索范围与筛选

第一轮重点补查 2026-11-19 至 2026-11-26 的新论文及修订。第二轮扩展到 2026 年 10—11 月的直接 WSP、权重表征、参数生成、模型合并、局部编辑和自修改机制。检索方式包括 arXiv 官方接口、论文原文、作者代码、网页搜索及相关列表交叉核对。新收录表示原目录未包含，不表示全部论文刚刚发表。

arXiv 接口按 `lastUpdatedDate` 降序返回，第一轮每次最多 80 条，第二轮每次最多 100 条。下列为第一轮查询；日期按首次提交和版本修订分别记录：

```text
all:"weight-space programming"
(all:"weight space programming" OR all:"weight programming" OR all:"self-rewriting")
  AND submittedDate:[202611190000 TO 202611262359]
```

接口查询与普通网页搜索均有遗漏：SELFWRITE 来自相关列表交叉核对，Weight-Space Reading 和 JEPA 世界模型手稿来自 alphaXiv 及作者仓库。第二轮另检索 `weight space`、`parameter generation`、`hypernetwork`、`model merging`、`weight editing`、`self-modifying` 等标题。宽泛的自改进/内化搜索触及返回上限，因此补充了限定计算机学科的自编辑标题查询；不把大量泛化的 RSI 或非神经网络匹配算作 WSP。结果属于经过筛选的覆盖，不是穷尽性目录。

第一轮 ICL 研究采用 11-23 的 v2；第二轮 VLM 数值审计和语言模型修复分别采用 11-19、11-20 的 v2，异秩 LoRA 合并采用 v2。已收录论文不重复添加。`2611.04268` 的扩散猜想及 `2611.18690` 的初步方案仍不作为完整大模型实验收录；`2611.22228` 则核对了已完成的 24 项 TIMED 实验，并注明共享 CMA-ES 拟合器和预注册负面结果。

## 第一轮：17 篇直接研究

| 方向 | 论文 / 首次提交 | 本轮提取的重点与边界 |
| --- | --- | --- |
| 确定性编辑对照 | [FWSP](https://arxiv.org/abs/2611.34612v1) · 11-25 | 固定工具库下比较算子路由；结构化故障上的结果不能推广为所有编辑问题都不需要语言模型。混合 LoRA 方案使用梯度。 |
| RTL 生成修复 | [Kolpona](https://arxiv.org/abs/2611.33973v1) · 11-25 | 分开记录 4B 模型本身的神经元编辑收益与推理时智能体、投票和选择收益；后续编辑轮次受测试结果启发。 |
| 闭式分类器构造 | [Closed-Form Classifiers](https://arxiv.org/abs/2611.33972v1) · 11-25 | 在冻结 RoBERTa 上监督拟合分类头；编码器权重不变。需计算多个模板的推理成本，开发集结论与留出数据集分开。 |
| 量化修复 | [Tool-Free Quantization Repair](https://arxiv.org/abs/2611.33031v1) · 11-24 | 检验模型直接读取数字权重的能力；分块回答和输入提示影响很大，固定量化规则是必要对照。 |
| 机器人执行修复 | [Robot Foundation Model Repair](https://arxiv.org/abs/2611.31715v1) · 11-24 | 采用仿真、配对场景、随机和反向编辑；三项明确成功，两项未取得显著修复。不能据此推断真实机器人或跨任务保持。 |
| 跨检查点规则复用 | [TowerBridge](https://arxiv.org/abs/2611.31233v1) · 11-23 | 从每个模型自身的图文表征重新计算修正；21 个 CLIP 检查点上的 RSUM 增益需与单项 Recall 百分点区分。 |
| 具身智能体自编辑 | [Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117v1) · 11-23 | ALFWorld 文本环境中的持续保留；四个夜间阶段只保留一项编辑，持续有效与持续获得新能力是不同结论。 |
| 检测模型编辑 | [IR-ODWSP](https://arxiv.org/abs/2611.29882v1) · 11-23 | 分开比较等推理成本折叠与增加延迟的变体；单模型等成本总体 AP 增益较小，跨模型对齐要求层宽匹配。 |
| 递归自编辑 | [SELFWRITE](https://arxiv.org/abs/2611.29513v1) · 11-22 | 五代中接受四项编辑，第五代无增益；最终数学测试有改善，但缺少跨领域能力保持与匹配随机搜索对照。 |
| 语音编辑负面证据 | [PAWP-TTS](https://arxiv.org/abs/2611.29455v1) · 11-22 | 有选择性的时长变化未形成超越匹配对照的准确率证据；先核对标签与音系，避免把数据伪差异当成模型缺陷。 |
| 小模型自编辑对照 | [Self-WSP](https://arxiv.org/abs/2611.28833v1) · 11-21 | 同时保留最佳与普通运行、随机搜索和冻结编辑器结果；模型给出的编辑理由不能替代机制证据。 |
| 权重安全评估 | [Autonomous Parameter Surgery](https://arxiv.org/abs/2611.27920v1) · 11-20 | 记录受限白盒威胁模型、独立确认集、干净输入与相邻触发控制；跨评论领域迁移不等于跨宿主程序复用。 |
| 多模态安全评估 | [TrojanMaxxing](https://arxiv.org/abs/2611.27425v1) · 11-20 | 分开记录攻击成功率、干净任务表现与防御测试；干净准确率保持不能证明安全保持。 |
| WSP 与 LoRA 对照 | [Spatial WSP vs LoRA](https://arxiv.org/abs/2611.27089v1) · 11-20 | LoRA 的目标任务优势伴随相邻距离任务严重退化；需要同时报告任务增益和能力保持。 |
| 科学模型修复 | [Particle-Physics WSP](https://arxiv.org/abs/2611.27079v1) · 11-20 | 比较 SAE、微调和不同信息条件的 WSP；区分修复软粒子敏感性与证明完整红外安全。 |
| ICL 写入权重 | [ICL-to-Weights](https://arxiv.org/abs/2611.26841v2) · 11-19，v2 为 11-23 | 模板依赖、编辑器自带任务知识和未完成运行会改变“匹配微调”的结论；连续编辑和增量相加可发生干扰。 |
| 面向编辑的训练 | [Edit-Ready Vision Training](https://arxiv.org/abs/2611.26408v1) · 11-19 | 整体方案包含梯度训练；编辑阶段与准备阶段分开。ERT 相对 ERM 有改善，但未证明整体显著优于 ENN。 |

## 扩展检索：再补 25 篇

| 分类 | 新增论文 | 收录理由与证据边界 |
| --- | --- | --- |
| 直接 WSP | [Weight Coding](https://arxiv.org/abs/2611.29613) | Pinterest 的留出日期、不同语料/指标及在线 A/B 结果；区分来源归因收益、业务目标权衡与其他召回源的损失。 |
| 直接 WSP | [AME](https://arxiv.org/abs/2611.34036) | 11 个少样本视觉数据集上的程序化适应；含预处理和分类器拟合，以及免反传和反传两种方案。 |
| 直接 WSP | [Scalpel and Brush](https://arxiv.org/abs/2611.33426) | 结合稀疏编辑、剪枝与隐藏测试；方程任务 BLEU 提升主要反映符号表达，不能当作数学正确性提高。 |
| 直接 WSP | [Game-Theoretic Policies](https://arxiv.org/abs/2611.31979) | 小型 RNN 的精确最优值和程序恢复；严格区分直接写出全部权重与由评估器编译状态机。 |
| 直接 WSP | [Blind Deployment-Fault Repair](https://arxiv.org/abs/2611.28781) | 盲诊断、脚本与完好模型对照；人工结构化故障及激活参考限制其现实外推。 |
| 直接 WSP | [LLM-Guided Transformer Repair](https://arxiv.org/abs/2611.25613) | 固定投影、脚本、黑盒搜索及 LoRA 对照，区分控制器选择和数值算子的贡献。 |
| 直接 WSP | [VLM Repair Low-Bit Audit](https://arxiv.org/abs/2611.23615) | 损坏权重的浮点低位可泄漏故障位置；舍入对照揭示成功修复依赖的数值线索。 |
| 直接 WSP | [Materials-Science WSP](https://arxiv.org/abs/2611.22013) | 从物理输入名称写出小网络，并测试科学先验用途；收益限于少标签区间，部分规则和外推基线更好。 |
| 直接 WSP | [Diffusion Program Construction](https://arxiv.org/abs/2611.22228) | 已完成的程序构造和修订对照；免梯度仍使用 CMA-ES，探索性收益不等于预注册成功。 |
| 直接 WSP | [Weight-Space Reading](https://www.alphaxiv.org/abs/2611.weight-space-reading-language-models) | 已读作者 PDF，单列 alphaXiv 手稿状态；权重访问收益、自读取优势和无效编辑误报分别记录。 |
| 直接 WSP，待核对 | [JEPA World Models](https://www.alphaxiv.org/abs/2611.wsp-jepa) | 已核对作者摘要和工具仓库，但完整 PDF 尚未取得；不将网页概述转成已核对的实验结论。 |
| 权重表征 | [DSProbe](https://arxiv.org/abs/2611.33998)、[UWE](https://arxiv.org/abs/2610.21995) | 参考点、权重位移及跨架构对称性；学习型权重编码不直接构成智能体编程证据。 |
| 权重生成 | [IGPG](https://arxiv.org/abs/2611.25538)、[CrossGMN](https://arxiv.org/abs/2610.01649) | 分别考察自回归权重 token 与跨架构初始化；将直接生成质量与后续训练/蒸馏收益分开。 |
| 权重组合 | [Latent Merger](https://arxiv.org/abs/2611.33048)、[RaTW](https://arxiv.org/abs/2611.33315)、[BRR](https://arxiv.org/abs/2611.33308)、[LR-Merge](https://arxiv.org/abs/2611.25000)、[异秩 LoRA 合并](https://arxiv.org/abs/2611.06486) | 补充固定秩组合、尾部能力保持、分组干扰、局部代理和谱筛选失衡；注明学习、标注验证及多组参数的成本。 |
| 相关基础 | [BaseRSI](https://arxiv.org/abs/2611.24578)、[CLAM](https://arxiv.org/abs/2611.20759)、[AutoHebb](https://arxiv.org/abs/2610.40757) | 分别是闭式流程内化、训练型超网络记忆及元学习赫布可塑性，不混作同一种自由程序式自编辑。 |
| 相关对照 | [Tiny Gradient Loop Repair](https://arxiv.org/abs/2611.33133)、[Ethical-Priority Edits](https://arxiv.org/abs/2611.24330) | 前者提供梯度基线；后者的权衡机制显式暴露，独立盲测编辑阶段尚未执行。 |

## 首页精选

`Research question` 表格保留 5 个互补问题，每项最多 3 篇，按质量和互补性选择，当前共 8 篇：WSP-Scope、iWSP、WeightCode、TowerBridge、HypoLoop、WeightLoop、Weight Coding、机器人基础模型修复。科学反馈问题下并列 HypoLoop 与 WeightLoop，分别关注反馈修订编辑方案和可复用的反馈驱动权重更新。选择依据包括系统轨迹与失败报告、隐藏算法测试、匹配对照与保持、未见宿主评估、科学任务的方法对照、在线实验及配对仿真控制。其余条目留在完整目录；首页不因收录数量增长而继续扩张。入选仍是对当前证据价值的编辑判断，不代表同行评审或独立复现。

## GitHub 链接核对

检查 48 篇原先缺少 GitHub 入口的直接 WSP 论文的摘要、HTML/PDF，并补查作者主页与仓库 README；为 15 篇补充作者 GitHub 入口，其中 13 篇链接到已发布代码，2 篇链接到项目仓库。直接研究的 GitHub 入口覆盖从 15/63 增至 30/63，中英文列表同步。

[Mixed Signals](https://github.com/DaraVaram/BioWSP) 的仓库主要托管配套说明、提示与展示页面，标为项目仓库；[计算生物学 Python 研究](https://github.com/satouma7/bioWSP) 的 README 明确代码待发布，保留该状态，不标为已发布代码。WSP for Policies 使用论文指定的 `wsp_verified` 分支，NCP 直接链接到 W-ISA 仓库中的对应目录。未将参考文献中的其他项目、依赖库或当前返回 404 的仓库标为论文代码。

## 社区贡献处理

- [PR #12](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pull/12)：核对作者的[原始结果表](https://github.com/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2/blob/main/README.md)，将五套基准共 1,054 题的未闭合轨迹口径修正为 305 → 41，即 28.9% → 3.9%；ARC-Challenge 在 T=0.6 下的变化按一位小数记为 -0.7 个百分点。保留修正并重新生成冲突页面，通过本地检查和 CI 后合并。
- [PR #13](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pull/13)：核对相关列表的主题后合并；本轮补充中文入口，将其保留为相关资源，不计入论文数。
- 截至本轮检查，没有开放的 Issue；检索接口与 GitHub Issues 列表均已核对。

## 验证

文献数据通过 `scripts/validate.py` 校验；Markdown 与 HTML 通过各自生成器重新生成并执行 `--check`。同时运行仓库现有 Python 数据/导航测试、Node 浏览器状态测试和生成脚本语法检查。
