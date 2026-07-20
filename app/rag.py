from app.retriever import Retriever
from app.llm import LLM


class RAG:

    def __init__(self):

        self.retriever = Retriever(k=3)

        self.llm = LLM()

    def ask(self, question: str):

        docs = self.retriever.search(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
Eres un asistente experto.

Responde únicamente usando la información del contexto.

Si la respuesta no existe en el contexto responde:

"No encontré esa información en los documentos."

Contexto

{context}

Pregunta

{question}

Respuesta:
"""

        response = self.llm.invoke(prompt)

        return response.content