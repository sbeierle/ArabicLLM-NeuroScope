# plot_firepower.py

import json
import matplotlib.pyplot as plt
import numpy as np

files = {
    "English": "en_report.json",
    "Fusha": "fusha_report.json",
    "Dialect": "dialect_report.json"
}

firepower_data = {}

for label, file in files.items():
    with open(file, "r") as f:
        data = json.load(f)
        norms = [data["activations"][layer][0] for layer in sorted(data["activations"].keys(), key=lambda x: int(x.split("_")[1]))]
        firepower_data[label] = norms

layers = list(range(len(next(iter(firepower_data.values())))))
width = 0.25
x = np.arange(len(layers))

plt.figure(figsize=(12, 6))
for i, (label, norms) in enumerate(firepower_data.items()):
    plt.bar(x + i * width, norms, width=width, label=label)

plt.title("Layer Firepower – Norm Intensity per Prompt")
plt.xlabel("Layer")
plt.ylabel("Activation Norm")
plt.xticks(x + width, layers)
plt.legend()
plt.tight_layout()
plt.savefig("firepower_comparison.png")
plt.show()
