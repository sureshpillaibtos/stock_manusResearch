import yfinance as yf
import pandas as pd
import streamlit as st

class YahooService:
    @staticmethod
    @st.cache_data(ttl=3600)
    def get_stock_data(symbol, period="6mo", interval="1d"):
        try:
            stock = yf.Ticker(symbol)
            df = stock.history(period=period, interval=interval)
            info = stock.info
            return df, info
        except Exception as e:
            st.error(f"Error fetching data for {symbol}: {e}")
            return pd.DataFrame(), {}

    @staticmethod
    @st.cache_data(ttl=3600)
    def get_market_data(indices):
        data = {}
        for name, symbol in indices.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="2d")
                if not hist.empty:
                    current = hist['Close'].iloc[-1]
                    prev = hist['Close'].iloc[-2]
                    change = current - prev
                    pct_change = (change / prev) * 100
                    data[name] = {
                        "price": current,
                        "change": change,
                        "pct_change": pct_change
                    }
            except:
                continue
        return data
