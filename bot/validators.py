def validate_order_args(args):
    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if args.order_type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")