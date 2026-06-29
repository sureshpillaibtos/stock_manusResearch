from services.yahoo_service import YahooService
from config.categories import MARKET_INDICES

class MarketService:
    @staticmethod
    def get_overview():
        return YahooService.get_market_data(MARKET_INDICES)
