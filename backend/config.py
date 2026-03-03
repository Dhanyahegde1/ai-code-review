from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str
    app_version: str

    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    redis_url: str
    openai_api_key: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()