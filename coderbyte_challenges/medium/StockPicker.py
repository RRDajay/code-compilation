def StockPicker(arr):

    min_value = arr[0]
    max_difference = 0

    for i in range(len(arr)):

        if (arr[i] < min_value):
            min_value = arr[i]

        elif (arr[i] - min_value > max_difference):
            max_difference = arr[i] - min_value

    return max_difference

        
# keep this function call here 
arr = [10,12,4,5,9]

print(StockPicker(arr))