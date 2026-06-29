import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.sidebar import render_sidebar
from modules.market_overview import render_market_overview
from modules.stock_analysis import render_stock_analysis
from modules.stock_compare import render_comparison

st.set_page_config(page_title="Stock Research Platform", layout="wide")

def main():
    # Sidebar
    sidebar_data = render_sidebar()
    
    # Navigation
    menu = ["Dashboard", "Compare Stocks"]
    choice = st.sidebar.radio("Navigation", menu)
    
    if choice == "Dashboard":
        render_market_overview()
        st.markdown("---")
        render_stock_analysis(
            sidebar_data["symbol"],
            sidebar_data["period"],
            sidebar_data["interval"],
            sidebar_data["chart_type"],
            sidebar_data["indicators"]
        )
    elif choice == "Compare Stocks":
        render_comparison()

if __name__ == "__main__":
    main()
