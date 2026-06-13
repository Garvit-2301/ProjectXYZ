from pydantic import BaseModel
from typing import Optional

class RecoveryMetrics(BaseModel):

    sleep_score: Optional[float] = None
    stress_score: Optional[float] = None
    body_battery: Optional[float] = None
    resting_hr: Optional[float] = None
    hrv: Optional[float] = None
    readiness: Optional[float] = None