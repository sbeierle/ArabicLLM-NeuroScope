# 📚 Glossary – Key Concepts in ArabicLLM-NeuroScope

This glossary provides simple explanations for the core terms used in this project, including token-level concepts, neuron activations, and evaluation techniques for LLMs on Arabic input (Fusha, Dialect) and English.

---

## 🔤 Terminology

| Term | Simple Explanation |
|------|---------------------|
| **Prompt** | The input question or instruction you give to an LLM. |
| **Token** | A small unit of text, like a word or part of a word. |
| **Tokenizer** | Splits text into tokens that the model can understand. |
| **Activation Norm** | Measures how strongly a token activates neurons in the model. Higher = deeper processing. |
| **Layer Norm** | A numerical value showing the strength of a token's activation in a specific layer. |
| **‖h‖ (Vector Norm)** | A formula to measure total activation strength of a token across its dimensions. |
| **Firepower** | Total sum of norms across all layers for a token. Shows how much attention it received. |
| **NER (Named Entity Recognition)** | Detects named things like countries, places, people, etc. |
| **Morphology** | Examines the structure of words (root, plural, tense, etc.). |
| **Token Fragility** | Measures how stably a word is tokenized – does it break into awkward parts? |
| **Logit** | The raw score a model gives each token before converting to probabilities. |
| **Decoder** | The model's part that generates the next token based on context. |
| **Bias** | Any preference built into the model (e.g., for English over Arabic). |
| **3D Plotly Map** | An interactive plot showing relationships between input type, layer, and activation norm. |
| **Spiderplot** | A radial graph comparing NER, morphology, and token stability across languages. |

---

## 🧠 How is the Vector Norm ‖h‖ Calculated?

A token goes through a transformer layer and activates **many neurons** (e.g., 4096 values in hidden state).  
The **norm** summarizes that high-dimensional vector into one number that shows its **overall strength**.

### 🧮 Formula:

\[
‖h‖ = \sqrt{h_1^2 + h_2^2 + \cdots + h_d^2}
\]

- \( h_1, h_2, ..., h_d \): individual activation values of the token
- Result: one single number → the **strength of token activation** in that layer

---

## 🔢 What Are Logits?

At the final step of decoding, the model assigns each token in the vocabulary a **logit** (a raw score).  
These logits are then converted to **probabilities** using the **Softmax** function.

### Example:

| Token     | Logit | Probability |
|-----------|--------|-------------|
| `"AI"`    | 15.2   | 70%         |
| `"Banana"`| 5.3    | 15%         |
| `"Beach"` | 3.8    | 10%         |
| `"Qatar"` | 1.2    | 5%          |

→ The token with the highest logit usually becomes the output — unless **sampling**, **temperature**, or **Top-K** is applied.

---

## ✨ Tip

If you're analyzing Arabic prompts and notice **low activation norms**, **high token fragility**, or **poor NER coverage** – this may indicate **semantic bias**, **vocabulary sparsity**, or **lack of dialect robustness**.

That's exactly what `ArabicLLM-NeuroScope` was built to uncover.

