#!/bin/bash

# Create main project structure
mkdir -p local-rag/backend/app
mkdir -p local-rag/backend/data
mkdir -p local-rag/backend/scripts
mkdir -p local-rag/frontend

# Create empty files
touch local-rag/backend/requirements.txt
touch local-rag/backend/docker-compose.yml

echo "✅ local-rag project structure created successfully!"
