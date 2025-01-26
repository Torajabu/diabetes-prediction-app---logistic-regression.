import streamlit as st
import requests
import json

# Define the FastAPI endpoint URL
API_URL = "http://localhost:8000/predict"

# Streamlit app layout
st.title("Diabetes Prediction App")
st.write("Enter the details below to make a prediction.")

# Input fields
st.header("Patient Details")
with st.form("diabetes_form"):
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose", min_value=0, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, step=1)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, step=1)
    insulin = st.number_input("Insulin", min_value=0, step=1)
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.1)
    age = st.number_input("Age", min_value=0, step=1)

    # Submit button
    submitted = st.form_submit_button("Predict")

# Prediction request
if submitted:
    input_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree_function,
        "Age": age
    }

    try:
        # Send the POST request to FastAPI
        response = requests.post(API_URL, data=json.dumps(input_data), headers={"Content-Type": "application/json"})
        
        if response.status_code == 200:
            prediction = response.json().get("prediction", "No prediction available")
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Error: {response.status_code}. Could not get prediction. Check server or input data.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
