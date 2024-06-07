n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

def backtrack(cur):
    if len(cur) == m:
        print(*cur)
        return
    for num in data:
        if num not in cur:
            cur.append(num)
            backtrack(cur)
            cur.pop()


backtrack([])
    