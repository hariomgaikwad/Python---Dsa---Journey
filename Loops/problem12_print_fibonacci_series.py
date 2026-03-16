# Display Fibonacci series up to 10 terms

# logic
# Start with a = 0 and b = 1.
# Print a.
# Next number = a + b.
# Update values: a = b, b = next.

n = 10

a = 0
b = 1

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    c = a + b 
    a = b
    b = c

