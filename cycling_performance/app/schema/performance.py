from pydantic import BaseModel


class AddPerformance(BaseModel):
    power_max: float
    hr_max: float
    vo2_max: float
    rf_max: float
    cadence_max: float
    athlete_id: int
    test_type_id: int

