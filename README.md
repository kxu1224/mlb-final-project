# TxGemma-GRPO-Therapeutics-Finetuning

**Final Project for Machine Learning in Computational Biology**  
*Exploring reinforcement learning for therapeutic-focused reasoning in language models*

## 🧬 Project Overview

This repository explores fine-tuning Google's [TxGemma](https://developers.googleblog.com/en/introducing-txgemma-open-models-improving-therapeutics-development/) (a specialized biomedical LLM) using DeepSeek's **GRPO reinforcement learning algorithm** through Unsloth's efficient training framework. We investigate whether RL-driven "reasoning" enhancement can improve small-molecule therapeutic development capabilities in non-reasoning-optimized models.

## 🔑 Key Features

- **Novel RL Approach**: Implements GRPO (Generalized Reinforcement Learning Policy Optimization) instead of standard SFT
- **VRAM Efficiency**: Leverages [Unsloth](https://github.com/unslothai/unsloth) for 2-5x faster training with 70% less memory usage
- **Therapeutic Focus**: Targets small-molecule development challenges through RL reward shaping
- **Reasoning Exploration**: Tests if "aha moment" reasoning emergence (observed in DeepSeek-R1) can be induced in TxGemma

## ⚙️ Technical Approach

**Base Model**  
[TxGemma](https://blog.research.google/2024/02/txgemma-open-models-to-improve-therapeutics.html) (9B-27B parameter, TxGemma models, fine-tuned from Gemma 2 using 7 million training examples, are open models designed for prediction and conversational therapeutic data analysis.)

**Key Components**  
1. **GRPO Algorithm**: Modified RL approach from [DeepSeek-R1]([https://arxiv.org/pdf/2501.12948])
2. **Unsloth Framework**: Memory-optimized LoRA fine-tuning
3. Custom reward model focusing on:
   - Molecular validity constraints
   - Binding affinity predictions
   - Synthetic accessibility scores

## 📚 Resources

| Resource | Description |
|----------|-------------|
| [Original TxGemma Colab](https://colab.research.google.com/github/google-gemini/gemma-cookbook/blob/main/TxGemma/[TxGemma]Finetune_with_Hugging_Face.ipynb) | Google's SFT implementation baseline |
| [GRPO Paper]([https://arxiv.org/pdf/2501.12948]) | DeepSeek's RL optimization methodology |
| [Unsloth Docs](https://github.com/unslothai/unsloth) | Memory-efficient training framework |
