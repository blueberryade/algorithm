N = int(input())

def backtracking(cur):
    if len(cur) == N:
        print(*cur)
        return
    
    for i in range(1,N+1):
        if i not in cur:
            cur.append(i)
            backtracking(cur)
            cur.pop()

backtracking([])

