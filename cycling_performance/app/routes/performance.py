# Routes pour la gestion des performances
from fastapi import APIRouter, HTTPException
from app.db.queries import add_performance, get_test_types, get_performances_by_athlete
from app.schema.performance import AddPerformance

router= APIRouter()

@router.post("/")
def create_test(add_test : AddPerformance):
    """
    Ajoute une nouvelle performance pour un athlète.
    """
    try:
        add_performance(add_test.power_max, add_test.hr_max, add_test.vo2_max, add_test.rf_max, add_test.cadence_max, add_test.athlete_id, add_test.test_type_id)
        return {"message": "Test ajouté avec succès"}
    except Exception as e:
        raise HTTPException(status_code=400, detail= "Erreur lors de l'ajout de la performance")


@router.get("/types")
def get_all_test_types():
    """
    Récupere tous les types de test disponibles.
    """
    test_types= get_test_types()
    if not test_types:
        raise HTTPException(status_code=404, detail="Aucun type de test trouvé")
    return {"test_types": [dict(test_type) for test_type in test_types]}


@router.get("/{athlete_id}")
def get_performances(athlete_id:int):
    """
    Recupere toutes les performances d'un athlète.
    """
    performances= get_performances_by_athlete(int(athlete_id))
    if not performances:
        raise HTTPException(status_code=505, detail="Aucun test trouvé pour cet athlete")
    return {"tests": [dict(test) for test in performances]}

