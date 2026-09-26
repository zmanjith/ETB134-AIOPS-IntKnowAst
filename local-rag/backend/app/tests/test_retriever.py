from retrieval.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve( "Why is my pod restarting?" )

for result in results:
    
    print(f"Score : {result.score:.3f}")

    print(f"Source: {result.payload['source']}")

    print(result.payload["text"][:250])

    print("-" * 80)