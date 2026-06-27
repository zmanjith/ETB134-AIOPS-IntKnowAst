# RAG Sequence Diagram

The following sequence diagram shows the end-to-end flow: ingest → vector store → retrieval → prompt → LLM → response.

```mermaid
sequenceDiagram
    participant User
    participant CLI as main.py
    participant RAG as rag.ask()
    participant Search as search.semantic_search()
    participant Qdrant
    participant EmbModel as SentenceTransformer
    participant PromptGen as build_prompt()
    participant Ollama as Ollama LLM
    participant Ingest as ingest.py
    participant MinIO as MinIO (object storage)
    participant LocalFS as Local file system

    User->>CLI: Enter question
    CLI->>RAG: ask(question)
    RAG->>Search: semantic_search(question)
    Search->>EmbModel: encode(query)
    Search->>Qdrant: query_points(collection="documents", vector)
    Qdrant-->>Search: top-k chunks (payload.text)
    Search-->>RAG: list of chunks
    RAG->>PromptGen: build_prompt(question, context)
    RAG->>Ollama: chat(model, prompt)
    Ollama-->>RAG: response
    RAG-->>CLI: answer
    CLI-->>User: print answer

    Note over Ingest,MinIO,LocalFS: Ingest flow (offline / setup)
    Ingest->>MinIO: (optional) fetch PDF object
    MinIO-->>Ingest: PDF bytes
    Ingest->>LocalFS: save or stream PDF
    Ingest->>EmbModel: encode(chunks)
    Ingest->>Qdrant: upsert(points with vector + payload)
    Qdrant-->>Ingest: ack
```
