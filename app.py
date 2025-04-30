import streamlit as st
from data_utils import load_data
import sys

sys.path.append("/Users/sumanshrestha/Documents/AI Class Omdena/capstone-project-makaisuman/pages")
from pages import data_exploration, model_training, prediction_page, eda

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
page = st.sidebar.radio("Go to", ["Data Exploration", "EDA", "Model Training", 'Prediction'])


# Display the selected page
if page == "Data Exploration":
    data_exploration.show(df)
elif page == "EDA":
    eda.show(df)
elif page == "Model Training":
    model_training.show(df)
else: # Prediction page
    prediction_page.show(df)


#Displaying my name
st.sidebar.markdown("### Developed by Suman Shrestha")