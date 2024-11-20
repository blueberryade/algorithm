import sys
from collections import defaultdict
input = sys.stdin.readline

N,d,k,c = map(int,input().split())
data = [int(input()) for _ in range(N)]

dic = defaultdict(int)
result = 0
cur_count = 0

dic[c] +=1
cur_count+=1

for i in range(k):
    if dic[data[i]] == 0:
        cur_count+=1
    dic[data[i]]+=1

result = cur_count

for i in range(k,N+k-1):
    start = (i-k) % N
    dic[data[start]]-=1
    if dic[data[start]] == 0:
        cur_count-=1
    
    end = i%N

    if dic[data[end]] == 0:
        cur_count+=1
    dic[data[end]]+=1  

    result = max(result,cur_count)

print(result)
    
