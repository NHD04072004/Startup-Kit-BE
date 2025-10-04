from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.database.models import User
from src.database.core import get_db
from src.auth.service import get_current_user
from . import schemas, service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=schemas.UserRead)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.patch("/me", response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def update_user_me(
    user_update: schemas.UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return service.update_user(db=db, current_user=current_user, user_update=user_update)
