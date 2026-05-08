# Exercise 10: Sum of set elements without sum()

# logic
# Create accumulator variable total = 0
# Loop through set elements
# Add each element to total

numbers = {10, 20, 30, 40, 50}

total = 0

for num in numbers:
    total += num

print("Sum:", total)