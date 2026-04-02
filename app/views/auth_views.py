# app/views/auth_views.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

from app.models.user_model import User
from app.utils.security import SECRET_KEY, ALGORITHM

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_user(email: str, password: str, db: Session):
    """
    Verify user credentials and return JWT token if valid.
    """
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not pwd_context.verify(password, user.password):
        return None

    # Create JWT token
    access_token_expires = timedelta(minutes=30)
    token_data = {"sub": user.email, "exp": datetime.utcnow() + access_token_expires}
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "token_type": "bearer"}