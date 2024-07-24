import sys
sys.setrecursionlimit(1000000)

t = int(input())

def dfs(i):
    global result
    visited[i] = True
    team.append(i)
    select = selected[i]

    if visited[select]:
        if select in team:
            result+=len(team[team.index(select):])
    else:
        dfs(select)


for _ in range(t):
    n = int(input())
    selected = [0]+list(map(int,input().split()))
    visited = [False]*(n+1)
    result = 0
    for i in range(1,n+1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n-result)
