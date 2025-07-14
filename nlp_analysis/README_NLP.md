
# 🧠 Arabic LLM NLP Evaluation Module

This module evaluates semantic understanding in Arabic prompts using linguistic metrics.

## 🔍 Purpose

To complement token-level and norm-based activation analysis with **linguistic quality metrics**, including:
- Named Entity Recognition (NER)
- Morphological sensitivity
- Token fragmentation (splitting of Arabic prefixes/suffixes)

## 📁 Files

| File                       | Description |
|---------------------------|-------------|
| `prompt_ner_fusha.txt`      | Classical Arabic prompt testing model's ability to recognize **Islamic holy sites** |
| `prompt_morph_dialect.txt`  | Dialect test measuring **Najdi vs. MSA form recognition** |
| `prompt_token_fragility.txt`| Tests **token splitting** and prefix handling in Arabic grammar |

## ✍️ Prompt Details

### 1. `prompt_ner_fusha.txt`

**Prompt:**
> أذكر كل الأماكن المقدسة في الإسلام التي وردت في هذا النص: زار المسلمون مكة والمدينة في رحلة الحج.

- Purpose: Test if LLM detects "مكة" and "المدينة" as holy places.
- Category: Named Entity Recognition (NER)
- Expected: High NER score if both entities are semantically processed.

---

### 2. `prompt_morph_dialect.txt`

**Prompt:**
> كيف تقول 'ich gehe' auf Najdi-Dialekt? Gib auch Varianten in Hocharabisch an.

- Purpose: See if dialectal forms like "أمشي" or "أروح" are returned.
- Category: Morphological Variance
- Expected: Low score for dialect if model lacks coverage.

---

### 3. `prompt_token_fragility.txt`

**Prompt:**
> ما الفرق بين 'مدينة' و 'بالمدينة'؟ وضح تفصيل التوكنات.

- Purpose: Evaluate how Arabic prefixes like "بـ" affect token splitting.
- Category: Token Fragmentation / Prefix Handling
- Expected: High token-split score = model poorly tokenizes such constructs.

---

## 📈 Output Format

Each evaluation will output:

```json
{
  "ner_score": 0.75,
  "token_split_score": 0.60,
  "morph_score": 0.4
}
```

These scores can then be visualized or integrated into your `arabicllm` GitHub project.

## ⚙️ Run Example

```bash
python nlp_eval.py prompt_ner_fusha.txt ner_result.json
```

---

© 2025 arabicLLM | NLP × Interpretability × Token Metrics
