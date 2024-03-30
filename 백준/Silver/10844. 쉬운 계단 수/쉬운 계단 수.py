import sys
input = sys.stdin.readline

N = int(input())
D = [[0 for j in range(11)] for i in range(N+1)]

for i in range(1,10):
    D[1][i] = 1

for i in range(2,N+1):
    D[i][0] = D[i-1][1]
    D[i][9] = D[i-1][8]
    for j in range(1,9):
        D[i][j] = (D[i-1][j-1]+D[i-1][j+1]) % 1000000000
sum = 0

for i in range(10):
    sum = (sum+D[N][i]) % 1000000000

print(sum)