# Routes for performance management
from fastapi import APIRouter, HTTPException
from app.db.queries import add_performance, get_test_types, get_performances_by_athlete, get_connection
from app.schema.performance import AddPerformance, UpdatePerformance

router = APIRouter()

@router.post("/")
def create_test(add_test: AddPerformance):
    """
    Add a new performance for an athlete.
    """
    try:
        # Add the performance to the database
        add_performance(
            add_test.power_max, add_test.hr_max, add_test.vo2_max,
            add_test.rf_max, add_test.cadence_max,
            add_test.athlete_id, add_test.test_type_id
        )
        return {"message": "Test successfully added"}
    except Exception as e:
        # Raise an exception if adding the performance fails
        raise HTTPException(status_code=400, detail="Error while adding performance")


@router.get("/types")
def get_all_test_types():
    """
    Retrieve all available test types.
    """
    # Get all test types from the database
    test_types = get_test_types()
    if not test_types:
        raise HTTPException(status_code=404, detail="No test types found")
    return {"test_types": [dict(test_type) for test_type in test_types]}


@router.get("/{athlete_id}")
def get_performances(athlete_id: int):
    """
    Retrieve all performances for a specific athlete.
    """
    # Get all performances for the given athlete ID
    performances = get_performances_by_athlete(int(athlete_id))
    if not performances:
        raise HTTPException(status_code=505, detail="No tests found for this athlete")
    return {"tests": [dict(test) for test in performances]}


@router.put("/update/{performance_id}")
def update_performance(update: UpdatePerformance, performance_id: int):
    """
    Update an existing performance.
    """
    # Get a connection to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the performance exists
    cursor.execute("SELECT * FROM performance WHERE id = ?;", (performance_id,))
    performance = cursor.fetchone()
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")

    # Build the update query dynamically
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

    # If no fields to update, raise an exception
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    # Add the performance ID to the list of values
    update_values.append(performance_id)

    # Execute the update query
    query = f"UPDATE performance SET {', '.join(update_fields)} WHERE id = ?;"
    cursor.execute(query, update_values)
    conn.commit()
    conn.close()

    return {"message": "Performance successfully updated"}


@router.delete("/delete/{performance_id}")
def delete_performance(performance_id: int):
    """
    Delete an existing performance.
    """
    # Get a connection to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the performance exists
    cursor.execute("SELECT * FROM performance WHERE id = ?;", (performance_id,))
    performance = cursor.fetchone()
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")

    # Delete the performance
    cursor.execute("DELETE FROM performance WHERE id = ?;", (performance_id,))
    conn.commit()
    conn.close()

    return {"message": "Performance successfully deleted"}