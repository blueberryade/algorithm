import heapq
INF = int(1e9)

n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
near_trash = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 0,0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            x,y = i,j
        if graph[i][j] == 'g':
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == '.':
                    near_trash[ni][nj] = 1



        
def dijkstra(i,j):
    distance = [[[INF]* m for _ in range(n)] for _ in range(2)]
    q = []
    heapq.heappush(q,(0,0,i,j))
    distance[0][i][j] = 0
    distance[1][i][j] = 0

    while q:
        trash,near,x,y = heapq.heappop(q)

        if graph[x][y] == 'F':
            return trash,near

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            
            if 0<=nx<n and 0<=ny<m:
                new_trash = trash
                new_near = near + near_trash[nx][ny]
                
                if graph[nx][ny]=='g':
                    new_trash+=1
                    
                if new_trash < distance[0][nx][ny] or (new_trash == distance[0][nx][ny] and new_near < distance[1][nx][ny]):
                    distance[0][nx][ny] = new_trash
                    distance[1][nx][ny] = new_near
                    heapq.heappush(q, (new_trash, new_near, nx, ny))


            

print(*dijkstra(x,y))