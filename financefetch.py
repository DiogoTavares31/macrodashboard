import yfinance as yf
import fear_and_greed
import streamlit as st

def get_fear_and_greed_index():
    """
    Fetch the current Fear & Greed Index value and description.
    Returns:
        tuple: (index_value, description)
    """
    fgi = fear_and_greed.get()
    return fgi.value, fgi.description

def display_fear_and_greed_gauge(index_value: int, description: str):
    """ Display the Fear & Greed Index gauge in Streamlit.
    Args:
        index_value (int): The current Fear & Greed Index value.
        description (str): A description of the index value.
    """
    st.markdown("### 🧭 Fear & Greed Sentiment Gauge")

    # Define the emoji or color based on index
    if index_value <= 24:
        emoji = "😨"
        level = "Extreme Fear"
        color = "#d9534f"
    elif index_value <= 44:
        emoji = "😟"
        level = "Fear"
        color = "#f0ad4e"
    elif index_value <= 54:
        emoji = "😐"
        level = "Neutral"
        color = "#5bc0de"
    elif index_value <= 74:
        emoji = "😊"
        level = "Greed"
        color = "#5cb85c"
    else:
        emoji = "😈"
        level = "Extreme Greed"
        color = "#4cae4c"

    # Render sentiment gauge
    st.markdown(f"""
    <div style="text-align: center; padding: 1em; background-color: #F1F2F4; border-radius: 10px;">
        <div style="font-size: 50px;">{emoji}</div>
        <div style="font-size: 22px; font-weight: bold; color: {color};">{level}</div>
        <div style="font-size: 16px; color: grey; margin-top: 0.5em;">Index Value</div>
        <div style="font-size: 32px; font-weight: bold; color: #333;">{index_value}</div>
        <!-- <div style="font-size: 14px; color: #888; margin-top: 0.3em;">({description.capitalize()})</div> -->
    </div>
    """, unsafe_allow_html=True)

def fetch_market_data():
    """
    Fetch market data for key indices and commodities.
    Returns:
        dict: A dictionary containing market data for S&P 500, Gold, Oil, and Wheat.
    """
    tickers = {
        "S&P 500 (SPY)": "SPY",
        "Gold (GLD)": "GLD",
        "Oil (USO)": "USO",
        "Wheat (WEAT)": "WEAT"
    }
    data = {}
    for label, ticker in tickers.items():
        df = yf.download(ticker, period="3mo", interval="1d", progress=False)
        if not df.empty:
            data[label] = df["Close"]
        else:
            st.warning(f"No data found for {label} ({ticker})")
    return data
