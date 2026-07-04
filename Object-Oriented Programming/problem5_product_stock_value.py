# Exercise 5: Product class with total stock value

# Logic
# __init__() stores name, price, and quantity
# total_value() returns price × quantity
# :.2f formats the result to 2 decimal places

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


p1 = Product("Laptop", 899.99, 5)

print(f"Total stock value of {p1.name}: ${p1.total_value():.2f}")