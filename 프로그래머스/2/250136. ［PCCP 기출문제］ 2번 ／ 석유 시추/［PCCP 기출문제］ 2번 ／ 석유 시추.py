from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    
    visited = [[False]*m for _ in range(n)]
    result = [0 for i in range(m)]
    
    def bfs(i,j):
        q = deque()    
        cnt = 0
        visited[i][j] = True
        q.append((i,j))
        min_y,max_y = j,j
        
        while q:
            x,y = q.popleft()
            min_y = min(min_y,y)
            max_y = max(max_y,y)
            cnt+=1
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    if land[nx][ny] == 1 and not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True
                        
        for i in range(min_y,max_y+1):
            result[i]+=cnt
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                
    answer = max(result)
        
    return answer