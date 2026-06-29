import pandas as pd

def add_rsi(df, length=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=length).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=length).mean()
    
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df
