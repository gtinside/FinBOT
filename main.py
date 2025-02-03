from fastapi import FastAPI
from dotenv import load_dotenv
from loguru import logger
from integration.fuzzy_data_connector import FuzzyDataConnector


load_dotenv()
FuzzyDataConnector().get_quote_data()