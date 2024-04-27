import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the trained model
model = pickle.load(open('triage_classification (4).pkl', 'rb'))

st.title("Triage Classifier")

st.write("""
A triage classifier that uses machine learning to distinguish the triage color from the given symptoms. 
""")

# Input fields
age = st.text_input("Enter age: ")
bmi = st.text_input("Enter BMI (Range: 15-50): ")
bp = st.text_input("Enter blood pressure (Range: 80-200): ")
chol = st.text_input("Enter cholesterol (Range: 100-500): ")
plasma_glucose = st.text_input("Enter plasma glucose (Range: 50-400): ")
exercise_angina_str = st.radio("Do you experience exercise angina (chest pain during physical exercise)?", ("No", "Yes"))
exercise_angina = 1 if exercise_angina_str == "Yes" else 0
cp_type_options = ["No Pain", "Mild", "Moderate", "Severe", "Very Severe"]
cp_type_str = st.selectbox("Select chest pain type:", cp_type_options, index=0)
cp_type_mapping = {"No Pain (0)": 0, "Mild (1)": 1, "Moderate (2)": 2, "Severe (3)": 3, "Very Severe (4)": 4}
cp_type = cp_type_mapping.get(cp_type_str)
input_data = None
# Convert input data to appropriate types and validate input
if age and bmi and bp and chol and plasma_glucose:
    input_data = np.array([[float(age), float(bmi), float(bp), float(chol), float(plasma_glucose), exercise_angina, cp_type]])
else:
    st.warning("Please fill in all the input fields.")

# Make prediction if input is valid
if input_data is not None:
    if st.button('Predict'):
        prediction = model.predict(input_data)
        predicted_color = np.unique(prediction, return_counts=True)[0][np.argmax(np.unique(prediction, return_counts=True)[1])]
        triage_mapping = {'red': 0, 'orange': 1, 'yellow': 2, 'green': 3}
        triage_mapping_inv = {v: k for k, v in triage_mapping.items()}
        predicted_color_label = triage_mapping_inv[predicted_color]
        st.write(f"Predicted triage color: {predicted_color_label}")
