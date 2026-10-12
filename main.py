
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import models
from database import engine, get_db
from schemas import UserCreate, UserUpdate, UserResponse
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management REST API")


@app.get("/")
def home():
    return {"message": "User Management API is running"}


# Create User
@app.post("/users", response_model=UserResponse,
          status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, str(user_data.email))

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    try:
        return crud.create_user(db, user_data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


# Get All Users with optional filters
@app.get("/users", response_model=list[UserResponse])
def read_users(
    city: str | None = None,
    is_active: bool | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_users(db, city=city, is_active=is_active)


# Get User by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# Update User
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_user = crud.get_user_by_email(db, str(user_data.email))

    if existing_user and existing_user.id != user_id:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    try:
        return crud.update_user(db, user, user_data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


# Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    crud.delete_user(db, user)

    return {"message": "User deleted successfully"}
