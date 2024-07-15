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
        parent[a] = b

g = int(input())
p = int(input())
airplane = [int(input()) for _ in range(p)]
parent = [i for i in range(g+1)]
cnt = 0

for i in airplane:
    root = find_parent(i)
    if root == 0:
        break
    
    union_parent(root,root-1)
    cnt+=1

print(cnt)




