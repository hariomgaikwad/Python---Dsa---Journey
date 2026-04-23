# Exercise 21: Count occurrences of all characters

# logic
# Use dictionary to store counts
# get(ch, 0) → default 0
# Increase count for each character

str1 = "apple"

freq = {}

for ch in str1:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)