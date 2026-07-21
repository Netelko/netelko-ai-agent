from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "NETELKO AI Agent"
    APP_VERSION: str = "1.0.0"

    LLM_PROVIDER: str = "ollama"

    OLLAMA_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:7b"

     # OCI Generative AI
    OCI_COMPARTMENT_OCID: str = ""
    OCI_ENDPOINT: str = ""
    OCI_MODEL_ID: str = ""


    EMBEDDING_MODEL: str = "BAAI/bge-m3"

    CHROMA_DB: str = "./chroma_db"

    DATA_PATH: str = "./data/documents"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
