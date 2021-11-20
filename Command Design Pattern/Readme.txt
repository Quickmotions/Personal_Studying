This Repo contains 2 different types of command Design Pattern examples.

(The examples are of a banking system which
calls on commands to be executed in order
to perform transactions on users accounts)

--------

Using States as the Truth:

This uses account balances as the ground truth. meaning that the actual values of the balances.
states what is real and is the confirmed accurate data.

This uses commands to undo commands to actually change the account balance and store past transactions
so that they can be redone.

transactions are executed as the program runs so the balances are constantly changing/holding the ground truth

--------

Using Transaction Log as the Truth:

This uses the past transactions list as the truth rather than the actual account balances.
meaning that everything that has occurred in the transactions totals up to the confirmed accurate data.#

This uses a ledger which stores all transactions. undo and redo just move the current location in the
ledger rather than actually undoing or redoing that command. When a new item is added to the ledger
all future transactions which were undone are deleted.

When computing the final balances. only the transactions which are up to the current index of the ledger are
executed.



Sources (guides) by ArjanCodes
- https://www.youtube.com/watch?v=FM71_a3txTo
- https://www.youtube.com/watch?v=rGu33Tk0tCM