# WSP 文献更新与社区贡献整理

截至 2026 年 11 月 26 日，本轮补充 17 篇预印本，直接 WSP 目录由 35 篇增至 52 篇，结构化目录总数由 163 条增至 180 条。已同步中英文 README、证据矩阵、检索目录和研究图谱。下表按研究问题整理；完整标题、模型、对照、能力保持及局限保存在 [entries.json](../data/entries.json) 和[证据矩阵](wsp-evidence.md)。

All 17 additions are preprints. Source-checked means the primary report was inspected; it does not mean independent experimental reproduction. Dates below are arXiv submission dates in UTC; the repository update date follows Asia/Shanghai.

## 检索范围与筛选

本轮重点补查 2026-11-19 至 2026-11-26 的新论文及修订，以覆盖上次更新附近可能遗漏的条目。检索方式包括 arXiv 官方接口、arXiv 论文原文、网页搜索及社区贡献中的链接交叉核对。

arXiv 接口按 `lastUpdatedDate` 降序返回，每次最多 80 条。本轮使用以下查询，并检查论文的首次提交日期与当前版本日期，而不是以搜索引擎的抓取时间判断新旧：

```text
all:"weight-space programming"
(all:"weight space programming" OR all:"weight programming" OR all:"self-rewriting")
  AND submittedDate:[202611190000 TO 202611262359]
```

接口查询与普通网页搜索均有遗漏：SELFWRITE 来自社区相关列表的交叉核对。因此本记录是经过筛选的本轮更新，不代表完整收录所有近期研究。ICL 写入研究采用 2026-11-23 的 v2；其余新增条目采用本轮可核对的 v1。WeightCode 已在目录中，未重复添加。更早的扩散猜想及其他不在本轮日期范围内的候选，未因关键词匹配而自动重新纳入。

## 按研究问题整理

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

## 阅读顺序

研究程序复用时，先读 TowerBridge，并对照已有的 WeightCode，核对每个宿主上重新计算的数据与反馈成本。研究机器人修复时，先看配对场景中的修好与损坏数量，再看平均成功率。[TowerBridge 原文](https://arxiv.org/html/2611.31233v1)、[机器人修复原文](https://arxiv.org/pdf/2611.31715)。

研究自我改进时，将 SELFWRITE、Self-WSP 和 Self-Upgrading Embodied Agents 一起读：分别检查被接受的编辑数量、随机搜索对照及收益是否主要来自减少循环或无效推理。稳定保留一次修复，还不能回答长期能力积累的问题。[SELFWRITE 原文](https://arxiv.org/html/2611.29513v1)、[Self-WSP 原文](https://arxiv.org/html/2611.28833v1)、[具身智能体原文](https://arxiv.org/html/2611.31117v1)。

设计实验时，加入确定性规则、同信息预算微调、随机编辑及未编辑模型的解码控制，并同时报告目标任务、相邻任务、失败运行和完整计算成本。对应本轮的 FWSP、Spatial WSP vs LoRA、PAWP-TTS 及 ICL-to-Weights；这些工作提供互补对照，而非统一的优劣排序。

## 社区贡献处理

- [PR #12](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pull/12)：核对作者的[原始结果表](https://github.com/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2/blob/main/README.md)，将五套基准共 1,054 题的未闭合轨迹口径修正为 305 → 41，即 28.9% → 3.9%；ARC-Challenge 在 T=0.6 下的变化按一位小数记为 -0.7 个百分点。保留修正并重新生成冲突页面，通过本地检查和 CI 后合并。
- [PR #13](https://github.com/Boom5426/Awesome-Weight-Space-Programming/pull/13)：核对相关列表的主题后合并；本轮补充中文入口，将其保留为相关资源，不计入论文数。
- 截至本轮检查，没有开放的 Issue；检索接口与 GitHub Issues 列表均已核对。

## 验证

文献数据通过 `scripts/validate.py` 校验；Markdown 与 HTML 通过各自生成器重新生成并执行 `--check`。同时运行仓库现有 Python 数据/导航测试、Node 浏览器状态测试和生成脚本语法检查。
