import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))
dic = {}

for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1

for i in nums:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')