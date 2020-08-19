def miniMaxSum(arr):

    arr1 = arr.copy()
    arr.remove(max(arr))
    arr1.remove(min(arr1))

    max_sum = sum(arr1)
    min_sum = sum(arr)

    print(max_sum, min_sum)

arr = [1,3,5,7,9]
miniMaxSum(arr)