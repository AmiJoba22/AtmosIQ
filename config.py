import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AtmosIQ"
TAGLINE = "Turning Air Quality Data into Everyday Decisions"

AIRNOW_API_KEY = os.getenv("AIRNOW_API_KEY")

if not AIRNOW_API_KEY:
    raise EnvironmentError(
        "AIRNOW_API_KEY is not set. "
        "Copy .env.example to .env and add your AirNow API key."
    )

AIRNOW_CURRENT_OBSERVATION_URL = "https://www.airnowapi.org/aq/observation/zipCode/current/"
AIRNOW_DISTANCE_MILES = 25