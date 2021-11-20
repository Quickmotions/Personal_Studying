from dataclasses import dataclass, field
from Transaction_Ground_Truth.banking.transaction import Transaction


@dataclass
class BankController:
    undo_stack: list[Transaction] = field(default_factory=list)
    redo_stack: list[Transaction] = field(default_factory=list)
    ledger: list[Transaction] = field(default_factory=list)
    current: int = 0

    def register(self, transaction: Transaction) -> None:
        # remove future transactions from ledger
        del self.ledger[self.current:]
        self.ledger.append(transaction)
        self.current += 1

    def undo(self) -> None:
        if self.current > 0:
            self.current -= 1
        if not self.undo_stack:
            return
        transaction = self.undo_stack.pop()
        transaction.undo()
        self.redo_stack.append(transaction)

    def redo(self) -> None:
        if self.current < len(self.ledger):
            self.current += 1
        if not self.redo_stack:
            return
        transaction = self.redo_stack.pop()
        transaction.redo()
        self.undo_stack.append(transaction)

    def compute_balances(self) -> None:
        for transaction in self.ledger[: self.current]:
            transaction.execute()