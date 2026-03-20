# Reverse an Integer Number

# logic
# Get last digit using num % 10
# Add it to reversed number → rev = rev * 10 + digit
# Remove last digit using num // 10
# Repeat until number becomes 0

num = 76542
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)