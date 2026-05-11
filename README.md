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

YouTube
·pixegami
 +3
2. langchain-community (Integrations) 

Medium
·Diwash Bhandari | Software Developer
Use: Contains third-party integrations, loaders, and tools that are not in the core langchain package.
In AI Projects: Allows seamless connection to vector databases (like Qdrant), PDF loaders, search tools (Google Search), and local/remote LLM providers. 

TechTarget
 +1
3. pypdf (Document Loading) 

GitHub
Use: A pure-Python library for reading and extracting text from PDF files.
In AI Projects: Used in the "data ingestion" phase of RAG. It extracts text from user-uploaded PDFs so that the text can be chunked, embedded, and indexed for the LLM to search. 

GitHub
 +1
4. sentence-transformers (Embeddings)
Use: A Python library for state-of-the-art text embeddings (turning text into numerical vectors).
In AI Projects: Crucial for semantic search. It turns your PDF text chunks and user queries into vectors that represent their meaning, allowing the system to find relevant information based on content, not just keywords. 

LinkedIn
·Dileep Pandiya
5. qdrant-client (Vector Database) 

Medium
·Umar Igan
Use: The client library for Qdrant, a high-performance vector search engine/database.
In AI Projects: Stores the numerical vectors created by sentence-transformers. It enables fast retrieval of the most relevant document chunks to be sent to the LLM. 

Medium
·Umar Igan
 +1
6. fastapi & uvicorn (Backend & Deployment) 

Medium
·Diwash Bhandari | Software Developer
fastapi: A modern web framework for building APIs with Python. It is used to create the API endpoints for your AI app (e.g., /chat, /upload_doc).
uvicorn: A fast ASGI server implementation needed to run the FastAPI application.
In AI Projects: Turns your AI script into a usable application that can be queried by a frontend (like React or Streamlit). 
