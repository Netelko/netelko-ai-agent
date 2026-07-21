from fastapi import FastAPI, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService
from app.services.ingest_service import IngestService
from app.models.ingest import IngestResponse

app = FastAPI(
    title="NETELKO AI Agent",
    version="1.0.0"
)

rag_service = RAGService()


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = rag_service.ask(request.question)

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )


@app.post("/ingest", response_model=IngestResponse)
def ingest():

    service = IngestService()

    result = service.ingest()

    return IngestResponse(**result)