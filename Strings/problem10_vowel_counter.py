# Exercise 10: Count vowels in a string

# logic
# Convert string to lowercase
# Loop through each character
# Check if it is in "aeiou"
# Increase count

str1 = "Hello World"

count = 0

for ch in str1.lower():
    if ch in "aeiou":
        count += 1

print("Vowel Count:", count)