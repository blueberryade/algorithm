from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    q = deque()
    
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2,r)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1 < i< x2 and y1 < j < y2:
                    graph[i][j] = 0
                    
                elif graph[i][j]!=0:
                    graph[i][j] = 1
    
    cx,cy = 2*characterX, 2*characterY
    ix,iy = 2*itemX,2*itemY

    q.append((cx,cy))
    visited[cx][cy] = 1
    
    while q:
        x,y = q.popleft()
        
        if x == ix and y == iy:
            return visited[x][y] // 2

            
        for d in range(4):
            nx = x +dx[d]
            ny = y +dy[d]
            
            if 0<=nx<102 and 0<=ny<102:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
    
    
    return 0