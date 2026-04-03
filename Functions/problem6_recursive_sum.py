# Exercise 6: Recursive sum from 0 to 10

# logic
# base case → n == 0 return 0
# Otherwise → n + recursive_sum(n-1)
# Function keeps calling itself

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print(recursive_sum(10))