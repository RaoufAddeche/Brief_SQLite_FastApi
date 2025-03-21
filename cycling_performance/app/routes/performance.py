# Routes pour la gestion des performances
from fastapi import APIRouter, HTTPException
from app.db.queries import add_performance, get_test_types, get_performances_by_athlete, get_connection
from app.schema.performance import AddPerformance, UpdatePerformance

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


@router.put("/update/{performance_id}")
def update_performance(update: UpdatePerformance, performance_id: int):
    """
    Met à jour une performance existante.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    #Vérifier si la performance existe
    cursor.execute("SELECT * FROM performance WHERE id= ?;", (performance_id,))
    performance = cursor.fetchone()
    if not performance:
        raise HTTPException(status_code=404, detail="Performance non trouvée")
    

    # Construire la requête de mise à jour
    update_fields = []
    update_values = []

    if update.power_max is not None:
        update_fields.append("power_max = ?")
        update_values.append(update.power_max)
    if update.hr_max is not None:
        update_fields.append("hr_max = ?")
        update_values.append(update.hr_max)
    if update.vo2_max is not None:
        update_fields.append("vo2_max = ?")
        update_values.append(update.vo2_max)
    if update.rf_max is not None:
        update_fields.append("rf_max = ?")
        update_values.append(update.rf_max)
    if update.cadence_max is not None:
        update_fields.append("cadence_max = ?")
        update_values.append(update.cadence_max)


    if not update_fields:
        raise HTTPException(status_code=400, detail="Aucun champ à mettre à jour")
    
    #Ajouter l'ID de la performance à la liste des valeurs
    update_values.append(performance_id)

    # Exécuter la requête de mise à jour
    query = f"UPDATE performance SET {', '.join(update_fields)} WHERE id = ?;"
    cursor.execute(query, update_values)
    conn.commit()
    conn.close()

    return {"message": "Performance mise à jour avec succès"}


@router.delete("/delete/{performance_id}")
def delete_performance(performance_id : int):
    """
    Supprime une performance existante.
    """
    conn= get_connection()
    cursor = conn.cursor()

    #Verifier si la performance existe
    cursor.execute("SELECT * FROM performance WHERE id= ?;", (performance_id,))
    performance = cursor.fetchone()
    if not performance:
        raise HTTPException(status_code=404, detail="Performance non trouvée")


    #Supprimer la performance
    cursor.execute("DELETE FROM performance WHERE id= ?;", (performance_id,))
    conn.commit()
    conn.close()

    return {"message": "Performance supprimée avec succès"}
