import math

n = int(input())

arr = [True for _ in range(n+1)]
prime_lst = []
for i in range(2,int(math.sqrt(n)+1)):
    if arr[i]== True:
        j = 2
        while i*j <=n:
            arr[i*j] = False
            j+=1
for i in range(2,n+1):
    if arr[i]:
        prime_lst.append(i)
        
result = 0
start = 0
end = 0

while end<=len(prime_lst):
    total = sum(prime_lst[start:end])
    if total == n:
        result+=1
        end+=1
    elif total < n:
        end+=1
    else:
        start+=1

print(result)        