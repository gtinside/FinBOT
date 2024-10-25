import polygon
from polygon import RESTClient
from dotenv import load_dotenv



class PolygonAPIConnector:
    def __init__(self) -> None:
        self.client = RESTClient()

    def get_data(self):
        data = self.client.get_daily_open_close_agg(ticker="AAPL", date="2024-10-22")
        print(data)


load_dotenv()
PolygonAPIConnector().get_data()
