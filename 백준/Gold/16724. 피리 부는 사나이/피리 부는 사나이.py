n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

result = 0

def dfs(x,y):
    global result
    visited[x][y] = True
    cycle.append((x,y))

    if graph[x][y] == 'U' and x > 0:
        x-=1
    elif graph[x][y] == 'D' and x < n-1:
        x+=1
    elif graph[x][y] == 'L' and y > 0:
        y-=1
    elif graph[x][y] == 'R' and y < m-1:
        y+=1
    
    if visited[x][y]:
        if (x,y) in cycle:
            result+=1
    else:
        dfs(x,y)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cycle = []
            dfs(i,j)
            
print(result)            

