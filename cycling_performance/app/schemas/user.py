from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    pseudo: Optional[str] = None
    email: EmailStr
    password:str
    is_coach: int


class UserLogin(BaseModel):
    email: EmailStr
    password:str


class UserRead(BaseModel):
    pseudo: Optional[str]
    email: EmailStr
    password:str
    is_coach: int


class UserUpdate(BaseModel):
    pseudo: Optional[str] = None
    email: Optional[EmailStr] = None
    is_coach: Optional[int] = None


class UserUpdatePassword(BaseModel):
    password: Optional[str] = None

