import os
import logging
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()
logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def create_order(self, **kwargs):
        logger.info(f"Order request: {kwargs}")
        response = self.client.futures_create_order(**kwargs)
        logger.info(f"Order response: {response}")
        return response