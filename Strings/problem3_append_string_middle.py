# Exercise 3: Append new string in middle

# logic
# Find middle index of s1
# Split string into two parts
# Add s2 in between

s1 = "Ault"
s2 = "Kelly"

mid = len(s1) // 2

result = s1[:mid] + s2 + s1[mid:]

print(result)