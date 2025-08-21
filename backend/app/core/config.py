from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    api_key: str
    rate_limit: str
    debug: bool
    log_level: str
    pgvector_dimension: int
    secret_key: str

    model_config = SettingsConfigDict(env_file='.env.local')

settings = Settings()
