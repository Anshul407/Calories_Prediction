import streamlit as st
import joblib
import pandas as pd
import time

# Load the trained model
model = joblib.load('calories_prediction_model.sav')

# Function to predict calories
def predict_calories(data):
    return model.predict(data)

# Main function for Streamlit app
def main():
    # Title and header image
    st.image('fitnessimg.jpeg', width=200)
    st.title('Calories Burned Prediction App')

    # Input fields
    st.sidebar.subheader('Enter User Details:')
    gender = st.sidebar.radio('Gender', ['Male', 'Female'])
    age = st.sidebar.slider('Age', 18, 100, 25)
    height = st.sidebar.slider('Height (cm)', 100, 250, 170)
    weight = st.sidebar.slider('Weight (kg)', 30, 200, 70)
    duration = st.sidebar.slider('Exercise Duration (min)', 10, 300, 60)
    heart_rate = st.sidebar.slider('Heart Rate (bpm)', 50, 200, 80)
    body_temp = st.sidebar.slider('Body Temperature (°C)', 35.0, 42.0, 37.0)

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
    if st.sidebar.button('Predict'):
        with st.spinner('Predicting Calories...'):
            time.sleep(2)  # Simulate prediction time
            calories = predict_calories(data)
            st.success(f'Predicted Calories Burned: {calories[0]:.2f} kcal')

    # Feedback section
    st.sidebar.subheader('Feedback')
    feedback = st.sidebar.text_area('Please share your feedback here:', '')

    if st.sidebar.button('Submit Feedback'):
        # Process feedback (e.g., store in database)
        st.sidebar.success('Thank you for your feedback!')

# Run the app
if __name__ == '__main__':
    main()
