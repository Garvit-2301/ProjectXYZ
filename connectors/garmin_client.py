from garminconnect import Garmin
from datetime import datetime

class GarminClient:
    def __init__(self, email: str, password: str):
        self.client = Garmin(email, password)
        self.client.login()

    def safe(self, func, *args):
        try:
            return func(*args)
        
        except:
            return {}
        
    def get_complete_health_profile(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return{
            "date": today,
            "daily_stats": self.safe(self.client.get_stats, today),
            "sleep": self.safe(self.client.get_sleep_data, today),
            "stress": self.safe(self.client.get_stress_data, today),
            "body_battery": self.safe(self.client.get_body_battery, today),
            "heart_rate": self.safe(self.client.get_heart_rates, today),
            "hrv": self.safe(self.client.get_hrv_data, today),
            "respiration": self.safe(self.client.get_respiration_data, today),
            "hydration": self.safe(self.client.get_hydration_data, today),
            "training_readiness": self.safe(self.client.get_training_readiness, today),
            "max_metrics": self.safe(self.client.get_max_metrics, today),
            "activities": self.safe(self.client.get_activities, 0, 20)
        }