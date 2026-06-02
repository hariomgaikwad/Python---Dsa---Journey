# Exercise 19: Pop element and handle empty set

# logic
# pop() removes and returns a random element from the set
# Calling pop() on an empty set raises KeyError
# Use try-except to handle the error safely

s = {100, 200, 300}

print("Popped:", s.pop())

s = set()

try:
    s.pop()
except KeyError:
    print("Error: pop from an empty set")