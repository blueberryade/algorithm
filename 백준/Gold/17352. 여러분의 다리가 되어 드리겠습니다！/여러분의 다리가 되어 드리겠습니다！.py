import sys
input = sys.stdin.readline

n = int(input())

def find(x):
    if parent[x]!=x:
        return find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


parent = [i for i in range(n+1)]
for _ in range(n-2):
    a,b = map(int,input().split())
    if find(a)!=find(b):
        union(a,b)


for i in range(2,n+1):
    if find(1)!=find(i):
        print(1,i)
        break