# Exercise 15: Remove common elements using difference_update()

# logic
# difference_update() removes common elements
# Updates original set directly

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a.difference_update(b)

print("a =", a)