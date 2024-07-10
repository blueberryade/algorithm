import sys
input = sys.stdin.readline

n = int(input())
MOD = 1000000000
BIT_RANGE = 1 << 10
NUM_RANGE = 10

dp = [[[0] * BIT_RANGE for _ in range(NUM_RANGE)] for _ in range(n + 1)]

for i in range(1,NUM_RANGE):
    dp[1][i][1<<i] = 1

for i in range(1,n):
    for j in range(NUM_RANGE):
        for k in range(BIT_RANGE):
            if j > 0:
                next = k | 1 << (j-1)
                dp[i+1][j-1][next] += dp[i][j][k]
                dp[i+1][j-1][next]%=MOD
            if j < 9:
                next = k | 1 << (j+1)
                dp[i+1][j+1][next] += dp[i][j][k]
                dp[i+1][j+1][next]%=MOD

result = 0
for i in range(NUM_RANGE):
    result+= dp[n][i][BIT_RANGE-1]
    result%=MOD
    
print(result)


