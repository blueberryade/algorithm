import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [False]*n
min_value = sys.maxsize


def backtracking(depth,idx):
    global min_value

    if depth == n // 2:
        a,b = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a+=board[i][j]
                elif not visited[i] and not visited[j]:
                    b+=board[i][j]
        min_value = min(min_value,abs(a-b))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1,i+1)
            visited[i] = False

backtracking(0,0)
print(min_value)