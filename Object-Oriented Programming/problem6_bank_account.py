# Exercise 6: BankAccount class

# Logic
# deposit() adds money to the balance.
# withdraw() checks if sufficient balance is available.
# If enough balance exists → deduct the amount.
# Otherwise → print "Insufficient funds" and keep the balance unchanged.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)
        else:
            print("Insufficient funds. Current balance:", self.balance)


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)