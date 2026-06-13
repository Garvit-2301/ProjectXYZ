from pydantic import BaseModel
from typing import Optional

class Workout(BaseModel):

    activity_name: Optional[str] = None
    activity_type: Optional[str] = None
    duration: Optional[float] = None
    calories: Optional[float] = None
    average_hr: Optional[float] = None
    max_hr: Optional[float] = None
    distance: Optional[float] = None