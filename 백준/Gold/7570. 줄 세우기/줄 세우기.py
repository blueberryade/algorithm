import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

dp = [0]*(max(data)+1)
max_length = 0

for num in data:
    if num > 1:
        dp[num] = dp[num-1]+1
    else:
        dp[num] = 1
    
    max_length = max(max_length,dp[num])

print(N-max_length)