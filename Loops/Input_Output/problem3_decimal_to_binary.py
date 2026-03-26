# Binary representation of a number

# logic 
# Use bin() to convert decimal → binary
# [2:] removes 0b prefix

num = int(input("Enter a number: "))

print("The binary representation of", num, "is", bin(num)[2:])