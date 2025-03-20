from pydantic import BaseModel


class UserCaracteristic(BaseModel):
    gender: str 
    age: int 
    weight: float 
    height: float 
    id_user: int

