# Exercise 15: Count character frequencies

# logic
# Loop through each character
# Use dictionary to store counts
# get(ch, 0) → default value

text = "hello world"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)