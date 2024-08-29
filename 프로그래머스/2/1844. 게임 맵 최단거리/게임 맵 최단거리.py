from collections import deque

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    def bfs(i,j):
        visited = [[0]*c for _ in range(r)]
        q = deque()
        q.append((i,j))
        visited[i][j] = 1
        
        while q:
            x,y = q.popleft()
            if x == r-1 and y == c-1:
                return visited[r-1][c-1]
            
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                
                if 0<=nx<r and 0<=ny<c and maps[nx][ny]!=0:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx,ny))
                        
                    
        
        return -1
    
    answer = bfs(0,0)
    
    return answer