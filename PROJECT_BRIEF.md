# AI Document & Study Assistant

## 1. Project Goal

Build a local-first AI document assistant that allows a user to:

- Upload PDF, DOCX, and TXT documents
- Extract and clean their text
- Split documents into useful chunks
- Create embeddings for those chunks
- Store them in a vector database
- Ask questions about the uploaded documents
- Retrieve relevant passages
- Generate answers grounded in those passages
- Display source information such as filename and page number

The project is primarily a learning project and should remain simple enough to build and understand within approximately one week.

---

## 2. Architecture

User
↓
Streamlit UI
↓
FastAPI API
↓
Document Processing
↓
Text Cleaning
↓
Chunking
↓
Embeddings
↓
Chroma Vector Database
↓
Similarity Retrieval
↓
RAG Prompt
↓
LLM
↓
Grounded Answer
↓
Streamlit UI

---

## 3. Technology Stack

### Programming
- Python 3.13
- VS Code
- Git
- GitHub
- GitHub Copilot

### Interface
- Streamlit

### API
- FastAPI

### Document Processing
- PyMuPDF for PDF
- python-docx for DOCX
- Python standard library for TXT

### Embeddings
- sentence-transformers / Hugging Face

### Vector Database
- Chroma

### LLM
- Prefer a local/free LLM using Ollama when hardware allows
- Use a simple fallback if local inference is impractical

### Deployment
- Docker
- Cloud deployment only if practical after the local version works

---

## 4. Supported Documents

Initial supported formats:

- PDF
- DOCX
- TXT

Unsupported or problematic documents should produce a clear error or warning rather than crashing the application.

---

## 5. Document Processing Requirements

The ingestion pipeline should:

1. Validate the uploaded file
2. Extract text
3. Preserve useful metadata
4. Clean unnecessary formatting noise
5. Detect extraction problems
6. Split text into chunks
7. Generate embeddings
8. Store chunks and metadata in Chroma

Important metadata should include:

- filename
- file type
- page number when available
- document ID
- chunk ID

---

## 6. RAG Requirements

The assistant should:

- Convert the user's question into an embedding
- Retrieve the most relevant chunks
- Pass retrieved context to the LLM
- Generate an answer using the retrieved context
- Avoid inventing information not supported by the retrieved context
- Clearly state when the available context is insufficient
- Show the sources used for the answer

---

## 7. Reliability Principles

The system should prefer graceful degradation over silently producing incorrect results.

Potential problems include:

- Two-column PDFs
- Tables
- Scanned/image-only PDFs
- Headers and footers
- Broken line formatting
- Corrupt files
- Password-protected PDFs
- Poorly extracted text
- Duplicate documents
- Retrieval failures

The application should warn the user when extraction quality may be unreliable.

OCR is NOT part of the initial version.

---

## 8. Testing

We will test the system using:

- Normal text PDF
- Two-column PDF
- Table-containing PDF
- Scanned PDF
- DOCX with headings
- TXT document
- Document with repeated headers/footers

Retrieval will also be tested independently using known questions and expected source passages.

---

## 9. Project Scope

### Included

- Document upload
- Document parsing
- Text cleaning
- Chunking
- Embeddings
- Vector search
- RAG
- FastAPI
- Streamlit
- Basic testing
- Git/GitHub
- Docker

### Not included initially

- Authentication
- Multi-user accounts
- OCR
- Fine-tuning
- AI agents
- Kubernetes
- Complex monitoring
- MLflow
- DVC
- Airflow
- SQL database
- Payment systems
- Production-scale infrastructure
- Advanced frontend development

These may only be added later if there is a clear technical reason.

---

## 10. Development Principle

This is a learning project.

For every major component:

1. Understand the concept
2. Build the simplest working version
3. Test it
4. Inspect the result
5. Improve only when necessary

Git commits should represent meaningful working milestones.

GitHub Copilot may assist with code generation, but generated code must be reviewed and understood before being accepted.

---

## 11. Success Criteria

The project is considered successful when a user can:

1. Start the application
2. Upload a PDF, DOCX, or TXT file
3. Successfully process the document
4. Ask a question about its contents
5. Receive an answer based on the document
6. See the source passage or source metadata
7. Receive a clear warning when the system cannot reliably answer
8. Run the project locally from a clean environment
9. Build and run the application using Docker