def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-2]
        dp[i]%=1000000007
    
    return dp[n]