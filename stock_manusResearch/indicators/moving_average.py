import pandas as pd

def add_sma(df, length):
    df[f'SMA{length}'] = df['Close'].rolling(window=length).mean()
    return df

def add_ema(df, length):
    df[f'EMA{length}'] = df['Close'].ewm(span=length, adjust=False).mean()
    return df
