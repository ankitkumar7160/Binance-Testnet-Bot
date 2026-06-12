import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import *

def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(
            args.side
        )

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        client = (
            BinanceClient()
            .get_client()
        )

        manager = OrderManager(
            client
        )

        print("\nORDER SUMMARY")
        print("-" * 40)

        print(
            f"Symbol : {symbol}"
        )

        print(
            f"Side : {side}"
        )

        print(
            f"Type : {order_type}"
        )

        print(
            f"Quantity : {quantity}"
        )

        if order_type == "MARKET":

            response = (
                manager.place_market_order(
                    symbol,
                    side,
                    quantity
                )
            )

        else:

            if not args.price:
                raise ValueError(
                    "Price required for LIMIT order"
                )

            response = (
                manager.place_limit_order(
                    symbol,
                    side,
                    quantity,
                    args.price
                )
            )

        print("\nSUCCESS")

        print(
            f"Order ID : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Average Price : "
            f"{response.get('avgPrice')}"
        )

    except Exception as e:

        print(
            f"\nFAILED : {str(e)}"
        )

if __name__ == "__main__":
    main()