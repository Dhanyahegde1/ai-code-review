
# Import BaseSettings from pydantic-settings
# This allows us to load configuration values automatically from environment variables or a .env file
from pydantic_settings import BaseSettings

# Import lru_cache to cache the settings object
# This prevents the settings from being recreated multiple times during the app lifecycle
from functools import lru_cache


# Settings class defines all configuration variables required by the application
# These values will be automatically loaded from the .env file
class Settings(BaseSettings):

    # Application name used in FastAPI documentation (Swagger UI)
    app_name: str

    # Application version displayed in API docs
    app_version: str

    # Database connection URL (used by SQLAlchemy)
    database_url: str

    # Secret key used for security features like JWT authentication
    secret_key: str

    # Algorithm used for encoding JWT tokens (e.g., HS256)
    algorithm: str

    # Token expiration time (in minutes)
    access_token_expire_minutes: int

    # Redis connection URL (used for background tasks or caching)
    redis_url: str

    # API key used to connect with OpenAI or other AI services
    openai_api_key: str


    # Inner Config class tells Pydantic where to read environment variables from
    class Config:

        # Load environment variables from the ".env" file located in the backend directory
        env_file = ".env"


# Cache the settings instance so it is created only once
# This improves performance and ensures the same configuration is used throughout the application
@lru_cache()
def get_settings():

    # Return the Settings object containing all configuration values
    return Settings()