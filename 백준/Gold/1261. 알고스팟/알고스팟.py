import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q,(0,0,0))
    distance[0][0] = 0

    while q:
        c,x,y = heapq.heappop(q)

        if c > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                cost = c + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (distance[nx][ny],nx,ny))

                
n,m = map(int,input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,input().rstrip())))
distance = [[INF]*(n) for _ in range(m)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dijkstra()
print(distance[m-1][n-1])

