from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.utils.security import verify_acess_token

# Define the OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieve the current user based on the provided OAuth2 token.

    Args:
        token (str): The OAuth2 token provided by the client.

    Returns:
        dict: The payload extracted from the token if valid.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    # Verify the access token
    payload = verify_acess_token(token)
    if not payload:
        # Raise an exception if the token is invalid or expired
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload