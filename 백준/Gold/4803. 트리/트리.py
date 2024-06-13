import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node,parent):
    visited[node] = True
    is_tree = True
    for i in graph[node]:
        if not visited[i]:
            if not dfs(i,node):
                is_tree = False
        elif i!=parent:
            is_tree = False
    return is_tree
            


test = 1
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            if dfs(i,-1):
                cnt+=1

    if cnt == 0:
        print(f"Case {test}: No trees.")
    elif cnt ==1:
        print(f"Case {test}: There is one tree.")
    else:
        print(f"Case {test}: A forest of {cnt} trees.")
    test+=1
