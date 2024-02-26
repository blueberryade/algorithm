import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
result = 0

for k in range(n):
    find = lst[k]
    i = 0
    j = n-1
    while i<j:
        if lst[i]+lst[j] == find:
            if i!=k and j!= k:
                result+=1
                break
            elif i == k:
                i+=1
            elif j == k:
                j-=1
        elif lst[i]+lst[j] <find:
            i+=1
        else:
            j-=1
print(result)            
