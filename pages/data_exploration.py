import streamlit as st
import sys
import io

sys.path.append("/Users/sumanshrestha/Documents/AI Class Omdena/capstone-project-makaisuman")
from visualizations import plot_time_series, plot_seasonal_patterns, plot_yearly_trends

def show(df):
    """
    Display the data exploration page
    """
    st.header("Data Exploration")

    # Show the raw data
    st.header("Raw Data we have Loaded" )
    st.dataframe(df.head(10))

    # About the data.
    st.info("About the Data")
    st.text("The dataset contains historical temperature data from 1989 to 2019. ")
    st.text("It includes the following columns: ")
    st.text( "Date: The date of the recorded climate data.")
    st.text("District: The geographical region within Nepal for which the climate data is recorded. There are 62 districts in this dataset.")
    st.text("Latitude and Longitude: The geographical coordinates of the district location, specifying its position on the Earth's surface.")
    st.text("Temp_2m: Temperature at 2 meters above the ground, measured in degrees Celsius (°C).")
    st.text("MaxTemp_2m: Maximum Temperature at 2 meters above the ground, measured in degrees Celsius (°C).")
    st.text("MinTemp_2m: Minimum Temperature at 2 meters above the ground, measured in degrees Celsius (°C).")
    st.text("TempRange_2m: Temperature Range at 2 meters above the ground, measured in degrees Celsius (°C).")
    st.text("year: The year of the recorded climate data, extracted from the Date column.")
    st.text("month: The month of the recorded climate data, extracted from the Date column.")
    st.text("day: The day of the recorded climate data, extracted from the Date column.")
    
    
    # basic statistics
    st.info("Statistical Summary")
    st.write(df.describe())


    # Checking of any missing data
    st.info("Checking any Missing data")
    st.write(df.isnull().sum())

    # summary of the Data
    st.info("Summary of Data")

    # Capture df.info() output
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    st.text(info_str)

