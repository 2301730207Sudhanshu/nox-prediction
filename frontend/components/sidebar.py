import streamlit as st

def show_sidebar():

    st.markdown("""
    <style>

    /* ===== SIDEBAR BACKGROUND ===== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f, #1c1c1c);
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    /* ===== REMOVE DEFAULT NAV ===== */
    [data-testid="stSidebarNav"] {display: none;}

    /* ===== PROFILE SECTION ===== */
    .profile {
        text-align: center;
        padding: 20px 10px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .profile img {
        border-radius: 50%;
        width: 70px;
        margin-bottom: 10px;
    }

    .profile-name {
        color: white;
        font-weight: 600;
        font-size: 16px;
    }

    .profile-email {
        color: gray;
        font-size: 12px;
    }

    /* ===== MENU BUTTONS ===== */
    .menu-btn {
        display: block;
        padding: 12px 15px;
        margin: 6px 10px;
        border-radius: 10px;
        color: #bbb;
        text-decoration: none;
        font-size: 14px;
        transition: all 0.3s ease;
    }

    .menu-btn:hover {
        background: rgba(255,255,255,0.08);
        color: white;
        transform: translateX(5px);
    }

    .active {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white !important;
        font-weight: 600;
        box-shadow: 0 0 10px rgba(0,198,255,0.5);
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= USER INFO =================
    user = st.session_state.get("user", {})

    name = user.get("name", "User")
    email = user.get("email", "")
    pic = user.get("picture", "https://cdn-icons-png.flaticon.com/512/149/149071.png")

    st.sidebar.markdown(f"""
    <div class="profile">
        <img src="{pic}">
        <div class="profile-name">{name}</div>
        <div class="profile-email">{email}</div>
    </div>
    """, unsafe_allow_html=True)

    # ================= MENU =================
    menu = {
        "🏠 Home": "🏠 Home",
        "📊 Dashboard": "📊 Dashboard",
        "🔮 Manual Prediction": "🔮 Manual Prediction",
        "📂 Batch Prediction": "📂 Batch Prediction",
        "📜 History": "📜 History",
        "📈 Analytics": "📈 Analytics",
        "📚 Research": "📚 Research",
        "👨‍💻 Team": "👨‍💻 Team"
    }

    if "page" not in st.session_state:
        st.session_state.page = "🏠 Home"

    selected = st.session_state.page

    for key in menu:
        active_class = "active" if selected == key else ""
        if st.sidebar.button(key, key=key):
            st.session_state.page = key
            st.rerun()

        st.sidebar.markdown(
            f"<div class='menu-btn {active_class}'>{key}</div>",
            unsafe_allow_html=True
        )

    st.sidebar.markdown("---")

    # ================= LOGOUT =================
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

    return st.session_state.page