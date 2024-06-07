import heapq
INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dijkstra():
    q = []
    q.append((graph[0][0],0,0))
    distance[0][0] = graph[0][0]

    while q:
        c,x,y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print(f'Problem {test}: {distance[x][y]}')

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
   
            if 0<=nx<n and 0<=ny<n:
                 cost = c + graph[nx][ny]
                 if cost < distance[nx][ny]:
                     distance[nx][ny] = cost
                     heapq.heappush(q,(cost,nx,ny))

test = 1                 
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    distance = [[INF]*n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    dijkstra()
    test+=1
