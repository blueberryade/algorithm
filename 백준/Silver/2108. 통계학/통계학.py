import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

print(round(sum(nums)/n))

print(nums[n//2])

dic = dict()
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
mx = max(dic.values())        
d = []
for i in dic:
    if mx == dic[i]:
        d.append(i)
if len(d)>1:
    print(d[1])
else:
    print(d[0])            


print(nums[-1]-nums[0])