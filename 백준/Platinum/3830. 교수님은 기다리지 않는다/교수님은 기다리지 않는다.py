import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x]!=x:
        root = find(parent[x])
        weight[x] += weight[parent[x]]
        parent[x] = root
    return parent[x]

def union(a,b,w):
    root_a,root_b = find(a),find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        weight[root_b] = weight[a]-weight[b]+w

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    weight = [0]*(n+1)

    for _ in range(m):
        data = input().split()
        if data[0] == '!':
            a,b,w = map(int,data[1:])
            union(a,b,w)
        else:
            a,b = map(int,data[1:])
            if find(a)==find(b):
                print(weight[b]-weight[a])
            else:
                print('UNKNOWN')

