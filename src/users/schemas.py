from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from src.database.models import UserRole

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)
    password_confirm: str
    role: UserRole

class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True