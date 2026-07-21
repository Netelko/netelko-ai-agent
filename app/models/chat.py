from pydantic import BaseModel


class Source(BaseModel):
    document: str
    page: int


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]