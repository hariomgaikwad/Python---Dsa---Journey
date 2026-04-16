# Exercise 8: Count all occurrences of "USA" ignoring case

# logic
# Convert string to lowercase using lower()
# Use count("usa") to count occurrences
# Print result

str1 = "Welcome to USA. usa awesome, isn't it?"

count = str1.lower().count("usa")

print("The USA count is:", count)