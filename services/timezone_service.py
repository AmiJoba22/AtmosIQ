from datetime import datetime
from zoneinfo import ZoneInfo

import pgeocode
from timezonefinder import TimezoneFinder


geo_locator = pgeocode.Nominatim("us")
timezone_finder = TimezoneFinder()


def get_timezone_from_zip(zip_code: str) -> str | None:
    location = geo_locator.query_postal_code(zip_code)

    if location is None or location.latitude != location.latitude:
        return None

    timezone_name = timezone_finder.timezone_at(
        lat=location.latitude,
        lng=location.longitude
    )

    return timezone_name


def get_local_time_from_zip(zip_code: str) -> str:
    timezone_name = get_timezone_from_zip(zip_code)

    if timezone_name is None:
        return "Local time unavailable"

    local_time = datetime.now(ZoneInfo(timezone_name))

    return local_time.strftime("%I:%M %p")