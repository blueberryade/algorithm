import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]*(n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for j in range(1,data[1]+1):
        graph[data[j+1]].append(i)
        indegree[i]+=1

q = deque()
result = [0]*(n+1)

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = time[i]

while q:
    now = q.popleft()
    for i in graph[now]:
        result[i] = max(result[i],result[now]+time[i])
        indegree[i]-=1
        if indegree[i] == 0:
            q.append(i) 
print(max(result))           
