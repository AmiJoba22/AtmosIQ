import streamlit as st

from services.recommendation import get_aqi_style, get_recommendation
from ui.cards import render_metric_card
from ui.charts import render_aqi_gauge, render_aqi_health_guide
from datetime import datetime



def render_dashboard(saved: dict) -> None:
    aqi = saved["aqi"]
    style = get_aqi_style(aqi)

    st.markdown(
        f"""
        <div class="aqi-hero-card" style="border-color:{style['color']}; box-shadow:0 0 35px {style['color']}44;">
            <div class="aqi-badge" style="background:{style['color']}22; color:{style['color']}; border:1px solid {style['color']}66;">
                {style['emoji']} {style['label'].upper()}
            </div>
            <div class="aqi-number">AQI {aqi}</div>
            <div class="aqi-location">
            <div class="aqi-location-label">📍 Reporting Area</div>
            <div>{saved["reporting_area"]}, {saved["state_code"]}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    #current_time = datetime.now().strftime("%I:%M %p")

    col1, col2, col3 = st.columns(3)

    with col1:
     render_metric_card(
    "🕒 Local Time",
    saved["local_time"],
    "Based on ZIP code"
)

    with col2:
        render_metric_card("Category", saved["category"], "Health level")

    with col3:
        render_metric_card("Pollutant", saved["pollutant"], "Main pollutant")

    st.markdown(
        f"""
        <div class="recommendation-card">
            <div class="section-title">❤️ Health Recommendation</div>
            {get_recommendation(aqi)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 AQI Risk Scale</div>', unsafe_allow_html=True)
    render_aqi_gauge(aqi)
    render_aqi_health_guide(aqi)
    st.markdown("</div>", unsafe_allow_html=True)