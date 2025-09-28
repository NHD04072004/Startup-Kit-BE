from fastapi import APIRouter, Depends
from src.database.models import User
from src.auth.service import get_current_user
from . import schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=schemas.UserRead)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user