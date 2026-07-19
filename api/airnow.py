import json
import logging

import requests
import streamlit as st
from config import AIRNOW_API_KEY, AIRNOW_CURRENT_OBSERVATION_URL, AIRNOW_DISTANCE_MILES

logger = logging.getLogger(__name__)


@st.cache_data(ttl=1800)
def fetch_current_air_quality(zip_code: str) -> list[dict] | None:
    params = {
        "format": "application/json",
        "zipCode": zip_code,
        "distance": AIRNOW_DISTANCE_MILES,
        "API_KEY": AIRNOW_API_KEY,
    }

    logger.info("Fetching AQI data for ZIP %s", zip_code)

    try:
        response = requests.get(
            AIRNOW_CURRENT_OBSERVATION_URL,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            logger.warning(
                "AQI data returned no readings for ZIP %s — no monitoring stations within range",
                zip_code,
            )
            return []

        logger.info(
            "AQI data fetched for ZIP %s — %d reading(s) returned",
            zip_code, len(data),
        )
        return data

    except requests.RequestException as e:
        if hasattr(e, "response") and e.response is not None:
            logger.error(
                "AirNow request failed for ZIP %s — HTTP %s",
                zip_code, e.response.status_code,
            )
        else:
            logger.error(
                "AirNow request failed for ZIP %s — %s",
                zip_code, type(e).__name__,
            )
        return None

    except (json.JSONDecodeError, ValueError):
        logger.error("AirNow returned unparseable response for ZIP %s", zip_code)
        return None
