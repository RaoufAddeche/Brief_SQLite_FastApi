from pydantic import BaseModel


class AddPerformance(BaseModel):
    power_max: float
    hr_max: float
    vo2_max: float
    rf_max: float
    cadence_max: float
    athlete_id: int
    test_type_id: int


class UpdatePerformance(BaseModel):
    power_max: float = None
    hr_max: int = None
    vo2_max: float = None
    rf_max: int = None
    cadence_max: int = None