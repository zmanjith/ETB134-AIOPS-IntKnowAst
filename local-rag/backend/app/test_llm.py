import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What is Kubernetes?"
        }
    ]
)

print(response["message"]["content"])