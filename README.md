# 🧠 Code Summarization and Evaluation using LLMs_DeepSeek_LLaMA_Cohere_Gemini
This research-oriented project investigates the capabilities of modern Large Language Models (LLMs)—specifically those deployed locally via Ollama (e.g., DeepSeek, LLaMA3)—for automated code summarization across multiple programming languages. The core objective is to systematically evaluate the impact of advanced prompting strategies on summarization performance across Python, JavaScript, and Java, using industry-standard evaluation metrics.

# 📌 Key Features:
**🔍 Prompt Engineering:** Implements five techniques — Zero-Shot, Few-Shot, Chain-of-Thought, Critique, and Expert.

**🤖 Multi-LLM Support:** Compare summaries across Cohere(via API), Gemini(via API), DeepSeek (via Ollama Framework), and LLaMA3 (via Ollama Framework).

**📊 Evaluation Metrics:** BLEU, ROUGE-L, METEOR, BERTScore.

**🧪 Dataset Coverage:** Experiments span Python, JavaScript, and Java using CodeXGLUE and CodeSearchNet Datasets.

**📑 IEEE-Style Report:** Comprehensive 12+ page academic report with reproducible experiments.

# 🚀 Key Highlights:
**🔧 Prompt Engineering Techniques:**
I implemented and benchmarked five prompting strategies designed to optimize LLM performance for source code summarization:

_Zero-Shot:_ Direct summarization without context.

_Few-Shot:_ Uses annotated examples in the prompt context.

_Chain-of-Thought:_ Guides the model through step-wise reasoning.

_Critique Prompting:_ Enforces self-review and refinement loops.

_Expert Simulation:_ Frames responses as if from a senior developer.

**🧠 Multi-LLM Backend (Local Inference):**
Instead of relying on cloud-based APIs, I leveraged locally hosted LLMs using Ollama for full control, reproducibility, and offline experimentation (along with LLMs using APIs):

-> DeepSeek-Coder (via Ollama)

-> LLaMA3 (via Ollama)

These models are wrapped using modular Python interfaces that support prompt injection, streaming, and output normalization.

**📊 Evaluation Metrics:**
I computed the following automatic evaluation metrics for objective comparison:

-> BLEU (n-gram overlap)

-> ROUGE-L (longest common subsequence)

-> METEOR (semantic-aware matching)

-> BERTScore (contextual embedding similarity using sentence-transformers)

# 📁 Project Structure:

code-summarization/ ├── data/ # Dataset download & preprocessing ├── models/ # LLM wrappers (deepseek, llama) ├── prompts/ # Prompt templates & techniques ├── evaluation/ # Metric calculations and statistical tests ├── results/ # Summary outputs and evaluation results └── main.py # Pipeline entry point

Note: "preprocessed_data" and "raw_data" can be downloaded from drive link given here https://drive.google.com/drive/folders/1pUfbv9NSXXTbkQxr63yhAz6D0vGs7iOV?usp=sharing

It also contains the python scripts to download the dataset from web and also to preprocess the dataset, which is used to generate the summaries.

# 🧪 Evaluation Pipeline:

1. **Preprocess datasets** from CodeXGLUE.

2. **Generate summaries** using each LLM with different prompting strategies.

3. **Evaluate quality** using BLEU, ROUGE, METEOR, and BERTScore.

4. **Run statistical tests** (paired t-test, ANOVA) to assess significance.

5. **Export results** to JSON and render in report/visualizations.


# 📚 Datasets:

**Source:** CodeXGLUE (https://github.com/microsoft/CodeXGLUE)

**Languages:** Python (251k+ functions), JavaScript (58k+ functions), Java (164k+ functions)

**Preprocessing Steps:** Length filtering, deduplication, normalization

# 📄 Report:

📘 IEEE-style academic paper included in /report, formatted for 2-column publication. Includes dataset breakdowns, prompt templates, evaluation results, statistical significance analysis, and limitations.

# 🤝 Contributor Tilak Brahmbhatt (202411016) — M.Tech ICT (Software Systems), DA-IICT
