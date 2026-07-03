# Exercise 3: Rectangle class with area and perimeter methods

# Logic
# __init__() initializes length and width
# area() returns length × width
# perimeter() returns 2 × (length + width)
# self lets methods access the object's own attributes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 4)

print("Area =", rect.area())
print("Perimeter =", rect.perimeter())