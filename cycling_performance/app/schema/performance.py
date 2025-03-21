from pydantic import BaseModel

# Schema for adding a new performance
class AddPerformance(BaseModel):
    """
    Schema for adding a new performance.
    """
    power_max: float  # Maximum power achieved during the test
    hr_max: float     # Maximum heart rate during the test
    vo2_max: float    # Maximum VO2 (oxygen consumption) during the test
    rf_max: float     # Maximum respiratory frequency during the test
    cadence_max: float  # Maximum cadence during the test
    athlete_id: int   # ID of the athlete associated with the performance
    test_type_id: int # ID of the test type associated with the performance


# Schema for updating an existing performance
class UpdatePerformance(BaseModel):
    """
    Schema for updating an existing performance.
    Fields are optional to allow partial updates.
    """
    power_max: float = None  # Updated maximum power (optional)
    hr_max: int = None       # Updated maximum heart rate (optional)
    vo2_max: float = None    # Updated maximum VO2 (optional)
    rf_max: int = None       # Updated respiratory frequency (optional)
    cadence_max: int = None  # Updated cadence (optional)