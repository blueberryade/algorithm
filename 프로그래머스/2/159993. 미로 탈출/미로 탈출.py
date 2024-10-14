from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    start_x,start_y = 0,0
    lever_x,lever_y = 0,0
    end_x,end_y = 0,0
    
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start_x,start_y = i,j
            if maps[i][j] == 'L':
                lever_x,lever_y = i,j
            if maps[i][j] == 'E':
                end_x,end_y = i,j
                   

    def bfs(x1,y1,x2,y2):
        q = deque()
        q.append((x1,y1))
        visited = [[-1]*m for _ in range(n)]
        visited[x1][y1] = 0
        
        while q:
            x,y = q.popleft()
            
            if x == x2 and y == y2:
                return visited[x][y]
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<n and 0<=ny<m and maps[nx][ny]!='X':
                    if visited[nx][ny] == -1:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y]+1
        return -1
    
    result1 = bfs(start_x,start_y,lever_x,lever_y)
    result2 = bfs(lever_x,lever_y,end_x,end_y)

    if result1 == -1 or result2 == -1:
        return -1
    else:
        return result1+result2
    

