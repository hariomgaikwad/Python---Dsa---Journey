# Exercise 14: Method overriding using super()

# Logic
# Bus inherits from Vehicle.
# Bus overrides the seating_capacity() method.
# The default capacity is set to 50.
# super().seating_capacity(capacity) calls the parent class
#  method instead of rewriting the logic.

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        super().seating_capacity(capacity)


bus = Bus("School Bus", 120)

bus.seating_capacity()