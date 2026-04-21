# Exercise 19: Create mixed string using alternating characters

# logic
# Traverse s1 from start and s2 from end
# Add characters alternately
# Append remaining characters at end

s1 = "Abc"
s2 = "Xyz"

result = ""

i = 0
j = len(s2) - 1

while i < len(s1) and j >= 0:
    result += s1[i] + s2[j]
    i += 1
    j -= 1

# add remaining characters (if any)
result += s1[i:] + s2[:j+1]

print(result)