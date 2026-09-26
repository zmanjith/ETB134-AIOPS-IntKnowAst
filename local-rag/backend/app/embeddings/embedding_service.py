
from sentence_transformers import SentenceTransformer

class EmbeddingService:  

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed_chunks(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        vectors = self.model.encode(texts)

        embedded_chunks = []

        for chunk, vector in zip(chunks, vectors):

            chunk["embedding"] = vector.tolist()

            embedded_chunks.append(chunk)

        return embedded_chunks
    
    def embed_query(self, question):

        vector = self.model.encode(question)

        return vector.tolist()