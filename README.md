# ArabicLLM-NeuroScope
🎯 Multilingual LLM Evaluation Suite for Arabic NLP.

Analyze activation flow, token strength & semantic bias of prompts in Fusha, Dialect, and English.

## 🧠 Overview
ArabicLLM-NeuroScope is a lightweight, reproducible framework for analyzing the behavior of Large Language Models (LLMs) when processing prompts in:

🇬🇧 English (reference baseline)
🇸🇦 Modern Standard Arabic (Fusha)
🗣️ Spoken Arabic Dialects (e.g. Saudi dialect)

It visualizes token activations, layer norms, and prompt flow across transformer layers – both neuronally and semantically.
```
## 📂 Folder Structure
ArabicLLM-NeuroScope/
├── prompt_analysis/           # Norm activation analysis
├── nlp_analysis/              # Token-level NLP evaluation
├── visual/                    # Plots (2D/3D PNG & HTML)
├── data/                      # Prompt files & JSON outputs
├── diagrams/                  # Mermaid diagrams & flowcharts
└── README.md
```
## 🔍 Prompt Activation Analysis

This module measures token firepower across layers using activation norms:  
$\|h_i\| = \sqrt{h_1^2 + h_2^2 + ... + h_d^2}$

📌 Interpretation:  
Higher norms across more layers → deeper processing  
Lower activation → soft filters, poor embedding, or weak tokenization

🧪 Example prompts:

- English: `"What is the history of artificial intelligence in the Middle East?"`
- Fusha: `"ما هو تاريخ الذكاء الاصطناعي في الشرق الأوسط؟"`
- Dialect: `"وش صار مع الذكاء الاصطناعي بالخليج؟"`

📊 Outputs:

- 📈 [`visual/layer_norm_comparison.png`](visual/layer_norm_comparison.png)
- 🔥 [`visual/firepower_comparison.png`](visual/firepower_comparison.png)
- 🧠 Interactive 3D: [`visual/activation_3d_plot.html`](visual/activation_3d_plot.html)

---

## 🧬 NLP Semantic Evaluation (NER, Morphology, Token Fragility)

Located in [`nlp_analysis/`](nlp_analysis/)

This module explores:

- 🧠 NER entity detection (e.g., tech, countries)
- 🧱 Morphological evaluation of dialect prompts
- 🧩 Token Fragility – how robust is the tokenizer for Arabic?

🎯 Goal: Reveal gaps in vocabulary coverage, semantic integrity, and LLM robustness in non-English languages.

📁 Key Files:

- Entry: [`nlp_analysis/nlp_eval.py`](nlp_analysis/nlp_eval.py)
- Prompts: [`nlp_analysis/prompt_ner_fusha.txt`](nlp_analysis/prompt_ner_fusha.txt)
- NER JSON: [`nlp_analysis/ner_result.json`](nlp_analysis/ner_result.json)
- Spider Plot: [`visual/nlp_spider_plot.png`](visual/nlp_spider_plot.png)
- Interactive: [`nlp_analysis/nlp_3d_eval.html`](nlp_analysis/nlp_3d_eval.html)

---

## 🔭 Visualizations

All plots are located in [`visual/`](visual/)

- 📈 [`layer_norm_comparison.png`](visual/layer_norm_comparison.png): Mean norm per layer by language
- 🔥 [`firepower_comparison.png`](visual/firepower_comparison.png): Sum of token norm activations
- 🧠 [`3D_activation_landscape2.png`](visual/3D_activation_landscape2.png): Prompt vs. Layer vs. Norm
- 🕸️ [`nlp_spider_plot.png`](visual/nlp_spider_plot.png): Semantic/NLP coverage
- 🧩 [`mermaid/mermaid_arabic_llm1.png`](mermaid/mermaid_arabic_llm1.png): Flowchart of entire system

---

## 🚀 How to Run

```bash
# Step 1: Prompt Activation (via Norms)
python scripts/analyze_prompt_activation.py \
  --model_path ../patched_model_main_bin \
  --prompt "$(cat prompts/prompt_fusha.txt)" \
  --output reports/fusha_report.json

# Step 2: NLP Evaluation
python nlp_analysis/nlp_eval.py \
  nlp_analysis/prompt_ner_fusha.txt \
  nlp_analysis/ner_result.json

# Step 3: Plotting
python scripts/plot_layer_norms_all.py
python scripts/plot_firepower.py
python nlp_analysis/nlp_spider_plot.py
python scripts/plot_3d_layernorm.py
