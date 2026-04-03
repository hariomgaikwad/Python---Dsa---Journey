# Exercise 5: Inner function

# logic
# define inner() inside outer()
# inner() returns sum of a + b
# Outer adds 5 to result
# Return final value

def outer(a, b):
    
    def inner(x, y):
        return x + y
    
    result = inner(a, b)
    return result + 5

# function call
print(outer(10, 5))