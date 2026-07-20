from app.retriever import Retriever

retriever = Retriever(k=3)

question = "¿que planes ofrece netelko dentro de su oferta de planes y precios?"

documents = retriever.search(question)

print(f"\nSe encontraron {len(documents)} documentos\n")

for i, doc in enumerate(documents, start=1):

    print("=" * 80)
    print(f"Resultado {i}")
    print("-" * 80)

    print("Metadata:")
    print(doc.metadata)

    print("\nContenido:")
    print(doc.page_content[:500])
    print()