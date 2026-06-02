# Exercise 18: Remove multiple items from a set

# logic
#  difference_update() removes all elements found in another set
# Updates the original set directly
# Useful for bulk removal operations

items = {10, 20, 30, 40, 50, 60}
to_remove = {20, 40, 60}

items.difference_update(to_remove)

print("items =", items)

