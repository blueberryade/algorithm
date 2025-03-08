import sys
input = sys.stdin.readline

N,L = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

result = 0
def check(line):
    visited = [False for _ in range(N)]
    for i in range(1,N):
        if abs(line[i-1]-line[i]) > 1:
            return False
        else:
            if line[i-1]>line[i]:
                for j in range(L):
                    if i+j>=N:
                        return False
                    if line[i]!=line[i+j]:
                        return False
                    if visited[i+j]:
                        return False
                    if not visited[i+j]:
                        visited[i+j] = True
            elif line[i-1]<line[i]:
                for j in range(L):
                    if i-1-j<0:
                        return False
                    if line[i-1]!=line[i-1-j]:
                        return False
                    if visited[i-1-j]:
                        return False
                    if not visited[i-1-j]:
                        visited[i-1-j] = True
    return True
                    
for i in graph:
    if check(i):
        result+=1
for j in range(N):
    if check([graph[i][j] for i in range(N)]):
        result+=1


print(result)