# Exercise 8: Find non-common elements in sets

# logic
# symmetric_difference() returns non-common elements
# Removes elements present in both sets

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.symmetric_difference(set_b)

print("Symmetric Difference:", result)