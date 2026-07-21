from app.embeddings import EmbeddingModel
from app.vectorstore import VectorStore


class Retriever:

    def __init__(self, k: int = 4):

        embedding = EmbeddingModel().get_embedding()

        vectordb = VectorStore(embedding).load()

        self.retriever = vectordb.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 5
            }
        )

    def search(self, question: str):

        return self.retriever.invoke(question)