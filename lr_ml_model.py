import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

@st.cache_data
def load_and_train_model():
    exercise_df = pd.read_csv('exercise.csv')
    calories_df = pd.read_csv('calories.csv')

    exercise_df.rename(columns={
        'User_ID': 'user_id',
        'Gender': 'gender',
        'Age': 'age',
        'Height': 'height',
        'Weight': 'weight',
        'Duration': 'duration',
        'Heart_Rate': 'heart_rate',
        'Body_Temp': 'body_temp'
    }, inplace=True)

    calories_df.rename(columns={
        'User_ID': 'user_id',
        'Calories': 'calories'
    }, inplace=True)

    df = pd.merge(exercise_df, calories_df, on='user_id')

    le = LabelEncoder()
    df['gender'] = le.fit_transform(df['gender'].str.lower())

    X = df[['age', 'weight', 'height', 'heart_rate', 'body_temp', 'duration', 'gender']]
    y = df['calories']

    model = LinearRegression()
    model.fit(X, y)

    return model

model = load_and_train_model()

st.set_page_config(page_title="Calories Burned Predictor", layout="centered")
st.title("🔥 Calories Burned Predictor")
st.markdown("Enter your details below to estimate how many calories you burned during your exercise session.")

# Inputs without steppers, all in one column:
age = st.text_input("Age",max_chars=3)
height = st.text_input("Height (cm)",max_chars=5)
heart_rate = st.text_input("Heart Rate (bpm)" ,max_chars=5)
gender = st.selectbox("Gender", ['Male', 'Female'])
weight = st.text_input("Weight (kg)", max_chars=5)
body_temp = st.text_input("Body Temperature (°C)",max_chars=4)
duration = st.text_input("Duration (minutes)", max_chars=5)

def to_float(val, default=0):
    try:
        return float(val)
    except ValueError:
        return default

age = to_float(age)
height = to_float(height)
heart_rate = to_float(heart_rate)
weight = to_float(weight)
body_temp = to_float(body_temp)
duration = to_float(duration)

gender_encoded = 1 if gender.lower() == 'male' else 0

if st.button("Predict Calories Burned"):
    input_data = [[age, weight, height, heart_rate, body_temp, duration, gender_encoded]]
    prediction = model.predict(input_data)
    st.success(f"✅ Estimated Calories Burned: **{prediction[0]:.2f} calories**")
