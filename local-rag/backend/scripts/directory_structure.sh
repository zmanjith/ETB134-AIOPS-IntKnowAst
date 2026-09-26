#!/bin/bash

# Create directories
mkdir -p backend/app/{loaders,chunking,embeddings,vectorstore,retrieval,rag}

# Create files
touch backend/app/loaders/pdf_loader.py
touch backend/app/loaders/markdown_loader.py
touch backend/app/loaders/text_loader.py
touch backend/app/chunking/splitter.py
touch backend/app/embeddings/embedding_service.py
touch backend/app/vectorstore/qdrant_service.py
touch backend/app/retrieval/search.py
touch backend/app/rag/prompt_builder.py
touch backend/app/rag/rag_service.py
touch backend/app/api.py
touch backend/app/ingest.py

echo "RAG backend folder structure and files created successfully!"