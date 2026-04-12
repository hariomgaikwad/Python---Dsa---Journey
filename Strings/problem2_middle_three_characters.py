# Exercise 2: Get middle three characters

# logic
# Find middle index → len(str1)//2
# Slice from mid-1 to mid+2
# This gives middle 3 characters

str1 = "JhonDipPeta"

mid = len(str1) // 2

result = str1[mid - 1 : mid + 2]

print(result)