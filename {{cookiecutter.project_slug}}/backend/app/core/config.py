from typing import List, Optional

from pydantic import BaseSettings, HttpUrl, PostgresDsn, root_validator
from pydantic.networks import AnyHttpUrl


class Settings(BaseSettings):

    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    SENTRY_DSN: Optional[HttpUrl] = None

    API_PATH: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 days

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # The following variables need to be defined in environment

    DATABASE_URL: PostgresDsn
    TEST_DATABASE_URL: Optional[PostgresDsn]

    SECRET_KEY: str
    #  END: required environment variables

    @root_validator
    def validate_database_url(cls, values):
        # Either one of the database urls need to be set
        assert values.get("DATABASE_URL") or values.get("TEST_DATABASE_URL")
        return values


settings = Settings()
