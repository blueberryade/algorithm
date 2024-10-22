import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
result = -1

def isSqrt(x):
    return int(math.sqrt(int(x))) ** 2 == int(x)

for i in range(n):
    for j in range(m):
        for row_d in range(-n,n):
            for col_d in range(-m,m):
                tmp = ''
                x,y = i,j
                if row_d == 0 and col_d == 0:
                    continue
                while 0<= x < n and 0 <= y < m:
                    tmp += str(graph[x][y])
                    if isSqrt(tmp):
                        result = max(result,int(tmp))
                    x+= row_d
                    y+= col_d

print(result)
