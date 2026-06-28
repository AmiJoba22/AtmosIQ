def get_aqi_style(aqi: int) -> dict:
    if aqi <= 50:
        return {"label": "Good", "emoji": "🟢", "color": "#10B981"}
    if aqi <= 100:
        return {"label": "Moderate", "emoji": "🟡", "color": "#FBBF24"}
    if aqi <= 150:
        return {"label": "Unhealthy for Sensitive Groups", "emoji": "🟠", "color": "#F97316"}
    if aqi <= 200:
        return {"label": "Unhealthy", "emoji": "🔴", "color": "#EF4444"}
    if aqi <= 300:
        return {"label": "Very Unhealthy", "emoji": "🟣", "color": "#8B5CF6"}
    return {"label": "Hazardous", "emoji": "⚫", "color": "#7F1D1D"}


def get_recommendation(aqi: int) -> str:
    if aqi <= 50:
        return "Air quality looks good today. Outdoor activities are a strong option for most people."
    if aqi <= 100:
        return "Air quality is moderate. Most people can go outside, but sensitive groups should pay attention."
    if aqi <= 150:
        return "Air quality may affect sensitive groups. Consider reducing prolonged outdoor activity if you have asthma, allergies, or breathing sensitivity."
    if aqi <= 200:
        return "Air quality is unhealthy. Consider limiting long or intense outdoor activity."
    if aqi <= 300:
        return "Air quality is very unhealthy. Outdoor activity should be limited when possible."
    return "Air quality is hazardous. Staying indoors is the safest option."