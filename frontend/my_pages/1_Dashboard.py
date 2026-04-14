import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go
from datetime import datetime
from db import insert_prediction

def show():
    # --- 1. RESEARCH HEADER ---
    st.markdown("""
        <div style="background: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; border-left: 8px solid #38bdf8; margin-bottom: 20px;">
            <h2 style="color: #0f172a; margin: 0;">📍 Shadipur Metro Subway Monitoring</h2>
            <p style="color: #64748b; margin: 0;"><b>Research Proof:</b> Physics-Informed NOx Prediction (Delhi Metro Blue Line)</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 2. LIVE FEED STATE ---
    if 'nox_history' not in st.session_state:
        # Initialize with dummy data if first load
        st.session_state.nox_history = list(np.random.uniform(40, 60, 20))
        st.session_state.timestamps = [datetime.now().strftime("%H:%M:%S") for _ in range(20)]

    # --- 3. PEAK HOUR LOGIC (Real-world Simulation) ---
    now = datetime.now()
    hour = now.hour
    
    # Define Peak vs Off-Peak (9am-11am & 6pm-8pm)
    is_morning_peak = 9 <= hour <= 11
    is_evening_peak = 18 <= hour <= 20
    
    if is_morning_peak or is_evening_peak:
        level_label, level_color, rgba_fill = "🚨 DANGEROUS", "#ef4444", "rgba(239, 68, 68, 0.2)"
        medical_impact = "High risk of acute respiratory distress and asthma exacerbation."
        mitigation = "CRITICAL: Deploying emergency scrubbers. High-speed fans active."
        base_nox, default_traffic, default_vent = np.random.uniform(280, 380), 38, 0.1
    elif 12 <= hour <= 17:
        level_label, level_color, rgba_fill = "⚠️ MODERATE", "#f59e0b", "rgba(245, 158, 11, 0.2)"
        medical_impact = "Potential throat irritation for sensitive groups."
        mitigation = "CAUTION: Ventilation increased to 70% capacity."
        base_nox, default_traffic, default_vent = np.random.uniform(110, 190), 22, 0.4
    else:
        level_label, level_color, rgba_fill = "✅ SAFE", "#22c55e", "rgba(34, 197, 94, 0.2)"
        medical_impact = "Air quality within safe subway standards."
        mitigation = "OPTIMAL: Energy-saving mode active."
        base_nox, default_traffic, default_vent = np.random.uniform(30, 80), 8, 0.7

    # --- 4. PARAMETERS ---
    st.markdown(f"### 🏗️ Live Parameters ({now.strftime('%I:%M:%S %p')})")
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            trains_per_hr = st.slider("Traffic Density (Trains/Hour)", 0, 45, default_traffic)
        with c2:
            vent_power = st.select_slider("Fan Efficiency", options=[0.1, 0.4, 0.7, 1.0], value=default_vent)
        with c3:
            temp = st.number_input("Tunnel Temp (°C)", value=31.5)
            st.caption("Tunnel Depth: 12.5m (Fixed)")

    # Simulated Physics Model calculation
    current_nox = base_nox + (trains_per_hr * 1.8) - (vent_power * 60) + np.random.normal(0, 3)

    # --- 5. METRICS ---
    m1, m2, m3, m4 = st.columns(4)
    # Calculate delta from last session state reading
    delta_val = current_nox - st.session_state.nox_history[-1]
    m1.metric("Current NOx", f"{current_nox:.1f} µg/m³", delta=f"{delta_val:.1f}")
    m2.metric("Exposure Risk", level_label)
    m3.metric("Traffic Mode", "RUSH HOUR" if (is_morning_peak or is_evening_peak) else "NORMAL")
    m4.metric("Model Status", "Healthy")

    # --- 6. MEDICAL & ACTION INSIGHTS ---
    st.markdown(f"""
        <div style="background:{level_color}15; border-left: 5px solid {level_color}; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h4 style="color:{level_color}; margin:0;">Level Analysis: {level_label}</h4>
            <p style="margin: 8px 0;"><b>Medical Impact:</b> {medical_impact}</p>
            <p style="margin: 0;"><b>Action:</b> {mitigation}</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 7. DATA UPDATES & GRAPHING ---
    st.session_state.nox_history.append(current_nox)
    st.session_state.timestamps.append(now.strftime("%H:%M:%S"))
    
    # Maintain rolling window of 30 points
    if len(st.session_state.nox_history) > 30:
        st.session_state.nox_history.pop(0)
        st.session_state.timestamps.pop(0)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=st.session_state.timestamps, 
        y=st.session_state.nox_history, 
        mode='lines+markers', 
        line=dict(color=level_color, width=3, shape='spline'), 
        fill='tozeroy', 
        fillcolor=rgba_fill
    ))
    
    fig.add_hline(y=200, line_dash="dash", line_color="#ef4444", annotation_text="DANGER")
    fig.add_hline(y=100, line_dash="dot", line_color="#f59e0b", annotation_text="WARNING")

    fig.update_layout(
        height=350, 
        margin=dict(l=10, r=10, t=20, b=10), 
        plot_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(range=[0, 500], title="NOx (µg/m³)")
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- 8. CONTINUOUS HISTORY SYNC ---
    # This block ensures every single 1-second update is pushed to the 'history' table
    user_data = st.session_state.get("user", {})
    email = user_data.get("email", "system_monitor")
    
    data_log = {
        "no": round(current_nox * 0.55, 2),
        "no2": round(current_nox * 0.45, 2),
        "traffic": float(trains_per_hr),
        "airflow": round(20.0 * vent_power, 2),
        "temperature": float(temp),
        "depth": 12.5,
        "status": level_label,
        "co": 0.4, "pm10": 52.0, "o3": 22.0, 
        "relativehumidity": 62.0, "wind_speed": 1.1
    }
    
    try:
        # insert_prediction stores in DB, which the History page reads
        insert_prediction(email, data_log, current_nox)
    except Exception as e:
        # Silently fail or log error to terminal to keep the dashboard running
        print(f"Database Sync Error: {e}")

    # --- 9. AUTO-REFRESH ---
    time.sleep(1) # Frequency: 1Hz
    st.rerun()