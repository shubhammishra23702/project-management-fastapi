from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.connection import get_db
from app.utils.deps import get_current_user
from app.schemas.user_schema import UserCreate, UserResponse
from app.views.user_view import create_user_view, get_users_view, update_user_view , delete_user_view

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print("Creating user:", user.email)
    return create_user_view(user, db)


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_users_view(db)

# UPDATE USER
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user_view(user_id, user, db)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
    

# DELETE USER
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = delete_user_view(user_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}