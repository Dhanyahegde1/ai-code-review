from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Code Review API"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
