import constants

import plotly.graph_objects as go
import streamlit as st


def render_aqi_gauge(current_aqi: int) -> None:
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=current_aqi,
            title={"text": "Current AQI"},
            gauge={
                "axis": {"range": [0, 500]},
                "bar": {"color": "#22D3EE"},
                "steps": [
                    {"range": [0,                                constants.AQI_GOOD],           "color": constants.COLOR_GOOD},
                    {"range": [constants.AQI_GOOD + 1,           constants.AQI_MODERATE],       "color": constants.COLOR_MODERATE},
                    {"range": [constants.AQI_MODERATE + 1,       constants.AQI_SENSITIVE],      "color": constants.COLOR_SENSITIVE},
                    {"range": [constants.AQI_SENSITIVE + 1,      constants.AQI_UNHEALTHY],      "color": constants.COLOR_UNHEALTHY},
                    {"range": [constants.AQI_UNHEALTHY + 1,      constants.AQI_VERY_UNHEALTHY], "color": constants.COLOR_VERY_UNHEALTHY},
                    {"range": [constants.AQI_VERY_UNHEALTHY + 1, 500],                          "color": constants.COLOR_HAZARDOUS},
                ],
            },
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#F8FAFC"},
        height=320,
        margin=dict(l=20, r=20, t=50, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)


def render_aqi_health_guide(current_aqi: int) -> None:
    categories = [
        {
            "emoji": constants.EMOJI_GOOD,
            "name": constants.LABEL_GOOD,
            "range": f"0–{constants.AQI_GOOD}",
            "min": 0,
            "max": constants.AQI_GOOD,
        },
        {
            "emoji": constants.EMOJI_MODERATE,
            "name": constants.LABEL_MODERATE,
            "range": f"{constants.AQI_GOOD + 1}–{constants.AQI_MODERATE}",
            "min": constants.AQI_GOOD + 1,
            "max": constants.AQI_MODERATE,
        },
        {
            "emoji": constants.EMOJI_SENSITIVE,
            "name": constants.LABEL_SENSITIVE,
            "range": f"{constants.AQI_MODERATE + 1}–{constants.AQI_SENSITIVE}",
            "min": constants.AQI_MODERATE + 1,
            "max": constants.AQI_SENSITIVE,
        },
        {
            "emoji": constants.EMOJI_UNHEALTHY,
            "name": constants.LABEL_UNHEALTHY,
            "range": f"{constants.AQI_SENSITIVE + 1}–{constants.AQI_UNHEALTHY}",
            "min": constants.AQI_SENSITIVE + 1,
            "max": constants.AQI_UNHEALTHY,
        },
        {
            "emoji": constants.EMOJI_VERY_UNHEALTHY,
            "name": constants.LABEL_VERY_UNHEALTHY,
            "range": f"{constants.AQI_UNHEALTHY + 1}–{constants.AQI_VERY_UNHEALTHY}",
            "min": constants.AQI_UNHEALTHY + 1,
            "max": constants.AQI_VERY_UNHEALTHY,
        },
        {
            "emoji": constants.EMOJI_HAZARDOUS,
            "name": constants.LABEL_HAZARDOUS,
            "range": f"{constants.AQI_VERY_UNHEALTHY + 1}–500",
            "min": constants.AQI_VERY_UNHEALTHY + 1,
            "max": 500,
        },
    ]

    st.markdown("### 🌈 AQI Risk Levels")

    for category in categories:
        active = category["min"] <= current_aqi <= category["max"]

        style = ""
        if active:
            style = """
                border:2px solid #22D3EE;
                background:rgba(34,211,238,.12);
                box-shadow:0 0 18px rgba(34,211,238,.20);
            """

        st.markdown(
            f"""
            <div class="aqi-guide-item" style="{style}">
                <strong>{category["emoji"]} {category["name"]}</strong>
                <span style="float:right;font-weight:700;color:#CBD5E1;">
                    {category["range"]}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
