# Exercise 4: Function with default argument

# logic
# Set default value → salary=9000
# If salary not passed → default is used
# Otherwise given value is used

def showEmployee(name, salary=9000):
    print("Name:", name, "salary:", salary)

# function calls
showEmployee("Ben", 12000)
showEmployee("Jessa")