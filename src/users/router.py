from fastapi import APIRouter, Depends, status, HTTPException
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

@router.put("/me/password", status_code=status.HTTP_200_OK)
def update_user_password_me(
    password_update: schemas.UserPasswordUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if password_update.new_password != password_update.new_password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New passwords do not match"
        )
    
    success = service.update_user_password(
        db=db, 
        current_user=current_user, 
        password_update=password_update
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect current password"
        )
        
    return {"message": "Password updated successfully"}