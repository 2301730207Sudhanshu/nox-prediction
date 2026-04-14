import streamlit as st
import pandas as pd
import json
from db import get_user_predictions

def show():
    # --- UI STYLING FOR LIGHT THEME ---
    st.markdown("""
        <style>
            .main { background-color: #f8fafc; }
            .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("# 📜 Prediction History")
    st.write("Analyze past NOx readings to identify traffic patterns and air quality trends.")

    # 1. GET USER DATA
    user = st.session_state.get("user", {})
    email = user.get("email", "unknown")
    data = get_user_predictions(email)

    if not data:
        st.info("No prediction history found yet. Start the Dashboard or Manual Prediction to generate data.")
        return

    # 2. DATA PROCESSING
    records = []
    for row in data:
        try:
            # row[0] is inputs, row[1] is predicted NOx, row[3] is timestamp
            input_data = json.loads(row[0])
            record = dict(input_data)
            record["Predicted_NOx"] = float(row[1])
            record["Time"] = pd.to_datetime(row[3])
            records.append(record)
        except Exception:
            continue

    if not records:
        st.warning("⚠️ Data format mismatch. Could not process history.")
        return

    df = pd.DataFrame(records).sort_values("Time", ascending=False)

    # 3. FILTERS
    st.subheader("🔍 Filter Records")
    col1, col2 = st.columns(2)

    with col1:
        min_v = float(df["Predicted_NOx"].min())
        max_v = float(df["Predicted_NOx"].max())
        if min_v == max_v: max_v = min_v + 1.0
        selected_range = st.slider("Filter by NOx Concentration", min_v, max_v, (min_v, max_v))

    with col2:
        date_range = st.date_input("Filter by Date Range", value=[])

    # Apply Filters
    filtered_df = df[
        (df["Predicted_NOx"] >= selected_range[0]) & 
        (df["Predicted_NOx"] <= selected_range[1])
    ]

    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date = pd.to_datetime(date_range[0]).date()
        end_date = pd.to_datetime(date_range[1]).date()
        filtered_df = filtered_df[
            (filtered_df["Time"].dt.date >= start_date) & 
            (filtered_df["Time"].dt.date <= end_date)
        ]

    # 4. SUMMARY STATS (Cleaned of Status Logic)
    st.subheader("📊 Research Summary")
    c1, c2, c3 = st.columns(3)
    
    avg_nox = filtered_df['Predicted_NOx'].mean()
    max_nox = filtered_df['Predicted_NOx'].max()

    c1.metric("Total Records", len(filtered_df))
    c2.metric("Avg NOx", f"{avg_nox:.2f} µg/m³")
    c3.metric("Peak Recorded", f"{max_nox:.2f} µg/m³")

    # 5. DATA TABLE
    st.subheader("📋 Detailed Logs")
    
    # Copy for display without modifying the original filtered_df
    display_df = filtered_df.copy()
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Time": st.column_config.DatetimeColumn("Timestamp", format="D MMM, HH:mm:ss"),
            "Predicted_NOx": st.column_config.NumberColumn(
                "NOx Level (µg/m³)",
                format="%.2f",
                help="Predicted concentration value"
            ),
            "no": "NO (Nitric Oxide)",
            "traffic": "Trains/Hr",
            "depth": "Depth (m)"
        }
    )

    if st.button("🗑️ Clear Filtered History View"):
        st.write("Note: To delete actual data, please contact the DB administrator.")