# Exercise 1: Basic set operations

# logic
# add() → adds element
# remove() → removes (error if not present)
# discard() → removes safely (no error)

fruits = {"apple", "banana", "cherry"}

# add element
fruits.add("mango")
print(fruits)

# remove element
fruits.remove("banana")
print("after remove,", fruits)

# discard element (no error if not present)
fruits.discard("banana")
print("after discard,", fruits)