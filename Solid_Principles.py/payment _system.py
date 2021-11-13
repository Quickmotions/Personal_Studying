# Uncle Bob's Solid Principles Learning (Fergus Haak 23/09/21)

# 1) single responsibility principle, one class should do everything split the responsibilities

# 2) open/closed principle, classes like payment processor shouldn't be edited to
# add new payment types, instead we should create an abstract method which lets us
# make new payment types as a new class rather than editing an existing one

# 3) Liskov substitution principle, payment processor cant have 2 different args stored with same name for example
# paypal payment doesnt use a code it uses an email address. this means we cant use security_code to store that data
# since its a different thing. instead we create an init function in the abstract class which handles the data for each
# payment type and sets the self variables with correct names

# 4) Interface segregation principle, split payment processor interface. for example we added new interface which
# handles sms authorization which is called upon on classes that support it

# 5) dependency inversion,


from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quanitity, price):
        self.items.append(name)
        self.quantities.append(quanitity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def set_status(self, status):
        self.status = status


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):

    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"verifying security code: {self.security_code}")
        order.set_status("paid")


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status("paid")


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing credit payment type")
        print(f"Verifying email address: {self.email_address}")
        order.set_status("paid")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
authorizer = SMSAuth()
processor = DebitPaymentProcessor("02424", authorizer)
authorizer.verify_code(354235)
processor.pay(order)
