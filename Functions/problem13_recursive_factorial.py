# Exercise 13: Recursive factorial

# logic
# Base case → if n == 0 or 1 return 1
# Otherwise → n * factorial(n-1)
# Function calls itself

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
