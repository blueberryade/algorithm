import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = list(input().rstrip())
    K = int(input())

    dic = defaultdict(list)

    for i,char in enumerate(W):
        dic[char].append(i)
    
    min_num = sys.maxsize
    max_num = -1
    
    for p in dic.values():
        if len(p) < K:
            continue

        for j in range(len(p)-K+1):
            length = p[j+K-1]-p[j]+1
            min_num = min(min_num,length)
            max_num = max(max_num,length)
    
    if min_num == sys.maxsize:
        print(-1)
    else:
        print(min_num,max_num)