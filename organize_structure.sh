#!/bin/bash

echo "🧠 Creating project structure for ArabicLLM-NeuroScope..."

mkdir -p prompts reports visual scripts mermaid nlp_analysis

# === Prompts ===
mv prompt_*.txt prompts/

# === Reports ===
mv *_report.json reports/

# === Visuals ===
mv *_comparison.png visual/
mv 3D_activation_landscape*.png visual/
mv arabic_llm1_*.png visual/
mv activation_3d_plot.html visual/

# === Scripts ===
mv analyze_prompt_activation.py scripts/
mv plot_layer_norms_all.py scripts/
mv plot_firepower.py scripts/
mv plot_3d_layernorm.py scripts/

# === Mermaid ===
mv mermaid_*.png mermaid/
mv mermaid_graph_*.mmd mermaid/

# === NLP Evaluation ===
mv nlp_*.py nlp_analysis/
mv ner_result.json nlp_analysis/
mv prompt_morph_dialect.txt nlp_analysis/
mv prompt_token_fragility.txt nlp_analysis/
mv prompt_ner_fusha.txt nlp_analysis/
mv nlp_spider_plot.png nlp_analysis/

echo "✅ Done! All files organized into folders."
