# Exercise 13: Access element from nested tuple

# logic
# matrix[1] → second tuple (4, 5, 6)
# matrix[1][2] → third element 6

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[1][2])