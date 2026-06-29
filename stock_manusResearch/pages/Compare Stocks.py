import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from modules.stock_compare import render_comparison

st.set_page_config(page_title="Compare Stocks - Stock Research Platform", layout="wide")

def main():
    render_comparison()

if __name__ == "__main__":
    main()
