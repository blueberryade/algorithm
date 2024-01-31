n,m = map(int,input().split())
dic = {}
for _ in range(n):
    s,p = input().split()
    dic[s] = p
for _ in range(m):
    s = input()
    print(dic[s])