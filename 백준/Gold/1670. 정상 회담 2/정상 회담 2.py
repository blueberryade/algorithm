import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*10001
MOD = 987654321
dp[0] = 1
dp[2] = 1
dp[4] = 2*dp[2]

for i in range(6,N+1,2):
    total = 0
    for j in range(0,i//2-1,2):
        total+=dp[j]*dp[i-j-2]*2
    if (i%4==2):
        total+=dp[(i-2)//2]*dp[(i-2)//2]
    dp[i] = total%MOD
print(dp[N])


