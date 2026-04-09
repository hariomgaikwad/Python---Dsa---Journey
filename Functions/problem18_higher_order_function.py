# Exercise 18: Higher-order function

# logic
# apply_operation() takes a function as argument
# Calls it using func(x, y)
# Pass different functions (add, sub)

def apply_operation(func, x, y):
    return func(x, y)

# functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# calls
print(apply_operation(add, 10, 5))
print(apply_operation(sub, 10, 5))