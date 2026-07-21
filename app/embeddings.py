from langchain_huggingface import HuggingFaceEmbeddings

from app.config import settings

model_name = settings.EMBEDDING_MODEL

class EmbeddingModel:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
    },
            encode_kwargs={
                "normalize_embeddings": True
    }
)

    def get_embedding(self):

        return self.embedding