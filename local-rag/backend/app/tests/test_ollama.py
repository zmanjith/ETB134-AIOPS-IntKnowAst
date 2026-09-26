from LLM.ollama_service import OllamaService

llm = OllamaService()

answer = llm.generate(
    "Explain what Kubernetes is in one sentence."
)

print(answer)