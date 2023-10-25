table = [list(map(int,input().split())) for _ in range(9)]

maxNum = 0
r =0
c =0
for row in range(9):
    for col in range(9):
        if maxNum <= table[row][col]:
            r = row+1
            c = col+1
            maxNum = table[row][col]
print(maxNum)
print(r,c)
            