# Exercise 14: Check if sets are disjoint

# logic
# isdisjoint() checks for common elements
# Returns True if no common elements exist

set_a = {1, 2, 3}
set_b = {4, 5, 6}

result = set_a.isdisjoint(set_b)

print("Are the sets disjoint?", result)