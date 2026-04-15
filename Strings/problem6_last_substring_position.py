# Exercise 6: Find last position of substring

# logic
# Use rfind() to search from right side
# It returns last index of substring

str1 = "Emma is a data scientist who knows Python. Emma works at google."

index = str1.rfind("Emma")

print("Last occurrence of Emma starts at index", index)