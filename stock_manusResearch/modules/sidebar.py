import streamlit as st
from config.categories import STOCK_CATEGORIES
from config.constants import PERIODS, INTERVALS, CHART_TYPES, INDICATORS

def render_sidebar():
    st.sidebar.title("Stock Research")
    
    category = st.sidebar.selectbox("Stock Categories", list(STOCK_CATEGORIES.keys()))
    stocks = STOCK_CATEGORIES[category]
    
    selected_stock = st.sidebar.selectbox("Stock", stocks)
    
    st.sidebar.markdown("---")
    period_label = st.sidebar.selectbox("Period", list(PERIODS.keys()), index=2)
    period = PERIODS[period_label]
    
    interval_label = st.sidebar.selectbox("Interval", list(INTERVALS.keys()))
    interval = INTERVALS[interval_label]
    
    st.sidebar.markdown("---")
    chart_type = st.sidebar.selectbox("Chart Type", CHART_TYPES)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Indicators")
    selected_indicators = []
    for ind in INDICATORS:
        if st.sidebar.checkbox(ind, value=(ind in ["SMA20", "SMA50", "SMA200"])):
            selected_indicators.append(ind)
            
    st.sidebar.markdown("---")
    analyse_btn = st.sidebar.button("Analyse")
    
    return {
        "category": category,
        "symbol": selected_stock,
        "period": period,
        "interval": interval,
        "chart_type": chart_type,
        "indicators": selected_indicators,
        "analyse": analyse_btn
    }
