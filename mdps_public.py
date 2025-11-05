# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
heart_model = pickle.load(open("heart_model.sav", "rb"))

with st.sidebar:
    selected = option_menu(
        "Multi-Disease Web App",
        ["Diabetes Prediction", "Heart Disease Prediction"],
        default_index=0
    )

# ---------------------- Diabetes Prediction ----------------------
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
        SkinThickness = st.text_input("Skin Thickness")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

    with col2:
        Glucose = st.text_input("Glucose Value")
        Insulin = st.text_input("Insulin")
        Age = st.text_input("Age")

    with col3:
        BloodPressure = st.text_input("Blood Pressure")
        BMI = st.text_input("BMI Value")

    diagnosis = ""

    if st.button("Diabetes Test Result"):
        try:
            # Convert all inputs to float
            user_input = [
                float(pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]

            prediction = diabetes_model.predict([user_input])
            if prediction[0] == 0:
                diagnosis = "Patient is non-diabetic"
            else:
                diagnosis = "Patient is diabetic"

        except ValueError:
            diagnosis = "⚠️ Please enter valid numeric values."

    st.success(diagnosis)

# ---------------------- Heart Disease Prediction ----------------------
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
        trestbps = st.text_input("Resting Blood Pressure")
        restecg = st.text_input("Resting Electrocardiographic Results")
        oldpeak = st.text_input("ST Depression Induced by Exercise")
        thal = st.text_input("Thal (0=Normal; 1=Fixed Defect; 2=Reversible Defect)")

    with col2:
        sex = st.text_input("Sex (1=Male, 0=Female)")
        chol = st.text_input("Serum Cholestrol in mg/dl")
        thalach = st.text_input("Maximum Heart Rate Achieved")
        slope = st.text_input("Slope of Peak Exercise ST Segment")

    with col3:
        cp = st.text_input("Chest Pain Type")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)")
        exang = st.text_input("Exercise Induced Angina (1=True, 0=False)")
        ca = st.text_input("Major Vessels Colored by Fluoroscopy")

    diagnosis = ""

    if st.button("Heart Disease Test Result"):
        try:
            # Convert all inputs to float
            user_input = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]

            prediction = heart_model.predict([user_input])
            if prediction[0] == 0:
                diagnosis = "No Heart Disease Detected"
            else:
                diagnosis = "Heart Disease Detected"

        except ValueError:
            diagnosis = "⚠️ Please enter valid numeric values."

    st.success(diagnosis)
