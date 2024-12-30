N,M = map(int,input().split())
data = list(map(int,input().split()))

arr = []
data.sort()

def backtracking(start):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(start,N):
        if not data[i] in arr:
            arr.append(data[i])
            backtracking(i+1)
            arr.pop()

backtracking(0)