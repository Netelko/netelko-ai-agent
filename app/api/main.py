from fastapi import FastAPI, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService
from app.services.ingest_service import IngestService
from app.models.ingest import IngestResponse
from app.utils.text import TextNormalizer

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

    print("=" * 60)
    print(f"Pregunta original: {request.question}")

    question = TextNormalizer.normalize(request.question)

    print(f"Pregunta normalizada: {question}")

    result = rag_service.ask(question)

    print("Respuesta generada correctamente")

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )

@app.post("/ingest", response_model=IngestResponse)
def ingest():

    service = IngestService()

    result = service.ingest()

    return IngestResponse(**result)