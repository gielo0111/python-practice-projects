import yfinance as yf
import streamlit as st
import pandas as pd

# Title of the app
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")
st.write("""
Gielo Joseph Fernandez
""")

# Define the ticker symbol
ticker_symbol = 'GOOGL'

# Get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# Get the historical prices for this ticker
try:
    ticker_df = ticker_data.history(period='1d', start='2010-05-31', end='2020-05-31')
    if ticker_df.empty:
        st.write("No data available.")
    else:
        # Display closing price chart
        st.write("## Closing Price")
        st.line_chart(ticker_df.Close)

        # Display volume chart
        st.write("## Volume Price")
        st.line_chart(ticker_df.Volume)
except Exception as e:
    st.error(f"Error fetching data: {e}")