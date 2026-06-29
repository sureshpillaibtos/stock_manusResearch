import plotly.graph_objects as go

def show_line_chart(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name=symbol))
    fig.update_layout(title=f'{symbol} Price History', template="plotly_dark", height=400)
    return fig
