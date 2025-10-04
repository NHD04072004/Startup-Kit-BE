from sqlalchemy.orm import Session
from src.core.security import get_password_hash
from . import schemas
from src.database.models import User, UserProfile

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db_user.profile = UserProfile()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, current_user: User, user_update: schemas.UserUpdate) -> User:
    update_data = user_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if hasattr(current_user, key):
            setattr(current_user, key, value)
        elif hasattr(current_user.profile, key):
            setattr(current_user.profile, key, value)

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
