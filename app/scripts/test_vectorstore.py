from app.embeddings import EmbeddingModel
from app.vectorstore import VectorStore

embedding = EmbeddingModel().get_embedding()

db = VectorStore(embedding).load()

print(db._collection.count())