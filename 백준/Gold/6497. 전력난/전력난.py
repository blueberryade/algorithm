import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
while True:
    v,e = map(int,input().split())
    if v == 0 and e == 0:
        break

    parent = [0] * (v+1)
    edges = []
    result = 0
    total = 0

    for i in range(1,v+1):
        parent[i] = i

    for _ in range(e):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))

    edges.sort()

    for edge in edges:
        cost,a,b  = edge
        total += cost
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result+=cost
    print(total-result)