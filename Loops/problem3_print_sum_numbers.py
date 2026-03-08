# Write a Python program to accept a number from 
# a user and calculate the sum of all numbers from 1 to the given number.

# logic
# s: store sum of all numbers
# run loop n times
# stop: n+1
# add current number to sum variable

num = int(input("Enter number: "))
total = 0

for i in range(1, num + 1):
    total += i

print("Sum is:", total)