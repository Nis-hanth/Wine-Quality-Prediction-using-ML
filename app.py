
# ============================================================
# 🍷 WINE QUALITY PREDICTION
# DECISION TREE + STREAMLIT
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle


# ============================================================
# 1. LOAD TRAINED MODEL
# ============================================================

with open("wine_quality_dt_model.pkl", "rb") as file:
    model = pickle.load(file)


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="wide"
)


# ============================================================
# 3. TITLE
# ============================================================

st.title("🍷 Wine Quality Prediction")

st.write(
    "Decision Tree Classifier"
)

st.info(
    "Enter the wine chemical properties and predict the wine quality."
)


# ============================================================
# 4. SIDEBAR
# ============================================================

st.sidebar.header("⚙️ Settings")

show_details = st.sidebar.checkbox(
    "Show entered values",
    value=True
)

show_probability = st.sidebar.checkbox(
    "Show prediction probability",
    value=True
)


# ============================================================
# 5. INPUT FEATURES
# ============================================================

st.header("🧪 Wine Chemical Properties")

st.write(
    "The slider ranges below are taken from the dataset statistics."
)


# ============================================================
# CREATE THREE COLUMNS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMN 1
# ============================================================

with col1:

    fixed_acidity = st.slider(
        "Fixed Acidity",
        min_value=4.6,
        max_value=15.9,
        value=8.3,
        step=0.1
    )

    volatile_acidity = st.slider(
        "Volatile Acidity",
        min_value=0.12,
        max_value=1.58,
        value=0.53,
        step=0.01
    )

    citric_acid = st.slider(
        "Citric Acid",
        min_value=0.0,
        max_value=1.0,
        value=0.27,
        step=0.01
    )

    residual_sugar = st.slider(
        "Residual Sugar",
        min_value=0.9,
        max_value=15.5,
        value=2.5,
        step=0.1
    )


# ============================================================
# COLUMN 2
# ============================================================

with col2:

    chlorides = st.slider(
        "Chlorides",
        min_value=0.012,
        max_value=0.611,
        value=0.087,
        step=0.001
    )

    free_sulfur_dioxide = st.slider(
        "Free Sulfur Dioxide",
        min_value=1.0,
        max_value=72.0,
        value=15.0,
        step=1.0
    )

    total_sulfur_dioxide = st.slider(
        "Total Sulfur Dioxide",
        min_value=6.0,
        max_value=289.0,
        value=46.0,
        step=1.0
    )

    density = st.slider(
        "Density",
        min_value=0.99007,
        max_value=1.00369,
        value=0.99675,
        step=0.00001
    )


# ============================================================
# COLUMN 3
# ============================================================

with col3:

    ph = st.slider(
        "pH",
        min_value=2.74,
        max_value=4.01,
        value=3.31,
        step=0.01
    )

    sulphates = st.slider(
        "Sulphates",
        min_value=0.33,
        max_value=2.00,
        value=0.66,
        step=0.01
    )

    alcohol = st.slider(
        "Alcohol",
        min_value=8.4,
        max_value=14.9,
        value=10.4,
        step=0.1
    )


# ============================================================
# 6. ADVANCED INFORMATION
# ============================================================

with st.expander("📊 Dataset ranges"):

    range_data = pd.DataFrame({
        "Feature": [
            "Fixed Acidity",
            "Volatile Acidity",
            "Citric Acid",
            "Residual Sugar",
            "Chlorides",
            "Free Sulfur Dioxide",
            "Total Sulfur Dioxide",
            "Density",
            "pH",
            "Sulphates",
            "Alcohol"
        ],

        "Minimum": [
            4.6,
            0.12,
            0.0,
            0.9,
            0.012,
            1.0,
            6.0,
            0.99007,
            2.74,
            0.33,
            8.4
        ],

        "Maximum": [
            15.9,
            1.58,
            1.0,
            15.5,
            0.611,
            72.0,
            289.0,
            1.00369,
            4.01,
            2.00,
            14.9
        ]
    })

    st.dataframe(
        range_data,
        use_container_width=True
    )


# ============================================================
# 7. CREATE INPUT DATA
# ============================================================

input_data = pd.DataFrame({

    "fixed acidity": [fixed_acidity],

    "volatile acidity": [volatile_acidity],

    "citric acid": [citric_acid],

    "residual sugar": [residual_sugar],

    "chlorides": [chlorides],

    "free sulfur dioxide": [free_sulfur_dioxide],

    "total sulfur dioxide": [total_sulfur_dioxide],

    "density": [density],

    "pH": [ph],

    "sulphates": [sulphates],

    "alcohol": [alcohol]
})


# ============================================================
# 8. SHOW ENTERED VALUES
# ============================================================

if show_details:

    st.subheader("📋 Entered Wine Values")

    st.dataframe(
        input_data,
        use_container_width=True
    )


# ============================================================
# 9. PREDICT BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🍷 Predict Wine Quality",
    type="primary",
    use_container_width=True
)


# ============================================================
# 10. PREDICTION
# ============================================================

if predict_button:

    # Make prediction
    prediction = model.predict(input_data)[0]


    # ========================================================
    # PREDICTION PROBABILITY
    # ========================================================

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(input_data)[0]

        classes = model.classes_

        max_probability = np.max(probabilities)

    else:

        max_probability = 0


    # ========================================================
    # RESULT
    # ========================================================

    st.subheader("🎯 Prediction Result")


    # Display prediction using metric
    st.metric(
        label="Predicted Wine Quality",
        value=str(prediction)
    )


    # ========================================================
    # QUALITY MESSAGE
    # ========================================================

    if prediction <= 4:

        st.error(
            "🍷 Low Quality Wine"
        )

    elif prediction <= 6:

        st.warning(
            "🍷 Medium Quality Wine"
        )

    else:

        st.success(
            "🍷 High Quality Wine"
        )


    # ========================================================
    # PROBABILITY
    # ========================================================

    if show_probability and hasattr(model, "predict_proba"):

        st.subheader("📈 Prediction Confidence")

        st.progress(
            float(max_probability)
        )

        st.write(
            f"Highest class probability: "
            f"{max_probability * 100:.2f}%"
        )


    # ========================================================
    # ALL CLASS PROBABILITIES
    # ========================================================

    if show_probability and hasattr(model, "predict_proba"):

        st.subheader("📊 Class Probabilities")

        probability_data = pd.DataFrame({
            "Wine Quality": classes,
            "Probability": probabilities
        })

        probability_data["Probability (%)"] = (
            probability_data["Probability"] * 100
        ).round(2)

        st.dataframe(
            probability_data[
                ["Wine Quality", "Probability (%)"]
            ],
            use_container_width=True
        )


# ============================================================
# 11. FOOTER
# ============================================================

st.divider()

st.caption(
    "🍷 Wine Quality Prediction | Decision Tree Machine Learning"
)

