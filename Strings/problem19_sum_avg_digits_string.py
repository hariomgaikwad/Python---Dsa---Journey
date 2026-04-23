# Exercise 20: Sum and average of digits in a string

# logic
# Check digit using isdigit()
# Add digits to total
# Count digits
# Average = total / count

str1 = "PYnative29@#8496"

total = 0
count = 0

for ch in str1:
    if ch.isdigit():
        total += int(ch)
        count += 1

average = total / count

print("Sum is:", total, "Average is", round(average, 2))