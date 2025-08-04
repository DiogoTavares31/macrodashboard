from fredapi import Fred
import streamlit as st
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

raw_key = os.getenv("FRED_API_KEY")

fred = Fred(api_key=raw_key)

def get_interest_rate():
    """
    Fetch the latest Federal Funds Rate from FRED.
    Returns:
        float: The latest Federal Funds Rate.
    """
    series_id = 'DPRIME'  # Federal Funds Rate
    data = fred.get_series_latest_release(series_id)
    return data.iloc[-1]

def get_inflation_rate():
    """
    Fetch the latest inflation rate (CPI) from FRED.
    Returns:
        float: The latest inflation rate as a percentage.
    """
    series_id = 'CPIAUCSL'  # Consumer Price Index for All Urban Consumers
    data = fred.get_series_latest_release(series_id)
    inflation_rate = ((data.iloc[-1] - data.iloc[-13]) / data.iloc[-13]) * 100
    return inflation_rate

def get_unemployment_rate():
    """
    Fetch the latest unemployment rate from FRED.
    Returns:
        float: The latest unemployment rate as a percentage.
    """
    series_id = 'UNRATE'  # Unemployment Rate
    data = fred.get_series_latest_release(series_id)
    return data.iloc[-1]

def get_gdp_growth_rate():
    """
    Fetch the latest GDP growth rate from FRED.
    Returns:
        float: The latest GDP growth rate as a percentage.
    """
    series_id = 'A191RL1Q225SBEA'  # Real GDP: Percent Change from Preceding Period
    data = fred.get_series_latest_release(series_id)
    return data.iloc[-1]

def economic_models():
    """
    Streamlit app to display economic models based on user input.
    """
    st.header("Interactive Economic Models")
        
    interest_rate = st.slider("Interest Rate (%)", 0.0, 10.0, 2.0, 0.1)
    inflation_rate = st.slider("Inflation Rate (%)", 0.0, 10.0, 3.0, 0.1)
    
    gdp_growth = max(0, 3 - 0.5 * interest_rate + 0.3 * inflation_rate)
    unemployment_rate = min(10, 5 + 0.2 * interest_rate - 0.1 * inflation_rate)
    
    st.write(f"Estimated GDP Growth: {gdp_growth:.2f}%")
    st.write(f"Estimated Unemployment Rate: {unemployment_rate:.2f}%")
    
    fig, ax = plt.subplots()
    ax.bar(["GDP Growth", "Unemployment Rate"], [gdp_growth, unemployment_rate], color=['blue', 'red'])
    ax.set_ylabel("Percentage")
    ax.set_title("Economic Impact Model")
    
    st.pyplot(fig)