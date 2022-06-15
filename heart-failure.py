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
    maximum_heart_rate_achieved = st.sidebar.slider('Maximum heart rate achieved', 60, 131, 202)
    data = {'age': age,
            'resting_blood_pressure': resting_blood_pressure,
            'cholesterol': cholesterol,
            'maximum_heart_rate_achieved': maximum_heart_rate_achieved}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

heart = pd.read_csv('https://raw.githubusercontent.com/rnurulhafiza/heart-failure-prediction/main/heart.csv')
               
X = iris.drop('heartdisease', axis = 1)
X.head()

y = iris['heartdisease']
y.head()

clf = RandomForestClassifier()
clf.fit(X, y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.table(['heartdisease', 'normal'])


st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
