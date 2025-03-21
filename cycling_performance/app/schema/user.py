from pydantic import BaseModel

# Schema for user registration
class UserConnexion(BaseModel):
    """
    Schema for user registration.
    """
    pseudo: str       # User's username or nickname
    email: str        # User's email address
    password: str     # User's password
    is_coach: bool    # Boolean indicating if the user is a coach (True) or not (False)


# Schema for user login
class LoginUser(BaseModel):
    """
    Schema for user login.
    """
    email: str        # User's email address
    password: str     # User's password