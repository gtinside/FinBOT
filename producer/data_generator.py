import time
import random
from typing import List
from integration.fuzzy_data_connector import FuzzyDataConnector
from model.quotes import MarketQuote, TapeEnum, MarketMetadata, BidAskData


"""
Responsible for
a) Reading the ticker from config file
b) Call OpenAPI to generate mock quote for that ticker
c) Use mock multiplier to generate 100 records per ticker
d) Push it to Kafka 
"""

fuzzy_data_con = FuzzyDataConnector()
def read_ticker_from_config():
    with open("conf/ticker.properties") as conf:
        tickers = conf.readlines()
    return [ticker.strip() for ticker in tickers]

def get_latest_quote(tickers):
     for ticker in tickers:
       yield fuzzy_data_con.get_quote_data(ticker)

def generate_mock_quotes_from_initial(initial_quote: MarketQuote, n: int = 100) -> List[MarketQuote]:
    """
    Generates `n` MarketQuote objects based on an initial MarketQuote object.
    Values are slightly varied to simulate market fluctuations.
    """
    mock_quotes = []
    base_sequence = initial_quote.market_metadata.sequence_number  # Use the initial sequence number

    for i in range(n):
        # Slightly adjust bid and ask prices to simulate real market movement
        bid_price = round(initial_quote.bid.price + random.uniform(-1.00, 1.00), 2)
        ask_price = round(bid_price + random.uniform(0.01, 1.00), 2)
        
        # Vary the bid and ask sizes within a reasonable range
        bid_size = max(1, initial_quote.bid.size + random.randint(-500, 500))
        ask_size = max(1, initial_quote.ask.size + random.randint(-500, 500))
        
        # Keep the same exchange but allow small changes in tape and timestamps
        exchange_id = initial_quote.bid.exchange_id
        tape = random.choice(list(TapeEnum))  # Allow some variation in tape
        timestamp = int(time.time()) + i  # Increment timestamp for each quote

        # Create a new MarketQuote with modified values
        quote = MarketQuote(
            event_type=initial_quote.event_type,
            ticker=initial_quote.ticker,
            bid=BidAskData(exchange_id=exchange_id, price=bid_price, size=bid_size),
            ask=BidAskData(exchange_id=exchange_id, price=ask_price, size=ask_size),
            market_metadata=MarketMetadata(
                timestamp=timestamp,
                sequence_number=base_sequence + i,  # Increment sequence number
                tape=tape
            )
        )
        
        yield quote

def data_producer_coordinator():
    tickers=read_ticker_from_config()
    for initial_quote in fuzzy_data_con.get_quote_data(tickers):
        quote = generate_mock_quotes_from_initial(initial_quote=initial_quote)
        




    
