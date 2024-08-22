import sys
from itertools import combinations
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

def count_by_range(arr,value):
	return bisect_right(arr,value) - bisect_left(arr,value)


def getSum(arr):
    sums =[]
    for i in range(1,len(arr)+1):
          for comb in combinations(arr,i):
                sums.append(sum(comb))
    sums.sort()                
    return sums



n,s = map(int,input().split())
data = list(map(int,input().split()))

left = data[:n//2]
right = data[n//2:]

left_sum = getSum(left)
right_sum = getSum(right)

result = 0

for i in left_sum:
      result+=count_by_range(right_sum,s-i)

result+=count_by_range(left_sum,s)      
result+=count_by_range(right_sum,s)

print(result)