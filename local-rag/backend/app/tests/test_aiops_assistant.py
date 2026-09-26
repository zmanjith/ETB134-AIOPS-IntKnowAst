from rag.rag_service import RagService

assistant = RagService()

question = "Why did the payment service fail to start?"

response = assistant.ask(question)

print("=" * 80)
print("QUESTION")
print("=" * 80)
print(response["question"])

print()

print("=" * 80)
print("ANSWER")
print("=" * 80)
print(response["answer"])

print()

print("=" * 80)
print("SOURCES")
print("=" * 80)

for source in response["sources"]:
    print(source)