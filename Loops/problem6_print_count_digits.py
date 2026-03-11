# Count total number of digits in a number using while loop

# logic
# floor division
# to reduce the last digit from number
# increment counter by 1

num = int(input("Enter a number:"))
count = 0

while num > 0:
    num = num // 10
    count += 1
print("Total Digits are :", count)