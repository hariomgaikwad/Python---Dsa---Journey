# Exercise 8: Initialize dictionary with default values

# logic
# Use dict.fromkeys(keys, default)
# Assigns same value to all keys

keys = ["math", "science", "english", "history"]
default = 0

result = dict.fromkeys(keys, default)

print(result)