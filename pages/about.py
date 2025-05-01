import streamlit as st

def show(df):
    


    st.header("📌 About the Project")

    st.markdown("""
    This project focuses on analyzing historical temperature trends and predicting future temperature values using data collected from **1989 to 2019**. The goal is to gain insights into climate behavior over the years and to build predictive models that can estimate future temperatures both at the national and district levels.

    ### 🔍 Project Objectives
    - Explore and understand the structure and characteristics of temperature data.
    - Conduct **Exploratory Data Analysis (EDA)** to identify trends, seasonality, and anomalies.
    - Train multiple regression models to forecast temperature trends.
    - Provide district-level insights and predictions to support regional climate understanding.

    ### 🧩 Dataset Overview
    - **Time Range:** 1989 - 2019  
    - **Key Features:** Date, Temperature (`Temp_2m`), District, Latitude, Longitude, and other weather variables.

    ### 🧠 Machine Learning Models Used
    We have trained and compared four different regression models to evaluate performance and robustness:
    - 🌲 **Random Forest Regressor**
    - 📉 **Ridge Regression**
    - 📈 **Lasso Regression**
    - 🔥 **Gradient Boosting Regressor**

    ### 📂 Project Sections
    1. **Data Exploration** – Understand the raw structure of the dataset.
    2. **Exploratory Data Analysis (EDA)** – Visualize patterns and trends over the years.
    3. **Model Training** – Train multiple models to forecast temperature.
    4. **Prediction** – Generate future temperature predictions using trained models.
    5. **Training with District** – Build district-specific models for regional forecasting.
    6. **Prediction with District** – Make temperature forecasts at the district level.

    ---

    
    """)
st.markdown("### 🔗 My Streamlit App:")
st.markdown("[Click here to visit my Streamlit app](https://capstone-project-makaisuman.streamlit.app/)")
