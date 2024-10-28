import os
import autogen
from integration.polygon_connector import PolygonAPIConnector
from dotenv import load_dotenv

load_dotenv()
llm_config = {"model": "claude-3-sonnet-20240229", "api_key": os.environ["ANTHROPIC_API_KEY"]}
polygon_api = PolygonAPIConnector()

stock_price_agent = autogen.AssistantAgent(
    name="StockPriceAgent",
    system_message="You are a stock price agent and can fetch stock price for a ticker for any given date",
    llm_config=llm_config,
)

stock_price_agent.register_function(
    function_map={
        "get_stock_price": polygon_api.get_data
    }
)

user_proxy_agent = autogen.UserProxyAgent(
    name = "User",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10
)

market_data_coordinator = autogen.GroupChat(
    agents=[user_proxy_agent, stock_price_agent]
)




class MarketDataCoordinator:
    def __init__(self):
        pass

class StockPriceAgent:
    def __init__(self) -> None:
        pass

class HighFrequencyTradingAgent:
    def __init__(self) -> None:
        pass

class VolumeAnalysisAgent:
    def __init__(self) -> None:
        pass

class OrderBookAgent:
    def __init__(self) -> None:
        pass

class MarketIndexAgent:
    def __init__(self) -> None:
        pass

class OptionsDataAgent:
    def __init__(self) -> None:
        pass
