# Exercise 12: Update set with multiple iterables

# logic
# update() accepts multiple iterables
# Adds all unique elements into set

base = {1, 2}
from_list = [3, 4]
from_tuple = (5, 6)
from_set = {7, 8}

base.update(from_list, from_tuple, from_set)

print("Updated set:", base)