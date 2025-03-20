from pydantic import BaseModel

class UserConnexion(BaseModel):
    pseudo: str
    email: str
    password : str
    is_coach: bool

class LoginUser(BaseModel):
    email: str
    password: str
