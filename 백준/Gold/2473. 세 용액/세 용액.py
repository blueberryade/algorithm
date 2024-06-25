import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

num = float('inf')
result = []

for i in range(n-2):
    start = i+1
    end = n-1
    while start < end:
        total = arr[i]+arr[start]+arr[end]

        if abs(total) < abs(num):
            num = total
            result = [arr[i],arr[start],arr[end]]

        if total < 0:
            start+=1
        elif total >0:
            end-=1
        else:
            break

print(result[0],result[1],result[2])        
