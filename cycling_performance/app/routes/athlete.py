# Routes pour la gestion des athlètes
from fastapi import APIRouter, HTTPException, Depends
from app.db.queries import add_caracteristic, get_performances_by_athlete
from app.utils.dependencies import get_current_user
from app.schema.catacteristic import UserCaracteristic


router = APIRouter()

@router.post("/caracteristic")
def add__athlete_caracteristic(user: UserCaracteristic):
    try:
        add_caracteristic(user.gender, user.age, user.weight, user.height, user.id_user)
        return {"message": "Caracteristique ajoutée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erreur lors de l'ajout de la caractéristique")

@router.get("/performance/{athlete_id}")
def get_athlete_performances(athlete_id):
    try:
        performances= get_performances_by_athlete(athlete_id)
        return{"performances": performances}
    except Exception as e:
        raise HTTPException(status_code=400, detail= "Erreur lors de la récupération des tests")
    
@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Bienvenue, {current_user['sub']} !"}