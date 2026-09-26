import datetime
import os
from urllib import response
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance
from qdrant_client.models import VectorParams
from qdrant_client.models import PointStruct


class QdrantService:

    COLLECTION_NAME = "documents"

    def __init__(self):

        self.client = QdrantClient(
            host=os.getenv("QDRANT_HOST", "localhost"),
            port=6333
        )


    def create_collection(self):

        if self.client.collection_exists(
            self.COLLECTION_NAME
        ):
            return

        self.client.create_collection(

            collection_name=self.COLLECTION_NAME,

            vectors_config=VectorParams(

                size=384,

                distance=Distance.COSINE

            )

        )

        print("Collection created")
    
    def upsert(self, embedded_chunks):

        points = []

        for chunk in embedded_chunks:

            points.append(

                PointStruct(

                    id=str(uuid.uuid4()),

                    vector=chunk["embedding"],

                    payload = {

                        "chunk_id": chunk["chunk_id"],
                        
                        "text": chunk["text"],

                        "source": chunk["metadata"]["source"],

                        "category": chunk["metadata"]["category"],

                        "technology": chunk["metadata"]["technology"],

                        "document_type": chunk["metadata"]["document_type"],

                        "page": chunk["metadata"]["page"],

                        "chunk": chunk["metadata"]["chunk"],
                        
                        "ingested_at": datetime.datetime.now().isoformat()

                    }

                )

            )

        self.client.upsert(

        collection_name=self.COLLECTION_NAME,

        points=points

         )   

        print(

            f"{len(points)} vectors uploaded."

        )
        
    def search(self, query_vector, 
           limit=5):

        response = self.client.query_points(

        collection_name=self.COLLECTION_NAME,

        query=query_vector,

        limit=limit

        )
        return response.points