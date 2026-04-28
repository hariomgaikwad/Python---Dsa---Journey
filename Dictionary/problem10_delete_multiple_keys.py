# Exercise 10: Delete a list of keys

# logic
# Loop through keys to remove
# Use pop(key, None)
# Removes key safely

product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}

keys_to_remove = ["stock", "warehouse"]

for key in keys_to_remove:
    product.pop(key, None)   # avoids error if key not found

print(product)