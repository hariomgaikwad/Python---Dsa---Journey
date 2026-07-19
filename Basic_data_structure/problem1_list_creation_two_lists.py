# Exercise 1: Create a new list using two lists

# Logic
# l1[1::2] gets elements at odd indexes.
# l2[0::2] gets elements at even indexes.
# Combine both lists using the + operator.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_index = l1[1::2]
even_index = l2[0::2]

l3 = odd_index + even_index

print("Element at odd-index positions from list one")
print(odd_index)

print("Element at even-index positions from list two")
print(even_index)

print("\nPrinting Final third list")
print(l3)