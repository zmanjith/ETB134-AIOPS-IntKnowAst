from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Connect to Qdrant
client = QdrantClient(
    host="localhost",
    port=6333
)

# Initialize the sentence transformer model for generating embeddings.
model = SentenceTransformer("all-MiniLM-L6-v2")

# Define a function for performing semantic search.
def semantic_search(query, limit=5):
    # Convert quer  y to embedding
    query_vector = model.encode(query).tolist()

    # UPDATED: Changed client.search -> client.query_points
    # UPDATED: Changed query_vector= -> query=
    results = client.query_points(
        collection_name="documents",
        query=query_vector,
        limit=limit
    )
    return [
        hit.payload["text"]
        for hit in results.points
    ]

# Define a function to display the search results in a readable format.
def display_results(results):
    print("\nTop Matches:\n")

    # UPDATED: Changed 'results' to 'results.points' to loop through the actual hits
    for idx, result in enumerate(results.points, start=1):
        score = round(result.score, 4)
        text = result.payload.get("text", "")

        print(f"{idx}. Score: {score}")
        print(text[:300])
        print("-" * 50)

# Main block execution
if __name__ == "__main__":
    query = input("Enter your search query: ")
    search_results = semantic_search(query)
    display_results(search_results)