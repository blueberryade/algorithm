import sys
input = sys.stdin.readline

def find_parent(x):
    while x!=parent[x]:
        x = parent[x]
    return x

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,input().split())
parent = [i for i in range(n)]
result = 0

for i in range(1,m+1):
    a,b = map(int,input().split())
    if find_parent(a) == find_parent(b):
        result = i
        break
    union_parent(a,b)

print(result)