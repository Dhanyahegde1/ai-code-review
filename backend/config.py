from pydantic_settings import BaseSettings
from functools import lru_cache



class Settings(BaseSettings):

   
    app_name: str

    # displays Application version 
    app_version: str

    # Database connection url
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    redis_url: str
    openai_api_key: str


    # ells where to read environment variables from
    class Config:
        env_file = ".env"


# Cache the settings instance 

@lru_cache()
def get_settings():
    return Settings()