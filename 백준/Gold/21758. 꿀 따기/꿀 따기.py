import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

S = [data[0]]

for i in range(1,N):
    S.append(S[i-1]+data[i])

result = 0

for i in range(1,N-1):
    result = max(result,S[N-2]+S[i-1]-data[i])

for i in range(1,N-1):
    result = max(result,S[N-1]-data[0]-data[i]+S[N-1]-S[i])

for i in range(1,N-1):
    result = max(result,S[N-2]-data[0]+data[i])

print(result)