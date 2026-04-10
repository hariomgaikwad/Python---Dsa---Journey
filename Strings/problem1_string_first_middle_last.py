# Exercise 1A: Create new string from first, middle, last characters

# logic
# First → str1[0]
# Middle → len(str1)//2
# Last → str1[-1]
# Combine al

str1 = "Hariom"

first = str1[0]
middle = str1[len(str1)//2]
last = str1[-1]

result = first + middle + last

print(result)