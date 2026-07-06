# Create a custom exception
class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient Balance")
        self.balance = self.balance - amount
        print("Remaining Balance:", self.balance)

        
account = BankAccount(5000)
try:
    account.withdraw(6000)
except InsufficientBalanceError as e:
    print(e)