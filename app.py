import streamlit as st
from data_utils import load_data
import sys

sys.path.append("/Users/sumanshrestha/Documents/AI Class Omdena/capstone-project-makaisuman/pages")
from pages import data_exploration, model_training, prediction_page, eda, prediction_page_with_district, model_training_with_district, about

# Set the page configuration
st.set_page_config(
    page_title = "Climate Trend Predictor",
    page_icon=' ',
    layout = 'wide'
)

# Give the title
st.title("Temperatures Analysis and Predictions")
st.markdown("Analyze historical Temperatures data and predict future trends")
st.markdown("Temperatures data from 1989 to 2019")


df = load_data()


# Give the sidebar for the app navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About","Data Exploration", "EDA", "Model Training", 'Prediction', 'Training with District', 'Prediction with District'])


# Display the selected page
if page == "About":
    about.show(df)
elif page == "Data Exploration":
    data_exploration.show(df)
elif page == "EDA":
    eda.show(df)
elif page == "Model Training":
    model_training.show(df)
# Train page with district
elif page == 'Training with District':
    model_training_with_district.show(df)
# Prediction page with district
elif page == "Prediction with District": 
    prediction_page_with_district.show(df)
else: # Prediction page
    prediction_page.show(df)


#Displaying my name
st.sidebar.markdown("### Developed by Suman Shrestha")