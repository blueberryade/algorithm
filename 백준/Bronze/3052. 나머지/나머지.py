arr = []
for _ in range(10):
    i = int(input())
    arr.append(i%42)
result = set(arr)
print(len(result))
