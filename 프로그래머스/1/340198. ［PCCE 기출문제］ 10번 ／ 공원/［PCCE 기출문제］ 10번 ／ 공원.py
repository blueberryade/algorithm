def solution(mats, park):
    n = len(park)
    m = len(park[0])
    dp = [[0]*m for _ in range(n)]
    max_len = 0
    
    for i in range(n):
        for j in range(m):
            if park[i][j]== '-1':
                dp[i][j] = 1

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                max_len = max(max_len,dp[i][j])
    answer = -1
    
    for i in mats:
        if i <= max_len:
            answer = max(answer,i)

    return answer