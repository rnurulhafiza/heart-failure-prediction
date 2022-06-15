import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.write("""
# Heart Failure Prediction App
This app predicts the **Heart Failure**.
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('Age', 28, 50, 77)
    resting_blood_pressure = st.sidebar.slider('Resting blood pressure', 0, 100, 200)
    cholesterol = st.sidebar.slider('Cholesterol', 0, 300, 603)
    fasting_blood_sugar = st.sidebar.slider('Fasting blood sugar', 0, 0.5, 1)
    data = {'age': age,
            'resting_blood_pressure': resting_blood_pressure,
            'cholesterol': cholesterol,
            'fasting_blood_sugar': fasting_blood_sugar}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

heart failure = pd.read_csv('https://raw.githubusercontent.com/rnurulhafiza/heart-failure-prediction/main/heart.csv')
               

