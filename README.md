# 🧠 Code Summarization and Evaluation using LLMs_DeepSeek_LLaMA_Cohere_Gemini
This research-oriented project investigates the capabilities of modern Large Language Models (LLMs)—specifically those deployed locally via Ollama (e.g., DeepSeek, LLaMA3)—for automated code summarization across multiple programming languages. The core objective is to systematically evaluate the impact of advanced prompting strategies on summarization performance across Python, JavaScript, and Java, using industry-standard evaluation metrics.

# 📌 Key Features:
🔍 Prompt Engineering: Implements five techniques — Zero-Shot, Few-Shot, Chain-of-Thought, Critique, and Expert.

🤖 Multi-LLM Support: Compare summaries across Cohere(via API), Gemini(via API), DeepSeek (via Ollama Framework), and LLaMA3 (via Ollama Framework).

📊 Evaluation Metrics: BLEU, ROUGE-L, METEOR, BERTScore.

🧪 Dataset Coverage: Experiments span Python, JavaScript, and Java using CodeXGLUE and CodeSearchNet Datasets.

📑 IEEE-Style Report: Comprehensive 12+ page academic report with reproducible experiments.

# 🚀 Key Highlights:
🔧 Prompt Engineering Techniques:
I implemented and benchmarked five prompting strategies designed to optimize LLM performance for source code summarization:

Zero-Shot: Direct summarization without context.

Few-Shot: Uses annotated examples in the prompt context.

Chain-of-Thought: Guides the model through step-wise reasoning.

Critique Prompting: Enforces self-review and refinement loops.

Expert Simulation: Frames responses as if from a senior developer.

🧠 Multi-LLM Backend (Local Inference)
Instead of relying on cloud-based APIs, I leveraged locally hosted LLMs using Ollama for full control, reproducibility, and offline experimentation (along with LLMs using APIs):

DeepSeek-Coder (via Ollama)

LLaMA3 (via Ollama)

These models are wrapped using modular Python interfaces that support prompt injection, streaming, and output normalization.

📊 Evaluation Metrics
I computed the following automatic evaluation metrics for objective comparison:

BLEU (n-gram overlap)

ROUGE-L (longest common subsequence)

METEOR (semantic-aware matching)

BERTScore (contextual embedding similarity using sentence-transformers)
