# Routes for statistics
from fastapi import APIRouter, HTTPException
from app.db.database import get_connection

router = APIRouter()

@router.get("/most_powerful_athlete")
def get_most_powerful_athlete():
    """
    Retrieve the athlete with the highest average maximum power.
    """
    # Connect to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Query to calculate the athlete with the highest average power
    query = """
    SELECT u.pseudo, AVG(p.power_max) as avg_power
    FROM performance p
    JOIN user u on p.athlete_id = u.id
    GROUP BY p.athlete_id
    ORDER BY avg_power DESC
    LIMIT 1;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    # If no result is found, raise an exception
    if not result:
        raise HTTPException(status_code=404, detail="No athlete found")

    # Return the athlete's name and their average power
    return {"athlete": result["pseudo"], "average_power": result["avg_power"]}


@router.get("/best_vo2max")
def get_best_vo2max():
    """
    Retrieve the athlete with the highest VO2 max.
    """
    # Connect to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Query to find the athlete with the highest VO2 max
    query = """
    SELECT u.pseudo, MAX(p.vo2_max) as max_vo2max
    FROM performance p
    JOIN user u ON p.athlete_id = u.id
    GROUP BY p.athlete_id
    ORDER BY max_vo2max DESC
    LIMIT 1;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    # If no result is found, raise an exception
    if not result:
        raise HTTPException(status_code=404, detail="No athlete found")

    # Return the athlete's name and their maximum VO2 max
    return {"athlete": result["pseudo"], "max_vo2max": result["max_vo2max"]}


@router.get("/best_power_to_weight_ratio")
def get_best_power_to_weight_ratio():
    """
    Retrieve the athlete with the best power-to-weight ratio.
    """
    # Connect to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Query to calculate the best power-to-weight ratio
    query = """
    SELECT u.pseudo, MAX(p.power_max / c.weight) as best_ratio
    FROM performance p
    JOIN user u ON p.athlete_id = u.id
    JOIN caracteristic c ON c.id_user = u.id
    GROUP BY p.athlete_id
    ORDER BY best_ratio DESC
    LIMIT 1;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    # If no result is found, raise an exception
    if not result:
        raise HTTPException(status_code=404, detail="No athlete found")

    # Return the athlete's name and their best power-to-weight ratio
    return {"athlete": result["pseudo"], "best_power_to_weight_ratio": result["best_ratio"]}