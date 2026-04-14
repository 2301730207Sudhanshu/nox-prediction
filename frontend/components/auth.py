import streamlit as st
from streamlit_oauth import OAuth2Component
import jwt

import os

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REFRESH_TOKEN_URL = "https://oauth2.googleapis.com/token"

REDIRECT_URI = "http://localhost:8501"
SCOPE = "openid email profile"


def google_login():
    oauth2 = OAuth2Component(
        CLIENT_ID,
        CLIENT_SECRET,
        AUTHORIZE_URL,
        TOKEN_URL,
        REFRESH_TOKEN_URL
    )

    result = oauth2.authorize_button(
        name="🔐 Login with Google",
        icon="https://www.google.com/favicon.ico",
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        key="google",
    )

    if result:
        token = result.get("token")

        if token:
            id_token = token.get("id_token")

            if id_token:
                decoded = jwt.decode(id_token, options={"verify_signature": False})

                st.session_state["user"] = {
                    "name": decoded.get("name"),
                    "email": decoded.get("email")
                }

                st.session_state["logged_in"] = True
                st.rerun()


def logout():
    st.session_state.clear()
    st.rerun()