import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
         
Shown are the stock closing price and volume of Google!
""")
st.write("""
Gielo Fernandez
"""    
)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
tickerSymbol='GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historiucal prices for this sticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

#open high low close bolume dividends stock splits
st.write("""
# Closing Price
""")
st.line_chart(tickerDF.Close)
st.write("""
# Volume Price
""")
st.line_chart(tickerDF.Volume)