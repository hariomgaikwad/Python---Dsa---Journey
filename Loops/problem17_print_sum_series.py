# Sum of series

# logic

# first number of sequence
# run loop n times
 # calculate the next term

terms = 5
num = 2
sum_seq = 0

for i in range(0, terms):
    print(num, end="+")
    sum_seq += num
    num = num * 10 + 2
print("\nSum of above series is:", sum_seq)