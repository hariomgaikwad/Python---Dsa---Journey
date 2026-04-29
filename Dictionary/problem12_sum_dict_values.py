# Exercise 12: Sum all values in dictionary

# logic
# Use values() to get all numbers
# Use sum() to add them

expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}

total = sum(expenses.values())

print("Total expenses:", total)