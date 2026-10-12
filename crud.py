
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User
from schemas import UserCreate, UserUpdate


def get_users(db: Session, city=None, is_active=None):
    statement = select(User)

    if city:
        statement = statement.where(User.city == city)

    if is_active is not None:
        statement = statement.where(User.is_active == is_active)

    return db.scalars(statement).all()


def get_user(db: Session, user_id: int):
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.scalar(statement)


def create_user(db: Session, user_data: UserCreate):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User, user_data: UserUpdate):
    user_data_dict = user_data.model_dump()

    for field, value in user_data_dict.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
