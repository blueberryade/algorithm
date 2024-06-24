n,k = map(int,input().split())
data = list(map(int,input().split()))

result = [sum(data[:k])]

for i in range(n-k):
    tmp = result[i]+data[k+i]-data[i]
    result.append(tmp)

print(max(result))
        

