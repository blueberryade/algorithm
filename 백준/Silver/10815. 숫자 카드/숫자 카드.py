import sys
input = sys.stdin.readline



n = int(input())
cards = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))

dic = {}
for i in cards:
    dic[i] = 0

for i in nums:
    if i in dic:
        print(1,end = ' ')
    else:
        print(0,end = ' ')