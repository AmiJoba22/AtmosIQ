import logging
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import pgeocode
from timezonefinder import TimezoneFinder

logger = logging.getLogger(__name__)

geo_locator = pgeocode.Nominatim("us")
timezone_finder = TimezoneFinder()


def get_timezone_from_zip(zip_code: str) -> str | None:
    location = geo_locator.query_postal_code(zip_code)

    if location is None or pd.isna(location.latitude):
        logger.warning("No coordinates found for ZIP %s — local time unavailable", zip_code)
        return None

    timezone_name = timezone_finder.timezone_at(
        lat=location.latitude,
        lng=location.longitude
    )

    if timezone_name is None:
        logger.warning("No timezone found for ZIP %s — local time unavailable", zip_code)

    return timezone_name


def get_local_time_from_zip(zip_code: str) -> str:
    timezone_name = get_timezone_from_zip(zip_code)

    if timezone_name is None:
        return "Local time unavailable"

    local_time = datetime.now(ZoneInfo(timezone_name))

    return local_time.strftime("%I:%M %p")
