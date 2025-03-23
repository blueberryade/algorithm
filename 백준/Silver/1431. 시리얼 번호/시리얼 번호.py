N = int(input())
data = []
for _ in range(N):
    s = input().rstrip()
    total = 0
    for i in s:
        if i.isdigit():
            total+=int(i)
    data.append((s,total))

data.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in data:
    print(i[0])
