from pos.line_item import LineItem
from pos.order import Order
from pos.system import POSSystem


def main() -> None:
    # create pos system and setup the payment proccessor
    system = POSSystem()
    system.setup_payment_processor("https://api.stripe.com/v2")

    # create the order
    order = Order(
        12345, "Fergus", "Town Street 94", "1456", "London", "fungus@email.com"
        )
    order.create_line_item(LineItem("Keyboard", 1, 5000))
    order.create_line_item(LineItem("SSD", 1, 15000))
    order.create_line_item(LineItem("USB cable", 2, 500))

    # register and process the order
    system.register_order(order)
    system.process_order(order)


if __name__ == '__main__':
    main()
