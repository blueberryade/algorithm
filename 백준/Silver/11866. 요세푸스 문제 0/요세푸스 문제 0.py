import sys

input = sys.stdin.readline

n,k = map(int,input().split())
idx = 0
queue = [i for i in range(1,n+1)]
lst = []
while queue:
    idx += k -1
    if idx >= len(queue):
        idx %= len(queue)
    lst.append(str(queue.pop(idx)))

print('<',', '.join(lst),'>',sep='')

