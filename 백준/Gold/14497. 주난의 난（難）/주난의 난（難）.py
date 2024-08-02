import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
distance = [[INF]*m for _ in range(n)]


def dijkstra(x1,y1):
    q = []
    heapq.heappush(q,(0,x1,y1))
    distance[x1][y1] = 0

    while q:
        cnt,x,y = heapq.heappop(q)

        if distance[x][y] < cnt:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                cost = cnt+(graph[nx][ny]!='0')
                if cost<distance[nx][ny]:
                    heapq.heappush(q,(cost,nx,ny))
                    distance[nx][ny] = cost

dijkstra(x1-1,y1-1)
print(distance[x2-1][y2-1])