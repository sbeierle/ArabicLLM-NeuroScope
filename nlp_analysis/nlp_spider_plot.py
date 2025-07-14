import json
import matplotlib.pyplot as plt
import numpy as np

def load_scores(filepaths):
    scores = {}
    for path in filepaths:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            label = path.replace("_result.json", "").replace(".json", "").replace("ner_", "")
            scores[label] = data
    return scores

def plot_spider(scores):
    categories = ["ner_score", "token_split_score", "morph_score"]
    labels = list(scores.keys())
    num_vars = len(categories)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for label in labels:
        values = [scores[label].get(c, 0) for c in categories]
        values += values[:1]
        ax.plot(angles, values, label=label)
        ax.fill(angles, values, alpha=0.2)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    ax.set_ylim(0, 1)
    ax.set_title("Arabic LLM NLP Evaluation")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig("nlp_spider_plot.png", dpi=300)

if __name__ == "__main__":
    scores = load_scores(["ner_result.json"])
    plot_spider(scores)
