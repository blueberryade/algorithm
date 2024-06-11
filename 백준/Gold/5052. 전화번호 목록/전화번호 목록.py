import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort()
    result = 'YES'

    for i in range(n-1):
        l = len(nums[i])
        if nums[i] == nums[i+1][:l]:
            result = 'NO'
            break
    print(result)
