import sys
input = sys.stdin.readline

def is_safe(row,col):
    for prev_r in range(row):
        if column[prev_r] == col or column[prev_r]-prev_r == col-row or column[prev_r]+prev_r == col+row:
            return False
    return True

def place_queen(row):
    global result
    if row == n:
        result+=1
        return
    for col in range(n):
        if is_safe(row,col):
            column[row] = col
            place_queen(row+1)
            column[row] = -1

n = int(input())
result = 0
column = [-1]*n

place_queen(0)
print(result)