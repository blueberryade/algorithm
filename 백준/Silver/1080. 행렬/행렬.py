N,M = map(int,input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]


def check(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0

result = 0

if (N < 3 or M < 3) and A !=B:
    result = -1
else:
    for r in range(N-2):
        for c in range(M-2):
            if A[r][c] != B[r][c]:
                result+=1
                check(r,c)
if result!=-1:
    if A!=B:
        result = -1
print(result)