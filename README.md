🔥 Calories Burned Predictor
=======================================
A simple Streamlit web app that predicts the number of calories burned during an exercise session using a Linear Regression model trained on user physiological and workout data.

Trained on merged datasets: exercise data and calories burned

Uses features like age, weight, height, heart rate, body temperature, duration, and gender

Encodes gender using label encoding for modeling

Provides real-time calorie burn prediction based on user inputs

Built with Python, Streamlit, Pandas, and scikit-learn

📌 Features
=========================================
Predict calories burned based on:
Age
Height
Weight
Heart Rate
Body Temperature
Duration
Gender
Interactive UI using Streamlit
Real-time prediction using a trained Linear Regression model

📂 Dataset
=======================================
This app uses two datasets:
exercise.csv: Contains user workout and physiological data.
calories.csv: Contains corresponding calories burned.
These datasets are merged on user_id for model training.

📊 Model
=======================================
Algorithm: Linear Regression
Preprocessing:
Label encoding for gender
Merging datasets
Feature selection

🧠 Inputs Used for Prediction
=======================================
Age
Weight (kg)
Height (cm)
Heart Rate (bpm)
Body Temperature (°C)
Duration (minutes)
Gender
