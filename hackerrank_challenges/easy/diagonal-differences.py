def diagonalDifferences(arr):

    # first diagonal rows and cols [0][0],[1][1],[2][2], ...[n][n]
    # second diagonal rows and cols [0][2], [1][1], [2][0]
    
    fd_sum, sd_sum = 0, 0
    n = len(arr)

    for i in range(len(arr)):
        fd_sum += arr[i][i]
        sd_sum += arr[i][n-1-i]
    
    return abs(fd_sum - sd_sum)

arr = [
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]

diagonalDifferences(arr)

print('')