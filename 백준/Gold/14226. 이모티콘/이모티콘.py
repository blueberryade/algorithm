from collections import deque

n = int(input())
q = deque()
q.append((1,0))
visited = [[-1]*(n+1) for _ in range(n+1)]
visited[1][0] = 0

while q:
    s,c = q.popleft()
    if visited[s][s] == -1:
        visited[s][s] = visited[s][c]+1
        q.append((s,s))
    
    if s+c <= n and visited[s+c][c] == -1:
        visited[s+c][c] = visited[s][c] + 1
        q.append((s+c,c))
    
    if s-1 >= 0 and visited[s-1][c] == -1:
        visited[s-1][c] = visited[s][c] + 1
        q.append((s-1,c))

result = -1
for i in range(1,n+1):
    if visited[n][i] != -1:
        if result == -1 or result > visited[n][i]:
            result = visited[n][i]

print(result)