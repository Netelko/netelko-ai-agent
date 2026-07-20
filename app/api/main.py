from fastapi import FastAPI, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

app = FastAPI(
    title="NETELKO AI Agent",
    version="1.0.0"
)

service = RAGService()


@app.get("/")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        answer = service.ask(request.question)

        return ChatResponse(
            answer=answer
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )