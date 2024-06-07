import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
    for i in range(n):
        for start,end,time in edges:
            if distance[end] > distance[start] + time:
                distance[end] = distance[start] + time
                if i == n-1:
                    return True
    return False

tc = int(input())

for _ in range(tc):
    n,m,w = map(int,input().split())
    edges = []
    distance = [INF]*(n+1)
    for _ in range(m):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))

    if bf():
        print("YES")
    else:
        print("NO")

