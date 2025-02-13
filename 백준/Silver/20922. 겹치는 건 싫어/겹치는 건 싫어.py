N,K = map(int,input().split())
A = list(map(int,input().split()))

left,right = 0,0
result = 0
check = [0]*100001

while right<N:
    if check[A[right]] < K:
        check[A[right]] +=1
        right+=1
    else:
        check[A[left]]-=1
        left+=1
    result = max(result,right-left)

print(result)