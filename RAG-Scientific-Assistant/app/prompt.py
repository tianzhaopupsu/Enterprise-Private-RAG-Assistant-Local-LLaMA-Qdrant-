def build_prompt(question, contexts):

    context_text = "\n\n".join(
        [f"[Source {i+1}]\n{c['text']}" for i, c in enumerate(contexts)]
    )

    return f"""
You are a strict information extraction system.

TASK:
Answer the question using ONLY the context.

RULES:
- If the answer is not explicitly in the context, output ONLY:
  Not found in provided documents.
- Do NOT explain anything.
- Do NOT add notes, comments, or follow-up questions.
- Do NOT repeat the question.
- Do NOT include headings or labels.
- Output must be 1–3 sentences maximum.

CONTEXT:
{context_text}

QUESTION:
{question}

ANSWER:
"""
