n,m = map(int,input().split())

def backtrack(cur):
    if len(cur) ==m:
        print(*cur)
        return
    for i in range(1,n+1):
        cur.append(i)
        backtrack(cur)
        cur.pop()

backtrack([])

