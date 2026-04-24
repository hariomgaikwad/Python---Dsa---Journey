# Exercise 2: Remove key, get items, check key existence

# logic
# pop("color") → removes key
# items() → returns all key-value pairs
# "key" in dict → checks existence

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

# remove key
car.pop("color")

# print updated dictionary
print(car)

# get all key-value pairs
print(car.items())

# check key existence
print("'brand' exists:", "brand" in car)
print("'color' exists:", "color" in car)