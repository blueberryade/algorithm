N = int(input())
data = list(map(int,input().split()))

result = 0
visited = [False]*N

def bactracking(cur):
    global result

    if len(cur) == N:
        total = 0
        for i in range(N-1):
            total+= abs(cur[i]-cur[i+1])
        result = max(result,total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            cur.append(data[i])
            bactracking(cur)
            visited[i] = False
            cur.pop()

bactracking([])
print(result)
