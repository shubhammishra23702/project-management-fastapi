from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.utils.connection import get_db
from app.views.auth_views import authenticate_user

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = authenticate_user(form_data.username, form_data.password, db)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token