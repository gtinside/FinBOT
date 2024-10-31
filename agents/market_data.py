import os
import autogen
from integration.polygon_connector import PolygonAPIConnector
from dotenv import load_dotenv

load_dotenv()
llm_config = {"model": "claude-3-sonnet-20240229", "api_key": os.environ["ANTHROPIC_API_KEY"], 
              "api_type": "anthropic"}
polygon_api = PolygonAPIConnector()

stock_price_agent = autogen.AssistantAgent(
    name="StockPriceAgent",
   system_message="""You are a stock price agent. Your task is to fetch historical stock prices for a give ticker and date""",
    llm_config=llm_config,
)


user_proxy_agent = autogen.UserProxyAgent(
    name = "User",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10
)

market_data_coordinator = autogen.GroupChat(
    agents=[user_proxy_agent, stock_price_agent],
    messages=[],
    max_round=3,
    speaker_selection_method="round_robin",
    enable_clear_history=True,
)

group_chat_manager = autogen.GroupChatManager(
    groupchat=market_data_coordinator
)

@user_proxy_agent.register_for_execution()
@stock_price_agent.register_for_llm(description="Function that return current price for a ticker and date")
def get_data(ticker="AAPL", date="2024-10-12"):
    return polygon_api.get_data(ticker, date)

@user_proxy_agent.register_for_execution()
@stock_price_agent.register_for_llm(description="Function that return volume data for a given ticker and a date range")
def get_volume_data(ticker='AAPL', start_date="2023-01-01", end_date="2023-10-30"):
    return polygon_api.get_volume_data(ticker=ticker, from_date=start_date, to_date=end_date)

