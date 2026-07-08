# Exercise 11: CoffeeMachine class

# Logic
# __init__() stores available water, coffee, and milk.
# make_latte() checks if:
# Water ≥ 200 ml
# Coffee ≥ 20 g
# Milk ≥ 150 ml
# If resources are enough:
# Deduct the required amounts.
# Print the remaining resources.
# Otherwise:
# Print "Not enough resources to make a latte."

class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_latte(self):
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            self.water -= 200
            self.coffee -= 20
            self.milk -= 150

            print(f"Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
        else:
            print("Not enough resources to make a latte.")


machine = CoffeeMachine(300, 100, 200)

machine.make_latte()
machine.make_latte()