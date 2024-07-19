import sys
input = sys.stdin.readline

def find(x):
    while x!=parent[x]:
        x = parent[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    
    parent[a] = b
    cost[b] = min(cost[a],cost[b])
        

n,m,k = map(int,input().split())
parent = [i for i in range(n+1)]
cost = [0]+ list(map(int,input().split()))

for _ in range(m):
    v,w = map(int,input().split())
    union(v,w)

result = 0

for i in range(1,n+1):
    if parent[i] == i:
        result+=cost[i]

if result > k:
    print('Oh no')
else:
    print(result)