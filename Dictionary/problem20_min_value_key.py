# Exercise 20: Find key with minimum value

# logic
# min() finds smallest key
# key=stock.get → compare values
# Returns key with minimum value
    
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

min_key = min(stock, key=stock.get)

print("Lowest stock item:", min_key)