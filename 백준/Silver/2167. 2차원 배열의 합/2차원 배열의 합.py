import sys
input= sys.stdin.readline

n,m = map(int,input().split())
arr = [[0]*(m+1)]
S = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    tmp = [0]+list(map(int,input().split()))
    arr.append(tmp)

for i in range(1,n+1):
    for j in range(1,m+1):
        S[i][j] = S[i][j-1]+S[i-1][j]-S[i-1][j-1] + arr[i][j]


k = int(input())
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    result = S[x2][y2]-S[x1-1][y2]-S[x2][y1-1]+S[x1-1][y1-1]
    print(result)            
                                                               