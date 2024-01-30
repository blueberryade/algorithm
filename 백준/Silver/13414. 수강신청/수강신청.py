import sys
input = sys.stdin.readline

k,l = map(int,input().split())
dic = {}
for i in range(l):
    s = input().rstrip()
    dic[s] = i

result = sorted(dic.items(),key=lambda x: x[1])

for i in range(k):
    if i < len(result):
        print(result[i][0])
    else:
        break