import os
from dotenv import load_dotenv
from connectors.garmin_client import GarminClient
from normalization.parser import GarminNormalizer
from agents.orchestrator.router import Router
from storage.db import init_db
from utils.formatter import(
    banner,
    print_response
)

load_dotenv

GARMIN_EMAIL = os.getenv("GARMIN_EMAIL")
GARMIN_PASSWORD = os.getenv("GARMIN_PASSWORD")

banner()

print("connecting to Garmin")

client = GarminClient(
    GARMIN_EMAIL,
    GARMIN_PASSWORD
)

print("pulling wearable data")

raw_data = (client.get_complete_health_profile())

print("Normalizing Data")

normalizer = GarminNormalizer()

profile = normalizer.normalize(raw_data)

print("Initializing Agents")

router = Router()

init_db()

print("LifeBot is ready.")

while True:
    query = input("You: ")

    if query.lower() in [
        "exit","quit"
    ]:
        break

    response = router.run(
        query,
        profile.model_dump()
    )

    print_response(response)