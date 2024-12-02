import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
limit = int(input())

dp = [[0]*(N+1) for _ in range(4)]
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1]+data[i-1]


for n in range(1,4):
    for m in range(n*limit,N+1):
        if n == 1:
            dp[n][m] = max(dp[n][m-1],S[m]-S[m-limit])
        else:
            dp[n][m] = max(dp[n][m-1],dp[n-1][m-limit]+S[m]-S[m-limit])

print(dp[3][N])