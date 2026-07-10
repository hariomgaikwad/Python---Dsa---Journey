# Exercise 16: Polymorphism using method overriding

# Logic
# Animal is the parent class.
# Dog and Cat inherit from Animal.
# Both classes override the speak() method.
# Calling speak() gives different results depending on the object.

class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())