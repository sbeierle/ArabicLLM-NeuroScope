import json
import plotly.graph_objects as go

# Lokale JSON-Dateien
files = {
    "English": "en_report.json",
    "Fusha": "fusha_report.json",
    "Dialect": "dialect_report.json"
}

traces = []
for lang_idx, (label, file_path) in enumerate(files.items()):
    with open(file_path, "r") as f:
        data = json.load(f)
        layers = sorted(data["activations"].keys(), key=lambda x: int(x.split("_")[1]))
        norms = [data["activations"][layer][0] for layer in layers]
        trace = go.Scatter3d(
            x=list(range(len(norms))),
            y=[label] * len(norms),
            z=norms,
            mode='lines+markers',
            name=label,
            marker=dict(size=6, symbol="circle"),
            line=dict(width=4)
        )
        traces.append(trace)

layout = go.Layout(
    title="🧠 3D Activation Landscape – Arabic vs English Prompts",
    scene=dict(
        xaxis=dict(title="Layer"),
        yaxis=dict(title="Prompt Type"),
        zaxis=dict(title="Activation Norm")
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig = go.Figure(data=traces, layout=layout)
fig.write_html("activation_3d_plot.html")
fig.show()
