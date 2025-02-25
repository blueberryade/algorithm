from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

kmax = 0 
length = N 

while length != 0: 
    length //= 2
    kmax += 1

depth = [0]*(N+1)
visited = [False]*(N+1)
parent = [[0 for _ in range(N+1)] for _ in range(kmax+1)]
distance = [0]*(N+1)

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        cur = q.popleft()
        for next_node,dist in tree[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                parent[0][next_node] = cur
                depth[next_node] = depth[cur]+1
                distance[next_node] = distance[cur]+dist

bfs(1)

for k in range(1, kmax + 1):
    for n in range(1, N + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]

def LCA(a,b):
    if depth[a] > depth[b]:  
        a,b = b,a
    for k in range(kmax,-1,-1):
        if pow(2,k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]
    
    for k in range(kmax,-1,-1):
        if a == b:
            break
        if parent[k][a]!=parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    
    return a if a==b else parent[0][a]

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    lca = LCA(a,b)
    print(distance[a]+distance[b]-2*distance[lca])