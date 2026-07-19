import constants
from services.recommendation import get_aqi_style, get_recommendation


class TestGetAqiStyle:
    def test_boundary_good(self):
        # AQI 50 is the last value in "Good" — must return Good label
        assert get_aqi_style(50)["label"] == constants.LABEL_GOOD

    def test_boundary_moderate_low(self):
        # AQI 51 is the first value in "Moderate" — must NOT return Good
        assert get_aqi_style(51)["label"] == constants.LABEL_MODERATE

    def test_boundary_moderate_high(self):
        assert get_aqi_style(100)["label"] == constants.LABEL_MODERATE

    def test_boundary_sensitive_low(self):
        assert get_aqi_style(101)["label"] == constants.LABEL_SENSITIVE

    def test_boundary_sensitive_high(self):
        assert get_aqi_style(150)["label"] == constants.LABEL_SENSITIVE

    def test_boundary_unhealthy_low(self):
        assert get_aqi_style(151)["label"] == constants.LABEL_UNHEALTHY

    def test_boundary_unhealthy_high(self):
        assert get_aqi_style(200)["label"] == constants.LABEL_UNHEALTHY

    def test_boundary_very_unhealthy_low(self):
        assert get_aqi_style(201)["label"] == constants.LABEL_VERY_UNHEALTHY

    def test_boundary_very_unhealthy_high(self):
        assert get_aqi_style(300)["label"] == constants.LABEL_VERY_UNHEALTHY

    def test_boundary_hazardous(self):
        # AQI 301 is the first value beyond Very Unhealthy — must return Hazardous
        assert get_aqi_style(301)["label"] == constants.LABEL_HAZARDOUS

    def test_style_dict_has_required_keys(self):
        result = get_aqi_style(50)
        assert "label" in result and "emoji" in result and "color" in result

    def test_color_matches_label(self):
        # Proves label and color are from the same category — not accidentally mismatched
        result = get_aqi_style(50)
        assert result["color"] == constants.COLOR_GOOD


class TestGetRecommendation:
    def test_good_range(self):
        assert "good" in get_recommendation(1).lower()

    def test_moderate_range(self):
        assert "moderate" in get_recommendation(75).lower()

    def test_sensitive_range(self):
        assert "sensitive" in get_recommendation(125).lower()

    def test_unhealthy_range(self):
        assert "unhealthy" in get_recommendation(175).lower()

    def test_very_unhealthy_range(self):
        assert "very unhealthy" in get_recommendation(250).lower()

    def test_hazardous_range(self):
        assert "hazardous" in get_recommendation(400).lower()

    def test_returns_string(self):
        assert isinstance(get_recommendation(50), str)
