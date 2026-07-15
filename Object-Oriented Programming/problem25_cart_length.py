# Exercise 25: Overload len() using __len__

# Logic
# items stores the list of cart items.
# __len__() tells Python what to return when len(cart) is called.
# len(cart) automatically calls cart.__len__().

class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


cart = Cart(["apple", "banana", "mango"])

print("Number of items in cart:", len(cart))