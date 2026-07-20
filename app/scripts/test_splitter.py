print("1. Iniciando script...")

from app.loaders import DocumentLoader
print("2. Loader importado")
from app.splitter import DocumentSplitter
print("3. Splitter importado")

loader = DocumentLoader("data/documents")
print("4. Loader creado")

documents = loader.load()
print("5. Documentos cargados")

print(f"Documentos originales: {len(documents)}")

splitter = DocumentSplitter()
print("6. Splitter creado")

chunks = splitter.split(documents)
print("7. Split realizado")

print(f"Chunks generados: {len(chunks)}")