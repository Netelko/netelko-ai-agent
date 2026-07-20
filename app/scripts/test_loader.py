
from app.loaders import DocumentLoader

loader = DocumentLoader("data/documents")

documents = loader.load()

print(f"Total documentos: {len(documents)}")

print()
for doc in documents:

    print("=" * 80)

    print(doc.metadata)

    print()

    print(doc.page_content[:300])



