import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]

def check(start_color):
    dp = [[0]*(M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0:
                v = (board[i][j]!=start_color)
            else:
                v = (board[i][j] == start_color)
            
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + v
    
    min_changes = sys.maxsize
    for i in range(1,N-K+2):
        for j in range(1,M-K+2):
            total = dp[i+K-1][j+K-1] - dp[i+K-1][j-1] - dp[i-1][j+K-1] + dp[i-1][j-1]
            min_changes = min(min_changes,total)
    
    return min_changes

result = min(check('B'),check('W'))
print(result)