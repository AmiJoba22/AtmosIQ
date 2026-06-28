import html
import streamlit as st


def render_metric_card(label: str, value: str | int, caption: str = "") -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-caption">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chat_bubble(role: str, content: str) -> None:
    safe_content = html.escape(content)

    if role == "user":
        bubble_class = "user-bubble"
        icon = "You"
    else:
        bubble_class = "assistant-bubble"
        icon = "🤖 AtmosIQ"

    st.markdown(
        f"""
        <div class="{bubble_class}">
            <strong>{icon}</strong><br>
            {safe_content}
        </div>
        """,
        unsafe_allow_html=True,
    )