# Exercise 11: Check URL validity

# logic
# startswith("https") → checks prefix
# endswith(".com") → checks suffix
# Use and to combine both conditions

str1 = "https://google.com"

result = str1.startswith("https") and str1.endswith(".com")

print("Is valid URL:", result)