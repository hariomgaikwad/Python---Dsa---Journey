# Exercise 12: Modify global variable

# logic
# Declare variable outside → global
# Use global keyword inside function
# Modify its value

global_var = 10

def modify():
    global global_var
    global_var = 20

modify()
print(global_var)