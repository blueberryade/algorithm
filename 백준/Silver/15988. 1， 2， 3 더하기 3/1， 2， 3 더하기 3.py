import sys
input = sys.stdin.readline

T = int(input())
dp = [1,2,4,7]
for _ in range(T):
    N = int(input())
    for i in range(len(dp),N):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[N-1])
