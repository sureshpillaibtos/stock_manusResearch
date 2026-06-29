import streamlit as st
import pandas as pd
from services.yahoo_service import YahooService
from charts.comparison_chart import show_comparison_chart
from config.categories import STOCK_CATEGORIES

def render_comparison():
    st.title("Stock Comparison")
    
    all_stocks = []
    for cat_stocks in STOCK_CATEGORIES.values():
        all_stocks.extend(cat_stocks)
    all_stocks = sorted(list(set(all_stocks)))
    
    selected_stocks = st.multiselect("Select Stocks to Compare", all_stocks, default=all_stocks[:2])
    
    if st.button("Analyse Comparison"):
        if not selected_stocks:
            st.warning("Please select at least one stock.")
            return
            
        data_dict = {}
        comparison_metrics = []
        
        with st.spinner("Fetching data..."):
            for symbol in selected_stocks:
                df, info = YahooService.get_stock_data(symbol, period="1y")
                if not df.empty:
                    data_dict[symbol] = df
                    comparison_metrics.append({
                        "Symbol": symbol,
                        "Name": info.get("longName", ""),
                        "Price": df['Close'].iloc[-1],
                        "1Y Return (%)": ((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100,
                        "Market Cap": info.get("marketCap", 0),
                        "PE Ratio": info.get("forwardPE", 0)
                    })
        
        # Performance Chart
        st.plotly_chart(show_comparison_chart(data_dict), use_container_width=True)
        
        # Comparison Table
        st.subheader("Key Metrics Comparison")
        comp_df = pd.DataFrame(comparison_metrics)
        st.dataframe(comp_df)
