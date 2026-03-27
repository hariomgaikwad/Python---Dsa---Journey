#  Hexadecimal representation of a number

# logic
# Use hex() to convert decimal → hexadecimal
# [2:] removes 0x prefix

num = int(input("Enter a number: "))

print("The hexadecimal value is", hex(num)[2:])