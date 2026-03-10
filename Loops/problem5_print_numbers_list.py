# Display numbers from the list that satisfy the conditions:
# 1. Number must be divisible by 5
# 2. If number > 150, skip it
# 3. If number > 500, stop the loop

# Expected Output:
# 75
# 150
# 145

# logic
# iterate each item of a list
# check if number is divisible by 5

numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:

    if item > 500:
        break

    elif item > 150:
        continue

    elif item % 5 == 0:
        print(item)