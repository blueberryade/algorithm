import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic_num = {}
dic_name = {}

for i in range(1,n+1):
    temp = input().strip()
    dic_num[i] = temp
    dic_name[temp] = i

for _ in range(m):
    x = input().strip()
    if x.isdigit():
        print(dic_num[int(x)])
    else:
        print(dic_name[x])