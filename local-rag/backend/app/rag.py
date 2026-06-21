import ollama

from search import semantic_search
from prompt_generator import build_prompt


def ask(question):

    chunks = semantic_search(question)

    context = "\n\n".join(chunks)

    prompt = build_prompt(
        question,
        context
    )

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]