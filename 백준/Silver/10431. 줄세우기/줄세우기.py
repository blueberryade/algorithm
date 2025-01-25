P = int(input())
for _ in range(P):
    data = list(map(int,input().split()))
    cnt = 0

    for i in range(1,len(data)-1):
        for j in range(i+1,len(data)):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
                cnt+=1
    print(data[0],cnt)