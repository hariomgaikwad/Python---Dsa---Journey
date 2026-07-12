# Exercise 19: Media inheritance

# Logic
# Media is the parent class and stores title and price.
# Book, Magazine, and DVD inherit from Media.
# Each child class has its own extra attribute:
# Book → author
# Magazine → issue
# DVD → duration
# Each class overrides the describe() method to display its own information.

class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

    def describe(self):
        print(f"Book: {self.title} by {self.author} - Rs.{self.price}")


class Magazine(Media):
    def __init__(self, title, price, issue):
        super().__init__(title, price)
        self.issue = issue

    def describe(self):
        print(f"Magazine: {self.title} ({self.issue}) - Rs.{self.price}")


class DVD(Media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration

    def describe(self):
        print(f"DVD: {self.title}, {self.duration} mins - Rs.{self.price}")


book = Book("Clean Code", 499, "Robert C. Martin")
magazine = Magazine("Wired", 150, "Monthly")
dvd = DVD("Inception", 299, 148)

book.describe()
magazine.describe()
dvd.describe()