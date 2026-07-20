from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class DocumentSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
    
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ],
            length_function=len,
            is_separator_regex=False,
        )

    def split(
        self,
        documents: list[Document]
    ) -> list[Document]:

        chunks = self.splitter.split_documents(documents)

        # Agregar identificador de chunk
        for i, chunk in enumerate(chunks):
            chunk.metadata["chunk_id"] = i

        return chunks