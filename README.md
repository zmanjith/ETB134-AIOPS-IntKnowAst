# ETB134-AIOPS-IntKnowAst
Internal Knowledge Assistant Operations usign AI Model




Base Libraries Used
##########################

This combination of libraries is the standard modern stack for building Retrieval-Augmented Generation (RAG) applications, such as "Chat with your PDF" bots, intelligent agents, or custom document search engines.
Here is a breakdown of their roles:
1. LangChain (Core Framework) 

LangChain
Use: The central orchestrator that connects LLMs (like GPT-4) with external data sources, memory, and tools.
In AI Projects: It allows you to chain together prompting, retrieval, and generation steps. It handles the "logic" flow of the app (e.g., taking user input, searching a database, sending context to the LLM).
Key Features: Prompt templates, LLM wrappers, and memory management for chatbots. 


2. langchain-community (Integrations) 

Use: Contains third-party integrations, loaders, and tools that are not in the core langchain package.
In AI Projects: Allows seamless connection to vector databases (like Qdrant), PDF loaders, search tools (Google Search), and local/remote LLM providers. 


3. pypdf (Document Loading) 

Use: A pure-Python library for reading and extracting text from PDF files.
In AI Projects: Used in the "data ingestion" phase of RAG. It extracts text from user-uploaded PDFs so that the text can be chunked, embedded, and indexed for the LLM to search. 

4. sentence-transformers (Embeddings)
Use: A Python library for state-of-the-art text embeddings (turning text into numerical vectors).
In AI Projects: Crucial for semantic search. It turns your PDF text chunks and user queries into vectors that represent their meaning, allowing the system to find relevant information based on content, not just keywords. 

5. qdrant-client (Vector Database) 

Use: The client library for Qdrant, a high-performance vector search engine/database.
In AI Projects: Stores the numerical vectors created by sentence-transformers. It enables fast retrieval of the most relevant document chunks to be sent to the LLM. 

6. fastapi & uvicorn (Backend & Deployment) 

fastapi: A modern web framework for building APIs with Python. It is used to create the API endpoints for your AI app (e.g., /chat, /upload_doc).
uvicorn: A fast ASGI server implementation needed to run the FastAPI application.
In AI Projects: Turns your AI script into a usable application that can be queried by a frontend (like React or Streamlit). 


---

# AIOps Intelligent Knowledge Assistant (Open Source Edition)

## Project Overview

The goal of this project is to build an **Enterprise AIOps Intelligent Knowledge Assistant** capable of helping Site Reliability Engineers (SREs), DevOps Engineers, and Cloud Engineers troubleshoot operational issues using Retrieval-Augmented Generation (RAG) combined with Large Language Models (LLMs).

The final system should continuously ingest operational knowledge (Runbooks, Incidents, RCAs, Logs, Metrics, Kubernetes Events, AWS Documentation, etc.), convert that knowledge into semantic vectors, retrieve relevant operational information for user questions, and provide accurate AI-generated operational guidance.

The project is being built in **phases**, starting with a fully open-source implementation that can later be migrated to AWS services.

---

# Original Architecture (AWS Based)

The original architecture was designed using AWS managed services.

```text
Enterprise Applications
        │
        ▼
Logs / Metrics / Events
        │
        ▼
CloudWatch / Prometheus / Loki
        │
        ▼
Knowledge Builder
        │
        ▼
Amazon Bedrock Embeddings
        │
        ▼
OpenSearch / Vector Database
        │
        ▼
Amazon Bedrock LLM
        │
        ▼
AIOps Assistant API
        │
        ▼
Slack / Teams / Web UI
```

The objective was to build a cloud-native AIOps platform.

---

# Why We Changed

To avoid AWS costs during development, the implementation was redesigned using entirely open-source components while keeping the architecture cloud-portable.

AWS services will later replace individual components without changing the application architecture.

---

# Current Open Source Architecture

```text
Knowledge Repository
        │
        ▼
Discovery Service
        │
        ▼
Document Loaders
        │
        ▼
Metadata Service
        │
        ▼
Chunking Service
        │
        ▼
Embedding Service
        │
        ▼
Qdrant Vector Database
        │
        ▼
Retriever
        │
        ▼
Prompt Builder
        │
        ▼
Ollama LLM
        │
        ▼
FastAPI
        │
        ▼
Chat UI
```

---

# Phase 1 - Initial RAG Prototype

The project originally started with a very simple RAG implementation.

The first version simply:

* Read one PDF
* Split into chunks
* Generated embeddings
* Stored vectors in Qdrant

Architecture

```text
PDF

↓

Chunk

↓

Embedding

↓

Qdrant
```

This proved that semantic search worked.

However, this architecture was too tightly coupled.

---

# Phase 2 - Enterprise Architecture Refactoring

The project was redesigned into independent services following enterprise software architecture principles.

The ingestion pipeline became:

```text
Knowledge Repository

↓

Discovery Service

↓

Loader Factory

↓

Document Loader

↓

Metadata Service

↓

Chunking Service

↓

Embedding Service

↓

Qdrant Service
```

Each component now has a single responsibility.

---

# Discovery Service

Purpose:

Discover every document inside the Knowledge Repository.

Instead of hardcoding PDFs, the Discovery Service recursively scans the knowledge folder.

Example:

```text
knowledge/

runbooks/

incidents/

kubernetes/

aws/

docker/
```

Output:

A list of all files to be processed.

---

# Loader Factory

Instead of writing one PDF reader, a Loader Factory was introduced.

