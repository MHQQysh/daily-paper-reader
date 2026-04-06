<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-03-08 ~ 2026-04-06
- 运行时间：2026-04-06 14:03:35 UTC
- 运行状态：成功
- 本次总论文数：17
- 精读区：6
- 速读区：11

### 今日简报（AI）
深度解析 17 篇高效推理新作，见证语义路由实现 98 倍加速与 ViT 自动剪枝的性能飞跃。
核心突破在于利用 Flash Attention 与多粒度随机剪枝（HiAP），在无需专用 GPU 的情况下大幅压低大模型与多模态推理成本。
建议优先研读 vLLM 语义路由优化与 ASAP 剪枝方案，掌握在有限算力下实现极致推理效率的实战路径。
- 详情：[/20260308-20260406/README](/20260308-20260406/README)

### 精读区论文标签
1. [HiAP: A Multi-Granular Stochastic Auto-Pruning Framework for Vision Transformers](/20260308-20260406/2603.12222v1-hiap-a-multi-granular-stochastic-auto-pruning-framework-for-vision-transformers)  
   标签：评分：9.0/10、query:llm
   evidence：视觉 Transformer 的多粒度随机自动剪枝
2. [98$\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router](/20260308-20260406/2603.12646v1-98times-faster-llm-routing-without-a-dedicated-gpu-flash-attention-prompt-compression-and-near-streaming-for-the-vllm-semantic-router)  
   标签：评分：9.0/10、query:flattn
   evidence：利用 Flash Attention 实现更快的 LLM 路由
3. [ASAP: Attention-Shift-Aware Pruning for Efficient LVLM Inference](/20260308-20260406/2603.14549v1-asap-attention-shift-aware-pruning-for-efficient-lvlm-inference)  
   标签：评分：9.0/10、query:llm
   evidence：用于高效多模态大模型推理的免训练剪枝方案
4. [FlashSampling: Fast and Memory-Efficient Exact Sampling](/20260308-20260406/2603.15854v1-flashsampling-fast-and-memory-efficient-exact-sampling)  
   标签：评分：9.0/10、query:flattn
   evidence：逐块片上计算，无需HBM显存实例化
5. [Scaling Attention via Feature Sparsity](/20260308-20260406/2603.22300v1-scaling-attention-via-feature-sparsity)  
   标签：评分：9.0/10、query:flattn
   evidence：FlashSFA IO感知内核扩展了FlashAttention
6. [FlatAttention: Dataflow and Fabric Collectives Co-Optimization for Large Attention-Based Model Inference on Tile-Based Accelerators](/20260308-20260406/2604.02110v1-flatattention-dataflow-and-fabric-collectives-co-optimization-for-large-attention-based-model-inference-on-tile-based-accelerators)  
   标签：评分：9.0/10、query:flattn
   evidence：分块加速器上的注意力数据流优化

### 速读区论文标签
1. [ASAP: Attention-Shift-Aware Pruning for Efficient LVLM Inference](/20260308-20260406/2603.14549v2-asap-attention-shift-aware-pruning-for-efficient-lvlm-inference)  
   标签：评分：8.0/10、query:llm
   evidence：适用于 LVLM 的 KV 缓存兼容剪枝方案
2. [Mixture-of-Depths Attention](/20260308-20260406/2603.15619v1-mixture-of-depths-attention)  
   标签：评分：8.0/10、query:flattn
   evidence：硬件高效算法，达到 FlashAttention-2 效率的 97.3%
3. [IWP: Token Pruning as Implicit Weight Pruning in Large Vision Language Models](/20260308-20260406/2604.00757v1-iwp-token-pruning-as-implicit-weight-pruning-in-large-vision-language-models)  
   标签：评分：8.0/10、query:llm
   evidence：Token剪枝作为大模型的隐式权重剪枝
4. [Scalable Training of Mixture-of-Experts Models with Megatron Core](/20260308-20260406/2603.07685v1-scalable-training-of-mixture-of-experts-models-with-megatron-core)  
   标签：评分：7.0/10、query:flattn
   evidence：涵盖内存重计算和融合的集成优化
5. [Flash-KMeans: Fast and Memory-Efficient Exact K-Means](/20260308-20260406/2603.09229v1-flash-kmeans-fast-and-memory-efficient-exact-k-means)  
   标签：评分：7.0/10、query:flattn
   evidence：利用类分块IO优化避免HBM显存显式实例化
6. [BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers](/20260308-20260406/2603.09582v1-binaryattention-one-bit-qk-attention-for-vision-and-diffusion-transformers)  
   标签：评分：7.0/10、query:flattn
   evidence：通过注意力二值化降低计算复杂度并替代点积运算
7. [S-HPLB: Efficient LLM Attention Serving via Sparsity-Aware Head Parallelism Load Balance](/20260308-20260406/2603.10353v1-s-hplb-efficient-llm-attention-serving-via-sparsity-aware-head-parallelism-load-balance)  
   标签：评分：7.0/10、query:flattn
   evidence：注意力推理中的并行性与负载均衡
8. [Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys](/20260308-20260406/2603.14224v1-self-indexing-kvcache-predicting-sparse-attention-from-compressed-keys)  
   标签：评分：7.0/10、query:flattn
   evidence：通过自索引KV缓存优化内存访问
9. [Scalable Training of Mixture-of-Experts Models with Megatron Core](/20260308-20260406/2603.07685v2-scalable-training-of-mixture-of-experts-models-with-megatron-core)  
   标签：评分：6.0/10、query:flattn
   evidence：细粒度重计算与内存优化
10. [Rethinking Attention Output Projection: Structured Hadamard Transforms for Efficient Transformers](/20260308-20260406/2603.08343v1-rethinking-attention-output-projection-structured-hadamard-transforms-for-efficient-transformers)  
   标签：评分：6.0/10、query:llm
   evidence：Transformer块中减少参数的结构化替换方法
11. [Fully Symbolic Analysis of Loop Locality: Using Imaginary Reuse to Infer Real Performance](/20260308-20260406/2603.10196v1-fully-symbolic-analysis-of-loop-locality-using-imaginary-reuse-to-infer-real-performance)  
   标签：评分：6.0/10、query:flattn
   evidence：张量操作中循环局部性和数据移动的符号化分析


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
