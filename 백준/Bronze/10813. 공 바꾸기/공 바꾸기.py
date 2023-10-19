n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp
    
for a in arr:
    print(a, end = ' ')