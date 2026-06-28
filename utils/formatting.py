def extract_main_reading(data: list[dict]) -> dict:
    pm25_reading = next(
        (item for item in data if item.get("ParameterName") == "PM2.5"),
        None
    )

    return pm25_reading or data[0]