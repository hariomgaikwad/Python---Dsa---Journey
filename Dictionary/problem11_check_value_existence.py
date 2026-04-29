# Exercise 11: Check if value exists in dictionary

# logic
# Use roles.values() to get all values
# Use in to check existence

roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}

print("editor exists:", "editor" in roles.values())
print("manager exists:", "manager" in roles.values())

