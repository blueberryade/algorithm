N = int(input())

lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)

result = []

for i in range(N):
    result.append(lst[i]*(i+1))
    
print(max(result))
