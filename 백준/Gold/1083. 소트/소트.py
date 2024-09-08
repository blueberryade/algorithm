n = int(input())
arr = list(map(int,input().split()))
s = int(input())

for i in range(n):
    max_idx = arr.index(max(arr[i:i+s+1]))

    while max_idx!=i and s:
        arr[max_idx],arr[max_idx-1] = arr[max_idx-1],arr[max_idx]
        max_idx-=1
        s-=1

    if s<=0:
        break

print(*arr)