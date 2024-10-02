import copy

n,m = map(int,input().split())
cctv = []
graph = []

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    for j in range(m):
        if 0<row[j]<6:
            cctv.append((row[j],i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = {
    1:[[0],[1],[2],[3]],
    2:[[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}
def fill(graph,d,x,y):
    for i in d:
        nx = x
        ny = y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny]==0:
                graph[nx][ny] = -1


def dfs(depth,graph):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count+=graph[i].count(0)
        min_value = min(min_value,count)
        return
    
    temp = copy.deepcopy(graph)
    num,x,y = cctv[depth]
    for i in direction[num]:
        fill(temp,i,x,y)
        dfs(depth+1,temp)
        temp = copy.deepcopy(graph)
    
min_value = int(1e9)
dfs(0,graph)
print(min_value)
