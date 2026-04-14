import streamlit as st
from streamlit_oauth import OAuth2Component
import jwt
import os
from dotenv import load_dotenv
import importlib
from PIL import Image
from datetime import datetime
from db import init_db
init_db()

# ================= 1. PAGE CONFIG =================
load_dotenv()
st.set_page_config(
    page_title="NOx Intelligence | Terminal",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= 2. SESSION INITIALIZATION =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ================= 3. DYNAMIC THEME ENGINE =================
def apply_theme():
    if not st.session_state.logged_in:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #020617 !important;
            background-image: 
                radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.12) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%) !important;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #f1f5f9 !important;
        }
        
        [data-testid="stHeader"], footer {visibility: hidden;}
        
        .research-header {
            text-align: center;
            margin: 20px 5%;
            padding: 20px 30px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            backdrop-filter: blur(12px);
        }
        .research-title-text {
            font-size: 1rem;
            color: #ffffff;
            letter-spacing: 1.2px;
            font-weight: 500;
            text-transform: uppercase;
        }
        .main-container { padding: 40px 10% 0 10%; }
        .main-heading { 
            font-size: 4rem; 
            font-weight: 800; 
            background: linear-gradient(135deg, #ffffff 30%, #34d399 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
        }
        .accuracy-badge {
            display: inline-flex; align-items: center;
            padding: 6px 16px; 
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #10b981; border-radius: 100px; 
            font-weight: 600; font-size: 0.75rem; 
        }
        .stButton > button {
            background: #ffffff !important;
            color: #020617 !important;
            border-radius: 14px !important;
            height: 50px !important;
            font-weight: 700 !important;
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        # LOGGED IN THEME
        st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f8fafc !important;
        }
        
        /* Navbar Pill Container */
        .nav-pill-container {
            display: flex;
            justify-content: center;
            gap: 8px;
            background: white;
            padding: 12px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
            margin-bottom: 25px;
        }

        /* Target navigation buttons specifically */
        div[data-testid="stHorizontalBlock"] button {
            background-color: #f1f5f9 !important;
            color: #64748b !important;
            border: 1px solid transparent !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            transition: all 0.2s ease-in-out !important;
        }

        div[data-testid="stHorizontalBlock"] button:hover {
            color: #10b981 !important;
            background-color: rgba(16, 185, 129, 0.1) !important;
            border-color: #10b981 !important;
        }
        </style>
        """, unsafe_allow_html=True)

apply_theme()

# ================= 4. AUTH HANDLER =================
def show_auth_card():
    CLIENT_ID = os.getenv("CLIENT_ID", "")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
    REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:8501")
    
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, "https://accounts.google.com/o/oauth2/v2/auth", "https://oauth2.googleapis.com/token", "https://oauth2.googleapis.com/token")
    
    img_path = "images/assets/4.png"
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)

    st.markdown("### Terminal Access")
    result = oauth2.authorize_button("Sign in with Google", icon="https://www.google.com/favicon.ico", redirect_uri=REDIRECT_URI, scope="openid email profile", key="google_auth")

    if result and "token" in result:
        decoded = jwt.decode(result["token"]["id_token"], options={"verify_signature": False})
        st.session_state.user = {"name": decoded.get("name"), "email": decoded.get("email")}
        st.session_state.logged_in = True
        st.rerun()

    st.markdown("<div style='text-align:center; margin: 10px 0; color:#94a3b8;'>OR</div>", unsafe_allow_html=True)

    if st.button("🍃 Enter as Guest Operator"):
        st.session_state.user = {"name": "Guest Operator", "email": "guest@shadipur.metro"}
        st.session_state.logged_in = True
        st.rerun()

# ================= 5. MAIN RENDER =================
if not st.session_state.logged_in:
    # --- Landing Page ---
    st.markdown('<div class="research-header"><div class="research-title-text">Physics-Informed Machine Learning Approach for NOx Prediction in Indian Subway Tunnel Environments Using Real-Time Air Quality Data </div></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
   
    c1, c2 = st.columns([1.3, 0.7], gap="large")
    with c1:
        st.markdown('<div class="accuracy-badge">🌿 98.8% Accuracy</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="main-heading">Delhi Metro<br>Air Intelligence</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color:#cbd5e1; font-size:1.1rem;">Bridging physical laws with state-of-the-art AI for subway air quality diagnostics.</p>', unsafe_allow_html=True)
        # ✅ NEW CONTENT (fills empty space beautifully)
        st.markdown("""
    <div style="
        margin-top: 25px;
        padding: 20px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        color:#cbd5e1;
        line-height:1.6;
        font-size:0.95rem;
    ">
    Air pollution in subway tunnel environments is a growing concern in densely populated cities like Delhi due to pollutant accumulation under limited ventilation. 
    This system presents a <b>physics-informed machine learning framework</b> to predict NOx concentrations using real-world air quality data (OpenAQ) combined with 
    simulated tunnel parameters such as airflow, traffic intensity, and depth.
    <br><br>
    Multiple models including Linear Regression, Polynomial Regression, Random Forest, and XGBoost were evaluated. 
    The <b>Random Forest model achieved the best performance</b> with an R² score of 0.988 and RMSE of 7.80.
    <br><br>
    Explainable AI techniques (SHAP & LIME) are integrated to ensure transparency, enabling reliable and interpretable predictions for real-time subway air monitoring systems.
    </div>
    """, unsafe_allow_html=True)
    with c2:
        show_auth_card()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- Sidebar ---
    st.sidebar.markdown(f"### 👤 {st.session_state.user['name']}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # --- ENHANCED NAVBAR ---
    st.markdown(f"## 🛠️ System Terminal / {st.session_state.page}")
    
    pages = ["Home", "Dashboard", "Manual", "Batch", "Analytics", "History", "Research", "Team"]
    
    # Render navigation as columns
    nav_cols = st.columns(len(pages))
    for i, p in enumerate(pages):
        # Highlighting the active button
        is_active = st.session_state.page == p
        style = "primary" if is_active else "secondary"
        
        if nav_cols[i].button(p, key=f"nav_btn_{p}", use_container_width=True, type=style):
            st.session_state.page = p
            st.rerun()
    
    st.markdown("<hr style='margin-top:0; opacity:0.1;'>", unsafe_allow_html=True)

    # --- MODULE LOADING ---
    modules_map = {
        "Home": "0_homepage", "Dashboard": "1_Dashboard", "Manual": "2_Manual_Prediction",
        "Batch": "3_Batch_Prediction", "Analytics": "4_Analytics", "History": "5_History",
        "Research": "6_Research", "Team": "7_Team"
    }

    try:
        mod_name = f"my_pages.{modules_map[st.session_state.page]}"
        mod = importlib.import_module(mod_name)
        mod.show()
    except Exception as e:
        st.error(f"Error loading {st.session_state.page}: {e}")