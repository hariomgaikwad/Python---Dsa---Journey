# Exercise 22: Identify object's class using type()

# Logic
# type(object) returns the object's class.
# .__name__ returns only the class name as a string.
# This helps identify the type of an object during runtime.

class Dog:
    pass


class Cat:
    pass


class Vehicle:
    pass


d = Dog()
c = Cat()
v = Vehicle()

print("d is of type:", type(d).__name__)
print("c is of type:", type(c).__name__)
print("v is of type:", type(v).__name__)