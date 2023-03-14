class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __add__(self, other):
        name = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        transactions = self._transactions + other._transactions
        return Account(name, amount).add_transactions(transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def handle_transaction(self, transaction_amount):
        balance = self.balance + transaction_amount
        if balance < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(transaction_amount)
            return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        balance = self.balance + amount
        if balance < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(amount)
            return f"New balance: {self.balance}"

    def add_transactions(self, transactions):
        self._transactions.extend(transactions)
        return self

    @property
    def balance(self):
        return self.amount + sum(self._transactions)


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
