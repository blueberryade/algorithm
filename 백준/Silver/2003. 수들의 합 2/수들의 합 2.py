import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(map(int,input().split()))

S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1]+lst[i-1]

result = 0
for i in range(1,N+1):
    for j in range(i,N+1):
        if S[j] - S[i-1] == M:
            result+=1
print(result)