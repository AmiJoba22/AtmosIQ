import streamlit as st

from api.airnow import fetch_current_air_quality
from config import APP_NAME
from services.chatbot import generate_chatbot_response
from services.location import clean_zip_code, is_valid_zip_code
from services.timezone_service import get_local_time_from_zip
from ui.cards import render_chat_bubble
from ui.dashboard import render_dashboard
from ui.sidebar import render_sidebar
from ui.styles import apply_custom_styles, render_footer, render_hero
from utils.formatting import extract_main_reading


st.set_page_config(
    page_title=APP_NAME,
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_custom_styles()

if "aqi_data" not in st.session_state:
    st.session_state.aqi_data = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "zip_input_key" not in st.session_state:
    st.session_state.zip_input_key = 0

if "pending_warning" not in st.session_state:
    st.session_state.pending_warning = None


def submit_question(question: str) -> None:
    if st.session_state.aqi_data is None:
        st.session_state.pending_warning = (
            "🌍 AtmosIQ: First, enter your ZIP code and click "
            "**Get Air Quality** so I can personalize my answer."
        )
        return

    saved = st.session_state.aqi_data

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": question,
        }
    )

    answer = generate_chatbot_response(
        question=question,
        aqi=saved["aqi"],
        category=saved["category"],
        pollutant=saved["pollutant"],
    )

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )


render_hero()

zip_code, search_clicked, reset_clicked = render_sidebar()

if reset_clicked:
    st.session_state.aqi_data = None
    st.session_state.chat_history = []
    st.session_state.pending_warning = None
    st.session_state.zip_input_key += 1
    st.rerun()

if search_clicked:
    zip_code = clean_zip_code(zip_code)

    if not zip_code:
        st.warning("📍 Please enter a ZIP code before retrieving air quality.")
        st.stop()

    if not is_valid_zip_code(zip_code):
        st.warning("⚠️ Please enter a valid 5-digit ZIP code.")
        st.stop()

    with st.spinner("🌍 AtmosIQ is analyzing today's air quality..."):
        data = fetch_current_air_quality(zip_code)

    if data is None:
        st.warning(
            "⚠️ AtmosIQ encountered a problem reaching the air quality service. "
            "Please check your connection and try again in a moment."
        )
    elif data == []:
        st.warning(
            "📍 No air quality monitoring stations were found within 25 miles of "
            f"ZIP code {zip_code}. Try a ZIP code for a nearby city."
        )
    else:
        main_reading = extract_main_reading(data)

        if main_reading is None:
            st.warning(
                "⚠️ AtmosIQ received data but it was not in the expected format. "
                "Please try again or use a different ZIP code."
            )
        else:
            st.session_state.aqi_data = {
                "aqi": main_reading.get("AQI"),
                "pollutant": main_reading["ParameterName"],
                "category": main_reading["Category"]["Name"],
                "reporting_area": main_reading["ReportingArea"],
                "state_code": main_reading["StateCode"],
                "zip_code": zip_code,
                "local_time": get_local_time_from_zip(zip_code),
            }

            st.session_state.chat_history = []
            st.session_state.pending_warning = None

if st.session_state.aqi_data is not None:
    saved = st.session_state.aqi_data
    render_dashboard(saved)

st.markdown(
    """
    <div class="ai-panel-header">
        <div class="ai-panel-title">AtmosIQ AI</div>
        <div class="ai-panel-subtitle">
            Ask about outdoor activity, health, pollutants, or today's air quality.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


if st.session_state.pending_warning:
    st.info(st.session_state.pending_warning)
    st.session_state.pending_warning = None

for message in st.session_state.chat_history:
    render_chat_bubble(message["role"], message["content"])

st.markdown("##### 💡 Quick Questions")

col1, col2 = st.columns(2)

with col1:
    st.button(
        "🏃 Safe to Run?",
        on_click=submit_question,
        args=("Is it safe to run outside today?",),
    )

    st.button(
        "👶 Kids Outside?",
        on_click=submit_question,
        args=("Can my kids play outside?",),
    )

with col2:
    st.button(
        "😷 Wear a Mask?",
        on_click=submit_question,
        args=("Should I wear a mask?",),
    )

    st.button(
        "🥾 Good Day to Hike?",
        on_click=submit_question,
        args=("Is today good for hiking?",),
    )

    st.markdown(
    """
    <div style="margin-top: 20px;"></div>
    """,
    unsafe_allow_html=True,
)

with st.form("atmosiq_chat_form", clear_on_submit=True):
    typed_question = st.text_input(
        "Ask AtmosIQ",
        placeholder="Example: Is it safe to run outside today?",
    )

    form_submitted = st.form_submit_button("Ask AtmosIQ")

if form_submitted:
    if not typed_question:
        st.warning("Please enter a question for AtmosIQ.")
    else:
        submit_question(typed_question)
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

render_footer()