# Gestion des mots de passe et JWT
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

pwd_context= CryptContext(schemes=["bcrypt"], deprecated = "auto")

#Clé secrète et algorithme pour JWT
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES= 30

#Hacher un mot de passe
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#verifier un mot de passe
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#Générer un token JWT
def create_acces_token(data: dict, expires_delta: timedelta = None)
    to_encode = data.copy()
    if expires_delta:
        expire= datetime.utcnow() + expires_delta
    else:
        expire= datetime.utcnow()+ timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithms=[ALGORITHM])
        return encoded_jwt
    
#Verifier un token JWT
def verify_acess_token(token: str):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    