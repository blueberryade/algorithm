import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[-1,-1] for _ in range(n+1)]
is_root = [True]*(n+1)
current_x = 0

for _ in range(n):
    p,left,right = map(int,input().split())
    tree[p][0] = left
    tree[p][1] = right
    if left!= -1:
        is_root[left] = False
    if right!=-1:
        is_root[right] = False

root_node = is_root[1:].index(True)+1
level_list = [[] for _ in range(n+1)]

def inorder(cur,level):
    global current_x
    if cur == -1:
        return
    if tree[cur][0]!= -1:
        inorder(tree[cur][0],level+1)
    current_x+=1
    level_list[level].append(current_x)
    if tree[cur][1]!=-1:
        inorder(tree[cur][1],level+1)


inorder(root_node,1)

max_distance = 0
max_level = 0

for level in range(1,n+1):
    if not level_list[level]:
        break
    dist = level_list[level][-1] - level_list[level][0] +1
    if dist > max_distance:
        max_distance = dist
        max_level = level
print(max_level,max_distance)        