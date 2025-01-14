T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int,input().split()))

    result = 0
    maxPrice = 0
    for i in range(N-1,-1,-1):
        if data[i] > maxPrice:
            maxPrice = data[i]
        else:
            result+=maxPrice-data[i]
    
    print(result)
