# Exercise 23: Type checking using isinstance() and issubclass()

# Logic
# isinstance(object, Class) checks whether an object belongs to a class or its parent class.
# issubclass(Child, Parent) checks whether one class inherits from another.
# Both functions understand inheritance, unlike type().

class Animal:
    pass


class Dog(Animal):
    pass


d = Dog()

print("Is d an instance of Dog?", isinstance(d, Dog))
print("Is d an instance of Animal?", isinstance(d, Animal))

print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))