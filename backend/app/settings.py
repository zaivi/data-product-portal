from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_SERVER: str

    # Other
    CORS_ALLOWED_ORIGINS: str = ""
    AWS_DEFAULT_REGION: str = "eu-west-1"
    AWS_DEFAULT_PROFILE: Optional[str] = None
    PORTAL_API_KEY: Optional[str] = None

    # OIDC Configuration
    OIDC_DISABLED: bool = True
    OIDC_CLIENT_ID: Optional[str] = None
    OIDC_CLIENT_SECRET: Optional[str] = None
    OIDC_AUTHORITY: Optional[str] = None
    OIDC_REDIRECT_URI: Optional[str] = None

    # Conveyor
    CONVEYOR_API_KEY: Optional[str] = None
    CONVEYOR_SECRET: Optional[str] = None
    LOGGING_DIRECTORY: str = "./tmp/logs"

    # Infrastructure
    INFRASTRUCTURE_LAMBDA_ARN: Optional[str] = None
    ENVIRONMENT_CONTEXT: Optional[str] = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
