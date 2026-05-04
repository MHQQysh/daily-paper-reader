<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-05-04 · 2026-05-04 20:24:58
- 运行时间：2026-05-04 20:31:42 UTC
- 运行状态：成功
- 本次总论文数：18
- 精读区：7
- 速读区：11

### 今日简报（AI）
今日聚焦大模型“瘦身”前沿，深度解析了视觉语言模型（LVLM）与大语言模型的结构化剪枝与层冗余优化。
重点推荐关于 LVLM 剪枝动态恢复及 LLM 深度剪枝校准的研究，这些成果为模型在有限资源下的高效运行提供了新方案。
建议开发者关注自适应 LoRA 秩分配与绿色压缩技术，探索更低碳、高效的模型微调与部署路径。
- 详情：[/all__20260504-202458-578393/README](/all__20260504-202458-578393/README)

### 精读区论文标签
1. [Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency](/all__20260504-202458-578393/2604.24380v1-structural-pruning-of-large-vision-language-models-a-comprehensive-study-on-pruning-dynamics-recovery-and-data-efficiency)  
   标签：评分：10.0/10、query:llm
   evidence：视觉语言模型中语言模型主干的结构化剪枝
2. [Rethinking Layer Redundancy in Large Language Models: Calibration Objectives and Search for Depth Pruning](/all__20260504-202458-578393/2604.24938v1-rethinking-layer-redundancy-in-large-language-models-calibration-objectives-and-search-for-depth-pruning)  
   标签：评分：10.0/10、query:llm
   evidence：基于校准目标移除Transformer块的大模型深度剪枝
3. [Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling](/all__20260504-202458-578393/2604.25098v1-doing-more-with-less-revisiting-the-effectiveness-of-llm-pruning-for-test-time-scaling)  
   标签：评分：10.0/10、query:llm
   evidence：研究非结构化剪枝在推理大模型中是否表现出与结构化剪枝类似的局限性
4. [Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models](/all__20260504-202458-578393/2604.27115v1-exploring-the-limits-of-pruning-task-specific-neurons-model-collapse-and-recovery-in-task-specific-large-language-models)  
   标签：评分：10.0/10、query:llm
   evidence：基于激活选择性指标对任务特定大语言模型进行系统性神经元剪枝研究。
5. [Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning](/all__20260504-202458-578393/2604.26340v1-adaptive-and-fine-grained-module-wise-expert-pruning-for-efficient-lora-moe-fine-tuning)  
   标签：评分：9.5/10、query:llm
   evidence：针对LoRA-MoE的自适应细粒度模块化专家剪枝
6. [Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers](/all__20260504-202458-578393/2604.23475v1-supernodes-and-halos-loss-critical-hubs-in-llm-feed-forward-layers)  
   标签：评分：9.0/10、query:llm
   evidence：基于激活梯度二阶矩的Fisher风格损失代理用于通道重要性评估
7. [DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference](/all__20260504-202458-578393/2604.24647v1-depthkv-layer-dependent-kv-cache-pruning-for-long-context-llm-inference)  
   标签：评分：9.0/10、query:llm
   evidence：针对大语言模型的KV缓存剪枝方法，利用层依赖敏感度

### 速读区论文标签
1. [Post-Optimization Adaptive Rank Allocation for LoRA](/all__20260504-202458-578393/2604.27796v1-post-optimization-adaptive-rank-allocation-for-lora)  
   标签：评分：8.5/10、query:llm
   evidence：使用SVD对LoRA秩进行剪枝的无数据压缩方法
2. [HeadRouter: Dynamic Head-Weight Routing for Task-Adaptive Audio Token Pruning in Large Audio Language Models](/all__20260504-202458-578393/2604.23717v1-headrouter-dynamic-head-weight-routing-for-task-adaptive-audio-token-pruning-in-large-audio-language-models)  
   标签：评分：8.0/10、query:llm
   evidence：大型音频语言模型中用于令牌剪枝的动态头权重路由
3. [Carbon-Taxed Transformers: A Green Compression Pipeline for Overgrown Language Models](/all__20260504-202458-578393/2604.25903v1-carbon-taxed-transformers-a-green-compression-pipeline-for-overgrown-language-models)  
   标签：评分：8.0/10、query:llm
   evidence：LLM的系统性多架构压缩流水线
4. [LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models](/all__20260504-202458-578393/2604.23950v1-learnpruner-rethinking-attention-based-token-pruning-in-vision-language-models)  
   标签：评分：7.0/10、query:llm
   evidence：在视觉语言模型中利用基于注意力的重要性估计进行标记剪枝。
5. [Coverage-Based Calibration for Post-Training Quantization via Weighted Set Cover over Outlier Channels](/all__20260504-202458-578393/2604.24008v1-coverage-based-calibration-for-post-training-quantization-via-weighted-set-cover-over-outlier-channels)  
   标签：评分：7.0/10、query:llm
   evidence：训练后量化压缩大语言模型
6. [Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding](/all__20260504-202458-578393/2604.24820v1-salca-a-sparsity-aware-hardware-accelerator-for-efficient-long-context-attention-decoding)  
   标签：评分：7.0/10、query:llm
   evidence：用于高效长上下文解码的动态稀疏注意力
7. [Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling](/all__20260504-202458-578393/2604.25578v1-marco-moe-open-multilingual-mixture-of-expert-language-models-with-efficient-upcycling)  
   标签：评分：7.0/10、query:llm
   evidence：混合专家语言模型中的高稀疏性设计
8. [Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective](/all__20260504-202458-578393/2604.25975v1-rethinking-kv-cache-eviction-via-a-unified-information-theoretic-objective)  
   标签：评分：7.0/10、query:llm
   evidence：通过信息瓶颈原理进行KV缓存驱逐以实现内存压缩
9. [Auto-FlexSwitch: Efficient Dynamic Model Merging via Learnable Task Vector Compression](/all__20260504-202458-578393/2604.28109v1-auto-flexswitch-efficient-dynamic-model-merging-via-learnable-task-vector-compression)  
   标签：评分：6.5/10、query:llm
   evidence：用于多任务适配的可学习任务向量压缩
10. [Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](/all__20260504-202458-578393/2604.23858v1-latent-inter-frame-pruning-a-training-free-method-bridging-traditional-video-compression-and-modern-diffusion-transformers-for-efficient-generation)  
   标签：评分：6.0/10、query:llm
   evidence：剪枝扩散Transformer中的重复潜变量块
11. [Kwai Summary Attention Technical Report](/all__20260504-202458-578393/2604.24432v1-kwai-summary-attention-technical-report)  
   标签：评分：6.0/10、query:llm
   evidence：KV缓存压缩技术，旨在减轻长上下文大模型中的二次复杂度问题。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
