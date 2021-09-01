from typing import Optional
from pydantic import BaseSettings, HttpUrl, PostgresDsn


class Settings(BaseSettings):

    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    SENTRY_DSN: Optional[HttpUrl] = None

    API_PATH: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 days

    # The following variables need to be defined in environment

    DATABASE_URL: PostgresDsn
    SECRET_KEY: str

    #  END: required environment variables


settings = Settings()
