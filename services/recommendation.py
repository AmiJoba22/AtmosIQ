import constants


def get_aqi_style(aqi: int) -> dict:
    if aqi <= constants.AQI_GOOD:
        return {"label": constants.LABEL_GOOD, "emoji": constants.EMOJI_GOOD, "color": constants.COLOR_GOOD}
    if aqi <= constants.AQI_MODERATE:
        return {"label": constants.LABEL_MODERATE, "emoji": constants.EMOJI_MODERATE, "color": constants.COLOR_MODERATE}
    if aqi <= constants.AQI_SENSITIVE:
        return {"label": constants.LABEL_SENSITIVE, "emoji": constants.EMOJI_SENSITIVE, "color": constants.COLOR_SENSITIVE}
    if aqi <= constants.AQI_UNHEALTHY:
        return {"label": constants.LABEL_UNHEALTHY, "emoji": constants.EMOJI_UNHEALTHY, "color": constants.COLOR_UNHEALTHY}
    if aqi <= constants.AQI_VERY_UNHEALTHY:
        return {"label": constants.LABEL_VERY_UNHEALTHY, "emoji": constants.EMOJI_VERY_UNHEALTHY, "color": constants.COLOR_VERY_UNHEALTHY}
    return {"label": constants.LABEL_HAZARDOUS, "emoji": constants.EMOJI_HAZARDOUS, "color": constants.COLOR_HAZARDOUS}


def get_recommendation(aqi: int) -> str:
    if aqi <= constants.AQI_GOOD:
        return "Air quality looks good today. Outdoor activities are a strong option for most people."
    if aqi <= constants.AQI_MODERATE:
        return "Air quality is moderate. Most people can go outside, but sensitive groups should pay attention."
    if aqi <= constants.AQI_SENSITIVE:
        return "Air quality may affect sensitive groups. Consider reducing prolonged outdoor activity if you have asthma, allergies, or breathing sensitivity."
    if aqi <= constants.AQI_UNHEALTHY:
        return "Air quality is unhealthy. Consider limiting long or intense outdoor activity."
    if aqi <= constants.AQI_VERY_UNHEALTHY:
        return "Air quality is very unhealthy. Outdoor activity should be limited when possible."
    return "Air quality is hazardous. Staying indoors is the safest option."
