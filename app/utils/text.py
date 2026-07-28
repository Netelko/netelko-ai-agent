import re
import unicodedata


class TextNormalizer:
    @staticmethod
    def normalize(text: str) -> str:
        """
        Normaliza una pregunta para mejorar la búsqueda:
        - Convierte a minúsculas
        - Elimina tildes
        - Elimina signos de puntuación
        - Elimina espacios repetidos
        """

        # Minúsculas
        text = text.lower().strip()

        # Eliminar tildes
        text = "".join(
            c for c in unicodedata.normalize("NFD", text)
            if unicodedata.category(c) != "Mn"
        )

        # Eliminar signos de puntuación
        text = re.sub(r"[^\w\s]", "", text)

        # Eliminar espacios repetidos
        text = re.sub(r"\s+", " ", text)

        return text