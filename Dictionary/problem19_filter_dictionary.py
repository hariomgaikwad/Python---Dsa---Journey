# Exercise 19: Filter dictionary based on condition

# logic
# Use dictionary comprehension
# Check condition → value > 60
# Keep only matching pairs

scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

result = {key: value for key, value in scores.items() if value > 60}

print(result)