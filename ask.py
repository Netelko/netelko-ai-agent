from app.rag_chain import RAGChain

rag = RAGChain()

print("========================================")
print("Agente IA - NETELKO")
print("Escriba 'exit' para salir.")
print("========================================")

while True:

    question = input("\nPregunta: ")

    if question.lower() == "exit":
        break

    answer = rag.ask(question)

    print("\nRespuesta:\n")

    print(answer)
