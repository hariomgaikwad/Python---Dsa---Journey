# Exercise 3: Find length of set without len()

# logic
# Loop through each element
# Increase counter
# Final count = length

animals = {"cat", "dog", "bird", "fish"}

count = 0

for item in animals:
    count += 1

print("Length of set:", count)