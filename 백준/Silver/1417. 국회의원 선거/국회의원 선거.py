n = int(input())
dasom = int(input())
data = [int(input()) for _ in range(n-1)]
data.sort(reverse=True)
cnt = 0

if n==1:
    print(0)
else:
    while data[0]>=dasom:
        dasom+=1
        data[0]-=1
        cnt+=1
        data.sort(reverse=True)
    print(cnt)