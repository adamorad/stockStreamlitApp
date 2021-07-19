import yfinance as yf
import streamlit as st
from datetime import datetime

st.write("""Stocks App""")

tickerSymbol = st.text_input("Give me a ticker and I will show you closing and volume graphs:", 'GOOGL')
try:
    tickerData = yf.Ticker(tickerSymbol)
except:
    tickerData = yf.Ticker('GOOGL')

tickerDf = tickerData.history(period='id', start='2010-01-01', end=datetime.today().strftime('%Y-%m-%d'))

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
