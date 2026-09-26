from pathlib import Path

from loaders.knowledge_loader import KnowledgeLoader
from metadata.metadata_service import MetadataService
from chunking.splitter import DocumentSplitter
from embeddings.embedding_service import EmbeddingService
from operational_inputs.log_summarizer import LogSummarizer
from vectorstore.qdrant_service import QdrantService


knowledge_path = Path("../../knowledge")

# 1. Load documents
loader = KnowledgeLoader()
documents = loader.load(knowledge_path)

print(f"Loaded {len(documents)} documents")

# 2. AI analysis (only for document types that need it)
processed_documents = []

log_creator = LogSummarizer()
for document in documents:

    if document["document_type"] == "log":
        document = log_creator.summarize(document)
        print(f"Summarized log document: {document['document_type']}")

    processed_documents.append(document)
    print(f"Processed document: {document['document_type']}")

# 3. Enrich metadata
metadata_service = MetadataService()
documents = metadata_service.enrich_documents(processed_documents)

print("Metadata enrichment completed")

# 4.Split into chunks
splitter = DocumentSplitter()
chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# 5.Generate embeddings
embedding_service = EmbeddingService()
embedded_chunks = embedding_service.embed_chunks(chunks)

print(f"Generated {len(embedded_chunks)} embeddings")

# 6.Upload to Qdrant
qdrant = QdrantService()
qdrant.create_collection()
qdrant.upsert(embedded_chunks)

print("Knowledge ingestion completed successfully.")