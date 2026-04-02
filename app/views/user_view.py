from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user_view(user: UserCreate, db: Session):
    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users_view(db: Session):
    return db.query(User).all()

def update_user_view(user_id: int, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db_user.email = user.email
    db_user.password = pwd_context.hash(user.password)

    db.commit()
    db.refresh(db_user)

    return db_user


# ✅ DELETE
def delete_user_view(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return False

    db.delete(db_user)
    db.commit()

    return True