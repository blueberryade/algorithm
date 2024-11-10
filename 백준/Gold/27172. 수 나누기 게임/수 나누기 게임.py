n = int(input())
data = list(map(int,input().split()))

maxNum = max(data)
s = set(data)
result = [0]*(maxNum+1)

for i in data:
    if i == maxNum:
        continue
    for j in range(2*i,maxNum+1,i):
        if j in s:
            result[i]+=1
            result[j]-=1
for i in data:
    print(result[i],end=' ')            