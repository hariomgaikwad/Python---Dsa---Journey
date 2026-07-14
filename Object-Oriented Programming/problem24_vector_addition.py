# Exercise 24: Operator overloading using __add__

# Logic
# __add__() overloads the + operator.
# When v1 + v2 is executed:
# x = 2 + 4 = 6
# y = 3 + 1 = 4
# __str__() defines how the object is displayed when printed.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)

result = v1 + v2

print(result)