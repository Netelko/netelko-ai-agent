from pydantic import BaseModel


class IngestResponse(BaseModel):
    documents: int
    chunks: int
    message: str