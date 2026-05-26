# Exercise 11: Add multiple elements to set using update()

# logic
# update() adds multiple elements
# Duplicate values are ignored automatically

fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango", "apple"]

fruits.update(new_fruits)

print("Updated set:", fruits)