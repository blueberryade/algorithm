import sys
input = sys.stdin.readline

n,m = map(int,input().split())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

left = 0
right = 0
min_diff = sys.maxsize

while left <n and right < n:
    diff = numbers[right] - numbers[left]
    if diff >=m:
        min_diff = min(min_diff,diff)
        left+=1
    else:
        right+=1

print(min_diff)        

