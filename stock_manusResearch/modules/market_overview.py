import streamlit as st
from services.market_service import MarketService
from utils.common import display_metric_card

def render_market_overview():
    st.subheader("Market Overview")
    market_data = MarketService.get_overview()
    
    cols = st.columns(len(market_data))
    for i, (name, data) in enumerate(market_data.items()):
        with cols[i]:
            display_metric_card(name, f"{data['price']:,.2f}", f"{data['pct_change']:.2f}%")
