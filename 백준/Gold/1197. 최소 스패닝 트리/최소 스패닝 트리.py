import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
q = []
parent = [i for i in range(N+1)]

for i in range(M):
    q.append(list(map(int,input().split())))
    
q.sort(key=lambda x:x[2])

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a

result = 0

for s,e,w in q:
    if find(s)!=find(e):
        union(s,e)
        result+=w

print(result)
