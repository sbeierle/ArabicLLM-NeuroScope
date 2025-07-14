# arabicllm/analyze_prompt_activation.py
# Core script to measure LLM activation & norm strength per prompt

import torch
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
from pathlib import Path
import argparse
import numpy as np

# --- Init ---
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--output", type=str, default="activation_report.json")
    parser.add_argument("--layers", type=int, default=32)
    return parser.parse_args()

# --- Activation Tracer ---
def trace_activations(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]

    activations = {}
    def save_hook(layer_id):
        def hook(module, input, output):
            norms = torch.norm(output[0], dim=-1).detach().cpu().numpy()
            activations[f"layer_{layer_id}"] = norms.tolist()
        return hook

    handles = []
    for i, layer in enumerate(model.model.layers):
        handles.append(layer.mlp.register_forward_hook(save_hook(i)))

    with torch.no_grad():
        _ = model.generate(input_ids, max_new_tokens=50)

    for h in handles:
        h.remove()

    return activations, input_ids.shape[1]

# --- Main Run ---
def main():
    args = get_args()
    model = AutoModelForCausalLM.from_pretrained(args.model_path, torch_dtype=torch.float16).eval()
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)

    activations, num_tokens = trace_activations(model, tokenizer, args.prompt)
    
    out = {
        "prompt": args.prompt,
        "input_tokens": num_tokens,
        "activations": activations
    }

    with open(args.output, "w") as f:
        json.dump(out, f, indent=2)

    print(f"[✔] Saved report to {args.output}")

if __name__ == "__main__":
    main()
