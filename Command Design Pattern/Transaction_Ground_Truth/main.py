from Transaction_Ground_Truth.banking.bank import Bank
from Transaction_Ground_Truth.banking.controller import BankController
from Transaction_Ground_Truth.banking.commands import Deposit, Withdrawal, Transfer, Batch


def main() -> None:
    bank = Bank()

    controller = BankController()

    # create accounts
    account1 = bank.create_account("Fergus")
    account2 = bank.create_account("Paul")
    account3 = bank.create_account("Simon")

    controller.register(Deposit(account1, 100000))

    controller.register(
        Batch(
            commands=[
                Deposit(account2, 100000),
                Deposit(account3, 100000),
                ]
            )
        )
    controller.undo()
    controller.undo()
    controller.redo()
    controller.redo()

    # transfer
    controller.register(Transfer(from_account=account2, to_account=account1, amount=50000))

    # withdrawal
    controller.register(Withdrawal(account1, 150000))
    controller.undo()

    controller.compute_balances()
    print(bank)


if __name__ == "__main__":
    main()
