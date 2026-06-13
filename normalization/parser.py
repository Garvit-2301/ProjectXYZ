from models.workout import Workout
from models.health_profile import HealthProfile
from models.recovery import RecoveryMetrics

class GarminNormalizer:

    def normalize(self, raw_data):
        recovery  =self.build_recovery(raw_data)
        workouts = self.build_workouts(raw_data.get("activities", []))

        return HealthProfile(
            recovery=recovery,
            workouts=workouts, 
            wearable_raw_data=raw_data
        )
    
    def build_recovery(self, raw_data):

        sleep_score = (
            raw_data.get("sleep", {}).get("dailySleepDTO", {}).get("sleepScores", {}).get("overall", {}).get("value", None)
        )

        stress = (
            raw_data.get("stress", {}).get("avgStressLevel", None)
        )

        body_battery = (
            raw_data.get("body_battery", {}).get("chargedValue", None)
        )

        return RecoveryMetrics(
            sleep_score=sleep_score,
            stress_score=stress,
            body_battery=body_battery   
        )
    
    def build_workouts(self, activities):

        parsed = []

        for activity in activities:
            parsed.append(
                Workout(
                    activity_name=activity.get("activityName"),
                    activity_type=activity.get("activityType", {}).get("typeKey"),
                    duration=activity.get("duration"),
                    calories=activity.get("calories"),
                    average_hr=activity.get("averageHR"),
                    max_hr=activity.get("maxHR"),
                    distance=activity.get("distance")
                )
            )
        return parsed