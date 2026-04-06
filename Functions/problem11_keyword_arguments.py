# Exercise 11: Function with keyword arguments

# logic
# Use **kwargs to accept multiple keyword arguments
# Loop through kwargs.items()
# Print key and value

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# function call
print_info(name="Hariom", age=18, city="Pune")