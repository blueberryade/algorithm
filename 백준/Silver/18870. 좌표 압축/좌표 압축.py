import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
lst = sorted(set(nums))

dic = {}
for i in range(len(lst)):
    dic[lst[i]] = i
for i in nums:
    print(dic[i], end=' ')