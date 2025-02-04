def dfs(x):
    visited[x] = True
    next = data[x]

    if not visited[next]:
        dfs(next)
    return


T = int(input())
for _ in range(T):
    N = int(input())
    data = [0]+list(map(int,input().split()))
    visited = [False]*(N+1)
    result = 0

    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            result+=1
    print(result)
