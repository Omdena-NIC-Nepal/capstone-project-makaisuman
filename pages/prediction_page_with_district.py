import streamlit as st
import numpy as np
import sys
from sklearn.preprocessing import LabelEncoder

sys.path.append("/Users/sumanshrestha/Documents/AI Class Omdena/capstone-project-makaisuman")
from models import load_model
from prediction import make_prediction, get_historical_context, get_historical_average,make_prediction_with_district, get_historical_average_by_district
from visualizations import plot_prediction_context

def show(df):
    """
    Display the predictions page
    """
    st.header("Temperature Predictions by District, year and month")

    # Check if the model exists in the session
    if 'model' not in st.session_state:
        model = load_model()
        if model is None:
            st.warning("No trained model found. Please go to the model training page first")
            st.stop()

        st.session_state['model'] = model
        st.session_state['model_type'] = "Pre-trained Model"

    # Show which model is being used
    st.info(f"Using {st.session_state['model_type']} for predictions")

    # Prediction input
    st.subheader("Select data for prediction: ")
    pred_district = st.selectbox("District", df['District'].unique())
    pred_year = st.slider("Year", 2010, 2025, 2020)
    pred_month = st.slider("Month", 1, 12, 6)

    # Initialize and fit LabelEncoder
    label_encoder = LabelEncoder()
    label_encoder.fit(df['District'])
    
    

    # make the prediction
    if st.button("Predict Temperature"):
        # Get model
        model = st.session_state['model']

        # make predictions
        pred_district_encode = label_encoder.transform([pred_district])[0]
        prediction = make_prediction_with_district(model,pred_district_encode, pred_year, pred_month)

        # Display the results
        st.success(f"Predicted Temperature for {pred_district} {pred_year} - {pred_month:02d}: {prediction:.2f} °C")
    
        # Historical Comparison
        hist_avg = get_historical_average_by_district(df, pred_month, pred_district)

        st.write(f"Historical Average for month {pred_month}: {hist_avg:.2f}°C")

        # calculate the difference from the historical average
        diff = prediction - hist_avg
        if diff > 0:
            st.write(f"Prediction is {diff:.2f}°C **higher** than historical average")
        else:
            st.write(f"Prediction is {abs(diff):.2f}°C **Lower** than historical average")

        # visualize prediction in context of historical data
        st.subheader("Prediction in Historical context")

        # Get the historical temperatures for the same month
        hist_temps = get_historical_context(df, pred_month)

        # Plot prediction context
        fig = plot_prediction_context(hist_temps, pred_year, pred_month, prediction)
        st.pyplot(fig)