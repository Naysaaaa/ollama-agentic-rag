# Agentic AI Research Assistant

An intelligent document-grounded research assistant built using Ollama, LangChain, LangGraph, FAISS, and Retrieval-Augmented Generation (RAG).

## Overview

This project enables users to query custom knowledge bases through natural language. The system retrieves relevant document chunks using semantic search and generates source-grounded responses using locally hosted Large Language Models (LLMs) powered by Ollama.

## Features

- Local LLM Inference using Ollama
- Retrieval-Augmented Generation (RAG)
- PDF Knowledge Base
- Semantic Search with FAISS
- Document Chunking and Embeddings
- Streamlit User Interface
- Source-Grounded Responses
- Multi-Agent Architecture (Upcoming)

## Architecture

User Query
↓
Retriever
↓
FAISS Vector Store
↓
Relevant Context
↓
Ollama LLM
↓
Generated Response

## Tech Stack

- Python
- Ollama
- Llama 3.2
- LangChain
- LangGraph
- FAISS
- HuggingFace Embeddings
- Streamlit

## Project Structure

```text
app/
├── agents/
├── core/
├── ingestion/
└── ui/

data/
vectorstore/
docs/
```

## Installation

```bash
git clone <repo-url>

cd ollama-agentic-rag

python3.13 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Run Ollama

```bash
ollama serve
```

## Run Application

```bash
streamlit run app/ui/streamlit_app.py
```

## Future Enhancements

- LangGraph Multi-Agent Workflow
- Citation Verification
- Conversation Memory
- Hybrid Search
- FastAPI Deployment
- Docker Support

## Author

Naysa