# Problem: Function with variable number of arguments

# Logic:
# 1. Use *args to accept multiple values
# 2. Print heading
# 3. Loop through args and print each

def func1(*args):
    print("Printing values")
    for i in args:
        print(i)

# Function calls
func1(20, 40, 60)
func1(80, 100)