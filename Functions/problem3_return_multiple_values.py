# Exercise 3: Return multiple values

# logic 
# Calculate addition and subtraction
# Return both values using return add, sub
# Python returns them as a tuple

def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub

res = calculation(40, 10)
print(res)