import streamlit as st


def apply_custom_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(34, 211, 238, 0.18), transparent 28%),
                radial-gradient(circle at top right, rgba(59, 130, 246, 0.16), transparent 28%),
                linear-gradient(135deg, #020617 0%, #0f172a 50%, #111827 100%);
            color: #f8fafc;
            min-height: 100vh;
        }

        header[data-testid="stHeader"] {
            background: #020617 !important;
            border-bottom: 1px solid rgba(34, 211, 238, 0.12);
        }

        div[data-testid="stToolbar"] {
           background: transparent !important;
        }

        .block-container {
          max-width: 1150px;
          padding-top: 4.5rem;
          padding-bottom: 3rem;
          padding-left: 2.5rem;
          padding-right: 2.5rem;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
            border-right: 1px solid rgba(34, 211, 238, 0.18);
        }

        .hero-card {
            padding: 34px;
            border-radius: 28px;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.94), rgba(14, 165, 233, 0.20));
            border: 1px solid rgba(34, 211, 238, 0.35);
            box-shadow: 0 0 40px rgba(34, 211, 238, 0.18);
            margin-bottom: 28px;
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.35);
            color: #6ee7b7;
            font-weight: 700;
            margin-bottom: 18px;
        }

        .hero-title {
            font-size: 3.4rem;
            font-weight: 900;
            letter-spacing: -0.05em;
            margin-bottom: 8px;
            color: #ffffff;
            text-shadow: 0 0 24px rgba(34, 211, 238, 0.35);
        }

        .hero-subtitle {
            color: #bae6fd;
            font-size: 1.15rem;
            max-width: 680px;
        }

        .metric-card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(34, 211, 238, 0.24);
            border-radius: 20px;
            padding: 22px;
            box-shadow: 0 0 24px rgba(34, 211, 238, 0.10);
            margin-bottom: 18px;
        }

        .metric-label {
            color: #93c5fd;
            font-size: 0.82rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 8px;
        }

        .metric-value {
            color: #ffffff;
            font-size: 2rem;
            font-weight: 900;
        }

        .metric-caption {
            color: #cbd5e1;
            font-size: 0.9rem;
            margin-top: 6px;
        }

        .aqi-hero-card {
            background:
                radial-gradient(circle at top left, rgba(34, 211, 238, 0.18), transparent 35%),
                linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.86));
            border: 1px solid rgba(34, 211, 238, 0.35);
            border-radius: 30px;
            padding: 34px;
            margin-bottom: 28px;
            text-align: center;
            box-shadow: 0 0 40px rgba(34, 211, 238, 0.18);
        }

        .aqi-badge {
            display: inline-block;
            padding: 9px 18px;
            border-radius: 999px;
            font-weight: 900;
            margin-bottom: 18px;
            letter-spacing: 0.06em;
        }

        .aqi-label {
            color: #93c5fd;
            font-size: 0.9rem;
            font-weight: 800;
            letter-spacing: 0.18em;
            text-transform: uppercase;
        }

        .aqi-number {
            font-size: 4.8rem;
            line-height: 1;
            font-weight: 950;
            color: #ffffff;
            margin: 8px 0 14px;
            text-shadow: 0 0 30px rgba(34, 211, 238, 0.35);
        }

        .aqi-location {
            color: #bae6fd;
            font-size: 1.2rem;
            font-weight: 700;
            margin-top: 10px;
        }

        .aqi-updated {
            color: #94a3b8;
            font-size: 0.95rem;
            margin-top: 10px;
        }

        .glass-card {
            background: rgba(15, 23, 42, 0.78);
            border: 1px solid rgba(148, 163, 184, 0.22);
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 12px 35px rgba(2, 6, 23, 0.35);
            margin-bottom: 22px;
        }

        .section-title {
            font-size: 1.35rem;
            font-weight: 900;
            color: #f8fafc;
            margin-bottom: 12px;
        }

        .recommendation-card {
            background: linear-gradient(135deg, rgba(37, 99, 235, 0.20), rgba(16, 185, 129, 0.14));
            border: 1px solid rgba(34, 211, 238, 0.24);
            border-radius: 22px;
            padding: 22px;
            color: #e0f2fe;
            box-shadow: 0 0 28px rgba(59, 130, 246, 0.12);
            margin-bottom: 24px;
        }

        .assistant-panel {
            background: rgba(2, 6, 23, 0.62);
            border: 1px solid rgba(34, 211, 238, 0.20);
            border-radius: 24px;
            padding: 24px;
            margin-top: 20px;
            box-shadow: 0 0 35px rgba(34, 211, 238, 0.10);
        }

        .example-pill {
            display: inline-block;
            padding: 8px 12px;
            margin: 6px 6px 6px 0;
            border-radius: 999px;
            background: rgba(59, 130, 246, 0.14);
            border: 1px solid rgba(147, 197, 253, 0.22);
            color: #dbeafe;
            font-size: 0.9rem;
        }

        .user-bubble {
            background: linear-gradient(135deg, #2563eb, #06b6d4);
            color: white;
            padding: 14px 16px;
            border-radius: 18px 18px 4px 18px;
            margin: 12px 0 12px auto;
            max-width: 78%;
            box-shadow: 0 0 18px rgba(59, 130, 246, 0.25);
        }

        .assistant-bubble {
            background: rgba(15, 23, 42, 0.90);
            color: #e5e7eb;
            padding: 16px 18px;
            border-radius: 18px 18px 18px 4px;
            margin: 12px auto 12px 0;
            max-width: 82%;
            border: 1px solid rgba(34, 211, 238, 0.22);
            box-shadow: 0 0 20px rgba(34, 211, 238, 0.10);
        }

        .footer {
            text-align: center;
            color: #94a3b8;
            padding: 28px 0 10px;
            border-top: 1px solid rgba(148, 163, 184, 0.18);
            margin-top: 30px;
        }

        .stButton button {
            width: 100%;
            border-radius: 14px;
            border: none;
            background: linear-gradient(135deg, #2563eb, #06b6d4);
            color: white;
            font-weight: 800;
            padding: 0.65rem 1rem;
        }

        .stTextInput input {
            border-radius: 14px;
        }



        section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

section[data-testid="stSidebar"] label {
    color: #dbeafe !important;
    font-weight: 700 !important;
}

section[data-testid="stSidebar"] p {
    color: #cbd5e1 !important;
}

section[data-testid="stSidebar"] .stCaptionContainer {
    color: #93c5fd !important;
}

section[data-testid="stSidebar"] input {
    background: #ffffff !important;
    color: #020617 !important;
}

.stTextInput input::placeholder {
    color: #64748b !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] input::placeholder {
    color: #64748b !important;
    opacity: 1 !important;
}

.ai-panel-header {
    padding-bottom: 16px;
    margin-bottom: 18px;
    border-bottom: 1px solid rgba(148, 163, 184, 0.18);
}

.ai-panel-title {
    font-size: 1.45rem;
    font-weight: 900;
    color: #f8fafc;
    letter-spacing: -0.02em;
}

.ai-panel-subtitle {
    color: #93c5fd;
    font-size: 0.95rem;
    margin-top: 6px;
    line-height: 1.6;
}

.aqi-location-label {
    color: #93c5fd;
    font-size: 0.82rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 800;
    margin-bottom: 4px;
}

.hero-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    text-align: center;

    padding: 48px 40px;

    border-radius: 28px;

    background: linear-gradient(
        135deg,
        rgba(15, 23, 42, 0.94),
        rgba(14, 165, 233, 0.20)
    );

    border: 1px solid rgba(34, 211, 238, 0.35);

    box-shadow: 0 0 40px rgba(34, 211, 238, 0.18);

    margin-bottom: 28px;
}

.hero-badge{
    display:inline-flex;
    align-items:center;
    justify-content:center;

    margin:0 auto 22px auto;

    padding:8px 16px;

    border-radius:999px;

    background:rgba(16,185,129,.15);

    border:1px solid rgba(16,185,129,.35);

    color:#6ee7b7;

    font-weight:700;
}

.hero-title{
    width:100%;

    text-align:center;

    font-size:3.4rem;

    font-weight:900;

    color:white;

    margin-bottom:12px;

    text-shadow:0 0 24px rgba(34,211,238,.35);
}

.hero-subtitle{
    max-width:700px;

    margin:0 auto;

    text-align:center;

    color:#bae6fd;

    font-size:1.15rem;

    line-height:1.7;
}

.stFormSubmitButton > button {
    color: #000000 !important;
    font-weight: 700;
}

        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-badge">🟢 Live Air Quality Monitoring</div>
            <div class="hero-title">🌍 AtmosIQ</div>
            <div class="hero-subtitle">
                Your intelligent air quality companion. Real-time environmental insights,
                personalized recommendations, and AI-powered guidance for everyday decisions.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        """
        <div class="footer">
            <strong>🌍 AtmosIQ</strong><br>
            Making healthier decisions through intelligent air quality insights.<br>
            Powered by Python • Streamlit • AirNow API
        </div>
        """,
        unsafe_allow_html=True,
    )