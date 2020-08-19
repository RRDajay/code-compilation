def simpleArraySum(array):

    acc_sum = 0

    for num in array:
        acc_sum += num

    return acc_sum


arr = [1,2,3]
print(simpleArraySum(arr))
