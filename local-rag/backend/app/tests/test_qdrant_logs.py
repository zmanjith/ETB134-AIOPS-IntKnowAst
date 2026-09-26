from vectorstore.qdrant_service import QdrantService

qdrant = QdrantService()

results = qdrant.client.scroll(
    collection_name=qdrant.COLLECTION_NAME,
    limit=10,
    with_payload=True
)

for point in results[0]:

    print("=" * 60)
    print("ID:", point.id)
    print("Source:", point.payload.get("source"))
    print("Category:", point.payload.get("category"))
    print("Technology:", point.payload.get("technology"))
    print(point.payload.get("text")[:500])