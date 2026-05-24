from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client.models import PointStruct

model = SentenceTransformer('all-MiniLM-L6-v2')

client = QdrantClient(
    host="localhost",
    port=6333
)

query = "Which is the Lab?"

query_vector = model.encode(query).tolist()

response = client.query_points(
    collection_name="documents",
    query=query_vector,          # Changed 'query_vector' parameter to 'query'
    limit=3
)

for result in response.points:
    print("\nScore:", result.score)
    print(result.payload["text"])