import streamlit as st

def format_currency(value):
    return f"${value:,.2f}"

def format_volume(value):
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    return f"{value:,}"

def calculate_percentage(current, previous):
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100

def color_positive_negative(value):
    color = "green" if value >= 0 else "red"
    return f"color: {color}"

def display_metric_card(label, value, delta=None):
    st.metric(label=label, value=value, delta=delta)
