import sys
input = sys.stdin.readline

dic = {}
n,m = map(int,input().split())
for _ in range(n):
    g = input().rstrip()
    c = int(input())
    dic[g] = []
    for _ in range(c):
        dic[g].append(input().rstrip())
    dic[g].sort()

for _ in range(m):
    name = input().rstrip()
    if int(input()) == 1:
        for t,m in dic.items():
            if name in m:
                print(t)
                break
    else:
        for i in dic[name]:
            print(i)