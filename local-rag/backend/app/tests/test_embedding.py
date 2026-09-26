from pathlib import Path

from loaders.knowledge_loader import KnowledgeLoader
from chunking.splitter import DocumentSplitter
from embeddings.embedding_service import EmbeddingService

loader = KnowledgeLoader()

documents = loader.load(Path("../../knowledge"))

splitter = DocumentSplitter()

chunks = splitter.split_documents(documents)

embedding_service = EmbeddingService()

embedded = embedding_service.embed_chunks(chunks)

print(embedded[3].keys())