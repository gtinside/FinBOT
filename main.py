from fastapi import FastAPI
from dotenv import load_dotenv
from loguru import logger
from producer.data_generator import data_producer_coordinator


load_dotenv()
data_producer_coordinator()
