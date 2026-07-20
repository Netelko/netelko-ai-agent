from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
    temperature=0
)

response = llm.invoke("Responde únicamente con la palabra: Hola")

print(response.content)