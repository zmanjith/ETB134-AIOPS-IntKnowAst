from embeddings.embedding_service import EmbeddingService
from vectorstore.qdrant_service import QdrantService


class Retriever:
    
    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.qdrant = QdrantService()
        
    def retrieve(self, question):

        # Use them directly
        query_vector = self.embedding_service.embed_query(question)
        results = self.qdrant.search(query_vector)
        return results