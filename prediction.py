import pandas as pd
import numpy as np

def make_prediction(model, year, month):
    """
    Make the temperature prediction for a given month or year
    """
    features = np.array([[year, month]])
    return model.predict(features)[0]

def get_historical_context(df, month):
    """
    Get historical temperatures for the same month
    """
    years = df['year'].unique()
    hist_temps = []

    for year in years:
        month_data = df[(df['year'] == year) & (df['month'] == month)]
        if not month_data.empty:
            hist_temps.append((year, month_data['Temp_2m'].values[0]))
    
    return hist_temps

def get_historical_average(df, month):
    """
    Get historical average temperatures of a given month
    """

    return df[df['month'] == month]['Temp_2m'].mean()

def get_historical_average_by_district(df, month, district):
    """
    Get historical average temperatures of a given month
    """
    return df[(df['month'] == month) & (df['District'] == district)]['Temp_2m'].mean()

# Prediction with district
def make_prediction_with_district(model, district, year, month):
   
    """
    Make the temperature prediction for a given month or year
    """
    features = np.array([[district, year, month]])
    return model.predict(features)[0]