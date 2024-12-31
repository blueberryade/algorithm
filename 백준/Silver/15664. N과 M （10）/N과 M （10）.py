N,M = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
arr = []
visited = [False]*N

def backtracking(idx):
    if len(arr) == M:
        print(*arr)
        return
    
    remember = 0
    for i in range(idx,N):
        if not visited[i] and remember!=data[i]:
            arr.append(data[i])
            visited[i] = True
            remember = data[i]
            backtracking(i)
            visited[i] = False
            arr.pop()
            

backtracking(0)
