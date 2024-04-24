import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('triage_classification.pkl','rb'))

st.title("Triage Classifier")

st.write("""
A triage classifier that uses machine learning to distinguish the triage color from the given symptoms. 
"""
)

age = st.text_input("Enter age: ")
bmi = st.text_input("Enter BMI (Range: 15-50): ", value="25")
bp = st.text_input("Enter blood pressure (Range: 80-200): ", value="120")
chol = st.text_input("Enter cholesterol (Range: 100-500): ", value="200")
plasma_glucose = st.text_input("Enter plasma glucose (Range: 50-400): ", value="100")
exercise_angina = st.text_input("Do you experience exercise angina (chest pain during physical exercise) (0: No, 1: Yes): ", value="0")
cp_type = st.selectbox("Select chest pain type:", ["No Pain (0)", "Mild (1)", "Moderate (2)", "Severe (3)", "Very Severe (4)"], index=0)
cp_type_mapping = {"No Pain (0)": "0", "Mild (1)": "1", "Moderate (2)": "2", "Severe (3)": "3", "Very Severe (4)": "4"}
cp_type = cp_type_mapping.get(cp_type)

# Prepare input data for prediction
input_data = np.array([[age, bmi, bp, chol, plasma_glucose, exercise_angina, cp_type]], dtype=np.float32)

if st.button('Predict'):
    # Make prediction
    prediction = model.predict(input_data)
    # Display prediction
    st.write(f"Predicted triage color: {prediction[0]}")