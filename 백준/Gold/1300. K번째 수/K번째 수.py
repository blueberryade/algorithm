N = int(input())
K = int(input())

start = 1
end = K

while start<=end:
    middle = (start+end)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(middle//i,N)
    if cnt >=K:
        result = middle
        end = middle - 1
    else:
        start = middle + 1
print(result)