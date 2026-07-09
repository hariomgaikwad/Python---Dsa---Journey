# Exercise 13: Inheritance

# Logic
# Vehicle is the parent class.
# Bus is the child class that inherits from Vehicle.
# Since Bus doesn't add anything new, we use pass.
# The Bus object can use the display() method inherited from Vehicle.

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")


class Bus(Vehicle):
    pass


bus1 = Bus("School Bus", 120)

bus1.display()