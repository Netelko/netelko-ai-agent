
from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
)
from langchain_core.documents import Document


class DocumentLoader:
    """
    Carga automáticamente archivos PDF y CSV desde una carpeta.
    """

    SUPPORTED_EXTENSIONS = {".pdf", ".csv"}

    def __init__(self, documents_path: str):
        self.documents_path = Path(documents_path)

    def load(self) -> list[Document]:

        documents = []

        if not self.documents_path.exists():
            raise FileNotFoundError(
                f"No existe la carpeta {self.documents_path}"
            )

        for file in self.documents_path.iterdir():

            if file.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                continue

            if file.suffix.lower() == ".pdf":
                docs = self._load_pdf(file)

            elif file.suffix.lower() == ".csv":
                docs = self._load_csv(file)

            documents.extend(docs)

        return documents

    def _load_pdf(self, file: Path):

        loader = PyPDFLoader(str(file))

        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = file.name
            doc.metadata["file_type"] = "pdf"

        return docs

    def _load_csv(self, file: Path):

        loader = CSVLoader(
            file_path=str(file),
            encoding="utf-8"
        )

        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = file.name
            doc.metadata["file_type"] = "csv"

        return docs