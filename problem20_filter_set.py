# Exercise 20: Filter elements divisible by 3

# logic
# Use set comprehension
# Check condition num % 3 == 0
# Store only divisible-by-3 numbers in a new set

numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}

divisible_by_3 = {num for num in numbers if num % 3 == 0}

print("divisible_by_3 =", divisible_by_3)