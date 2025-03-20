# Routes pour l'authentification
from fastapi import APIRouter, HTTPException
from app.db.queries import add_user, get_user_by_email
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from app.utils.security import hash_password, verify_password, create_access_token
from datetime import timedelta
from app.schema.user import UserConnexion, LoginUser


router = APIRouter()

@router.post("/register")
def register_user(user : UserConnexion):
    hashed_password = hash_password(user.password)
    try:
        add_user(user.pseudo,user.email,hashed_password, user.is_coach)
        return {"message": "Utilisateur enregistré avec succès"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erreur lors de l'enregistrement")

@router.post("/login")
def login_user(user: LoginUser):
    print(user.email)
    db_user= get_user_by_email(user.email)
    if not user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail= "Email ou mot de passe incorrect")
    
    #Générer un token JWT
    acces_token= create_access_token(
        data={"sub": db_user["email"]}, expires_delta=timedelta(minutes=30)
    )
    return {"acces_token": acces_token, "token_type": "bearer"}