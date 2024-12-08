import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    data = list(map(int,input().split()))
    result = 0

    if M!=N:
        for j in range(M-1):
            data.append(data[j])
    
    start, end = 0,M-1
    total = sum(data[:M])

    if total < K:
        result+=1
    while end < len(data)-1:
        total-=data[start]
        start+=1
        end+=1
        total+=data[end]
        if total < K:
            result+=1

    print(result)