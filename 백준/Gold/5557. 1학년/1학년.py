N = int(input())
data= list(map(int,input().split()))

dp = [[0]*21 for _ in range(N-1)]
dp[0][data[0]]=1

for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j+data[i] <= 20:
                dp[i][j+data[i]]+=dp[i-1][j]
            if j-data[i] >=0:
                dp[i][j-data[i]]+=dp[i-1][j]

print(dp[-1][data[-1]])