from app.rag_chain import RAGChain


class RAGService:

    def __init__(self):
        self.rag = RAGChain()

    def ask(self, question: str):
        return self.rag.ask(question)
    
   
   