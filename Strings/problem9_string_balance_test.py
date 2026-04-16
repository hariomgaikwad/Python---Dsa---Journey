# Exercise 9: Check if strings are balanced

# logic
# Loop through each character in s1
# Check if it exists in s2
# If any missing → False
# Else → True

def string_balance(s1, s2):
    for char in s1:
        if char not in s2:
            return False
    return True

# test cases
print(string_balance("yn", "Pynative"))
print(string_balance("ynf", "PyNative"))