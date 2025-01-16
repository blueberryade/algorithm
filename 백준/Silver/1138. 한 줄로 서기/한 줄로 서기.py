N = int(input())
data = list(map(int,input().split()))
result = [0]*N

for i in range(1,N+1):
    tmp = data[i-1]
    cnt = 0
    for j in range(N):
        if cnt == tmp and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            cnt+=1

print(*result)

