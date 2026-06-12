from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


class BinanceClient:

    def __init__(self):

        if not API_KEY or not API_SECRET:
            raise ValueError(
                "BINANCE_API_KEY or BINANCE_API_SECRET missing in .env"
            )

        self.client = Client(
            API_KEY,
            API_SECRET,
            testnet=True
        )

    def get_client(self):
        return self.client