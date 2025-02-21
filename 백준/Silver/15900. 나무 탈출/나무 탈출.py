import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False]*(N+1)
arr = [0]*(N+1)
result = 0
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(cur):
    visited[cur] = True
    for i in tree[cur]:
        if not visited[i]:
            arr[i] = arr[cur]+1
            dfs(i)

dfs(1)

for i in range(2,N+1):
    if len(tree[i]) == 1:
        result+=arr[i]

if result%2 == 0:
    print('No')
else:
    print('Yes')
