N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

minPrice = price[0]
result = 0

for i in range(N-1):
    if minPrice>price[i]:
        minPrice = price[i]
    result+= minPrice*distance[i]
print(result)
