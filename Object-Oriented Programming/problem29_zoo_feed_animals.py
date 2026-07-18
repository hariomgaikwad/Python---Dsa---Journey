# Exercise 29: Composition + Polymorphism

# Logic
# Animal is the base class.
# Each animal has its own eat() method.
# Zoo stores different animal objects.
# feed_all() calls eat() for every animal.
# Python automatically calls the correct eat() method (polymorphism).

class Animal:
    def eat(self):
        pass


class Lion(Animal):
    def eat(self):
        print("Lion eats meat.")


class Elephant(Animal):
    def eat(self):
        print("Elephant eats grass.")


class Parrot(Animal):
    def eat(self):
        print("Parrot eats seeds.")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        for animal in self.animals:
            animal.eat()


zoo = Zoo()

zoo.add_animal(Lion())
zoo.add_animal(Elephant())
zoo.add_animal(Parrot())

zoo.feed_all()