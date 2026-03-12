# Write a Python program to print the following reverse number pattern using a for loop

# Pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# logic
# Set n = 5 for the number of rows.
# Use an outer for loop from n to 1.
# Use an inner for loop from i to 1 to print numbers in reverse.
# Use print() to move to the next line after each row.

n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()