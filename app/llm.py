from langchain_ollama import ChatOllama
from app.config import settings

class LLM:

    def __init__(self):

        self.model = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_URL,
            temperature=0
        )

    def invoke(self, prompt: str):

        return self.model.invoke(prompt)