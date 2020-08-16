board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board1 = [
    [0,0,0,0,0,0,6,8,0],
    [0,0,0,0,7,3,0,0,9],
    [3,0,9,0,0,0,0,4,5],
    [4,9,0,0,0,0,0,0,0],
    [8,0,3,0,5,0,9,0,2],
    [0,0,0,0,0,0,0,3,6],
    [9,6,0,0,0,0,3,0,8],
    [7,0,0,6,8,0,0,0,0],
    [0,2,8,0,0,0,0,0,0]
]

def PrintBoard(board):
    for row in range(len(board)):
        if row % 3 == 0:
            print(' -- -- -- -- -- -- -- -- -- ')

        for col in range(len(board[row])):
            if col % 3 == 0:
                print(' | ', end='')
            print(str(board[row][col]) + ' ',  end='')
        print('\n')

def FindEmpty(board): 
    # returns locations of blank spaces in board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)
    return None 

def Valid(board, num, pos):

    # Check similar numbers per row
    for col in range(len(board)):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Check similar numbers per col
    for row in range(len(board)):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    return True

def Solve(board):

    find = FindEmpty(board)

    if not find:
        return True

    else:
        row, col = find

        for num in range(1, 10):
            if Valid(board, num, (row, col)):
                board[row][col] = num

                if Solve(board):
                    return True    

                board[row][col] = 0

    return False

        
PrintBoard(board)
print(FindEmpty(board1))
print(Solve(board1))