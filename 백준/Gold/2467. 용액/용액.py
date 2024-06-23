import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

num = float('inf')
left = 0
right = 0

for i in range(n):
    cur = data[i]

    start = i+1
    end = n-1

    while start <= end:
        mid = (start+end) // 2
        tmp = cur+data[mid]

        if abs(tmp) < num:
            num = abs(tmp)
            left = i
            right = mid

            if tmp == 0:
                break
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1
            
print(data[left],data[right])        
