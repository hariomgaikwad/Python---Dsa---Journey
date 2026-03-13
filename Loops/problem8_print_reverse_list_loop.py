# Write a Python program to print a list in reverse order using a loop.
# Given
# list1 = [10, 20, 30, 40, 50]

# logic
# get list size
# len(list1) -1 because index start with 0
# iterate list in reverse order
# star from last item to first

list1 = [10, 20, 30, 40, 50]

size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])