import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())

    flag = [False]*(N+1)
    data = []
    for _ in range(M):
        a,b = map(int,input().split())
        data.append((a,b))

    data.sort(key=lambda x:x[1])

    result = 0

    while data:
        a,b = data.pop(0)
        for i in range(a,b+1):
            if not flag[i]:
                flag[i] = True
                result+=1
                break
    
    print(result)
    
