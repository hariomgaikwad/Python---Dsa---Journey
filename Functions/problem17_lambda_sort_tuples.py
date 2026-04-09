# Exercise 17: Sort list of tuples by second element

# logic
# sorted() sorts the list
# key=lambda x: x[1] → sort using second element
# Returns new sorted list

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

sorted_data = sorted(data, key=lambda x: x[1])

print("The sorted list of tuples based on the second element is:", sorted_data)