# Exercise 21: Vehicle class hierarchy

# Logic
# Vehicle is the parent class.
# Bike, Truck, and Bus inherit from Vehicle.
# Each subclass sets its own max_speed using super().__init__().
# Each subclass has its own describe() method to display the speed.

class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed


class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)

    def describe(self):
        print(f"Bike max speed: {self.max_speed} km/h")


class Truck(Vehicle):
    def __init__(self):
        super().__init__(90)

    def describe(self):
        print(f"Truck max speed: {self.max_speed} km/h")


class Bus(Vehicle):
    def __init__(self):
        super().__init__(100)

    def describe(self):
        print(f"Bus max speed: {self.max_speed} km/h")


bike = Bike()
truck = Truck()
bus = Bus()

bike.describe()
truck.describe()
bus.describe()