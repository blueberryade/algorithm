from collections import deque

def solution(n, computers):
    
    def bfs(i):
        q = deque()
        q.append(i)

        while q:
            x = q.popleft()
            visited[x] = True
            for i in range(n):
                if computers[x][i] and not visited[i]:
                    q.append(i)
                
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer+=1
        
    return answer