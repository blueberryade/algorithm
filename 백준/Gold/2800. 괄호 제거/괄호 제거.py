from itertools import combinations

data = list(input())
stack = []
index = []
result = set()

for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        index.append((stack.pop(),i))

for i in range(1,len(index)+1):
    for c in combinations(index,i):
        tmp = data[:]
        for x,y in c:
            tmp[x] = tmp[y] = ''
        result.add("".join(tmp))

result = sorted(list(result))
for i in result:
    print(i)