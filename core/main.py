import autogen
from loguru import logger
from fastapi import FastAPI
from agents.market_data import market_data_coordinator, user_proxy_agent, stock_price_agent

group_chat_manager = autogen.GroupChatManager(
    groupchat=market_data_coordinator
)
app = FastAPI()

@app.post("/chat")
def send_message(message: str):
    logger.info("Message Received {}", message)
    response = user_proxy_agent.initiate_chat(group_chat_manager, message=message)
    return response
