# Exercise 18: Count chars, digits, symbols

str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for ch in str1:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Total counts of chars, digits, and symbols:")
print("Chars =", chars, "Digits =", digits, "Symbol =", symbols)