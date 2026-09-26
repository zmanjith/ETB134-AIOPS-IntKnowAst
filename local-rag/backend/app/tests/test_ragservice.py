from app.rag.rag_service import RagService

service = RagService()
result = service.ask("What is Kubernetes?")

print("Answer:\n", result["answer"])
print("\nSources:", result["sources"])

