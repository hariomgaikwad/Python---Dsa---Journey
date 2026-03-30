# Exercise 9: Right-aligned output

# logic
# {word:>20} → right-align text in width of 20
# > means right alignment
# Then print number after it


word = input("Enter a word: ")
num = float(input("Enter a number: "))

print(f"{word:>20} {num}")