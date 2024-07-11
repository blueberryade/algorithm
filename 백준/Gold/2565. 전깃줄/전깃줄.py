n = int(input())
dp  = [1]*n
data = []

for _ in range(n):
    a,b = map(int,input().split())
    data.append([a,b])

data.sort()

for i in range(1,n):
    for j in range(0,i):
        if data[j][1]<data[i][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))

