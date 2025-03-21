# Routes for athlete management
from fastapi import APIRouter, HTTPException, Depends
from app.db.queries import add_caracteristic, get_performances_by_athlete
from app.utils.dependencies import get_current_user
from app.schema.catacteristic import UserCaracteristic

router = APIRouter()

@router.post("/caracteristic")
def add_athlete_caracteristic(user: UserCaracteristic):
    """
    Add characteristics for an athlete.
    """
    try:
        # Add the athlete's characteristics to the database
        add_caracteristic(user.gender, user.age, user.weight, user.height, user.id_user)
        return {"message": "Characteristic successfully added"}
    except Exception as e:
        # Raise an exception if adding the characteristic fails
        raise HTTPException(status_code=400, detail="Error while adding the characteristic")


@router.get("/performance/{athlete_id}")
def get_athlete_performances(athlete_id):
    """
    Retrieve all performances for a specific athlete.
    """
    try:
        # Get all performances for the given athlete ID
        performances = get_performances_by_athlete(athlete_id)
        return {"performances": performances}
    except Exception as e:
        # Raise an exception if retrieving performances fails
        raise HTTPException(status_code=400, detail="Error while retrieving performances")


@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    """
    A protected route that requires authentication.
    """
    # Return a welcome message for the authenticated user
    return {"message": f"Welcome, {current_user['sub']}!"}