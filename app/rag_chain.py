from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.llm import LLM
from app.retriever import Retriever


class RAGChain:

    def __init__(self):

        self.retriever = Retriever(k=5).retriever

        llm = LLM().model

        prompt = ChatPromptTemplate.from_template(
            """
Eres un asistente experto de NETELKO.

Responde únicamente utilizando la información del contexto.

Reglas:

1. Responde siempre en español.
2. No inventes información.
3. Si la respuesta no está en el contexto responde:

"No encontré esa información en los documentos disponibles."

4. Si es posible resume la información.
5. No menciones cosas que no aparecen en el documento.

Contexto:

{context}

Pregunta:

{question}

Respuesta:
"""
        )

        self.chain = (
            {
                "context": itemgetter("question") | self.retriever,
                "question": itemgetter("question"),
            }
            | prompt
            | llm
            | StrOutputParser()
        )

    def ask(self, question: str):

        # Recuperar los documentos relevantes
        docs = self.retriever.invoke(question)

        # Obtener la respuesta del LLM
        answer = self.chain.invoke(
            {
                "question": question
            }
        )

        # Construir las fuentes sin duplicados
        sources = []
        seen = set()

        for doc in docs:

            key = (
                doc.metadata.get("source_file"),
                doc.metadata.get("page")
            )

            if key in seen:
                continue

            seen.add(key)

            sources.append(
                {
                    "document": doc.metadata.get("source_file"),
                    "page": doc.metadata.get("page", 0) + 1
                }
            )

        return {
            "answer": answer,
            "sources": sources
        }