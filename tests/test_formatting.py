from utils.formatting import extract_main_reading

VALID_PM25 = {
    "AQI": 42,
    "ParameterName": "PM2.5",
    "ReportingArea": "Stone Mountain",
    "StateCode": "GA",
    "Category": {"Number": 1, "Name": "Good"},
}

VALID_OZONE = {
    "AQI": 38,
    "ParameterName": "O3",
    "ReportingArea": "Stone Mountain",
    "StateCode": "GA",
    "Category": {"Number": 1, "Name": "Good"},
}

INVALID_MISSING_KEY = {
    "AQI": 42,
    "ParameterName": "PM2.5",
    # Missing ReportingArea, StateCode, Category
}

INVALID_BAD_CATEGORY = {
    "AQI": 42,
    "ParameterName": "PM2.5",
    "ReportingArea": "Stone Mountain",
    "StateCode": "GA",
    "Category": "Good",  # String instead of dict — fails _is_valid_reading
}


def test_returns_pm25_when_present_and_valid():
    result = extract_main_reading([VALID_PM25, VALID_OZONE])
    assert result is not None
    assert result["ParameterName"] == "PM2.5"


def test_prefers_pm25_over_other_pollutants():
    # PM2.5 appears second — function must still select it, not the first item
    result = extract_main_reading([VALID_OZONE, VALID_PM25])
    assert result["ParameterName"] == "PM2.5"


def test_falls_back_to_first_valid_when_no_pm25():
    result = extract_main_reading([VALID_OZONE])
    assert result is not None
    assert result["ParameterName"] == "O3"


def test_skips_invalid_pm25_and_falls_back():
    # PM2.5 is present but invalid — should fall back to the valid O3 reading
    result = extract_main_reading([INVALID_BAD_CATEGORY, VALID_OZONE])
    assert result is not None
    assert result["ParameterName"] == "O3"


def test_returns_none_when_all_readings_invalid():
    result = extract_main_reading([INVALID_MISSING_KEY, INVALID_BAD_CATEGORY])
    assert result is None


def test_returns_none_for_empty_list():
    result = extract_main_reading([])
    assert result is None


def test_category_name_accessible_on_valid_result():
    result = extract_main_reading([VALID_PM25])
    assert result["Category"]["Name"] == "Good"
