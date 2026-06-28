from services.recommendation import get_recommendation


def branded_response(message: str) -> str:
    return message


def air_quality_summary(aqi: int, category: str) -> str:
    if aqi <= 50:
        return "Today's air quality looks good."
    if aqi <= 100:
        return "Today's air quality is moderate."
    if aqi <= 150:
        return "Air quality may affect sensitive groups today."
    if aqi <= 200:
        return "Air quality is unhealthy today."
    if aqi <= 300:
        return "Air quality is very unhealthy today."
    return "Air quality is hazardous today."


def generate_chatbot_response(
    question: str,
    aqi: int,
    category: str,
    pollutant: str
) -> str:
    question = question.lower()
    summary = air_quality_summary(aqi, category)

    if any(phrase in question for phrase in ["who is atmosiq", "what is atmosiq", "tell me about atmosiq", "who are you"]):
     return branded_response(
        "I'm AtmosIQ, your intelligent air quality companion. "
        "I help turn live air quality data into simple guidance so you can make better everyday decisions about outdoor activity, health, and environmental awareness."
    )

    if any(word in question for word in ["run", "exercise", "workout", "jog"]):
        if aqi <= 100:
            return branded_response(
                f"{summary} Outdoor exercise should be reasonable for most people. "
                "If you are sensitive to air pollution, keep the workout lighter and pay attention to how you feel."
            )
        return branded_response(
            f"{summary} I would avoid intense outdoor exercise today and consider moving your workout indoors."
        )

    if any(word in question for word in ["kids", "children", "child", "play", "recess"]):
        if aqi <= 50:
            return branded_response(
                f"{summary} Outdoor play is a good option for most children."
            )
        if aqi <= 100:
            return branded_response(
                f"{summary} Outdoor play may be okay, but children who are sensitive to air pollution should take breaks."
            )
        return branded_response(
            f"{summary} I would limit outdoor play for children today, especially if they have asthma, allergies, or breathing sensitivity."
        )

    if "mask" in question:
        if aqi <= 100:
            return branded_response(
                f"{summary} A mask is usually not necessary for most people, but sensitive individuals should use personal judgment."
            )
        return branded_response(
            f"{summary} Wearing a well-fitting mask outdoors may help reduce exposure, especially for sensitive groups."
        )

    if any(word in question for word in ["asthma", "breathing", "allergies", "lungs"]):
        if aqi <= 100:
            return branded_response(
                f"{summary} If you have asthma or breathing sensitivity, stay aware of symptoms and follow your healthcare provider's guidance."
            )
        return branded_response(
            f"{summary} If you have asthma, allergies, or breathing sensitivity, reduce prolonged outdoor activity and keep prescribed medication nearby."
        )

    if any(word in question for word in ["hiking", "bike", "cycling", "walk", "dog"]):
        if aqi <= 100:
            return branded_response(
                f"{summary} Outdoor activity should be manageable for most people. Consider keeping it shorter if you are sensitive."
            )
        return branded_response(
            f"{summary} I would shorten outdoor activities today or choose an indoor alternative if possible."
        )

    if any(word in question for word in ["mood", "focus", "tired", "energy"]):
        if aqi <= 100:
            return branded_response(
                f"{summary} Air quality is less likely to be a major issue for most people today, but mood and focus can also be affected by sleep, stress, hydration, and overall health."
            )
        return branded_response(
                f"{summary} Poor air quality may affect comfort, energy, or focus for some people. It is still one factor among sleep, stress, hydration, and health."
        )

    if "pm2.5" in question or "pm25" in question:
        return branded_response(
            f"The main pollutant currently reported is {pollutant}. PM2.5 refers to tiny particles that can travel deep into the lungs."
        )

    if "aqi" in question:
        return branded_response(
            f"AQI stands for Air Quality Index. Today's category is {category}, which helps explain how clean or polluted the air is."
        )

    if any(word in question for word in ["safe", "outside", "outdoors"]):
        return branded_response(
            f"{summary} {get_recommendation(aqi)}"
        )

    return branded_response(
        f"{summary} {get_recommendation(aqi)}"
    )