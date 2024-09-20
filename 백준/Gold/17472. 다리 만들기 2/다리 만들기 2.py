from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs(i,j,num):
    q = deque()
    q.append((i,j))
    graph[i][j] = num
    visited[i][j] = True

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = num
                    q.append((nx,ny))
num = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            bfs(i,j,num)
            num+=1


def find_bridge():
    bridges = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                island_num = graph[i][j]
                for d in range(4):
                    x, y, length = i, j, 0
                    while True:
                        x += dx[d]
                        y += dy[d]
                        if 0 <= x < n and 0 <= y < m:
                            if graph[x][y] == island_num:  
                                break
                            if graph[x][y] > 0 and graph[x][y] != island_num: 
                                if length >= 2: 
                                    bridges.append((length, island_num, graph[x][y]))
                                break
                            if graph[x][y] == 0:  
                                length += 1
                        else:
                            break
    return bridges



def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

bridges = find_bridge()
bridges.sort()
parent = [i for i in range(num)]
result = 0
edge_used = 0

for bridge in bridges:
    cost,a,b = bridge
    if find(a)!= find(b):
        union(a,b)
        result += cost
        edge_used+=1

if result ==0 or edge_used != num-2 :
    print(-1)
else:
    print(result)
