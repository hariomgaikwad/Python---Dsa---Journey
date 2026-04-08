# Exercise 16: Double elements using lambda and map

# logic
# map() applies function to each element
# lambda x: x * 2 → doubles value
# Convert to list using list()

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))

print("The doubled numbers are:", doubled)