import sys
input = sys.stdin.readline


sudoku = [list(map(int,input().split())) for _ in range(9)]
empty_positions = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def check(x,y,num):
    for i in range(9):
        if sudoku[x][i] == num or sudoku[i][y] == num:
            return False
        
    start_x, start_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[start_x+i][start_y+j]== num:
                return False
    return True

def dfs(idx):
    if idx == len(empty_positions):
        return True

    x,y = empty_positions[idx]
    for num in range(1,10):
        if check(x,y,num):
            sudoku[x][y] = num
            if dfs(idx+1):
                return True
            sudoku[x][y] = 0

    return False


dfs(0)
for i in sudoku:
    print(*i)
