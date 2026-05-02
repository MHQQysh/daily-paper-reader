<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-05-02 · 2026-05-02 20:29:44
- 运行时间：2026-05-02 20:34:04 UTC
- 运行状态：成功
- 本次总论文数：19
- 精读区：8
- 速读区：11

### 今日简报（AI）
今日聚焦大模型“瘦身”前沿，深度探讨了视觉语言模型（LVLM）与大语言模型的结构化剪枝与层冗余优化。
核心结论指出，通过重新审视层冗余和动态恢复机制，可在极低数据依赖下实现多模态模型的高效压缩与性能找回。
建议优先关注结构化剪枝与自适应 LoRA 技术，这是当前解决大模型部署算力瓶颈的关键路径。
- 详情：[/all__20260502-202944-673441/README](/all__20260502-202944-673441/README)

### 精读区论文标签
1. [Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency](/all__20260502-202944-673441/2604.24380v1-structural-pruning-of-large-vision-language-models-a-comprehensive-study-on-pruning-dynamics-recovery-and-data-efficiency)  
   标签：评分：10.0/10、query:llm
   evidence：大型视觉语言模型的结构化剪枝
2. [Rethinking Layer Redundancy in Large Language Models: Calibration Objectives and Search for Depth Pruning](/all__20260502-202944-673441/2604.24938v1-rethinking-layer-redundancy-in-large-language-models-calibration-objectives-and-search-for-depth-pruning)  
   标签：评分：10.0/10、query:llm
   evidence：通过移除Transformer块进行深度剪枝并研究层冗余
3. [Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling](/all__20260502-202944-673441/2604.25098v1-doing-more-with-less-revisiting-the-effectiveness-of-llm-pruning-for-test-time-scaling)  
   标签：评分：10.0/10、query:llm
   evidence：推理大模型中结构化与非结构化剪枝的对比
4. [Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models](/all__20260502-202944-673441/2604.27115v1-exploring-the-limits-of-pruning-task-specific-neurons-model-collapse-and-recovery-in-task-specific-large-language-models)  
   标签：评分：10.0/10、query:llm
   evidence：基于激活选择性的任务特定大语言模型神经元剪枝系统研究
5. [Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers](/all__20260502-202944-673441/2604.23475v1-supernodes-and-halos-loss-critical-hubs-in-llm-feed-forward-layers)  
   标签：评分：9.0/10、query:llm
   evidence：基于激活梯度二阶矩的Fisher风格损失代理，用于通道级重要性评估
6. [DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference](/all__20260502-202944-673441/2604.24647v1-depthkv-layer-dependent-kv-cache-pruning-for-long-context-llm-inference)  
   标签：评分：9.0/10、query:llm
   evidence：针对大语言模型的层依赖KV缓存剪枝方法
7. [Carbon-Taxed Transformers: A Green Compression Pipeline for Overgrown Language Models](/all__20260502-202944-673441/2604.25903v1-carbon-taxed-transformers-a-green-compression-pipeline-for-overgrown-language-models)  
   标签：评分：9.0/10、query:llm
   evidence：针对大语言模型的系统性多架构压缩流水线
8. [Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning](/all__20260502-202944-673441/2604.26340v1-adaptive-and-fine-grained-module-wise-expert-pruning-for-efficient-lora-moe-fine-tuning)  
   标签：评分：9.0/10、query:llm
   evidence：LoRA-MoE微调中的模块化专家剪枝

### 速读区论文标签
1. [Post-Optimization Adaptive Rank Allocation for LoRA](/all__20260502-202944-673441/2604.27796v1-post-optimization-adaptive-rank-allocation-for-lora)  
   标签：评分：8.5/10、query:llm
   evidence：使用SVD剪枝LoRA秩的无数据压缩方法，提高参数效率
2. [HeadRouter: Dynamic Head-Weight Routing for Task-Adaptive Audio Token Pruning in Large Audio Language Models](/all__20260502-202944-673441/2604.23717v1-headrouter-dynamic-head-weight-routing-for-task-adaptive-audio-token-pruning-in-large-audio-language-models)  
   标签：评分：7.5/10、query:llm
   evidence：大型音频语言模型中用于推理效率的任务自适应音频令牌剪枝
3. [DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](/all__20260502-202944-673441/2604.22281v1-docpruneefficient-document-question-answering-via-background-question-and-comprehension-aware-token-pruning)  
   标签：评分：7.0/10、query:llm
   evidence：视觉语言模型的Token剪枝框架
4. [Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation](/all__20260502-202944-673441/2604.22312v1-guess-verify-refine-data-aware-top-k-for-sparse-attention-decoding-on-blackwell-via-temporal-correlation)  
   标签：评分：7.0/10、query:llm
   evidence：稀疏注意力解码中的Top-K选择延迟瓶颈
5. [Network Edge Inference for Large Language Models: Principles, Techniques, and Opportunities](/all__20260502-202944-673441/2604.22906v1-network-edge-inference-for-large-language-models-principles-techniques-and-opportunities)  
   标签：评分：7.0/10、query:llm
   evidence：边缘推理模型优化（包括剪枝）的全面综述
6. [Preserving Long-Tailed Expert Information in Mixture-of-Experts Tuning](/all__20260502-202944-673441/2604.23036v1-preserving-long-tailed-expert-information-in-mixture-of-experts-tuning)  
   标签：评分：7.0/10、query:llm
   evidence：MoE模型中专家的系统性剪枝
7. [From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors](/all__20260502-202944-673441/2604.23277v1-from-similarity-to-structure-training-free-llm-context-compression-with-hybrid-graph-priors)  
   标签：评分：7.0/10、query:llm
   evidence：使用图先验的长文本大语言模型上下文压缩框架
8. [LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models](/all__20260502-202944-673441/2604.23950v1-learnpruner-rethinking-attention-based-token-pruning-in-vision-language-models)  
   标签：评分：7.0/10、query:llm
   evidence：在视觉语言模型中利用LLM的注意力分数剪枝不重要的视觉标记
9. [Stabilizing Efficient Reasoning with Step-Level Advantage Selection](/all__20260502-202944-673441/2604.24003v1-stabilizing-efficient-reasoning-with-step-level-advantage-selection)  
   标签：评分：6.5/10、query:llm
   evidence：通过剪枝和步骤级选择进行推理压缩，以保持准确性
10. [Mixture of Heterogeneous Grouped Experts for Language Modeling](/all__20260502-202944-673441/2604.23108v1-mixture-of-heterogeneous-grouped-experts-for-language-modeling)  
   标签：评分：6.0/10、query:llm
   evidence：通过异构专家架构高效扩展性能
11. [Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](/all__20260502-202944-673441/2604.23858v1-latent-inter-frame-pruning-a-training-free-method-bridging-traditional-video-compression-and-modern-diffusion-transformers-for-efficient-generation)  
   标签：评分：6.0/10、query:llm
   evidence：剪枝扩散Transformer中的重复潜块


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
