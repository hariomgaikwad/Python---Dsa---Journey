# Exercise 20: Discounted Order using inheritance

# Logic
# Order is the parent class and stores order_id and total.
# DiscountedOrder inherits from Order.
# super().__init__() initializes the parent class attributes.
# discounted_total() calculates a 10% discount:
# total × 0.90

class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total


class DiscountedOrder(Order):
    def __init__(self, order_id, total):
        super().__init__(order_id, total)

    def discounted_total(self):
        return self.total * 0.90


order = DiscountedOrder("ORD001", 1200)

print("Order ID:", order.order_id)
print("Original Total:", order.total)
print("Discounted Total:", order.discounted_total())