n = int(input())
arr = [[0]*100 for _ in range(100)]
for _ in range(n):
    y1,x1 = map(int,input().split())
    for i in range(x1,x1+10):
        for j in range(y1,y1+10):
            arr[i][j] = 1

result = 0
for i in range(100):
    result+=arr[i].count(1)
print(result)