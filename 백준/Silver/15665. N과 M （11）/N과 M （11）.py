N,M = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
cur = []

def backtracking():
    if len(cur) == M:
        print(*cur)
        return
    
    remember = 0
    for i in range(N):
        if remember!=data[i]:
            cur.append(data[i])
            remember = data[i]
            backtracking()
            cur.pop()
            

backtracking()
