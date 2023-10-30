n,k = map(int, input().split())
lst = []
for i in range(1,n+1):
    if n%i ==0:
        lst.append(i)

print(lst[k-1] if len(lst)>=k else 0)