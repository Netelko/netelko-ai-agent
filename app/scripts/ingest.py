from app.loaders import DocumentLoader
from app.splitter import DocumentSplitter
from app.embeddings import EmbeddingModel
from app.vectorstore import VectorStore

print("Cargando documentos...")

loader = DocumentLoader("data/documents")
documents = loader.load()

print(f"Documentos: {len(documents)}")

print("Dividiendo documentos...")

splitter = DocumentSplitter()
chunks = splitter.split(documents)

print(f"Chunks: {len(chunks)}")

print("Creando embeddings...")

embedding = EmbeddingModel().get_embedding()

print("Guardando en ChromaDB...")

vectordb = VectorStore(embedding)

vectordb.create(chunks)

print()

print("Proceso terminado correctamente.")