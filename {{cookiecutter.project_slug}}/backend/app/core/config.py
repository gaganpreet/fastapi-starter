import sys
from typing import Any, Dict, List, Optional

from pydantic import HttpUrl, PostgresDsn, field_validator
from pydantic.networks import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    SENTRY_DSN: Optional[HttpUrl] = None

    API_PATH: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 days

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # The following variables need to be defined in environment

    TEST_DATABASE_URL: Optional[PostgresDsn]
    DATABASE_URL: PostgresDsn
    ASYNC_DATABASE_URL: Optional[PostgresDsn]

    @field_validator("DATABASE_URL", mode="before")
    def build_test_database_url(cls, v: Optional[str], info: Dict[str, Any]):
        """Overrides DATABASE_URL with TEST_DATABASE_URL in test environment."""
        url = v
        if "pytest" in sys.modules:
            if not info.data.get("TEST_DATABASE_URL"):
                raise Exception(
                    "pytest detected, but TEST_DATABASE_URL is not set in environment"
                )
            url = info.data["TEST_DATABASE_URL"]
        if url:
            return url.replace("postgres://", "postgresql://")
        return url

    @field_validator("ASYNC_DATABASE_URL")
    def build_async_database_url(cls, v: Optional[str], info: Dict[str, Any]):
        """Builds ASYNC_DATABASE_URL from DATABASE_URL."""
        v = info.data["DATABASE_URL"]
        return v.replace("postgresql", "postgresql+asyncpg", 1) if v else v

    SECRET_KEY: str
    #  END: required environment variables


settings = Settings()
