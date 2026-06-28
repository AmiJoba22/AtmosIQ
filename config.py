import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AtmosIQ"
TAGLINE = "Turning Air Quality Data into Everyday Decisions"

AIRNOW_API_KEY = os.getenv("AIRNOW_API_KEY")
AIRNOW_CURRENT_OBSERVATION_URL = "https://www.airnowapi.org/aq/observation/zipCode/current/"
AIRNOW_DISTANCE_MILES = 25