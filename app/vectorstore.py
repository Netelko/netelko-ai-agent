from langchain_chroma import Chroma

from app.config import CHROMA_DB


class VectorStore:

    def __init__(self, embedding):

        self.embedding = embedding

    def create(self, documents):

        vectordb = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding,
            persist_directory=CHROMA_DB
        )

        return vectordb

    def load(self):

        return Chroma(
            persist_directory=CHROMA_DB,
            embedding_function=self.embedding
        )