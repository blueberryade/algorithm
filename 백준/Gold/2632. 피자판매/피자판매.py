import sys
from collections import defaultdict
input = sys.stdin.readline

def get_all_sums(pizza,length):
    count = defaultdict(int)
    for i in range(length):
        cur_sum = pizza[i]
        count[cur_sum]+=1

        for j in range(1,length-1):
            cur_sum+=pizza[(i+j)%length]
            count[cur_sum]+=1
    count[0]+=1
    count[sum(pizza)]+=1
    return count

k = int(input())
m,n = map(int,input().split())
a = [int(input()) for _ in range(m)]
b = [int(input()) for _ in range(n)]

countA = get_all_sums(a,m)
countB = get_all_sums(b,n)

result = 0
 
for a in countA:
    if k-a in countB:
        result+=countA[a]*countB[k-a]
print(result)


