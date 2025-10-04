from typing import Optional
from pydantic.networks import HttpUrl
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from src.database.models import UserRole


class UserProfileBase(BaseModel):
    avatar_url: Optional[HttpUrl] = None
    bio: Optional[str] = None
    website_url: Optional[HttpUrl] = None
    location: Optional[str] = None

class UserProfileRead(UserProfileBase):
    user_id: int

    class Config:
        from_attributes = True

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
    is_active: bool
    created_at: datetime
    profile: UserProfileRead

    class Config:
        from_attributes = True