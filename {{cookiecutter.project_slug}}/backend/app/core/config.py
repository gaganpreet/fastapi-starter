from typing import Optional
from pydantic import BaseSettings, HttpUrl, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    DATABASE_URL: PostgresDsn
    SENTRY_DSN: Optional[HttpUrl] = None

    API_PATH: str = "/api/v1"


settings = Settings()
