n = int(input())

dic = {}

for _ in range(n):
    name,work = input().split()
    if work == 'enter':
        dic[name] = 'enter'
    else:
        del dic[name]
result = sorted(dic.keys(),reverse = True)
for i in result:
    print(i)