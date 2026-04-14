import streamlit as st
import pandas as pd
import plotly.express as px
import json
from db import get_user_predictions

def show():
    st.markdown("# 📈 Advanced Analytics")
    st.write("Deep insights into NOx trends and environmental impact.")

    # ================= FETCH DATA =================
    user = st.session_state.get("user", {})
    email = user.get("email", "unknown")

    data = get_user_predictions(email)

    if not data:
        st.warning("⚠️ No data available. Run predictions first.")
        st.stop()

    # ================= PROCESS DATA =================
    records = []

    for row in data:
        try:
            input_data = json.loads(row[0])

            record = dict(input_data)
            record["Predicted_NOx"] = float(row[1])
            record["Time"] = pd.to_datetime(row[3])

            records.append(record)

        except Exception:
            continue

    if not records:
        st.error("❌ Failed to process data.")
        st.stop()

    df = pd.DataFrame(records).sort_values("Time")

    # ================= KPI SECTION =================
    st.divider()

    avg_nox = df["Predicted_NOx"].mean()
    max_nox = df["Predicted_NOx"].max()
    min_nox = df["Predicted_NOx"].min()

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Average NOx", f"{avg_nox:.2f}")
    m2.metric("Peak NOx", f"{max_nox:.2f}", delta=f"+{max_nox - avg_nox:.1f}")
    m3.metric("Min NOx", f"{min_nox:.2f}")
    m4.metric("Samples", len(df))

    # ================= TREND =================
    st.markdown("### 🕒 NOx Trend Over Time")

    fig_trend = px.line(
        df,
        x="Time",
        y="Predicted_NOx",
        markers=True,
        line_shape="spline"
    )

    fig_trend.update_layout(hovermode="x unified")

    st.plotly_chart(fig_trend, use_container_width=True)

    # ================= DISTRIBUTION =================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 NOx Distribution")

        fig_hist = px.histogram(
            df,
            x="Predicted_NOx",
            nbins=20,
            marginal="box"
        )

        st.plotly_chart(fig_hist, use_container_width=True)

    # ================= FEATURE IMPACT =================
    with col2:
        st.markdown("### 🔥 Feature Impact (SHAP Summary)")

        feature_counts = {}

        for row in data:
            if row[2]:
                try:
                    tf = json.loads(row[2])
                    for key in tf.keys():
                        feature_counts[key] = feature_counts.get(key, 0) + 1
                except:
                    continue

        if feature_counts:
            feat_df = pd.DataFrame({
                "Feature": list(feature_counts.keys()),
                "Impact": list(feature_counts.values())
            }).sort_values("Impact")

            fig_bar = px.bar(
                feat_df,
                y="Feature",
                x="Impact",
                orientation="h"
            )

            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("No SHAP feature data available.")

    # ================= CORRELATION =================
    with st.expander("🧪 Correlation Matrix"):
        numeric_df = df.select_dtypes(include=["float64", "int64"])

        if numeric_df.shape[1] > 1:
            corr = numeric_df.corr()

            fig_corr = px.imshow(
                corr,
                text_auto=True,
                aspect="auto"
            )

            st.plotly_chart(fig_corr, use_container_width=True)
        else:
            st.warning("Not enough numeric data for correlation.")

    # ================= DATA TABLE =================
    st.markdown("### 📋 Prediction Logs")

    st.dataframe(
        df.sort_values("Time", ascending=False),
        use_container_width=True,
        column_config={
            "Time": st.column_config.DatetimeColumn(
                "Timestamp",
                format="D MMM, HH:mm"
            ),
            "Predicted_NOx": st.column_config.ProgressColumn(
                "NOx Level",
                min_value=0,
                max_value=max_nox,
                format="%.2f"
            )
        }
    )