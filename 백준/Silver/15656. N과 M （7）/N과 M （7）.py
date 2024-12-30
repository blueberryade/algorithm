N,M = map(int,input().split())
data = list(map(int,input().split()))

arr = []
data.sort()

def backtracking():
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(N):
        arr.append(data[i])
        backtracking()
        arr.pop()

backtracking()