from dataclasses import dataclass

currency_prefix = "£"


@dataclass
class Item:

    def __init__(self):
        """Creates blank storage for item details"""
        self.item_name = []
        self.price = []

    def add_item(self, item_name: str, price: float):
        """appends a new item to the item class"""
        self.item_name.append(item_name)
        self.price.append(price)

    def show_item(self, name):
        """shows the item data from item name"""
        try:
            index = self.item_name.index(name)
        except ValueError:
            print(f"Error: Item {name} not in items.")
        else:
            print(f"{self.item_name[index]}, "
                  f"{self.price[index]}")

    def all_item_names(self) -> list:
        """returns all item names in items class"""
        return self.item_name

    def length(self) -> int:
        """returns the length of item class"""
        return len(self.item_name)

    def append_new(self, item_name):
        price = input(f"Enter the price for {item_name} as a float: ")
        self.item_name.append(item_name)
        self.price.append(price)


class Storage:

    def __init__(self):
        """Creates lists for storage of all items in storage"""
        self.items = []
        self.quantities = []

    def add_stock(self, item_list, item: str, amount: int):
        """Adds a new item and quantity to storage"""
        if item in item_list.all_item_names():
            self.items.append(item)
            self.quantities.append(amount)
        else:
            item_list.append_new(item)

    def update_stock(self, item_list, balance, item: str, change: int):
        """changes the value of an item in storage"""
        try:
            index = self.items.index(item)
        except ValueError:
            print(f"Error: Item {item} not in Storage.")
        else:
            previous = self.quantities[index]
            new = previous + change
            self.quantities[index] = new
            print(f"Updated {self.items[index]} from {previous} to {new}")
            print(f"Change in Balance: {currency_prefix}{find_balance_change(item_list, balance, item, change)}")


class Balance:

    def __init__(self, starting_balance: float):
        """Sets the balance to a specified starting balance"""
        self.balance = starting_balance

    def change_balance(self, change: float):
        """Changes the value of the balance"""
        self.balance += change

    def get_balance(self, should_print: bool = False) -> float:
        """returns the balance or prints it if specified"""
        if should_print:
            print(f"Your Balance: {currency_prefix}{self.balance}")
        else:
            return self.balance


def find_balance_change(item_list, balance, item_name: str, change: int) -> float:
    """Calculates the loss/profit of a change in storage item amount"""
    index = item_list.all_item_names().index(item_name)
    price = item_list.price[index]
    change_in_bal = round(price * change, 2)
    balance.change_balance(change_in_bal)
    return change_in_bal


item_list = Item()
item_list.add_item('Bag', 450.0)
item_list.add_item('Chair', 41.0)
item_list.show_item('Bag')
item_list.show_item('Human')

balance = Balance(1000.0)

storage = Storage()
storage.add_stock(item_list, 'Bag', 1000)
storage.update_stock(item_list, balance, 'Bag', -10)
storage.update_stock(item_list, balance, 'Bag', 26)
storage.update_stock(item_list, balance, 'Help', 1)

balance.get_balance(True)
