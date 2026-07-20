from langchain_ollama import ChatOllama

from app.config import (
    OLLAMA_MODEL,
    OLLAMA_URL
)


class LLM:

    def __init__(self):

        self.model = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_URL,
            temperature=0
        )

    def invoke(self, prompt: str):

        return self.model.invoke(prompt)