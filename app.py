import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('calories_prediction_model.sav')

# Function to predict calories
def predict_calories(data):
    return model.predict(data)

# Main function for Streamlit app
def main():
    # Title
    st.title('Calories Burned Prediction App')

    # Input fields
    gender = st.radio('Gender', ['Male', 'Female'])
    age = st.slider('Age', 18, 100, 25)
    height = st.slider('Height (cm) (1 foot=30.48cm)', 100, 250, 170)
    weight = st.slider('Weight (kg)', 30, 200, 70)
    duration = st.slider('Exercise Duration (min)', 10, 300, 60)
    heart_rate = st.slider('Heart Rate (bpm)', 50, 200, 80)
    body_temp = st.slider('Body Temperature (°C)', 35.0, 42.0, 37.0)

    # Convert gender to numeric
    gender_encoded = 1 if gender == 'Female' else 0

    # Prepare input data as DataFrame
    data = pd.DataFrame({
        'Gender': [gender_encoded],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp]
    })

    # Predict calories
    if st.button('Predict'):
        calories = predict_calories(data)
        st.success(f'Your Have Burned: {calories[0]:.2f} Calories')

# Run the app
if __name__ == '__main__':
    main()
