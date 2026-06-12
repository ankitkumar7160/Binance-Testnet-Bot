from binance.enums import *
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_market_order(
            self,
            symbol,
            side,
            quantity):

        try:

            logger.info(
                f"MARKET ORDER REQUEST : "
                f"{symbol} {side} {quantity}"
            )

            response = (
                self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            )

            logger.info(
                f"MARKET RESPONSE : {response}"
            )

            return response

        except Exception as e:

            logger.error(str(e))
            raise

    def place_limit_order(
            self,
            symbol,
            side,
            quantity,
            price):

        try:

            logger.info(
                f"LIMIT ORDER REQUEST : "
                f"{symbol} {side} "
                f"{quantity} {price}"
            )

            response = (
                self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )
            )

            logger.info(
                f"LIMIT RESPONSE : {response}"
            )

            return response

        except Exception as e:

            logger.error(str(e))
            raise