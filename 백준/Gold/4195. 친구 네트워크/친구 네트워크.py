import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a
        num[a]+=num[b]
    print(num[a])

t = int(input())

for _ in range(t):
    f = int(input())
    parent = {}
    num = {}
    for i in range(f):
        a,b = input().split()
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1

        union_parent(a,b)
