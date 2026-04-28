<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-04-28 · 2026-04-28 20:02:02
- 运行时间：2026-04-28 20:08:21 UTC
- 运行状态：成功
- 本次总论文数：18
- 精读区：7
- 速读区：11

### 今日简报（AI）
今日聚焦大模型高效压缩，深度探讨结构化剪枝与深度裁剪在性能与预算间的平衡。
重点关注 GRASPrune 的全局门控机制与 SimDiff 的深度裁剪方案，揭示了模型规模、频谱统计与可压缩性间的深层关联。
建议优先研读两篇满分论文，掌握如何在保持精度的前提下实现 LLM 与视频多模态模型的极致瘦身。
- 详情：[/all__20260428-200202-391804/README](/all__20260428-200202-391804/README)

### 精读区论文标签
1. [GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models](/all__20260428-200202-391804/2604.19398v1-grasprune-global-gating-for-budgeted-structured-pruning-of-large-language-models)  
   标签：评分：10.0/10、query:llm
   evidence：针对FFN和KV头的LLM结构化剪枝框架
2. [SimDiff: Depth Pruning via Similarity and Difference](/all__20260428-200202-391804/2604.19520v1-simdiff-depth-pruning-via-similarity-and-difference)  
   标签：评分：10.0/10、query:llm
   evidence：通过相似性和差异性进行深度剪枝以移除冗余层
3. [Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency](/all__20260428-200202-391804/2604.24380v1-structural-pruning-of-large-vision-language-models-a-comprehensive-study-on-pruning-dynamics-recovery-and-data-efficiency)  
   标签：评分：10.0/10、query:llm
   evidence：大型视觉语言模型的结构化剪枝与恢复训练
4. [Evolutionary Negative Module Pruning for Better LoRA Merging](/all__20260428-200202-391804/2604.17753v1-evolutionary-negative-module-pruning-for-better-lora-merging)  
   标签：评分：9.0/10、query:llm
   evidence：即插即用的LoRA剪枝方法以排除有害模块
5. [Focus Session: Hardware and Software Techniques for Accelerating Multimodal Foundation Models](/all__20260428-200202-391804/2604.21952v1-focus-session-hardware-and-software-techniques-for-accelerating-multimodal-foundation-models)  
   标签：评分：9.0/10、query:llm
   evidence：基础模型中Transformer块和MLP通道的结构化剪枝
6. [Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers](/all__20260428-200202-391804/2604.23475v1-supernodes-and-halos-loss-critical-hubs-in-llm-feed-forward-layers)  
   标签：评分：9.0/10、query:llm
   evidence：用于通道级重要性评估的Fisher风格损失代理
7. [DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference](/all__20260428-200202-391804/2604.24647v1-depthkv-layer-dependent-kv-cache-pruning-for-long-context-llm-inference)  
   标签：评分：9.0/10、query:llm
   evidence：针对大语言模型推理的层相关KV缓存剪枝

### 速读区论文标签
1. [Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales](/all__20260428-200202-391804/2604.20682v1-variance-is-not-importance-structural-analysis-of-transformer-compressibility-across-model-scales)  
   标签：评分：8.0/10、query:llm
   evidence：Transformer可压缩性与重要性指标的结构化分析
2. [Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs](/all__20260428-200202-391804/2604.20937v1-sink-token-aware-pruning-for-fine-grained-video-understanding-in-efficient-video-llms)  
   标签：评分：8.0/10、query:llm
   evidence：用于高效视频大模型的视觉令牌剪枝
3. [Predicting LLM Compression Degradation from Spectral Statistics](/all__20260428-200202-391804/2604.18085v1-predicting-llm-compression-degradation-from-spectral-statistics)  
   标签：评分：7.0/10、query:llm
   evidence：预测低秩压缩方法带来的性能下降
4. [Stability Implies Redundancy: Delta Attention Selective Halting for Efficient Long-Context Prefilling](/all__20260428-200202-391804/2604.18103v1-stability-implies-redundancy-delta-attention-selective-halting-for-efficient-long-context-prefilling)  
   标签：评分：7.0/10、query:llm
   evidence：用于高效长文本预填充的令牌剪枝
5. [HybridGen: Efficient LLM Generative Inference via CPU-GPU Hybrid Computing](/all__20260428-200202-391804/2604.18529v1-hybridgen-efficient-llm-generative-inference-via-cpu-gpu-hybrid-computing)  
   标签：评分：7.0/10、query:llm
   evidence：用于高效大模型推理的KV缓存剪枝
6. [Forget, Then Recall: Learnable Compression and Selective Unfolding via Gist Sparse Attention](/all__20260428-200202-391804/2604.20920v1-forget-then-recall-learnable-compression-and-selective-unfolding-via-gist-sparse-attention)  
   标签：评分：7.0/10、query:llm
   evidence：可学习压缩与要点稀疏注意力
7. [Sub-Token Routing in LoRA for Adaptation and Query-Aware KV Compression](/all__20260428-200202-391804/2604.21335v1-sub-token-routing-in-lora-for-adaptation-and-query-aware-kv-compression)  
   标签：评分：7.0/10、query:llm
   evidence：查询感知的KV压缩和子Token路由以提高效率
8. [DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](/all__20260428-200202-391804/2604.22281v1-docpruneefficient-document-question-answering-via-background-question-and-comprehension-aware-token-pruning)  
   标签：评分：7.0/10、query:llm
   evidence：无须训练且渐进式的文档标记剪枝框架
9. [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](/all__20260428-200202-391804/2604.17935v1-how-much-cache-does-reasoning-need-depth-cache-tradeoffs-in-kv-compressed-transformers)  
   标签：评分：6.0/10、query:llm
   evidence：Transformer中KV压缩与缓存权衡的理论研究
10. [AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation](/all__20260428-200202-391804/2604.18348v1-adacluster-adaptive-query-key-clustering-for-sparse-attention-in-video-generation)  
   标签：评分：6.0/10、query:llm
   evidence：用于Transformer压缩的稀疏注意力和聚类
11. [River-LLM: Large Language Model Seamless Exit Based on KV Share](/all__20260428-200202-391804/2604.18396v1-river-llm-large-language-model-seamless-exit-based-on-kv-share)  
   标签：评分：6.0/10、query:llm
   evidence：通过动态跳过冗余层来加速推理


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
