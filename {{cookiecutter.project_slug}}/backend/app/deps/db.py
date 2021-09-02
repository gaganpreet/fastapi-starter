from typing import Generator
from app.db import Session


def get_db() -> Generator:
    db = None
    try:
        db = Session()
        yield db
    finally:
        if db is not None:
            db.close()
