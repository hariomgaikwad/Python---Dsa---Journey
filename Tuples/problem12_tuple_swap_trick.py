# Exercise 12: Swap values using tuple unpacking

# logic
# Python packs values into tuple internally
# Tuple unpacking swaps values without temp variable

a = 100
b = 200

a, b = b, a

print("After swap: a =", a, ", b =", b)