from pydantic import BaseModel
from typing import Dict
from typing import List

from models.workout import Workout
from models.recovery import RecoveryMetrics

class HealthProfile(BaseModel):

    recovery: RecoveryMetrics
    workouts: List[Workout]
    wearable_raw_data: Dict