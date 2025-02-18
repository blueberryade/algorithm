from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K,M,P = map(int,input().split())
    graph = [[] for _ in range(M+1)]
    indegree = [0]*(M+1)
    arr = [[] for _ in range(M+1)]

    for _ in range(P):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    q = deque()

    for i in range(1,M+1):
        if indegree[i]== 0:
            q.append(i)
            arr[i] = [1,0]
    
    while q:
        now = q.popleft()
        order = arr[now][0]+arr[now][1]
        for next in graph[now]:
            indegree[next]-=1
            if not arr[next] or arr[next][0]<order:
                arr[next] = [order,0]
            elif arr[next][0] == order:
                arr[next][1] = 1
            
            if indegree[next] == 0:
                q.append(next)
                
    print(K,sum(arr[M]))