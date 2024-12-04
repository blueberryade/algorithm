from collections import defaultdict
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
data = list(map(int,input().split()))
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1]+data[i-1]

result = 0

dic = defaultdict(list)
for i in range(N,0,-1):
    total = S[i]

    if total == K:
        result+=1
    
    target = total+K
    result+=len(dic[target])

    dic[total].append(i)

print(result)