It automatically selects the correct loader.

Example:

```text
PDF

↓

PDFLoader

Markdown

↓

MarkdownLoader

Text

↓

TextLoader

Logs

↓

LogLoader (future)

JSON

↓

JSONLoader (future)
```

This allows adding new document types without modifying existing code.

---

# Document Loaders

Each loader converts its file type into one standardized document object.

Example

```python
{
    "text": "...",

    "source": "...",

    "filepath": "...",

    "category": "...",

    "document_type": "pdf"
}
```

All downstream services operate on this common document format.

---

# Metadata Service

Purpose:

Enrich every document with deterministic metadata.

Metadata includes:

* Source
* Filename
* Extension
* Category
* Technology
* Document Type

Example

```python
metadata = {

    "source":"CrashLoopBackOff.md",

    "category":"runbooks",

    "technology":"kubernetes",

    "document_type":"markdown"
}
```

Later, AI-based classification will enrich this metadata further.

---

# Chunking Service

The Chunking Service receives enriched documents.

Responsibilities:

* Split text into semantic chunks
* Preserve metadata
* Generate deterministic chunk identifiers

Each chunk contains:

```python
{
    "chunk_id": "...",

    "text":"...",

    "metadata": {...}
}
```

Chunk IDs are human-readable and deterministic.

Example

```text
runbooks/CrashLoopBackOff:p3:c2
```

During Qdrant storage, these IDs are converted into deterministic UUIDs while preserving the original chunk ID inside the payload.

---

# Embedding Service

Purpose:

Convert chunk text into numerical vectors.

Current model:

```
SentenceTransformer

all-MiniLM-L6-v2
```

The Embedding Service is completely independent of:

* PDFs
* Kubernetes
* AWS
* Qdrant

It only converts text into vectors.

---

# Qdrant Vector Store

Purpose:

Store semantic vectors.

Each point contains:

* UUID
* Embedding vector
* Payload

Payload includes:

```python
{
    "chunk_id": "...",

    "text": "...",

    "source": "...",

    "category": "...",

    "technology": "...",

    "page": 1,

    "chunk": 2
}
```

This enables semantic retrieval and metadata filtering.

---

# Retriever

The Retriever represents the beginning of the query pipeline.

Flow

```text
Question

↓

Embedding Service

↓

Qdrant Similarity Search

↓

Top K Chunks
```

Both documents and user questions use the same embedding model.

The Retriever currently returns semantic search results successfully.

---

# Current Pipeline Status

## Ingestion Pipeline

```text
Knowledge Repository

↓

Discovery

↓

Loader Factory

↓

Document Loader

↓

Metadata

↓

Chunking

↓

Embedding

↓

Qdrant
```

Completed.

---

## Query Pipeline

```text
User Question

↓

Embedding

↓

Retriever

↓

Relevant Chunks
```

Completed.

---

## Remaining Pipeline

```text
Relevant Chunks

↓

Prompt Builder

↓

Ollama

↓

FastAPI

↓

Chat UI
```

Currently under development.

---

# Capability-Based Roadmap

The project is divided into capabilities.

---

## Capability 1

Enterprise Knowledge Repository

Completed.

Includes:

* Knowledge discovery
* Loader Factory
* Multiple document loaders
* Metadata enrichment
* Chunking
* Embedding generation
* Vector database storage
* Semantic retrieval

---

## Capability 2

AIOps Intelligent Assistant

In Progress.

Components under development:

* Prompt Builder
* Ollama integration
* RAG orchestration
* FastAPI endpoint
* Chat interface

---

## Future Capabilities

### Capability 3

Operational Knowledge Builder

Automatically ingest:

* Logs
* Kubernetes Events
* Prometheus Alerts
* Loki Logs

---

### Capability 4

Incident Intelligence

Store:

* Incidents
* Root Cause Analyses
* Runbooks

Generate AI-assisted operational recommendations.

---

### Capability 5

Continuous Learning

Every resolved incident generates:

* RCA
* Runbook
* Knowledge update

The system continuously improves itself.

---

# Final Target Architecture

```text
Enterprise Applications
        │
        ▼
Logs / Metrics / Events
        │
 ┌──────────────┬──────────────┐
 │              │              │
 ▼              ▼              ▼
Loki      Prometheus     Alertmanager
        │
        ▼
Knowledge Builder
        │
        ▼
Discovery
        │
        ▼
Loader Factory
        │
        ▼
Document Loaders
        │
        ▼
Metadata Service
        │
        ▼
Chunking
        │
        ▼
Embedding Service
        │
        ▼
Qdrant
        │
        ▼
Retriever
        │
        ▼
Prompt Builder
        │
        ▼
Ollama
        │
        ▼
AIOps Assistant API
        │
        ▼
Slack / Teams / Web UI
```

---

# Current Milestone

The project has successfully completed the **knowledge ingestion** and **semantic retrieval** phases. Documents from the knowledge repository are automatically discovered, loaded, enriched with metadata, chunked, embedded using `all-MiniLM-L6-v2`, stored in Qdrant, and retrieved semantically based on embedded user questions.

The next development stage is to complete the **Prompt Builder**, integrate **Ollama**, expose the pipeline through **FastAPI**, and deliver the first fully functional **AIOps Intelligent Knowledge Assistant MVP**. Once that is complete, the project will evolve beyond static documentation by incorporating live operational data (logs, metrics, events) and implementing continuous learning from incidents and root cause analyses. This preserves the original AWS-oriented architecture while enabling rapid development using open-source technologies.
