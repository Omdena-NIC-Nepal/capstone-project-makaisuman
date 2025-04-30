import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    ''' Loading the data from data Temperature.csv'''
    df = pd.read_csv('/Users/sumanshrestha/Documents/AI Class Omdena/capstone-project-makaisuman/data/Temperature.csv')
    # Convert the date column to datetime
    df['Date']= pd.to_datetime(df['Date'])
    # Extract the features 
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    return df


def prepare_features(df):
    """
    Prepare features for model training

    """
    X = df[['year', 'month']].values
    y = df['temperatures'].values

    return X, y