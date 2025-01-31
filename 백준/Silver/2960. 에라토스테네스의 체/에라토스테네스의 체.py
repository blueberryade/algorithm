N,K = map(int,input().split())

A = [True]*(N+1)
cnt = 0

for i in range(2,N+1):
    for j in range(i,N+1,i):
        if A[j]:
            A[j] = False
            cnt+=1
            if cnt == K:
                print(j)
