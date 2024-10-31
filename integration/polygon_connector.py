import json
import polygon
from polygon import RESTClient
from dotenv import load_dotenv



class PolygonAPIConnector:
    def __init__(self) -> None:
        self.client = RESTClient()

    def get_data(self, ticker, date):
        return str(self.client.get_daily_open_close_agg(ticker=ticker, date=date))
    
    def get_volume_data(self, ticker, from_date, to_date):
        return str(self.client.get_aggs(ticker, from_=from_date, to=to_date, multiplier=1, timespan="day"))