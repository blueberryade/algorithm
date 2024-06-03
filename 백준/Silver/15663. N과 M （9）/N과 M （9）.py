import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
visited = [False]*n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != data[i]:
            visited[i] = True
            temp.append(data[i])
            remember = data[i]
            dfs()
            visited[i] = False
            temp.pop()


dfs()
