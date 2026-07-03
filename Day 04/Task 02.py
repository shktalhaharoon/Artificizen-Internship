class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New Balance:", self.balance)

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Remaining Balance:", self.balance)

        else:
            print("Insufficient Balance")

account = BankAccount(5000)
account.deposit(1000)
account.withdraw(2000)
account.withdraw(5000)