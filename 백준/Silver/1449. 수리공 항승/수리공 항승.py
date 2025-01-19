N,L = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

start = data[0]
cnt = 1

for i in data[1:]:
    if (i+0.5)-(start-0.5) <=L:
        continue
    else:
        start = i
        cnt+=1

print(cnt)