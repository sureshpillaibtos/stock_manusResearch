import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from modules.sidebar import render_sidebar
from modules.stock_analysis import render_stock_analysis

st.set_page_config(page_title="Stock Analysis - Stock Research Platform", layout="wide")

def main():
    sidebar_data = render_sidebar()
    render_stock_analysis(
        sidebar_data["symbol"],
        sidebar_data["period"],
        sidebar_data["interval"],
        sidebar_data["chart_type"],
        sidebar_data["indicators"]
    )

if __name__ == "__main__":
    main()
