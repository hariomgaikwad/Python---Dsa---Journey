# Exercise 17: Keep non-common elements using symmetric_difference_update()

# logic
# symmetric_difference_update() keeps non-common elements
# Removes shared values and updates original set

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a.symmetric_difference_update(b)

print("a =", a)