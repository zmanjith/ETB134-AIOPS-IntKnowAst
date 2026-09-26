from rag.rag_service import RagService

rag = RagService()

response = rag.ask(
    "Why is my pod in CrashLoopBackOff?"
)

print("\nQuestion:")
print(response["question"])

print("\nAnswer:")
print(response["answer"])

print("\nSources:")
for source in response["sources"]:
    print("-", source)