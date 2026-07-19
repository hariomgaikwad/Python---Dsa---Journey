# Exercise 2: Remove and add item in a list

# Logic
# pop(4) removes and returns the element at index 4.
# insert(2, item) adds the removed element at index 2.
# append(item) adds the same element to the end of the list.

list1 = [54, 44, 27, 79, 91, 41]

# Remove item at index 4
item = list1.pop(4)
print("List After removing element at index 4", list1)

# Add removed item at index 2
list1.insert(2, item)
print("List after Adding element at index 2", list1)

# Add the same item at the end
list1.append(item)
print("List after Adding element at last", list1)