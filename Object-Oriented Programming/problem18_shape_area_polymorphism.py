# Exercise 18: Polymorphism with Shape classes

# Logic
# Shape is the parent class.
# Each child class overrides the area() method.
# Circle: π × r²
# Square: side²
# Triangle: ½ × base × height
# All objects use the same method name (area()), but each calculates the area differently.

import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(7)
square = Square(4)
triangle = Triangle(6, 8)

print("Circle area:", round(circle.area(), 2))
print("Square area:", square.area())
print("Triangle area:", triangle.area())