# Exercise 10: Positional and keyword arguments

# logic
# Positional values passed in order
# Keyword values passed using parameter names

def describe_pet(animal_type, pet_name):
    print("I have a", animal_type)
    print("My pet name is", pet_name)

# positional arguments
describe_pet("dog", "manya")

# keyword arguments
describe_pet(animal_type="cat", pet_name="mauu")