import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def is_connected(district):
    visited = [False]*n
    q = deque()
    q.append(district[0])
    visited[district[0]] = True
    count = 1
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor in district  and not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                count+=1
    
    return count == len(district)

def population_difference():
    min_diff = INF

    for i in range(1,n//2+1):
        for c in combinations(range(n),i):
            group_a = list(c)
            groub_b = [x for x in range(n) if x not in group_a]

            if is_connected(group_a) and is_connected(groub_b):
                pop_a = sum(population[j] for j in group_a)
                pop_b = sum(population[j] for j in groub_b)
                min_diff = min(min_diff,abs(pop_a-pop_b))
    return min_diff      


n = int(input())
population = list(map(int,input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int,input().split()))
    graph[i] = [x-1 for x in data[1:]]


result = population_difference()


if result == INF:
    print(-1)
else:
    print(result)