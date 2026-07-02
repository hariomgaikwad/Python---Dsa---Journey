# Exercise 2: Vehicle class with instance attributes

# Logic
# __init__() is the constructor and runs automatically when an object is created.
# self.name, self.max_speed, and self.mileage are instance attributes.
# Each object stores its own values.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle("Tesla Model S", 250, 18)

print("Vehicle Name:", vehicle1.name)
print("Speed:", vehicle1.max_speed)
print("Mileage:", vehicle1.mileage)