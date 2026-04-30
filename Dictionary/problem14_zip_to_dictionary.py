# Exercise 14: Map two lists using zip

# logic
# zip(attributes, details) → pairs elements
# dict() → converts to dictionary

attributes = ["brand", "model", "year", "color"]
details = ["Honda", "Civic", 2023, "silver"]

result = dict(zip(attributes, details))

print(result)