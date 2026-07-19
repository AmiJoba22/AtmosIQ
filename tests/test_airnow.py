import json
from unittest.mock import MagicMock, patch

import pytest

from api.airnow import fetch_current_air_quality

SAMPLE_RESPONSE = [
    {
        "AQI": 42,
        "ParameterName": "PM2.5",
        "ReportingArea": "Stone Mountain",
        "StateCode": "GA",
        "Category": {"Number": 1, "Name": "Good"},
    }
]


@pytest.fixture(autouse=True)
def clear_cache():
    # @st.cache_data caches by function arguments. Clearing before every test
    # ensures the mocked HTTP response is actually called — not a cached real result.
    fetch_current_air_quality.clear()
    yield


def _make_response(json_data=None, status_code=200, raise_for_status=None):
    mock = MagicMock()
    mock.status_code = status_code
    if raise_for_status:
        mock.raise_for_status.side_effect = raise_for_status
    else:
        mock.raise_for_status.return_value = None
    if json_data is not None:
        mock.json.return_value = json_data
    return mock


class TestFetchCurrentAirQuality:
    def test_success_returns_list(self):
        # Proves: a clean 200 response with valid JSON returns the parsed list
        with patch("api.airnow.requests.get") as mock_get:
            mock_get.return_value = _make_response(json_data=SAMPLE_RESPONSE)
            result = fetch_current_air_quality("30088")
        assert result == SAMPLE_RESPONSE

    def test_empty_response_returns_empty_list(self):
        # Proves: AirNow returning [] (no nearby stations) returns [] not None
        with patch("api.airnow.requests.get") as mock_get:
            mock_get.return_value = _make_response(json_data=[])
            result = fetch_current_air_quality("00000")
        assert result == []

    def test_http_error_returns_none(self):
        # Proves: a 4xx/5xx response returns None so app.py shows the error state
        import requests as req
        http_err = req.HTTPError(response=MagicMock(status_code=403))
        with patch("api.airnow.requests.get") as mock_get:
            mock_get.return_value = _make_response(
                status_code=403,
                raise_for_status=http_err,
            )
            result = fetch_current_air_quality("30088")
        assert result is None

    def test_connection_error_returns_none(self):
        # Proves: a network-level failure (no internet) returns None not an exception
        import requests as req
        with patch("api.airnow.requests.get") as mock_get:
            mock_get.side_effect = req.ConnectionError("Network unreachable")
            result = fetch_current_air_quality("30088")
        assert result is None

    def test_invalid_json_returns_none(self):
        # Proves: an unparseable response body returns None not a crash
        with patch("api.airnow.requests.get") as mock_get:
            mock = _make_response()
            mock.json.side_effect = json.JSONDecodeError("Expecting value", "", 0)
            mock_get.return_value = mock
            result = fetch_current_air_quality("30088")
        assert result is None

    def test_timeout_returns_none(self):
        # Proves: a slow AirNow server (ReadTimeout) returns None not an exception
        import requests as req
        with patch("api.airnow.requests.get") as mock_get:
            mock_get.side_effect = req.ReadTimeout("timed out")
            result = fetch_current_air_quality("30088")
        assert result is None
