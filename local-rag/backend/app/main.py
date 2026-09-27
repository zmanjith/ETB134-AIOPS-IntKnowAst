from rag.rag_service import RagService

rag_service = RagService()

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    result = rag_service.ask(question)

    print("\nAnswer:")
    print(result["answer"])
    print("\nSources:", result["sources"])
    