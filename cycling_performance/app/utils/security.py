# Gestion des mots de passe et JWT
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context= CryptContext(schemes=["bcrypt"], deprecated = "auto")


#Hacher un mot de passe
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#verifier un mot de passe
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Générer un token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt
    
#Verifier un token JWT
def verify_acess_token(token: str):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        return None