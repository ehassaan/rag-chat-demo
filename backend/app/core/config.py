from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    api_key: str
    rate_limit: str 
    debug: bool
    log_level: str
    pgvector_dimension: int
    secret_key: str
    cohere_api_key: str
    embedding_model: str = "embed-v4.0"
    generation_model: str = "command-a-03-2025"
    max_response_tokens: int = 8192

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
