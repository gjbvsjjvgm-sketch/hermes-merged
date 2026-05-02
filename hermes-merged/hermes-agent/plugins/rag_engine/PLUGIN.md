---
name: rag-engine
version: 1.0.0
description: Retrieval-Augmented Generation engine - document ingestion, vector storage, semantic search, and grounded responses
category: knowledge
tools: [file, web, terminal]
---

# RAG Engine Plugin

Full RAG pipeline for grounded, factual AI responses with document knowledge.

## Vector Store Providers

| Provider | Type | Scale | Cost |
|----------|------|-------|------|
| ChromaDB | Local | Small-Med | Free |
| Pinecone | Cloud | Large | Pay-per-use |
| Qdrant | Self-hosted/Cloud | Large | Free/Paid |
| FAISS | Local | Large | Free |

## Features
- Document ingestion (PDF, DOCX, TXT, MD, HTML)
- Automatic chunking with overlap
- Multi-model embeddings (OpenAI, Cohere, local)
- Hybrid search (semantic + keyword)
- Relevance scoring and filtering
- Source citation in responses
- Incremental index updates
