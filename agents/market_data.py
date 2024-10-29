import os
import autogen
from integration.polygon_connector import PolygonAPIConnector
from dotenv import load_dotenv

load_dotenv()
llm_config = {"model": "claude-3-sonnet-20240229", "api_key": os.environ["ANTHROPIC_API_KEY"], "api_type": "anthropic"}
polygon_api = PolygonAPIConnector()

stock_price_agent = autogen.AssistantAgent(
    name="StockPriceAgent",
   system_message="""You are a stock price agent. Your task is to fetch historical stock prices by invoking the `get_stock_price` function when provided with a ticker symbol and date. Call `get_stock_price(ticker, date)` directly whenever a user asks for a stock price.""",
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
    agents=[user_proxy_agent, stock_price_agent],
    messages=[]
)

group_chat_manager = autogen.GroupChatManager(
    groupchat=market_data_coordinator
)