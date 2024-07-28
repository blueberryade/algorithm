import sys
input = sys.stdin.readline

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None

def is_valid(board,row,col,num):
    for x in range(9):
        if board[row][x] == num:
            return False
    
    for x in range(9):
        if board[x][col] == num:
            return False
    
    start_row, start_col = 3 * (row//3), 3 * (col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
            
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row,col = empty

    for num in range(1,10):
        if is_valid(board,row,col,num):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0

    return False


board = [list(map(int,input().rstrip())) for _ in range(9)]

solve(board)

for row in board:
    print("".join(map(str,row)))