import streamlit as st
import pandas as pd
import requests
from db import insert_prediction
from explainer import explain_lime_plot, explain_shap_plot

REQUIRED_COLUMNS = [
    "no2", "traffic", "no", "wind_speed", "airflow",
    "co", "temperature", "o3", "pm10",
    "relativehumidity", "depth"
]

def get_risk_info(nox_value):
    """Categorizes NOx levels and provides health advice."""
    if nox_value is None:
        return "Unknown", "N/A", "N/A"
    
    if nox_value < 50:
        return "Safe ✅", "Low risk; clean air quality.", "Continue normal outdoor activities."
    elif 50 <= nox_value <= 100:
        return "Moderate ⚠️", "Possible respiratory irritation for sensitive groups.", "Reduce long periods of intense outdoor exertion."
    else:
        return "Dangerous 🚨", "High risk of inflammation and reduced lung function.", "Avoid outdoor activities; stay indoors with air filtration."

def show():
    st.markdown("# 📂 Batch NOx Prediction")
    st.write("Upload a CSV file for automated large-scale prediction.")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"],
        help=f"Required columns: {', '.join(REQUIRED_COLUMNS)}"
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # ================= VALIDATION =================
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]

        if missing_cols:
            st.error(f"❌ Missing columns: {missing_cols}")
            st.stop()

        with st.expander("👀 Preview Data", expanded=True):
            st.dataframe(df, use_container_width=True)

        # ================= RUN =================
        if st.button("🚀 Run Batch Prediction", use_container_width=True):
            predictions = []
            errors = 0
            user = st.session_state.get("user", {})
            email = user.get("email", "unknown")

            progress_bar = st.progress(0)
            status = st.empty()
            total = len(df)
            session = requests.Session()

            with st.spinner("🧠 Processing dataset..."):
                for i, row in df.iterrows():
                    progress_bar.progress((i + 1) / total)
                    status.caption(f"Processing {i+1}/{total}")
                    data = {col: float(row[col]) for col in REQUIRED_COLUMNS}

                    try:
                        response = requests.post(
                            "https://nox-prediction-1.onrender.com/predict",
                            json=data,
                            timeout=10
                        )
                        if response.status_code == 200:
                            result = response.json()
                            pred = result.get("predicted_NOx")
                            if pred is not None:
                                predictions.append(pred)
                                insert_prediction(email, data, pred)
                            else:
                                predictions.append(None)
                                errors += 1
                        else:
                            predictions.append(None)
                            errors += 1
                    except Exception:
                        predictions.append(None)
                        errors += 1

            progress_bar.empty()
            status.empty()

            # ================= RESULTS & ANALYSIS =================
            df["Predicted_NOx"] = predictions
            
            # Map Risk, Health Impact, and Action
            analysis = [get_risk_info(p) for p in predictions]
            df["Status"] = [a[0] for a in analysis]
            df["Health Risk"] = [a[1] for a in analysis]
            df["Action Recommended"] = [a[2] for a in analysis]

            st.success(f"✅ Completed {total} rows")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Rows", total)
            col2.metric("Success", total - errors)
            col3.metric("Failed", errors)

            with st.container(border=True):
                st.subheader("📄 Results & Health Guidance")
                st.dataframe(df, use_container_width=True)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "📥 Download Analyzed CSV",
                    data=csv,
                    file_name="nox_full_analysis.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            # ================= EXPLAINABILITY =================
            st.divider()
            st.subheader("🔍 Explainability (Sample Row)")
            try:
                sample = df.dropna(subset=["Predicted_NOx"]).iloc[0]
                sample_data = [sample[col] for col in REQUIRED_COLUMNS]
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### LIME")
                    st.pyplot(explain_lime_plot(sample_data))
                with col2:
                    st.write("#### SHAP")
                    st.pyplot(explain_shap_plot(sample_data))
            except Exception:
                st.warning("Could not generate explanations.")