import streamlit as st
import sys

sys.path.append("/Users/sumanshrestha/Documents/AI Class Omdena/capstone-project-makaisuman")
from visualizations import  plot_monthly_distribution, plot_time_series, plot_seasonal_patterns, plot_yearly_trends, plot_temp_distribution_by_district1, plot_temperature_distribution_by_selected_district, plot_correlation


def show(df):
    
    # Time series plot
    st.subheader("Temperatures over time")
    fig = plot_time_series(df)
    st.pyplot(fig)

    # Monthly Plot
    st.subheader("Monthly Temperature pattern using Average")
    fig = plot_monthly_distribution(df)
    st.pyplot(fig)

    

    # Yearly average temperatures
    st.subheader("Yearly Average Temperatures")
    fig = plot_yearly_trends(df)
    st.pyplot(fig)

 
 

    #Temperature Distribution by District1
    st.subheader("Temperature Distribution for First 10 Districts")
    # Temperature variable selection
    fig= plot_temp_distribution_by_district1(df)
    st.pyplot(fig)
    

    # Temperature Distribution by Selected District
    st.title("Temperature Distribution by Selected District")
    fig= plot_temperature_distribution_by_selected_district(df)
    st.pyplot(fig)

    # Correlation Matrix of Climate Data
    st.title("Correlation Matrix of Climate Data")
    fig= plot_correlation(df)
    st.pyplot(fig)






    '''
    #Temperature Distribution by District
    st.title("Temperature Distribution by District")
    # Temperature variable selection
    fig= plot_temp_distribution_by_district(df)
    st.pyplot(fig)


    ## Average Temperature Map by District
    st.subheader("Average Temperature Map by District")
    fig = plot_average_temp_district(df)
    fig


    # Seasonal Plot
    st.subheader("Seasonal Temperature pattern")
    fig = plot_seasonal_patterns(df)
    st.pyplot(fig)
'''