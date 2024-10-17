import sys
input = sys.stdin.readline

n = int(input())
data = [0]+[int(input()) for _ in range(n)]
dp = [1]*(n+1)

for i in range(1,n+1):
    for j in range(1,i):
        if data[j]<data[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))
