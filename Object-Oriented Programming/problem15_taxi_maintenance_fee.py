# Exercise 15: Add maintenance fee using super()

# Logic
# Vehicle stores the base_fare.
# Taxi inherits from Vehicle.
# super().__init__(base_fare) calls the parent constructor.
# total_fare() adds a 10% maintenance fee to the base fare.

class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare


class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)

    def total_fare(self):
        return self.base_fare + (self.base_fare * 0.10)


taxi = Taxi(500)

print("Total fare with maintenance fee:", taxi.total_fare())