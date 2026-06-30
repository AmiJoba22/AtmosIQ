_REQUIRED_KEYS = ("AQI", "ParameterName", "ReportingArea", "StateCode", "Category")


def _is_valid_reading(reading: dict) -> bool:
    if not all(key in reading for key in _REQUIRED_KEYS):
        return False
    category = reading.get("Category")
    return isinstance(category, dict) and "Name" in category


def extract_main_reading(data: list[dict]) -> dict | None:
    pm25_reading = next(
        (item for item in data if item.get("ParameterName") == "PM2.5"),
        None,
    )

    if pm25_reading and _is_valid_reading(pm25_reading):
        return pm25_reading

    for reading in data:
        if _is_valid_reading(reading):
            return reading

    return None
