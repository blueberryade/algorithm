n,k = map(int,input().split())
data = []
dp = [[0]*(k+1) for _ in range(n+1)]
for _ in range(n):
    data.append(list(map(int,input().split())))  

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= data[i-1][0]:
            dp[i][j] = max(data[i-1][1]+dp[i-1][j-data[i-1][0]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
