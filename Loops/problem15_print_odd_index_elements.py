# Print elements at odd index positions

# logic

# Index starts from 0
# Odd indexes 
# Use range(1, len(list), 2)
# Print elements at those indexes

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list), 2):
    print(my_list[i], end=" ")