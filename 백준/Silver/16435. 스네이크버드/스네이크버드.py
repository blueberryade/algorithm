N,L = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
for i in data:
    if i <= L:
        L+=1
print(L)