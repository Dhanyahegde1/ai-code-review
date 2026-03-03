# backend/config.py
from pydantic_settings import BaseSettings 
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "AI Code Review"
    app_version: str = "0.1.0"
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "secret123"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    redis_url: str = "redis://localhost:6379"
    openai_api_key: str = "dummy_key"

    class Config:
        env_file = ".env"  # optional, can override with real values later

@lru_cache()
def get_settings():
    return Settings()