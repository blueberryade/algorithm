from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
        
    distance = [-1]*(n+1)
    
    q = deque() 
    q.append(1)
    distance[1] = 0

    while q:
        now = q.popleft()

        for i in graph[now]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[now]+1
        
    for d in distance:
        if d == max(distance):
            answer+=1
    return answer