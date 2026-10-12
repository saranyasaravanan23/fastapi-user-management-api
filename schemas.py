
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    age: int = Field(ge=18, le=60)
    city: str = Field(min_length=1)
    is_active: bool = True


class UserUpdate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    age: int = Field(ge=18, le=60)
    city: str = Field(min_length=1)
    is_active: bool


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    city: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
