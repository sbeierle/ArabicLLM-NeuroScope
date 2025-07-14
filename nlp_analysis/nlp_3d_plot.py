import json
import plotly.graph_objects as go

# Lade JSON
with open("ner_result.json", "r", encoding="utf-8") as f:
    ner = json.load(f)

# Daten vorbereiten
dims = ["NER (Fusha)", "Token Split Fragility", "Morph Sensitivity"]
scores = [ner["ner_score"], ner["token_split_score"], ner["morph_score"]]

# 3D "Bar"-Effekt durch Linien + Marker
fig = go.Figure()

for i, (dim, score) in enumerate(zip(dims, scores)):
    fig.add_trace(go.Scatter3d(
        x=[i, i], y=[0, 0], z=[0, score],
        mode="lines+markers+text",
        marker=dict(size=6),
        line=dict(width=10),
        text=[None, f"{score:.2f}"],
        textposition="top center",
        name=dim
    ))

# Achsen und Layout
fig.update_layout(
    title="Arabic NLP Evaluation (NER / Morphology / Split Robustness)",
    scene=dict(
        xaxis=dict(title="Metric Index", tickvals=list(range(len(dims))), ticktext=dims),
        yaxis=dict(title=""),
        zaxis=dict(title="Score", range=[0, 1]),
    ),
    margin=dict(l=20, r=20, b=20, t=50)
)

fig.write_html("nlp_3d_eval.html")
print("✅ Exported: nlp_3d_eval.html")
