from sqlalchemy.orm import Session

from . import models, schemas

from .models import User
from .schemas import userCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.userCreate):
    db_user = models.User(
            **user.dict()
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def dbOTP(db: Session, email, otp):
    db_user_otp = models.user_auth_otp(
            user = email,
            OTP = otp
        )
    db.add(db_user_otp)
    db.commit()
    db.refresh(db_user_otp)
    return db_user_otp
          