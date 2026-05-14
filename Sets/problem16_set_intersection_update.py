# Exercise 16: Keep common elements using intersection_update()

# logic
# intersection_update() keeps only common elements
# Original set gets modified directly

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a.intersection_update(b)

print("a =", a)