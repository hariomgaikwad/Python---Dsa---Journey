# Exercise 4: Create new string from first, middle, last chars

# logic
# Take first char of both strings
# Take middle char of both strings
# Take last char of both strings
# Join all together

s1 = "America"
s2 = "Japan"

result = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]

print(result)