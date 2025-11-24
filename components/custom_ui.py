import streamlit as st

def apply_custom_theme():
    st.markdown(
        """
        <style>
        /* ---------- GLOBAL LAYOUT ---------- */
        .stApp {
            background: radial-gradient(circle at top left, #1b2335 0, #020617 55%, #000000 100%);
            color: #e5e7eb;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", sans-serif;
        }

        /* Center main content on wide screens */
        @media (min-width: 1024px) {
            .main-block {
                max-width: 1200px;
                margin: 0 auto;
                padding: 1.5rem 0 3rem 0;
            }
        }

        @media (max-width: 1023px) {
            .main-block {
                padding: 0.5rem 0 2rem 0;
            }
        }

        /* ---------- SIDEBAR ---------- */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #020617 0%, #020617 40%, #020617 100%);
            border-right: 1px solid rgba(148, 163, 184, 0.4);
        }

        [data-testid="stSidebar"] * {
            color: #e5e7eb !important;
        }

        /* ---------- TITLES & TEXT ---------- */
        .app-title {
            font-weight: 800;
            font-size: clamp(1.8rem, 2.6vw, 2.4rem);
            background: linear-gradient(90deg, #38bdf8, #4ade80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }

        .app-subtitle {
            color: #9ca3af;
            font-size: 0.95rem;
            margin-bottom: 1.2rem;
        }

        /* ---------- CARD CONTAINERS ---------- */
        .card {
            background: rgba(15, 23, 42, 0.9);
            border-radius: 18px;
            padding: 1.2rem 1.4rem;
            box-shadow:
                0 18px 45px rgba(15, 23, 42, 0.85),
                0 0 0 1px rgba(148, 163, 184, 0.12);
            border: 1px solid rgba(148, 163, 184, 0.18);
            margin-bottom: 1rem;
        }

        .card-header {
            font-weight: 600;
            font-size: 0.95rem;
            color: #e5e7eb;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .card-header-pill {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.70rem;
            padding: 0.07rem 0.35rem;
            border-radius: 999px;
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #7dd3fc;
        }

        /* ---------- BUTTONS ---------- */
        .stButton > button {
            background: linear-gradient(135deg, #2563eb 0%, #22c55e 100%) !important;
            color: #ecfeff !important;
            border-radius: 999px !important;
            padding: 0.5rem 1rem !important;
            border: none !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.45);
            transition: transform 0.08s ease-out, box-shadow 0.08s ease-out, filter 0.1s ease-out;
        }

        .stButton > button:hover {
            transform: translateY(-1px) scale(1.02);
            box-shadow: 0 18px 40px rgba(37, 99, 235, 0.65);
            filter: brightness(1.05);
        }

        .stButton > button:active {
            transform: translateY(0px) scale(0.99);
            box-shadow: 0 5px 18px rgba(15, 23, 42, 0.8);
        }

        /* Stop button variant using aria-label trick if needed later */

        /* ---------- SLIDER ---------- */
        .stSlider > div > div > div {
            color: #e5e7eb !important;
        }

        /* ---------- METRICS ---------- */
        div[data-testid="metric-container"] {
            background: radial-gradient(circle at top left, rgba(37, 99, 235, 0.25), rgba(15, 23, 42, 0.98));
            border-radius: 16px;
            padding: 0.9rem 0.95rem;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(59, 130, 246, 0.4);
        }

        div[data-testid="metric-container"] label {
            color: #9ca3af !important;
            font-size: 0.78rem !important;
        }

        div[data-testid="metric-container"] .metric-value {
            font-size: 1.3rem !important;
        }

        /* ---------- MAP IFRAMES ---------- */
        iframe {
            border-radius: 16px !important;
            border: 1px solid rgba(148, 163, 184, 0.45) !important;
        }

        @media (min-width: 1024px) {
            .map-wrapper {
                margin-top: 0.3rem;
            }
        }

        @media (max-width: 768px) {
            .map-wrapper {
                margin-top: 0.2rem;
            }
        }

        /* ---------- ALERTS ---------- */
        .stAlert {
            border-radius: 12px !important;
            border-width: 1px !important;
        }

        /* ---------- SMALL BADGE TEXT ---------- */
        .pill-muted {
            display: inline-flex;
            padding: 0.12rem 0.55rem;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.5);
            font-size: 0.65rem;
            color: #9ca3af;
            gap: 0.3rem;
            align-items: center;
        }
        </style>

        <script src="static/pwa.js"></script>
        """,
        unsafe_allow_html=True,
    )
