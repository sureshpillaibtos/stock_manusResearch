from dataclasses import dataclass
import pandas as pd

@dataclass
class StockData:
    symbol: str
    info: dict
    history: pd.DataFrame
    
    @property
    def current_price(self):
        return self.history['Close'].iloc[-1]
    
    @property
    def price_change(self):
        return self.history['Close'].iloc[-1] - self.history['Close'].iloc[-2]
    
    @property
    def percent_change(self):
        return (self.price_change / self.history['Close'].iloc[-2]) * 100
