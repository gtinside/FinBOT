from pydantic import BaseModel
from typing import Dict
from enum import Enum, IntEnum

class TapeEnum(IntEnum):
    NYSE =  1
    AMEX = 2
    Nasdaq = 3


class BidAskData(BaseModel):
    exchange_id: int
    price: float
    size: int


class MarketMetadata(BaseModel):
    timestamp: int
    sequence_number: int
    tape: int


class MarketQuote(BaseModel):
    event_type: str
    ticker: str
    bid: BidAskData
    ask: BidAskData
    market_metadata: MarketMetadata