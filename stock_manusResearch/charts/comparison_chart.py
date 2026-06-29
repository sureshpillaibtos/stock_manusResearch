import plotly.graph_objects as go
import pandas as pd

def show_comparison_chart(data_dict):
    fig = go.Figure()
    for symbol, df in data_dict.items():
        if not df.empty:
            # Normalize to starting price of 100
            norm_price = (df['Close'] / df['Close'].iloc[0]) * 100
            fig.add_trace(go.Scatter(x=df.index, y=norm_price, mode='lines', name=symbol))
    
    fig.update_layout(title='Stock Performance Comparison (Normalized to 100)',
                     yaxis_title='Normalized Price',
                     template="plotly_dark", height=500)
    return fig
