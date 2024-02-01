import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        a,b = input().split()
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    cnt = 1
    for k in dic:
        cnt*= len(dic[k])+1
    print(cnt-1)
