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
                    {"range": [0, 50], "color": "#10B981"},
                    {"range": [51, 100], "color": "#FBBF24"},
                    {"range": [101, 150], "color": "#F97316"},
                    {"range": [151, 200], "color": "#EF4444"},
                    {"range": [201, 300], "color": "#8B5CF6"},
                    {"range": [301, 500], "color": "#7F1D1D"},
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
        {"emoji": "🟢", "name": "Good", "range": "0–50", "min": 0, "max": 50},
        {"emoji": "🟡", "name": "Moderate", "range": "51–100", "min": 51, "max": 100},
        {"emoji": "🟠", "name": "Unhealthy for Sensitive Groups", "range": "101–150", "min": 101, "max": 150},
        {"emoji": "🔴", "name": "Unhealthy", "range": "151–200", "min": 151, "max": 200},
        {"emoji": "🟣", "name": "Very Unhealthy", "range": "201–300", "min": 201, "max": 300},
        {"emoji": "⚫", "name": "Hazardous", "range": "301–500", "min": 301, "max": 500},
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