# Routes pour l'authentification
from fastapi import APIRouter, HTTPException
from app.db.queries import add_user, get_user_by_email
from app.utils.security import hash_password, verify_password, create_acces_token
from datetime import timedelta



router = APIRouter()

@router.post("/register")
def register_user(pseudo: str, email: str, password: str, is_coach: bool):
    hashed_password = hash_password(password)
    try:
        add_user(pseudo,email,password, hashed_password, is_coach)
        return {"message": "Utilisateur enregistré avec succès"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erreur lors de l'enregistrement")

@router.post("/login")
def login_user(email: str, password: str):
    user= get_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401 detail= "Email ou mot de passe incorrect")
    
    #Générer un token JWT
    acces_token= create_acces_token(
        data={"sub": user["email"]}, expires_delta=timedelta(minutes=30)
    )
    return {"acces_token": acces_token, "token_type": "bearer"}