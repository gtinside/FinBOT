import json
import polygon
from polygon import RESTClient
from dotenv import load_dotenv



class PolygonAPIConnector:
    def __init__(self) -> None:
        self.client = RESTClient()

    def get_data(self, ticker, date):
        return str(self.client.get_daily_open_close_agg(ticker=ticker, date=date))