# Exercise 14: Accept 5 float numbers and store in list

# logic 
# Create empty list numbers
# Use loop to take 5 inputs
# Convert to float and store using append()
# Print list

numbers = []

for i in range(5):
    num = float(input("Enter number: "))
    numbers.append(num)

print(numbers)