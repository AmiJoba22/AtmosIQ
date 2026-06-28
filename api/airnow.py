import requests
from config import AIRNOW_API_KEY, AIRNOW_CURRENT_OBSERVATION_URL, AIRNOW_DISTANCE_MILES


def fetch_current_air_quality(zip_code: str) -> list[dict] | None:
    params = {
        "format": "application/json",
        "zipCode": zip_code,
        "distance": AIRNOW_DISTANCE_MILES,
        "API_KEY": AIRNOW_API_KEY,
    }

    try:
        response = requests.get(
            AIRNOW_CURRENT_OBSERVATION_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data if data else None
    except requests.RequestException:
        return None