import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import calendar
import folium
import streamlit as st

def plot_time_series(df):
    """
    Plot the temperatures over time
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Temp_2m'], label='Temperature', color='tab:blue')
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Monthly Temperatures")
    ax.grid(True)
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_monthly_distribution(df):
    """
    Plot the monthly distribution of temperatures
    """
    # Group by Month and calculate average temperature
    monthly_avg = df.groupby('month')['Temp_2m'].mean().reset_index()
    monthly_avg['month'] = monthly_avg['month'].apply(lambda x: calendar.month_abbr[x])
    #Sort months by calendar order
    monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=calendar.month_abbr[1:], ordered=True)
    monthly_avg = monthly_avg.sort_values('month')

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=monthly_avg, x='month', y='Temp_2m', palette='coolwarm', ax=ax)
    ax.set_title('Average Temperature by Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Average Temperature (°C)')
    return fig



def plot_seasonal_patterns(df):
    """
    plot for monthly temperature distributions
    """
    fig, ax = plt.subplots(figsize = (10, 6))
    sns.boxplot(x = 'month', y = 'Temp_2m', data = df, ax = ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperatures in C")
    ax.set_title("Monthly Temperatures Distributions")
    return fig


def plot_yearly_trends(df):
    """
    Plot the yearly average temperatures
    """
    fig, ax = plt.subplots(figsize = (10, 6))
    yearly_avg = df.groupby('year')['Temp_2m'].mean().reset_index()
    ax.plot(yearly_avg['year'], yearly_avg['Temp_2m'], marker = 'o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperatures in C")
    ax.set_title("Yearly Average Temperatures ")
    ax.grid(True)
    return fig

def plot_actual_vs_predicted(y_test, y_pred):
    """
    Plot the actual vs predicted values
    """
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.scatter(y_test, y_pred, alpha = 0.7)
    ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
    ax.set_xlabel("Actual Temperatures")
    ax.set_ylabel("Predicted Temperatures in C")
    ax.set_title("Actual vs Predicted Temperatures ")
    return fig

def plot_prediction_context(hist_temps, pred_year, pred_month, prediction):
    """
    Plot for me the prediction in historical context
    """

    year_hist, temp_hist = zip(*hist_temps)

    fig, ax = plt.subplots(figsize = (10, 6))

    # Plot the historical data for the same month
    ax.scatter(year_hist, temp_hist, label = f"Historical (Month {pred_month})", color = "blue")
    ax.plot(year_hist, temp_hist, 'b--', alpha = 0.6)

    # Plot the prediction
    ax.scatter([pred_year], [prediction], color = 'red', s =100, label = "Prediction")

    # Add a trend line
    z = np.polyfit(year_hist, temp_hist, 1)
    p = np.poly1d(z)
    ax.plot(range(2010, pred_year + 1), p(range(2010, pred_year + 1)), 'g-', label = "Trend")

    ax.set_xlabel("Year")
    ax.set_ylabel(f"Temperature for month {pred_month}")
    ax.set_title(f"Historical and predicted tempertures fo rhe moth of {pred_month} ")
    plt.legend()
    ax.grid(True)

    return fig

'''def plot_temp_distribution_by_district(df):
    # Plot with matplotlib/seaborn
    fig = plt.figure(figsize=(14, 8))
    sns.boxplot(data=df, x='District', y='Temp_2m', orient='h', palette='coolwarm')
    plt.title('Temperature Distribution by District')
    plt.ylabel('Temperature at 2m (°C)')
    plt.xlabel('District')
    plt.tight_layout()
    return fig 
'''

def plot_temp_distribution_by_district1(df):
    # Get first 10 districts alphabetically (or change to .head(10) if based on appearance)
    first_10_districts = df['District'].drop_duplicates().sort_values().head(10)
    filtered_df = df[df['District'].isin(first_10_districts)]
    # Create the figure
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=filtered_df, x='District', y='Temp_2m', ax=ax)
    ax.set_title('Temperature Distribution by District (First 10)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_temperature_distribution_by_selected_district(df):
    # Dropdown for district selection
    districts = sorted(df['District'].unique())
    selected_district = st.selectbox("Select a District", districts)

    # Filter data for selected district
    filtered_df = df[df['District'] == selected_district]

    # Create boxplot for the selected district
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x='District', y='Temp_2m', ax=ax)
    ax.set_title(f'Temperature Distribution in {selected_district}')
    plt.tight_layout()
    return fig

def plot_correlation(df):
    # Compute correlation (only for numeric columns)
    corr = df.corr(numeric_only=True)

    # Display correlation matrix as a heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    return fig
