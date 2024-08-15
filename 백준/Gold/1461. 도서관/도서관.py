n,m = map(int,input().split())
books = list(map(int,input().split()))

left = []
right = []

for b in books:
    if b<0:
        left.append(abs(b))
    else:
        right.append(b)

left.sort(reverse=True)
right.sort(reverse=True)
distance = []

for i in range(len(left)):
    if i%m == 0:
        distance.append(left[i])

for i in range(len(right)):
    if i%m==0:
        distance.append(right[i])
        
distance.sort()

result = sum(distance)*2 - distance[-1]
print(result)