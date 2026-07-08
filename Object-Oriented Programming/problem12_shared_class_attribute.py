# Exercise 12: Class attribute shared by all objects

# Logic
# color is a class attribute, so it is shared by all Vehicle objects.
# name and speed are instance attributes, so each object has its own values.
# Initially, both vehicles have the color White.
# When Vehicle.color is changed to Red, the change is reflected in both 
# objects because they share the same class attribute.

class Vehicle:
    color = "White"   # Class attribute

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(f"{self.name} - Color: {Vehicle.color}, Speed: {self.speed}")


v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

v1.display()
v2.display()

# Change class attribute
Vehicle.color = "Red"

v1.display()
v2.display()