# Exercise 3: Create dictionary from two lists

# logic
# zip(keys, values) → pairs elements
# dict() → converts pairs into dictionary

keys = ["name", "age", "city"]
values = ["Raj", 25, "India"]

result = dict(zip(keys, values))

print(result)