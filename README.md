# DocuMind AI

**A Source-Grounded Document Question Answering System Using Retrieval-Augmented Generation (RAG)**

## Overview

DocuMind AI is an AI-powered document question-answering application that allows users to ask questions about documents and receive answers grounded in retrieved document content.

The project combines document processing, vector search, large language models, and source citations to make information retrieval more useful and transparent.

## Features

- Document loading and text extraction
- Text chunking and embedding generation
- Vector storage and semantic search with ChromaDB
- Retrieval-Augmented Generation (RAG)
- LLM-powered question answering
- Conversation history and session IDs
- Persistent conversation storage using SQLAlchemy
- Source metadata and page citations
- REST API built with FastAPI

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- OpenAI API
- Sentence Transformers
- SQLAlchemy
- SQLite

## Architecture

```text
Document
   ↓
Document Loader
   ↓
Text Splitter
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Retriever
   ↓
Relevant Context + Conversation History
   ↓
LLM
   ↓
Answer + Source Citations
```

## Project Structure

```text
app/
├── api/
├── chatbot/
├── config/
├── database/
├── llm/
└── rag/

data/
├── documents/
└── processed/

tests/
.env.example
.gitignore
requirements.txt
README.md
run.py
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd DocuMind-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file based on `.env.example` and add your own API key and model name.

Never commit `.env` or expose API keys.

### 5. Add documents

Place your permitted PDF, TXT, or DOCX files in the appropriate directory under `data/documents/`.

Run the document indexing process before querying the chatbot, using the indexing command supported by the project.

### 6. Start the API

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Usage

Send a POST request to `/chat` with a session ID and question. The exact request schema depends on the current API implementation.

Example:

```json
{
  "session_id": "demo-session",
  "message": "What is this document about?"
}
```

The response contains an answer and, when source metadata is available, source information.

## Security

- Keep API keys in environment variables.
- Do not commit private documents or local databases.
- Validate uploaded files before processing.
- Avoid exposing sensitive document content in logs or API responses.

## Current Limitations

- Answer quality depends on document quality and retrieval relevance.
- Source citations depend on correct metadata being preserved.
- Conversation persistence and multi-user behavior should be tested before production deployment.
- Additional authentication, upload validation, and deployment hardening may be required.

## Future Improvements

- Document upload endpoint
- Improved retrieval and reranking
- More reliable claim-level citations
- Automated tests
- Authentication and user-specific sessions
- Production deployment

## Author

Add your name and relevant portfolio or LinkedIn links here.