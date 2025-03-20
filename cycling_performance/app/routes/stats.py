# Routes pour les statistiques
from fastapi import APIRouter, HTTPException
from app.db.database import get_connection

router= APIRouter()


@router.get("/most_powerful_atlete")
def get_most_powerful_athlete():
    """recupere l'athlete avec la puissance maximale moyenne la plus élevée"""
    conn = get_connection()
    cursor= conn.cursor()
    query= """
    SELECT u.pseudo, AVG(t.power_max) as avg_power
    FROM test t
    JOIN user u on t.athlete_id= u.id
    GROUP.BY t.athlete_id
    ORDER BY avg_power DESC
    LIMIT 1;
    """
    cursor.execute(query)
    result= cursor.fetchone()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="Aucun athlète trouvé")
    return {"athlete": result["pseudo"], "average_power": result["avg_power"]}

@router.get("/best_vo2max")
def get_best_vo2max():
    """
    Récupere l'athlète avec le vo2max le plus élevé
    """
    conn= get_connection()
    cursor= conn.cursor()
    query= """
    SELECT u.pseudo, MAX(t.vo2max) as max_vo2max
    FROM test t
    JOIN user u ON t.athlete_id = u.id
    GROUP BY t.athlete_id
    ORDER BY max_vo2max DESC
    LIMIT 1;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    conn.closer
    
    if not result:
        raise HTTPException(status_code=404, detail= "Aucun athlète trouvé")
    return {"athlete": result["pseudo"], "max_vo2max": result["max_vo2max"]}


@router.get("/best_power_to_weight_ratio")
def get_best_power_to_weight_ratio()
    """
    Récupere l'athlete avec le meilleur rapport puissance poids.
    """
    conn= get_connection()
    cursor= conn.cursor()
    query="""
    SELECT u.pseudo, MAX(t.power_max/c.weight) as best_ratio
    FROM test t
    JOIN user u ON t.athlete_id= u_id
    JOIN caracteristic c ON c.id_user= u.id
    GROUP BY t.athlete_id
    ORDER BY best_ratio DESC
    LIMIT 1;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    if not result: 
        raise HTTPException(status_code=404, detail=" Aucun athlète trouvé")
    return {"athlete": result["pseudo"], "}