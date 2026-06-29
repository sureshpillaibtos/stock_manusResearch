import streamlit as st
import pandas as pd
from services.yahoo_service import YahooService
from utils.common import format_currency, format_volume, display_metric_card
from charts.candlestick import show_candlestick
from charts.line_chart import show_line_chart
from indicators.moving_average import add_sma, add_ema
from indicators.rsi import add_rsi
from indicators.macd import add_macd
from indicators.bollinger import add_bbands

def render_stock_analysis(symbol, period, interval, chart_type, indicators):
    df, info = YahooService.get_stock_data(symbol, period, interval)
    
    if df.empty:
        st.warning("No data found for this stock.")
        return

    # Header
    st.title(f"{info.get('longName', symbol)} ({symbol})")
    
    # Summary Metrics
    col1, col2, col3, col4 = st.columns(4)
    current_price = df['Close'].iloc[-1]
    prev_close = df['Close'].iloc[-2]
    change = current_price - prev_close
    pct_change = (change / prev_close) * 100
    
    with col1:
        display_metric_card("Current Price", format_currency(current_price), f"{change:.2f} ({pct_change:.2f}%)")
    with col2:
        display_metric_card("Market Cap", format_volume(info.get('marketCap', 0)))
    with col3:
        display_metric_card("Volume", format_volume(df['Volume'].iloc[-1]))
    with col4:
        display_metric_card("52 Week High", format_currency(info.get('fiftyTwoWeekHigh', 0)))

    # Apply Indicators
    active_indicators = []
    for ind in indicators:
        if ind == "SMA20": 
            add_sma(df, 20)
            active_indicators.append("SMA20")
        elif ind == "SMA50": 
            add_sma(df, 50)
            active_indicators.append("SMA50")
        elif ind == "SMA200": 
            add_sma(df, 200)
            active_indicators.append("SMA200")
        elif ind == "EMA20": 
            add_ema(df, 20)
            active_indicators.append("EMA20")
        elif ind == "RSI": 
            add_rsi(df)
            active_indicators.append("RSI")
        elif ind == "MACD": 
            df = add_macd(df)
            active_indicators.extend(["MACD", "MACD_Signal"])
        elif ind == "Bollinger Bands": 
            df = add_bbands(df)
            active_indicators.extend(["BBU", "BBL"])

    # Chart
    st.subheader("Stock Chart")
    if chart_type == "Candlestick":
        fig = show_candlestick(df, symbol, active_indicators)
        st.plotly_chart(fig, use_container_width=True)
    else:
        fig = show_line_chart(df, symbol)
        st.plotly_chart(fig, use_container_width=True)

    # Previous 10 Days Table
    st.subheader("Previous 10 Days Data")
    st.table(df.tail(10)[['Open', 'High', 'Low', 'Close', 'Volume']].sort_index(ascending=False))
