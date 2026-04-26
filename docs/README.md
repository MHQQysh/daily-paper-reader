<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-04-26 · 2026-04-26 20:04:49
- 运行时间：2026-04-26 20:08:36 UTC
- 运行状态：成功
- 本次总论文数：17
- 精读区：6
- 速读区：11

### 今日简报（AI）
今日深度解析 17 篇模型压缩前沿，聚焦 LLM 结构化剪枝、VLM 量化及 LoRA 合并等提效方案。
满分力作 GRASPrune 与 SimDiff 分别在全局门控与深度剪枝上取得突破，显著优化了大模型在有限预算下的性能表现。
建议优先研读结构化剪枝新算法及频谱统计预测技术，为实现大模型的高效轻量化部署提供实操参考。
- 详情：[/all__20260426-200449-874064/README](/all__20260426-200449-874064/README)

### 精读区论文标签
1. [GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models](/all__20260426-200449-874064/2604.19398v1-grasprune-global-gating-for-budgeted-structured-pruning-of-large-language-models)  
   标签：评分：10.0/10、query:llm
   evidence：针对大语言模型FFN通道和KV头组的结构化剪枝框架
2. [SimDiff: Depth Pruning via Similarity and Difference](/all__20260426-200449-874064/2604.19520v1-simdiff-depth-pruning-via-similarity-and-difference)  
   标签：评分：10.0/10、query:llm
   evidence：通过识别和移除冗余层对大语言模型进行深度剪枝
3. [Graph-Guided Adaptive Channel Elimination for KV Cache Compression](/all__20260426-200449-874064/2604.16983v1-graph-guided-adaptive-channel-elimination-for-kv-cache-compression)  
   标签：评分：9.0/10、query:llm
   evidence：针对大语言模型KV缓存压缩的通道剪枝
4. [Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales](/all__20260426-200449-874064/2604.20682v1-variance-is-not-importance-structural-analysis-of-transformer-compressibility-across-model-scales)  
   标签：评分：9.0/10、query:llm
   evidence：Transformer可压缩性与重要性指标的结构分析
5. [HieraSparse: Hierarchical Semi-Structured Sparse KV Attention](/all__20260426-200449-874064/2604.16864v1-hierasparse-hierarchical-semi-structured-sparse-kv-attention)  
   标签：评分：8.0/10、query:llm
   evidence：半结构化稀疏KV缓存注意力以提高效率
6. [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](/all__20260426-200449-874064/2604.17297v1-crisp-compressing-redundancy-in-chain-of-thought-via-intrinsic-saliency-pruning)  
   标签：评分：8.0/10、query:llm
   evidence：利用内在显著性剪枝压缩冗余并降低延迟

### 速读区论文标签
1. [Towards Joint Quantization and Token Pruning of Vision-Language Models](/all__20260426-200449-874064/2604.17320v1-towards-joint-quantization-and-token-pruning-of-vision-language-models)  
   标签：评分：8.0/10、query:llm
   evidence：视觉语言模型的协同量化与令牌剪枝
2. [Evolutionary Negative Module Pruning for Better LoRA Merging](/all__20260426-200449-874064/2604.17753v1-evolutionary-negative-module-pruning-for-better-lora-merging)  
   标签：评分：8.0/10、query:llm
   evidence：即插即用的 LoRA 剪枝方法，用于排除有害模块
3. [Predicting LLM Compression Degradation from Spectral Statistics](/all__20260426-200449-874064/2604.18085v1-predicting-llm-compression-degradation-from-spectral-statistics)  
   标签：评分：8.0/10、query:llm
   evidence：预测大语言模型压缩性能下降
4. [CATP: Confidence-Aware Token Pruning for Camouflaged Object Detection](/all__20260426-200449-874064/2604.16854v1-catp-confidence-aware-token-pruning-for-camouflaged-object-detection)  
   标签：评分：7.0/10、query:llm
   evidence：针对Transformer的置信度感知Token剪枝
5. [Prune, Interpret, Evaluate: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution](/all__20260426-200449-874064/2604.16889v1-prune-interpret-evaluate-a-cross-layer-transcoder-native-framework-for-efficient-circuit-discovery-via-feature-attribution)  
   标签：评分：7.0/10、query:llm
   evidence：基于梯度加权归因的转码器特征剪枝
6. [Efficient Task Adaptation in Large Language Models via Selective Parameter Optimization](/all__20260426-200449-874064/2604.17051v1-efficient-task-adaptation-in-large-language-models-via-selective-parameter-optimization)  
   标签：评分：7.0/10、query:llm
   evidence：用于选择性优化的参数元素重要性
7. [Towards a Data-Parameter Correspondence for LLMs: A Preliminary Discussion](/all__20260426-200449-874064/2604.17384v1-towards-a-data-parameter-correspondence-for-llms-a-preliminary-discussion)  
   标签：评分：7.0/10、query:llm
   evidence：讨论了大语言模型中数据剪枝与参数剪枝的对应关系
8. [MoE-nD: Per-Layer Mixture-of-Experts Routing for Multi-Axis KV Cache Compression](/all__20260426-200449-874064/2604.17695v1-moe-nd-per-layer-mixture-of-experts-routing-for-multi-axis-kv-cache-compression)  
   标签：评分：7.0/10、query:llm
   evidence：通过令牌剔除和低秩投影进行KV缓存压缩
9. [Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines](/all__20260426-200449-874064/2604.16734v1-reducing-peak-memory-usage-for-modern-multimodal-large-language-model-pipelines)  
   标签：评分：6.0/10、query:llm
   evidence：多模态大语言模型的KV缓存压缩
10. [D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation](/all__20260426-200449-874064/2604.16940v1-d-qrelo-training--and-data-free-delta-compression-for-large-language-models-via-quantization-and-residual-low-rank-approximation)  
   标签：评分：6.0/10、query:llm
   evidence：通过量化和低秩近似对大模型进行增量压缩
11. [EvoComp: Learning Visual Token Compression for Multimodal Large Language Models via Semantic-Guided Evolutionary Labeling](/all__20260426-200449-874064/2604.17087v1-evocomp-learning-visual-token-compression-for-multimodal-large-language-models-via-semantic-guided-evolutionary-labeling)  
   标签：评分：6.0/10、query:llm
   evidence：多模态大模型推理效率的视觉Token压缩


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
