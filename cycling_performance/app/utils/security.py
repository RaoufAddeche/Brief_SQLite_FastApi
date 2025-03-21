# Password and JWT management
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

# Initialize the password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password
def hash_password(password: str) -> str:
    """
    Hash a plain text password using bcrypt.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

# Verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify that a plain text password matches a hashed password.

    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Generate a JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create a JWT token with an optional expiration time.

    Args:
        data (dict): The data to encode in the token.
        expires_delta (timedelta, optional): The token's expiration time. Defaults to the configured expiration time.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Add expiration time to the token payload
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")  # Encode the token
    return encoded_jwt

# Verify a JWT token
def verify_acess_token(token: str):
    """
    Verify the validity of a JWT token.

    Args:
        token (str): The JWT token to verify.

    Returns:
        dict: The decoded payload if the token is valid.
        None: If the token is invalid or expired.
    """
    try:
        # Decode the token using the secret key and HS256 algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        # Return None if the token is invalid or expired
        return None