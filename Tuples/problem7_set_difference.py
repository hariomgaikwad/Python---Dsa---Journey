# Exercise 7: Find elements present in A but not in B

# logic
# difference() removes common elements
# Returns only unique elements from Set A

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.difference(set_b)

print("Difference (A - B):", result)