from app.loaders import DocumentLoader
from app.splitter import DocumentSplitter
from app.embeddings import EmbeddingModel
from app.vectorstore import VectorStore
from app.config import settings


class IngestService:

    def ingest(self):

        # Cargar documentos
        loader = DocumentLoader(settings.DATA_PATH)
        documents = loader.load()

        # Dividir en chunks
        splitter = DocumentSplitter()
        chunks = splitter.split(documents)

        # Embeddings
        embedding = EmbeddingModel().get_embedding()

        # Guardar en ChromaDB
        vectordb = VectorStore(embedding)
        vectordb.create(chunks)

        return {
            "documents": len(documents),
            "chunks": len(chunks),
            "message": "Base vectorial actualizada correctamente."
        }