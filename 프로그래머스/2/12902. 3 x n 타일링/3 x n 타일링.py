def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[2] = 3
    dp[4] = 11
    
    for i in range(6,n+1):
        if i%2 != 0:
            dp[i] = 0
        else:
            dp[i] = dp[i-2]*3+2
            for j in range(i-4,-1,-2):
                dp[i] += dp[j] * 2
            dp[i] = dp[i]%1000000007
    
    return dp[n]