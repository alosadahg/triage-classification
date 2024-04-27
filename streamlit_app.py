import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the trained model
model = pickle.load(open('triage_classification (5).pkl', 'rb'))

st.title("Triage Classifier")

st.write("""
A triage classifier that uses machine learning to distinguish the triage color from the given symptoms. 
""")

input_data = None

bp_range = (60, 200)
chol_range = (100, 300)
plasma_glucose_range = (50, 300)

age = st.number_input("Enter age: ", value=None, placeholder=15, key='age', min_value=0, max_value=150)
bmi = st.number_input("Enter BMI: ", key='bmi', value=None)
bp = st.number_input("Enter blood pressure: ", value=None,placeholder=80, key='bp', min_value=bp_range[0], max_value=bp_range[1])
chol = st.number_input("Enter cholesterol: ",value=None,placeholder=100,  key='chol', min_value=chol_range[0], max_value=chol_range[1])
plasma_glucose = st.number_input("Enter plasma glucose: ", value=None,placeholder=50, key='plasma_glucose', min_value=plasma_glucose_range[0], max_value=plasma_glucose_range[1])
exercise_angina_str = st.radio("Do you experience exercise angina (chest pain during physical exercise)?", ("No", "Yes"), index=0)
exercise_angina = 1 if exercise_angina_str == "Yes" else 0
cp_type_options = ["No Pain (0)", "Mild (1)", "Moderate (2)", "Severe (3)", "Very Severe (4)"]
cp_type_str = st.selectbox("Select chest pain type:", cp_type_options, index=0)
cp_type_mapping = {"No Pain (0)": 0, "Mild (1)": 1, "Moderate (2)": 2, "Severe (3)": 3, "Very Severe (4)": 4}
cp_type = cp_type_mapping.get(cp_type_str)

# Validate input
if age and bmi and bp and chol and plasma_glucose:
    # 'chest_pain_type', 'cholesterol', 'exercise_angina', 'blood pressure', 'age', 'plasma glucose', 'bmi'
    input_data = np.array([[cp_type, float(chol),  exercise_angina, float(bp), float(age), float(plasma_glucose), float(bmi)]])
else:
    st.warning("Please fill in all the input fields.")

# Make prediction if input is valid
if st.button('Predict'):
    prediction = model.predict(input_data)
    triage_order = {0: 'Green', 1: 'Yellow', 2: 'Orange', 3: 'Red'}
    st.write(f"Predicted triage color: {triage_order[prediction[0]]}")
