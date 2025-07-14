import json
import sys

def mock_nlp_eval(prompt_path, output_path):
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt = f.read()

    # Simulierte Scores (echte Logik später integrierbar)
    if "مكة" in prompt or "المدينة" in prompt:
        result = {"ner_score": 0.75, "token_split_score": 0.60, "morph_score": 0.4}
    elif "Najdi" in prompt:
        result = {"ner_score": 0.2, "token_split_score": 0.3, "morph_score": 0.1}
    else:
        result = {"ner_score": 0.5, "token_split_score": 0.5, "morph_score": 0.5}

    with open(output_path, 'w', encoding='utf-8') as out:
        json.dump(result, out, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nlp_eval.py <prompt_file.txt> <output_file.json>")
        sys.exit(1)
    mock_nlp_eval(sys.argv[1], sys.argv[2])
