import json
import polygon
from polygon import RESTClient
from dotenv import load_dotenv

class PolygonAPIConnector:
    """
    A class to interact with the Polygon API, allowing retrieval of stock data such as daily open-close 
    information and trading volume over specified date ranges.
    
    Attributes:
    -----------
    client : RESTClient
        An instance of the Polygon RESTClient, initialized with the API key from the environment.
    """

    def __init__(self) -> None:
        """
        Initializes the PolygonAPIConnector instance by setting up the REST client.
        Ensure the API key is available in the environment variables, loaded using `load_dotenv()` if 
        stored in an `.env` file.
        """
        self.client = RESTClient()

    def get_data(self, ticker: str, date: str) -> str:
        """
        Retrieves the daily open-close data for a given ticker on a specified date.
        
        Parameters:
        -----------
        ticker : str
            The ticker symbol of the stock (e.g., "AAPL" for Apple Inc.).
        date : str
            The date for which data is requested, formatted as "YYYY-MM-DD".
        
        Returns:
        --------
        str
            A string representation of the daily open-close data retrieved from the API, including 
            open price, close price, and trading volume.
        
        Example:
        --------
        ```python
        connector.get_data("AAPL", "2024-11-01")
        ```
        """
        return str(self.client.get_daily_open_close_agg(ticker=ticker, date=date))
    
    def get_volume_data(self, ticker: str, from_date: str, to_date: str) -> str:
        """
        Retrieves the daily trading volume data for a specified ticker over a given date range.
        
        Parameters:
        -----------
        ticker : str
            The ticker symbol of the stock (e.g., "AAPL" for Apple Inc.).
        from_date : str
            The start date of the data range, formatted as "YYYY-MM-DD".
        to_date : str
            The end date of the data range, formatted as "YYYY-MM-DD".
        
        Returns:
        --------
        str
            A string representation of the aggregated volume data retrieved from the API, including 
            daily trading volumes for each day in the specified range.
        
        Example:
        --------
        ```python
        connector.get_volume_data("AAPL", "2024-01-01", "2024-11-01")
        ```
        """
        return str(self.client.get_aggs(ticker, from_=from_date, to=to_date, multiplier=1, timespan="day"))
