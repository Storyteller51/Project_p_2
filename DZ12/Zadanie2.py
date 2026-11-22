class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Зачем снимаешь отрицательную сумму, чудик???")
        if amount > self._balance:
            raise ValueError("МАЛО грошей")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

account = BankAccount("Никитос", 1000)

print(account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(300)
print(account.balance)     # 1200

#account.withdraw(5000)