from retrieval.retriever import Retriever

retriever = Retriever()

question = "Why did the payment service fail to connect to the database?"

results = retriever.retrieve(question)

for result in results:

    print("=" * 60)

    print("Score:", result.score)

    print("Source:", result.payload["source"])

    print(result.payload["text"][:500])