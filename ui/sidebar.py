import streamlit as st


def render_sidebar() -> tuple[str, bool, bool]:
    st.sidebar.markdown("## 🌍 AtmosIQ")
    st.sidebar.caption("Real-Time Air Quality Intelligence")
    st.sidebar.divider()

    zip_code = st.sidebar.text_input(
        label="📍 ZIP Code",
        placeholder="Enter ZIP code",
        help="Enter a valid 5-digit U.S. ZIP code to retrieve local air quality.",
        max_chars=5,
        key=f"zip_code_input_{st.session_state.zip_input_key}",
    )

    search_clicked = st.sidebar.button("Get Air Quality")
    reset_clicked = st.sidebar.button("Reset AtmosIQ")

    st.sidebar.divider()
    st.sidebar.caption("Powered by AirNow API")

    return zip_code, search_clicked, reset_clicked