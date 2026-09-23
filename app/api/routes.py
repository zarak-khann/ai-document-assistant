from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.ingestion.pipeline import IngestionPipeline
from app.core.llm import LLM
from app.core.rag import RAGPipeline
from app.core.retriever import Retriever


router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

pipeline = IngestionPipeline()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is missing")

    extension = Path(file.filename).suffix.lower()

    if extension not in {".pdf", ".docx", ".txt"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, and TXT files are supported",
        )

    file_path = UPLOAD_DIR / file.filename

    content = await file.read()
    file_path.write_bytes(content)

    chunk_count = pipeline.ingest(str(file_path))

    return {
        "filename": file.filename,
        "chunks_stored": chunk_count,
        "message": "Document uploaded and processed successfully",
    }


class QueryRequest(BaseModel):
    question: str


retriever = Retriever()
llm = LLM()

rag = RAGPipeline(
    retriever=retriever,
    llm=llm,
)


@router.post("/query")
async def query_document(request: QueryRequest):
    result = rag.answer(request.question)

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"],
    }