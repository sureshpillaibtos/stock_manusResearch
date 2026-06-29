import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_candlestick(df, symbol, indicators=None):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                       vertical_spacing=0.03, subplot_titles=(f'{symbol} Price', 'Volume'), 
                       row_width=[0.2, 0.7])

    # Candlestick
    fig.add_trace(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name='Price'), row=1, col=1)

    # Indicators
    if indicators:
        for ind in indicators:
            if ind in df.columns:
                fig.add_trace(go.Scatter(x=df.index, y=df[ind], name=ind), row=1, col=1)

    # Volume
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'), row=2, col=1)

    fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_dark")
    return fig
