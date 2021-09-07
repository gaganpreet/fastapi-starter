from sqlalchemy.orm.session import Session
from uuid import uuid4

from app.models.user import User


def test_user_model(db: Session):
    user = User(id=uuid4(), email="test@example.com", hashed_password="1234")
    db.add(user)
    db.commit()
    assert user.id
