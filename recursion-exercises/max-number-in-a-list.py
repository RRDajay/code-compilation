# Write a recursive Python function that has a
# parameter representing a list of integers and returns the maximum
# stored in the list. Thinking recursively, the maximum is either the
# first value in the list or the maximum of the rest of the list,
# whichever is larger. If the list only has 1 integer, then its maximum
# is this single value, naturally. 

def maxValue(arr):
    
    if len(arr) == 1:
        return arr[0]

    else:
        m = maxValue[arr[1:]]
        return m if m > arr[0] else arr[0]

arr = [1, 10, 19, 8, 19]

print(maxValue(arr))