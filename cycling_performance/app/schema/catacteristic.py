from pydantic import BaseModel

# Schema for user characteristics
class UserCaracteristic(BaseModel):
    """
    Schema for adding or managing user characteristics.
    """
    gender: str       # Gender of the user (e.g., "male", "female", etc.)
    age: int          # Age of the user
    weight: float     # Weight of the user in kilograms
    height: float     # Height of the user in meters
    id_user: int      # ID of the user associated with these characteristics