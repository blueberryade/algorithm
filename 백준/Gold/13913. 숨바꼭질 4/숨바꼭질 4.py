from collections import deque

n,k = map(int,input().split())
dist = [0]*100001
check = [0]*100001

def move(now):
    data = []
    tmp = now
    for _ in range(dist[now]+1):
        data.append(tmp)
        tmp = check[tmp]
    print(' '.join(map(str,data[::-1])))


def bfs():
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()
        if now == k:
            print(dist[now])
            move(now)
            return
        
        for next_node in (now-1,now+1,now*2):
            if 0<=next_node<=100000 and dist[next_node]==0:
                dist[next_node] = dist[now]+1
                q.append(next_node)
                check[next_node] = now

bfs()


