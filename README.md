# AI Document & Study Assistant

An AI-powered document assistant that allows users to upload PDF, DOCX, and TXT files and ask questions about their content.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant document sections before generating an answer with a local LLM.

## Features

* Upload PDF, DOCX, and TXT documents
* Extract and clean document text
* Split documents into smaller chunks
* Generate vector embeddings
* Store embeddings using ChromaDB
* Retrieve relevant document chunks for questions
* Generate answers using a local Ollama LLM
* Display document sources and page numbers
* FastAPI backend
* Streamlit user interface
* Automated tests with pytest
* Docker support

## Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 │ HTTP requests
 ▼
FastAPI API
 │
 ├── Document Ingestion
 │    ├── Load
 │    ├── Clean
 │    └── Chunk
 │
 ├── Embeddings
 │
 ├── ChromaDB
 │
 └── RAG Pipeline
      ├── Retriever
      └── Ollama LLM
```

## RAG Pipeline

The main workflow is:

```text
Upload Document
      ↓
Load Document
      ↓
Clean Text
      ↓
Create Chunks
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
      ↓
User Asks Question
      ↓
Embed Question
      ↓
Retrieve Relevant Chunks
      ↓
Send Context + Question to LLM
      ↓
Generate Answer
```

## Tech Stack

* Python 3.13
* FastAPI
* Uvicorn
* Streamlit
* ChromaDB
* Sentence Transformers
* PyMuPDF
* python-docx
* Ollama
* Qwen 2.5 3B
* Pytest
* Docker

## Project Structure

```text
ai-document-assistant/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── llm.py
│   │   └── rag.py
│   ├── ingestion/
│   │   ├── loaders.py
│   │   ├── cleaner.py
│   │   ├── chunker.py
│   │   └── pipeline.py
│   ├── models/
│   │   └── schemas.py
│   └── main.py
├── ui/
│   └── streamlit_app.py
├── data/
│   ├── uploads/
│   └── chroma/
├── tests/
├── requirements.txt
├── README.md
└── PROJECT_BRIEF.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ai-document-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama separately and make sure the required model is available:

```bash
ollama pull qwen2.5:3b
```

### 5. Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Start the Streamlit interface

Open another terminal and activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then run:

```bash
streamlit run ui/streamlit_app.py
```

## Testing

Run the complete test suite:

```bash
pytest -v
```

The project currently contains automated tests covering document loading, cleaning, chunking, embeddings, vector storage, retrieval, LLM interaction, RAG, ingestion, and end-to-end behavior.

## API Endpoints

### `GET /health`

Checks whether the FastAPI backend is running.

### `POST /upload`

Uploads and processes a PDF, DOCX, or TXT document.

### `POST /query`

Accepts a question and returns an answer generated from retrieved document context.

## Limitations

* Scanned/image-only PDFs are not processed with OCR.
* The application currently uses a shared vector collection.
* Ollama must be installed locally when running without Docker.
* The project is designed as a practical learning project rather than a production-ready system.

## Purpose

This project was built as a practical implementation of concepts including:

* Document processing
* Text embeddings
* Vector databases
* Semantic retrieval
* Retrieval-Augmented Generation
* Local LLMs
* REST APIs
* Streamlit applications
* Automated testing
* Docker

The goal was to connect these concepts into one working AI application rather than build a highly complex production system.
