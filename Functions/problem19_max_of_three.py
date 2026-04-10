
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input
a = 10
b = 25
c = 15

# Function call
result = find_max(a, b, c)

print("Maximum number is:", result)