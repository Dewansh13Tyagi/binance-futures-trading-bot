import argparse
import logging
from bot.logging_config import setup_logging
from bot.validators import validate_order_args
from bot.orders import place_order

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser("Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--order-type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order_args(args)

        print("\nOrder Request Summary")
        print(vars(args))

        response = place_order(
            args.symbol,
            args.side,
            args.order_type,
            args.quantity,
            args.price
        )

        print("\nOrder Placed Successfully")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        logger.exception("Order failed")
        print("Order Failed:", e)

if __name__ == "__main__":
    main()