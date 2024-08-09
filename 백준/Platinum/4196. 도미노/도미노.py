import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node,graph,visited,queue):
    visited[node] = 1

    for next_node in graph[node]:
        if visited[next_node] == 0:
            dfs(next_node,graph,visited,queue)
    queue.append(node)

def make_queue(n,graph,visited):
    queue = []

    for node in range(1,n+1):
        if visited[node] == 0:
            dfs(node,graph,visited,queue)

    return queue

def reverse_dfs(node,graph,visited,graph_indegree,cnt):
    visited[node] = 1
    graph_indegree[node] = cnt

    for next_node in graph[node]:
        if visited[next_node] == 0:
            reverse_dfs(next_node,graph,visited,graph_indegree,cnt)
    

def check_scc(queue,graph,visited,graph_indegree):
    cnt = 0

    while queue:
        node = queue.pop()
        if visited[node] == 0:
            cnt+=1
            reverse_dfs(node,graph,visited,graph_indegree,cnt)
    return cnt
        

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)

    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        reverse_graph[y].append(x)
    
    queue = make_queue(n,graph,visited)
    visited = [0]*(n+1)
    graph_indegree = [0]*(n+1)

    cnt = check_scc(queue,reverse_graph,visited,graph_indegree)
    scc_indegree = [0]*(cnt+1)

    for idx in range(1,n+1):
        for parent in graph[idx]:
            if not (graph_indegree[idx] == graph_indegree[parent]):
                scc_indegree[graph_indegree[parent]] +=1
    
    result = 0
    for node in range(1,len(scc_indegree)):
        if scc_indegree[node] == 0:
            result+=1
    print(result)



