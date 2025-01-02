import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

result = sys.maxsize
visited = [False]*N
total = 0

def dfs(cnt,x):
    global result,total

    if cnt == N-1:
        if data[x][0]:
            total+=data[x][0]
            if total < result:
                result = total
            total -= data[x][0]
        return  

    
    for i in range(1,N):
        if not visited[i] and data[x][i]:
            visited[i] = True
            total+=data[x][i]
            dfs(cnt+1,i)
            visited[i] = False
            total-=data[x][i]

dfs(0,0)
print(result)