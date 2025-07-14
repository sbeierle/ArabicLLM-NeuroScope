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
This analysis measures token firepower across layers using activation norms:
$\|h_i\| = \sqrt{h_1^2 + h_2^2 + ... + h_d^2}$

Higher norms across more layers = deeper processing. Lower activation = bias, poor embedding, or soft filters.

🧪 Tested prompts:

* English: "What is the history of artificial intelligence in the Middle East?"
* Fusha: "ما هو تاريخ الذكاء الاصطناعي في الشرق الأوسط؟"
* Dialect: "وش صار مع الذكاء الاصطناعي بالخليج؟"

📊 Outputs:

* Per-layer norms `layer_norm_comparison.png`
* Firepower comparison `firepower_comparison.png`
* Interactive 3D HTML landscape `activation_3d_plot.html`

## 🧬 NLP Semantic Evaluation (NER, Morphology, Token Fragility)
This module explores:

* 🧠 NER recognition of entities (e.g., countries, tech terms)
* 🧱 Morphological patterns in dialect Arabic
* 🧩 Token fragility: how Arabic phrases are split into unstable subwords

🎯 Goal: Reveal biases in tokenizer, vocab sparsity, and semantic integrity of LLMs trained mostly on English.

📁 Files:

* `nlp_eval.py` (entry point)
* `ner_result.json`
* `nlp_spider_plot.png` (NER coverage, language comparison)
* `prompt_ner_fusha.txt`, `prompt_token_fragility.txt`

## 🔭 Visualizations
* 📈 `layer_norm_comparison.png`: Layer-wise processing strength
* 🔥 `firepower_comparison.png`: Global token intensity
* 🧠 `3D_activation_landscape2.png`: Prompt vs. layer vs. norm
* 🕸️ `nlp_spider_plot.png`: Semantic reach (NER & Morphology)
* 🧩 Mermaid diagrams: Flow logic & architecture

## 🚀 How to Run
```bash
# Step 1: Prompt Activation
python analyze_prompt_activation.py \
  --model_path ../patched_model_main_bin \
  --prompt "$(cat prompt_fusha.txt)" \
  --output fusha_report.json

# Step 2: NLP Analysis
python nlp_eval.py prompt_ner_fusha.txt ner_result.json

# Step 3: Plotting
python plot_layer_norms_all.py
python plot_firepower.py
python nlp_spider_plot.py
python plot_3d_layernorm.py
