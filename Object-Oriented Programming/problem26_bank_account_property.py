# Exercise 26: Encapsulation using @property

# Logic
# __balance is a private attribute, so it cannot be accessed directly.
# @property creates a getter to safely read the balance.
# @balance.setter creates a setter to safely update the balance.
# The setter checks that the new balance is not negative before updating it.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid balance. Must be non-negative.")


account = BankAccount(1000)

print("Current balance:", account.balance)

account.balance += 500
print("Current balance:", account.balance)

account.balance = -200