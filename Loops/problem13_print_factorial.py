# Factorial using for loop

# logic
# Take input from user
# Initialize factorial = 1
# Loop from 1 to n
# Multiply each number with factorial
# Print final result

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "is", factorial)