import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from lime.lime_tabular import LimeTabularExplainer

# ===== LOAD MODEL =====
model = joblib.load("../backend/model/RESEARCH_model.pkl")

# ===== FEATURES =====
feature_names = [
    "no2", "traffic", "no", "wind_speed", "airflow",
    "co", "temperature", "o3", "pm10", "relativehumidity", "depth"
]

# ===== DUMMY DATA FOR LIME =====
training_data = np.random.rand(100, 11)

lime_explainer = LimeTabularExplainer(
    training_data,
    feature_names=feature_names,
    mode="regression"
)

# ===== SHAP EXPLAINER =====
shap_explainer = shap.Explainer(model, training_data)


# ================= LIME GRAPH =================
def explain_lime_plot(input_data):
    input_array = np.array(input_data).reshape(1, -1)

    exp = lime_explainer.explain_instance(
        input_array[0],
        model.predict,
        num_features=10
    )

    fig = exp.as_pyplot_figure()
    return fig


# ================= SHAP GRAPH =================
def explain_shap_plot(input_data):
    input_array = np.array(input_data).reshape(1, -1)

    shap_values = shap_explainer(input_array)

    fig, ax = plt.subplots()
    shap.plots.bar(shap_values[0], show=False)

    return fig