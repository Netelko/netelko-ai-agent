from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from app.llm import LLM
from app.retriever import Retriever


class RAGChain:

    def __init__(self):

        retriever = Retriever(k=3)

        llm = LLM().model

        prompt = ChatPromptTemplate.from_template(
            """
Eres un asistente experto de NETELKO.

Responde únicamente utilizando la información del contexto.

Si la respuesta no existe en el contexto responde exactamente:

"No encontré esa información en los documentos."

Contexto:
{context}

Pregunta:
{question}

Respuesta:
"""
        )

        self.chain = (
            {
                "context": itemgetter("question") | retriever.retriever,
                "question": itemgetter("question"),
            }
            | prompt
            | llm
            | StrOutputParser()
        )

    def ask(self, question: str):

        return self.chain.invoke(
            {
                "question": question
            }
        )