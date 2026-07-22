# Exercise 4: Count occurrence of each element

# Logic
# Create an empty dictionary.
# Check each element in the list.
# If the element already exists, increase its count by 1.
# Otherwise, add it to the dictionary with a count of 1.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict = {}

for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item", count_dict)