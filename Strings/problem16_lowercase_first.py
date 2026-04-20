# Exercise 17: Arrange lowercase first, then uppercase

# logic
# Separate lowercase and uppercase
# Join → lowercase + uppercase

str1 = "PyNaTive"

lower = ""
upper = ""

for ch in str1:
    if ch.islower():
        lower += ch
    else:
        upper += ch

result = lower + upper

print(result)