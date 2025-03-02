import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N+1)]
result = 0
q = []
for _ in range(M):
    a,b,c = map(int,input().split())
    q.append((a,b,c))
    result+=c

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

cnt = 0

for a,b,c in q:
    if find(a)!=find(b):
        union(a,b)
        result-=c

for i in range(1,N+1):
    if i == parent[i]:
        cnt+=1

if cnt > 1:
    print(-1)
else:
    print(result)