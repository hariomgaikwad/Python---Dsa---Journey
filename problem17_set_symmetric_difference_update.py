# Exercise 17: Keep non-common elements

# logic
# symmetric_difference_update() keeps only non-common elements
# Removes shared values and updates the original set

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a.symmetric_difference_update(b)

print("a =", a)