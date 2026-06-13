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

        # Handle body_battery which might be a list or dict
        body_battery_data = raw_data.get("body_battery", {})
        body_battery = None
        if isinstance(body_battery_data, dict):
            body_battery = body_battery_data.get("chargedValue", None)
        elif isinstance(body_battery_data, list) and len(body_battery_data) > 0:
            # If it's a list, try to get the first element's chargedValue
            body_battery = body_battery_data[0].get("chargedValue", None) if isinstance(body_battery_data[0], dict) else None

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