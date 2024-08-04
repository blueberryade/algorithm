import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    visited = [[-1]*(w+2) for _ in range(h+2)]
    q = deque()
    q.append((i,j))
    visited[i][j] = 0

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<h+2 and 0<=ny<w+2:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] =='.' or graph[nx][ny] =='$':
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx,ny))
                    elif graph[nx][ny] == '#':
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx,ny))
    return visited


t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    graph = [list('.'*(w+2))]
    for _ in range(h):
        graph.append(list('.'+input().rstrip()+'.'))
    graph.append(list('.'*(w+2)))

    prisonsers = []
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j] == '$':
                prisonsers.append((i,j))   
    prisonser1,prisonser2 = prisonsers
 
    outer = bfs(0,0)
    p1 = bfs(prisonser1[0],prisonser1[1])
    p2 = bfs(prisonser2[0],prisonser2[1])

    result = INF

    for i in range(h+2):
        for j in range(w+2):
            if outer[i][j]!=-1 and p1[i][j]!=-1 and p2[i][j]!=-1:
                total_cost = outer[i][j]+p1[i][j]+p2[i][j]
                if graph[i][j] == '*':
                    continue
                if graph[i][j] == '#':
                    total_cost-=2
                result = min(result,total_cost)


    print(result)