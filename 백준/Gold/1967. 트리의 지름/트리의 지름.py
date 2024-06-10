import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])


def dfs(node,d):
    for next,next_d in tree[node]:
        if visited[next] == -1:
            visited[next] = next_d+d
            dfs(next,next_d+d)

visited = [-1]*(n+1)
visited[1] = 0
dfs(1,0)

temp = visited.index(max(visited))
visited = [-1]*(n+1)
visited[temp] = 0
dfs(temp,0)

print(max(visited))
