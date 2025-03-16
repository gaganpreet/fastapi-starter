import sys
from functools import cached_property
from typing import Any

from pydantic import HttpUrl, PostgresDsn, field_validator
from pydantic.networks import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    SENTRY_DSN: HttpUrl | None = None

    API_PATH: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 days

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    TEST_DATABASE_URL: PostgresDsn | None = None
    DATABASE_URL: PostgresDsn

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def build_test_database_url(cls, v: str | None, info: dict[str, Any]) -> str:
        """Overrides DATABASE_URL with TEST_DATABASE_URL in test environment."""
        if v is None:
            raise ValueError("DATABASE_URL cannot be None")

        if "pytest" in sys.modules:
            test_url = info.data.get("TEST_DATABASE_URL")
            if not test_url:
                raise ValueError(
                    "pytest detected, but TEST_DATABASE_URL is not set in environment"
                )
            v = str(test_url)

        return v.replace("postgres://", "postgresql://")

    @cached_property
    def ASYNC_DATABASE_URL(self):
        """Builds ASYNC_DATABASE_URL from DATABASE_URL."""
        v = str(self.DATABASE_URL)
        return v.replace("postgresql", "postgresql+asyncpg", 1) if v else v

    SECRET_KEY: str


settings = Settings()
