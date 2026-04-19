# Exercise 14: Remove character at index i

# logic
# Take part before index → str1[:i]
# Skip character at i
# Add remaining → str1[i+1:]

str1 = "Python"
i = 2

result = str1[:i] + str1[i+1:]

print(result)