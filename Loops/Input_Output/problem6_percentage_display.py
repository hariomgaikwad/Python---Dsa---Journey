# Exercise 8: Calculate and display percentage

# logic
# Calculate → (num / den) * 100
# Use :.2f to format 2 decimal places
# Add % symbol in print

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

percentage = (num / den) * 100

print(f"The result is: {percentage:.2f}%")