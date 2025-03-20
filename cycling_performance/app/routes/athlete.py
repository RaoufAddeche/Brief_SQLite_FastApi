# Routes pour la gestion des athlètes
from fastapi import APIRouter, HTTPException, Depends
from app.db.queries import add_caracteristic, get_tests_by_athlete
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.post("/caracteristic")
def add__athlete_caracteristic(gender: str, age: int, weight: float, height: float, id_user: int):
    try:
        add__athlete_caracteristic(gender, age, weight, height, id_user)
        return {"message": "Caracteristique ajoutée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erreur lors de l'ajout de la caractéristique")

@router.get("/test/{athlete_id}")
def get_athlete_tests(athlete_id):
    try:
        tests= get_tests_by_athlete(athlete_id)
        return{"tests": tests}
    except Exception as e:
        raise HTTPException(status_code=400, detail= "Erreur lors de la récupération des tests")
    
@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Bienvenue, {current_user['sub']} !"}