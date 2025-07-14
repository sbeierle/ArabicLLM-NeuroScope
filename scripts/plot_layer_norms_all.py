# plot_layer_norms_all.py

import json
import matplotlib.pyplot as plt

# Dateipfade lokal im arabicllm/ Ordner
files = {
    "English": "en_report.json",
    "Arabic (Fusha)": "fusha_report.json",
    "Arabic (Saudi Dialect)": "dialect_report.json"
}

plt.figure(figsize=(12, 6))

for label, filename in files.items():
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        layers = sorted(data["activations"].keys(), key=lambda x: int(x.split("_")[1]))
        norms = [data["activations"][layer][0] for layer in layers]
        plt.plot(range(len(norms)), norms, label=label, marker="o")

plt.title("LLM Activation Norms per Layer – Arabic vs English")
plt.xlabel("Layer")
plt.ylabel("Activation Norm")
plt.legend()
plt.grid(True)
plt.xticks(range(len(norms)))
plt.tight_layout()
plt.savefig("layer_norm_comparison.png")
plt.show()
