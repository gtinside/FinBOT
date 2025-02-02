from fastapi import FastAPI
from loguru import logger
from integration.fuzzy_data_connector import FuzzyDataConnector



FuzzyDataConnector().get_quote_data()