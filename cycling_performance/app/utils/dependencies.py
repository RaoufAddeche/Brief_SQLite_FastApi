from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.utils.security import verify_acess_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload= verify_acess_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")
    return payload