import streamlit as st
import requests
from db import insert_prediction
from explainer import explain_lime_plot, explain_shap_plot

def show():
    st.markdown("# 🔮 Manual NOx Prediction")
    st.write("Enter sensor values below to generate an AI-powered NOx prediction.")

    # ================= INPUT SECTION =================
    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🌐 Environmental Factors")
            no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, value=0.0)
            no = st.number_input("NO (µg/m³)", min_value=0.0, value=0.0)
            co = st.number_input("CO (mg/m³)", min_value=0.0, value=0.0)
            pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, value=0.0)
            o3 = st.number_input("O3 (µg/m³)", min_value=0.0, value=0.0)

        with col2:
            st.markdown("### 🏗️ Tunnel & Traffic")
            traffic = st.number_input("Traffic Density", min_value=0.0, value=0.0)
            wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, value=0.0)
            airflow = st.number_input("Airflow (m³/s)", min_value=0.0, value=0.0)
            temperature = st.number_input("Temperature (°C)", value=25.0)
            relativehumidity = st.number_input("Relative Humidity (%)", min_value=0.0, value=50.0)
            depth = st.number_input("Tunnel Depth (m)", min_value=0.0, value=10.0)

    # ================= BUTTON =================
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        predict_btn = st.button("🚀 Run AI Analysis", use_container_width=True)

    # ================= PREDICTION =================
    if predict_btn:

        # Validate input (basic check)
        if all(v == 0.0 for v in [no2, no, co, pm10, o3, traffic, wind_speed, airflow]):
            st.warning("⚠️ Please enter meaningful sensor values before predicting.")
            return

        data = {
            "no2": no2, "traffic": traffic, "no": no,
            "wind_speed": wind_speed, "airflow": airflow, "co": co,
            "temperature": temperature, "o3": o3, "pm10": pm10,
            "relativehumidity": relativehumidity, "depth": depth
        }

        data_list = list(data.values())

        with st.spinner("🧠 Model is analyzing data..."):
            try:
                response = requests.post(
                     "https://nox-prediction-1.onrender.com/predict",
                     json=data,
                     timeout=10
                    )

                if response.status_code != 200:
                    st.error("❌ Backend error. Check API.")
                    return

                result = response.json()

                if "predicted_NOx" in result:
                    prediction = result["predicted_NOx"]

                    # 🎉 Result Display
                    st.balloons()

                    st.markdown("## 🎯 Prediction Result")
                    st.success(f"### {prediction:.2f} µg/m³")

                    # 🔥 Range display (as you wanted)
                    st.info("Expected Range: **33.95 → 544.61 µg/m³**")

                    st.divider()

                    # ================= EXPLAINABILITY =================
                    st.markdown("## 🔍 Explainability")

                    tab1, tab2 = st.tabs(["📊 LIME", "📈 SHAP"])

                    with tab1:
                        st.caption("Local explanation (this prediction)")
                        lime_fig = explain_lime_plot(data_list)
                        st.pyplot(lime_fig)

                    with tab2:
                        st.caption("Global feature importance")
                        shap_fig = explain_shap_plot(data_list)
                        st.pyplot(shap_fig)

                    # ================= SAVE =================
                    user = st.session_state.get("user", {})
                    email = user.get("email", "unknown")

                    insert_prediction(email, data, prediction)

                    st.toast("✅ Saved to history", icon="💾")

                else:
                    st.error("❌ Invalid response from model.")

            except requests.exceptions.ConnectionError:
                st.error("🚫 Cannot connect to backend. Is FastAPI running on port 8000?")

            except Exception as e:
                st.error(f"Unexpected error: {e}")