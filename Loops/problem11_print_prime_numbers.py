# Print Prime Numbers in a Range

# logic
# Loop through numbers from start to end.
# For each number, check divisibility from 2 to num-1.
# If divisible → not prime (break).
# If no divisor found → print the number.


start = 25
end = 50

print("Prime numbers between", start, "and", end, "are")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)