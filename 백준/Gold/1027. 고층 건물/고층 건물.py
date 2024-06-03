n = int(input())

building = list(map(int,input().split()))
result = 0

for i in range(n):
    temp = n-1
    for j in range(i+1,n):
        for k in range(i+1,j):
            if building[k] - building[i] >= (((building[j]-building[i])/(j-i))*(k-i)):
                temp -=1
                break
    for j in range(0,i):
        for k in range(j+1,i):
            if building[k] - building[j] >= (((building[i]-building[j])/(i-j))*(k-j)):
                temp -=1
                break
    result = max(temp,result)
print(result)