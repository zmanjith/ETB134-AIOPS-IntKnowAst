import ollama
import os

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
        model=os.getenv(   "OLLAMA_HOST",
                    "http://ollama:11435"
                    ),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]