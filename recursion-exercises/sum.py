# Complete the following Python program to compute the sum 
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively:

def sum(num):

    if num == 1:
        return 1

    elif num == 0:
        return 0

    else:
        return num + sum(num-1)


for _ in range(11):
    print(sum(_))