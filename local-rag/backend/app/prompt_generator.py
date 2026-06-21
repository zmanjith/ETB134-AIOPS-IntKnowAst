def build_prompt(question, context):

    prompt = f"""
You are an AI assistant.

Answer ONLY from the supplied context.

If the answer is not found,
say:

"I could not find the answer in the documents."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt